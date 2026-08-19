#!/usr/bin/env python3
"""Focused structural validation for A2 Beyond Patir Survey Review."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "a2 beyond patir survey review.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "A2 Beyond Patir Survey:"
MISSIONS = [
    "A2 Beyond Patir Survey: Field Review",
    "A2 Beyond Patir Survey: Publication Result",
    "A2 Beyond Patir Survey: Later Reader",
    "A2 Beyond Patir Survey: Privacy Reader",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}")
        raise SystemExit(1)


def mission_blocks() -> dict[str, str]:
    starts = list(re.finditer(r'^mission "([^"]+)"$', TEXT, re.M))
    blocks: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(TEXT)
        blocks[match.group(1)] = TEXT[match.start():end]
    return blocks


def assert_local_gotos(blocks: dict[str, str]) -> None:
    for mission, block in blocks.items():
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, re.M))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, re.M))
        missing = sorted(gotos - labels)
        require(not missing, f"{mission}: unresolved goto labels: {missing}")


def main() -> int:
    blocks = mission_blocks()
    require(list(blocks) == MISSIONS, f"unexpected mission order: {list(blocks)}")
    require("Nadiya Voss" in TEXT, "missing named Deep survey analyst Nadiya Voss")
    require(TEXT.count('attributes "deep"') == 4, "every stage must be Deep-scoped")
    require(TEXT.count('not attributes "station"') == 4, "every stage must exclude stations")

    first = blocks[MISSIONS[0]]
    for system in ("Athiri", "Chanai", "Ghila"):
        require(f'has "visited system: {system}"' in first, f"missing core visit gate: {system}")
    for system in ("Maithi", "Mitera", "Thepa"):
        require(f'has "visited system: {system}"' in first, f"missing extended-survey reader: {system}")
    require("[Extended field survey: Maithi, Mitera, and Thepa]" in first,
            "missing explicit extended-survey requirement label")
    require('to display\n\t\t\t\t\t\thas "visited system: Maithi"' in first,
            "extended route must remain hidden until its visited-system evidence exists")

    for route in (
        "conservative corridors",
        "reproducible data",
        "independent replication",
        "extended comparison",
    ):
        require(first.count(f'"{PREFIX} route {route}" = 1') == 1,
                f"missing or duplicate positive route: {route}")
    require(first.count(f'"{PREFIX} followup pending" = 1') == 4,
            "every positive route must schedule publication followup")
    require(first.count(f'"{PREFIX} route private" = 1') == 1, "missing privacy route")
    require(first.count(f'"{PREFIX} refusal reader pending" = 1') == 1,
            "privacy route must schedule its own reader")

    followup = blocks[MISSIONS[1]]
    for outcome in (
        "bounded navigation chart",
        "reproducible dataset",
        "replicated limits",
        "layered hazard model",
    ):
        require(f'"{PREFIX} outcome {outcome}" = 1' in followup,
                f"missing publication outcome: {outcome}")
    require(f'"{PREFIX} followup pending" = 0' in followup, "followup must clear pending state")
    require(f'"{PREFIX} later reader pending" = 1' in followup, "followup must schedule later reader")

    later = blocks[MISSIONS[2]]
    for outcome in (
        "bounded navigation chart",
        "reproducible dataset",
        "replicated limits",
    ):
        require(f'has "{PREFIX} outcome {outcome}"' in later,
                f"later reader must explicitly consume outcome: {outcome}")
    require(f'"{PREFIX} precedent anonymous" = 1' in later, "missing anonymous precedent choice")
    require(f'"{PREFIX} precedent named with record" = 1' in later, "missing named precedent choice")
    require(f'"{PREFIX} later reader pending" = 0' in later, "later reader must clear pending state")

    privacy = blocks[MISSIONS[3]]
    require(f'"{PREFIX} private refusal anonymously noted" = 1' in privacy,
            "missing bounded anonymous refusal outcome")
    require(f'"{PREFIX} private refusal fully removed" = 1' in privacy,
            "missing full privacy outcome")
    require(f'"{PREFIX} refusal reader pending" = 0' in privacy,
            "privacy reader must clear pending state")

    require("on complete" not in TEXT, "staged survey flow must not depend on on-complete lifecycle")

    # Engine-owned exploration history is an input only.
    require(not re.search(r'^\s*(?:set|clear)\s+"visited system:', TEXT, re.M),
            "visited-system history must never be set or cleared by A2")
    require(not re.search(r'^\s*"visited system:[^"]+"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M),
            "visited-system history must never be assigned by A2")

    # This is an evidence/memory slice, not a material reward or reputation shortcut.
    for pattern, label in (
        (r'^\s*payment\b', "payment"),
        (r'^\s*cargo\b', "cargo"),
        (r'^\s*outfit\b', "outfit"),
        (r'^\s*ship\b', "ship"),
        (r'^\s*"reputation:[^"]+"\s*(?:=|\+=|-=)', "reputation"),
        (r'^\s*"world:[^"]+"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', "world authority"),
    ):
        require(not re.search(pattern, TEXT, re.M), f"unexpected {label} mutation")

    assert_local_gotos(blocks)
    print("PASS: A2 Beyond Patir survey-review structure validated")
    print("PASS: core_visits=Athiri,Chanai,Ghila extended=Maithi,Mitera,Thepa")
    print("PASS: positive_routes=4 privacy_route=1 publication_outcomes=4")
    print("PASS: visited-system/world/material/reputation authority remains read-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
