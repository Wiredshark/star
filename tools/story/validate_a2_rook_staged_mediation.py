#!/usr/bin/env python3
"""Focused structural validator for the staged Imani Rook mediation slice."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "a2 rook staged mediation.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "A2 Rook Mediation:"
MISSIONS = [
    "A2 Rook Mediation: First Meeting",
    "A2 Rook Mediation: Case Review",
    "A2 Rook Mediation: Later Reader",
    "A2 Rook Mediation: Refusal Reader",
]
HEADER = """# Copyright (c) 2026 by the Endless Sky contributors
#
# Endless Sky is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

"""


def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}")
        raise SystemExit(1)


def mission_blocks() -> dict[str, str]:
    starts = list(re.finditer(r'^mission "([^"]+)"$', TEXT, re.M))
    result: dict[str, str] = {}
    for i, match in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(TEXT)
        result[match.group(1)] = TEXT[match.start():end]
    return result


def check_local_gotos(blocks: dict[str, str]) -> None:
    for mission, block in blocks.items():
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        require(not missing, f"{mission} unresolved goto labels: {missing}")


def assignments() -> list[str]:
    found: list[str] = []
    for line in TEXT.splitlines():
        stripped = line.strip()
        if stripped.startswith('"') and re.search(r'"\s*(?:=|\+=|-=)\s*-?\d+\s*$', stripped):
            found.append(stripped)
    return found


def main() -> int:
    require(TEXT.startswith(HEADER), "missing canonical GPL content header")
    require(TEXT.endswith("\n"), "file must end with newline")

    blocks = mission_blocks()
    require(list(blocks) == MISSIONS, f"unexpected mission order: {list(blocks)}")
    require("Imani Rook" in TEXT, "missing named character Imani Rook")
    require(TEXT.count('source "New Boston"') == 4, "all four missions must be scoped to New Boston")
    require(TEXT.count('"offer precedence" 9') == 4, "all four state-only missions require offer precedence 9")
    require(TEXT.count("\n\t\t\t\tdecline\n") == 7, "expected seven state-only decline terminals")
    require("\n\t\t\t\taccept\n" not in TEXT, "state-only A2 missions must not accept")
    require("on complete" not in TEXT, "ambiguous on-complete lifecycle must not return")

    first = blocks[MISSIONS[0]]
    require("[Combat experience: convoy command]" in first, "missing combat requirement label")
    require('to activate\n\t\t\t\t\t\t"combat rating" >= 5' in first,
            "combat response must remain visible-disabled below threshold")
    require("[Prior service: Deep convoy]" in first, "missing Deep convoy requirement label")
    require('to display\n\t\t\t\t\t\thas "Deep: Syndicate Convoy: done"' in first,
            "Deep convoy response must be hidden until authoritative history exists")
    for route in ("balanced", "command", "logistics"):
        require(f'"{PREFIX} route {route}" = 1' in first, f"missing route write: {route}")
    require(f'"{PREFIX} refused" = 1' in first, "missing refusal write")
    require(first.count(f'"{PREFIX} review pending" = 1') == 3,
            "positive first-meeting routes must schedule exactly three review paths")
    require(first.count(f'"{PREFIX} refusal reader pending" = 1') == 1,
            "refusal must schedule exactly one dedicated reader")

    review = blocks[MISSIONS[1]]
    for route in ("balanced", "command", "logistics"):
        require(f'branch {route}\n\t\t\t\thas "{PREFIX} route {route}"' in review,
                f"review missing explicit route gate: {route}")
        require(f'label {route}' in review, f"review missing route label: {route}")
        require(f'"{PREFIX} outcome {route}" = 1' in review, f"missing review outcome: {route}")
    require(review.count("goto finish") == 3, "all three review routes must explicitly converge")
    require(f'"{PREFIX} review pending" = 0' in review, "review must clear pending state")
    require(f'"{PREFIX} review seen" = 1' in review, "review must mark itself seen")
    require(f'"{PREFIX} later reader pending" = 1' in review, "review must schedule later reader")

    later = blocks[MISSIONS[2]]
    for route in ("balanced", "command", "logistics"):
        require(f'branch {route}\n\t\t\t\thas "{PREFIX} outcome {route}"' in later,
                f"later reader missing explicit outcome gate: {route}")
        require(f'label {route}' in later, f"later reader missing outcome label: {route}")
    require(later.count("goto choice") == 3, "all three outcome routes must converge on future-contact choice")
    require(f'"{PREFIX} future contact welcomed" = 1' in later, "missing future-contact welcome")
    require(f'"{PREFIX} future contact declined" = 1' in later, "missing future-contact decline")
    require(later.count("goto finish") == 2, "both future-contact routes must explicitly converge")
    require(f'"{PREFIX} later reader pending" = 0' in later, "later reader must clear pending state")
    require(f'"{PREFIX} later reader seen" = 1' in later, "later reader must mark itself seen")

    refusal = blocks[MISSIONS[3]]
    require(f'"{PREFIX} refusal respected" = 1' in refusal, "missing respected-refusal outcome")
    require(f'"{PREFIX} no future mediation" = 1' in refusal, "missing no-future-mediation outcome")
    require(refusal.count("goto finish") == 2, "both refusal-reader choices must explicitly converge")
    require(f'"{PREFIX} refusal reader pending" = 0' in refusal, "refusal reader must clear pending state")
    require(f'"{PREFIX} refusal reader seen" = 1' in refusal, "refusal reader must mark itself seen")

    for assignment in assignments():
        condition = assignment.split('"', 2)[1]
        require(condition.startswith(PREFIX), f"write escaped A2 namespace: {assignment}")

    for token in (
        '"combat rating" =',
        '"combat rating" +=',
        '"combat rating" -=',
        '"Deep: Syndicate Convoy: done" =',
        '"Deep: Syndicate Convoy: done" +=',
        '"Deep: Syndicate Convoy: done" -=',
        '"world:',
    ):
        require(token not in TEXT, f"authoritative input/world state must remain read-only or absent: {token}")

    for directive in ("destination ", "waypoint ", "passenger ", "cargo ", "payment ", "reputation ", "ship ", "fleet "):
        require(not re.search(rf'^\s*{re.escape(directive)}', TEXT, re.M),
                f"dialogue-only slice must not add gameplay directive: {directive.strip()}")

    check_local_gotos(blocks)
    print("PASS: staged Imani Rook mediation structure validated")
    print("PASS: missions=4; precedence=9; terminals=7 decline / 0 accept")
    print("PASS: first_meeting_routes=3 + refusal")
    print("PASS: review_routes=balanced/command/logistics explicitly gated")
    print("PASS: later_reader_routes=balanced/command/logistics explicitly gated")
    print("PASS: refusal_reader=explicit and one-shot")
    print("PASS: authoritative_inputs=read-only; writes=A2 namespace only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
