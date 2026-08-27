#!/usr/bin/env python3
"""Focused structural validation for A2 Republic Customs Review.

This validator protects the current-main ownership, lifecycle, routing, and
save-compatibility contract of the integrated customs-review narrative loop.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "a2 republic customs review.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "A2 Republic Customs Review:"
MISSIONS = [
    "A2 Republic Customs Review: Secondary Review",
    "A2 Republic Customs Review: Disposition",
    "A2 Republic Customs Review: Noll Remembers",
]
CANONICAL_HEADER = """# Copyright (c) 2026 by the Endless Sky contributors
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


def assert_local_gotos(blocks: dict[str, str]) -> None:
    for mission, block in blocks.items():
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, re.M))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, re.M))
        missing = sorted(gotos - labels)
        require(not missing, f"{mission}: unresolved goto labels {missing}")


def assignment_lines(text: str) -> list[str]:
    # Match actual condition assignments only. Comparisons such as >= and <= are
    # read-only inputs and must not be misclassified as writes.
    pattern = re.compile(
        r'^\s*"([^"]+)"\s*(?:\+=|-=|\?=|<\?=|>\?=|=(?!=))\s*[-+]?\d+(?:\.\d+)?\s*$',
        re.M,
    )
    return [match.group(1) for match in pattern.finditer(text)]


def main() -> int:
    require(TEXT.startswith(CANONICAL_HEADER + "\n"), "missing canonical GPL content header")
    require(TEXT.endswith("\n"), "file must end with newline")

    blocks = mission_blocks()
    require(list(blocks) == MISSIONS, f"unexpected mission order: {list(blocks)}")
    require(TEXT.count('government "Republic"') == 3, "all stages must be Republic-scoped")
    require(TEXT.count('not attributes "station"') == 3, "all stages must exclude station sources")
    require(TEXT.count('"offer precedence" 9') == 3, "all stages must use offer precedence 9")
    require(TEXT.count("\n\t\t\t\tdecline\n") == 6, "expected six converged state-only decline terminals")
    require(not re.search(r'^\s*accept\s*$', TEXT, re.M), "state-only accept endpoint found")

    first = blocks[MISSIONS[0]]
    require('"world: republic customs scrutiny" >= 3' in first,
            "initial review must require elevated A1 scrutiny")
    require('"world: republic border pressure" >= 4' in first,
            "initial framing must consume current border pressure")
    require("[Underworld experience: repeated pirate contracts]" in first,
            "missing underworld-history requirement label")
    require('"pirate jobs" >= 5' in first,
            "missing repeated pirate-job threshold")
    for label in ("audit", "record", "context", "counsel"):
        require(f"goto {label}" in first and f"label {label}" in first,
                f"missing explicit first-stage route {label}")
    for route in ("document audit", "written basis", "underworld context", "formal process"):
        require(first.count(f'"{PREFIX} route {route}" = 1') == 1,
                f"missing or duplicate first-stage route write: {route}")
    require(first.count(f'"{PREFIX} disposition pending" = 1') == 4,
            "every first-stage route must schedule disposition")

    disposition = blocks[MISSIONS[1]]
    require('"world: republic customs scrutiny" < 3' in disposition,
            "disposition must wait for A1 scrutiny recovery")
    route_to_outcome = {
        "audit": ("route document audit", "bounded audit"),
        "record": ("route written basis", "written uncertainty"),
        "context": ("route underworld context", "contextualized routing"),
        "counsel": ("route formal process", "refusal preserved"),
    }
    for label, (route, outcome) in route_to_outcome.items():
        require(f"branch {label}" in disposition, f"disposition missing branch {label}")
        require(f'has "{PREFIX} {route}"' in disposition,
                f"disposition missing route reader: {route}")
        require(f"label {label}" in disposition, f"disposition missing label {label}")
        require(disposition.count(f'"{PREFIX} outcome {outcome}" = 1') == 1,
                f"missing or duplicate disposition outcome: {outcome}")
    require(disposition.count("goto finish") == 4,
            "all four disposition outcomes must explicitly converge")
    require(f'"{PREFIX} disposition pending" = 0' in disposition,
            "disposition must clear pending state")
    require(f'"{PREFIX} disposition seen" = 1' in disposition,
            "disposition must persist seen state")
    require(f'"{PREFIX} later reader pending" = 1' in disposition,
            "disposition must schedule later reader")

    later = blocks[MISSIONS[2]]
    outcome_routes = {
        "audit": "bounded audit",
        "record": "written uncertainty",
        "context": "contextualized routing",
        "refusal": "refusal preserved",
    }
    for label, outcome in outcome_routes.items():
        require(f"branch {label}" in later, f"later reader missing branch {label}")
        require(f'has "{PREFIX} outcome {outcome}"' in later,
                f"later reader missing outcome reader: {outcome}")
        require(f"label {label}" in later, f"later reader missing label {label}")
        require("goto choice" in later.split(f"label {label}", 1)[1].split("label ", 1)[0],
                f"later reader route {label} does not explicitly converge to choice")
    require(f'"{PREFIX} precedent use bounded" = 1' in later,
            "missing bounded precedent choice")
    require(f'"{PREFIX} precedent kept private" = 1' in later,
            "missing privacy choice")
    require(later.count("goto finish") == 2,
            "both precedent choices must explicitly converge")
    require(f'"{PREFIX} later reader pending" = 0' in later,
            "later reader must clear pending state")
    require(f'"{PREFIX} later reader seen" = 1' in later,
            "later reader must persist seen state")

    assignments = assignment_lines(TEXT)
    require(assignments, "no persistent assignments detected")
    for name in assignments:
        require(name.startswith(PREFIX), f"write outside A2 namespace: {name}")
    for forbidden in (
        "world: republic customs scrutiny",
        "world: republic border pressure",
        "pirate jobs",
    ):
        require(forbidden not in assignments, f"authoritative input write found: {forbidden}")

    forbidden_directives = (
        r'^\s*payment\b', r'^\s*cargo\b', r'^\s*outfit\b', r'^\s*ship\b',
        r'^\s*destination\b', r'^\s*waypoint\b', r'^\s*npc\b', r'^\s*timer\b',
        r'^\s*"reputation:[^"]+"\s*(?:=|\+=|-=)',
    )
    for pattern in forbidden_directives:
        require(not re.search(pattern, TEXT, re.M), f"unexpected gameplay/material directive: {pattern}")

    require("on complete" not in TEXT, "state-only staged flow must not depend on on-complete lifecycle")
    require("dialogue pretending" not in TEXT.lower(), "developer/meta language leaked into dialogue")
    assert_local_gotos(blocks)

    print("PASS: A2 Republic customs-review current-main contract validated")
    print("PASS: missions=3 routes=4 outcomes=4 precedent_choices=2")
    print("PASS: explicit routing=initial + disposition + later reader")
    print("PASS: lifecycle=offer_precedence_9 + six_declines + zero_accepts")
    print("PASS: ownership=A1/pirate inputs read-only; writes confined to A2 namespace")
    print("PASS: save_compatibility=existing condition names preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
