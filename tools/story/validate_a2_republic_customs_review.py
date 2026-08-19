#!/usr/bin/env python3
"""Focused structural validation for A2 Republic Customs Review."""
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


def assert_local_gotos(blocks: dict[str, str]) -> None:
    for mission, block in blocks.items():
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, re.M))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, re.M))
        missing = sorted(gotos - labels)
        require(not missing, f"{mission}: unresolved goto labels {missing}")


def main() -> int:
    blocks = mission_blocks()
    require(list(blocks) == MISSIONS, f"unexpected mission order: {list(blocks)}")
    require("Elian Ward" in TEXT, "missing Elian Ward")
    require("Sera Noll" in TEXT, "missing Sera Noll")
    require(TEXT.count('government "Republic"') == 3, "all stages must be Republic-scoped")
    require(TEXT.count('not attributes "station"') == 3, "all stages must exclude station sources")

    first = blocks[MISSIONS[0]]
    require('"world: republic customs scrutiny" >= 3' in first,
            "initial review must require elevated A1 scrutiny")
    require('"world: republic border pressure" >= 4' in first,
            "initial framing must consume current border pressure")
    require("[Underworld experience: repeated pirate contracts]" in first,
            "missing underworld-history requirement label")
    require('to activate\n\t\t\t\t\t\t"pirate jobs" >= 5' in first,
            "underworld response must be visible-disabled until pirate-job threshold")

    for route in ("document audit", "written basis", "underworld context", "formal process"):
        require(first.count(f'"{PREFIX} route {route}" = 1') == 1,
                f"missing or duplicate first-stage route write: {route}")
    require(first.count(f'"{PREFIX} disposition pending" = 1') == 4,
            "every first-stage route must schedule disposition")

    disposition = blocks[MISSIONS[1]]
    require('"world: republic customs scrutiny" < 3' in disposition,
            "disposition must wait for A1 scrutiny to decay below threshold")
    for outcome in (
        "bounded audit",
        "written uncertainty",
        "contextualized routing",
        "refusal preserved",
    ):
        require(disposition.count(f'"{PREFIX} outcome {outcome}" = 1') == 1,
                f"missing or duplicate disposition outcome: {outcome}")
    require(f'"{PREFIX} disposition pending" = 0' in disposition,
            "disposition must clear pending state")
    require(f'"{PREFIX} later reader pending" = 1' in disposition,
            "disposition must schedule later reader")

    later = blocks[MISSIONS[2]]
    for outcome in (
        "bounded audit",
        "written uncertainty",
        "contextualized routing",
    ):
        require(f'has "{PREFIX} outcome {outcome}"' in later,
                f"later reader does not explicitly consume outcome: {outcome}")
    # refusal-preserved is the intentional default/fallthrough outcome.
    require(f'"{PREFIX} precedent use bounded" = 1' in later,
            "missing bounded precedent choice")
    require(f'"{PREFIX} precedent kept private" = 1' in later,
            "missing privacy choice")
    require(f'"{PREFIX} later reader pending" = 0' in later,
            "later reader must clear pending state")

    require("on complete" not in TEXT, "staged flow must not depend on on-complete lifecycle")
    require("dialogue pretending" not in TEXT.lower(), "developer/meta language leaked into dialogue")

    forbidden_authority_writes = (
        r'^\s*"world: republic customs scrutiny"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        r'^\s*"world: republic border pressure"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        r'^\s*"pirate jobs"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
    )
    for pattern in forbidden_authority_writes:
        require(not re.search(pattern, TEXT, re.M), f"authoritative input write found: {pattern}")

    forbidden_material_actions = (
        r'^\s*payment\b',
        r'^\s*cargo\b',
        r'^\s*outfit\b',
        r'^\s*ship\b',
        r'^\s*"reputation:[^"]+"\s*(?:=|\+=|-=)',
    )
    for pattern in forbidden_material_actions:
        require(not re.search(pattern, TEXT, re.M), f"unexpected material/reputation action found: {pattern}")

    assert_local_gotos(blocks)
    print("PASS: A2 Republic customs-review structure validated")
    print("PASS: stages=3 routes=4 outcomes=4")
    print("PASS: A1 scrutiny recovery is read, never narrative-written")
    print("PASS: later consequence reader + precedent privacy choice present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
