#!/usr/bin/env python3
"""Focused structural validator for the staged Imani Rook mediation slice."""
from pathlib import Path
import re
import sys

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


def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}")
        raise SystemExit(1)


def mission_blocks() -> dict[str, str]:
    starts = list(re.finditer(r'^mission "([^"]+)"$', TEXT, re.M))
    result = {}
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


def main() -> int:
    blocks = mission_blocks()
    require(list(blocks) == MISSIONS, f"unexpected mission order: {list(blocks)}")
    require("Imani Rook" in TEXT, "missing named character Imani Rook")
    require(TEXT.count('source "New Boston"') == 4, "all four missions must be scoped to New Boston")

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
    require(f'"{PREFIX} refusal reader pending" = 1' in first,
            "refusal must schedule its dedicated reader")

    review = blocks[MISSIONS[1]]
    for outcome in ("balanced", "command", "logistics"):
        require(f'"{PREFIX} outcome {outcome}" = 1' in review, f"missing review outcome: {outcome}")
    require(f'"{PREFIX} review pending" = 0' in review, "review must clear pending state")
    require(f'"{PREFIX} later reader pending" = 1' in review, "review must schedule later reader")

    later = blocks[MISSIONS[2]]
    require(f'"{PREFIX} future contact welcomed" = 1' in later, "missing future-contact welcome")
    require(f'"{PREFIX} future contact declined" = 1' in later, "missing future-contact decline")
    require(f'"{PREFIX} later reader pending" = 0' in later, "later reader must clear pending state")

    refusal = blocks[MISSIONS[3]]
    require(f'"{PREFIX} refusal respected" = 1' in refusal, "missing respected-refusal outcome")
    require(f'"{PREFIX} no future mediation" = 1' in refusal, "missing no-future-mediation outcome")
    require(f'"{PREFIX} refusal reader pending" = 0' in refusal, "refusal reader must clear pending state")

    require("on complete" not in TEXT, "ambiguous on-complete lifecycle must not return")
    for token in (
        '"combat rating" =',
        '"combat rating" +=',
        '"Deep: Syndicate Convoy: done" =',
        '"Deep: Syndicate Convoy: done" +=',
    ):
        require(token not in TEXT, f"authoritative input must remain read-only: {token}")

    check_local_gotos(blocks)
    print("PASS: staged Imani Rook mediation structure validated")
    print("PASS: missions=4")
    print("PASS: first_meeting_routes=3 + refusal")
    print("PASS: special_responses=visible-disabled combat + hidden Deep history")
    print("PASS: lifecycle=offer-state-review-reader; no on-complete dependency")
    print("PASS: authoritative_inputs=read-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
