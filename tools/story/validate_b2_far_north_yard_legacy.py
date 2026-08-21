#!/usr/bin/env python3
"""Focused structural validation for the B2 Far North Yard Legacy slice."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 far north yard legacy.txt"

MISSIONS = (
    'mission "B2 Far North Yard Legacy: Offer"',
    'mission "B2 Far North Yard Legacy: Review"',
    'mission "B2 Far North Yard Legacy: Vale Remembers"',
)
CHARACTERS = ("Tessa Vale", "Rowan Pike")
ROUTES = (
    "B2 Far North Yard Legacy: route balanced",
    "B2 Far North Yard Legacy: route vale",
    "B2 Far North Yard Legacy: route pike",
)
EXPLICIT_REVIEW_BRANCHES = (
    "B2 Far North Yard Legacy: route vale",
    "B2 Far North Yard Legacy: route pike",
)
SETTLEMENTS = (
    "B2 Far North Yard Legacy: settlement protected training",
    "B2 Far North Yard Legacy: settlement supervised production",
)


def require(text: str, needle: str, failures: list[str], message: str) -> None:
    if needle not in text:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    if not DATA.is_file():
        print(f"FAIL: missing {DATA.relative_to(ROOT)}")
        return 1

    text = DATA.read_text(encoding="utf-8")

    for mission in MISSIONS:
        require(text, mission, failures, f"missing mission: {mission}")
    for character in CHARACTERS:
        require(text, character, failures, f"missing named character: {character}")
    for route in ROUTES:
        require(text, f'"{route}" = 1', failures, f"route never written: {route}")
    for route in EXPLICIT_REVIEW_BRANCHES:
        require(text, f'has "{route}"', failures, f"review branch never reads route: {route}")
    for settlement in SETTLEMENTS:
        require(text, f'"{settlement}" = 1', failures, f"settlement never written: {settlement}")
        require(text, f'has "{settlement}"', failures, f"settlement never read: {settlement}")

    # The balanced route is deliberately the Review conversation's fallthrough
    # case. Vale and Pike have explicit branches; if neither is set, the balanced
    # route is the only remaining introduced state.
    require(text, 'has "B2 Far North Yard Legacy: introduced"', failures,
            "review mission does not require the initial interaction")
    require(text, 'not "B2 Far North Yard Legacy: reviewed"', failures,
            "review mission is not one-shot gated")
    if '\t\t\tbranch balanced' in text:
        failures.append("balanced route should remain the intentional Review fallthrough")

    require(text, '"B2 Far North Yard Legacy: declined" = 1', failures,
            "decline route is not persisted")
    require(text, '"B2 Far North Yard Legacy: aftermath seen" = 1', failures,
            "later reader is not one-shot persisted")
    require(text, 'source "Prime"', failures,
            "production slice is not anchored at Prime")

    labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
    gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE)
    missing = sorted(set(gotos) - labels)
    if missing:
        failures.append(f"goto target(s) missing labels: {missing}")

    # These missions are dialogue/state-only. Accepting any terminal path would
    # leave an objective-less mission in the active mission list after the
    # conversation closes, so every terminal path must decline after writing the
    # same persistent state.
    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        failures.append("state-only Far North Yard missions must not leave accepted missions active")

    decline_count = len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE))
    if decline_count != 7:
        failures.append(f"expected exactly seven state-only dialogue terminals to decline, found {decline_count}")

    for objective in (
        '\tdestination ',
        '\tstopover ',
        '\twaypoint ',
        '\tnpc ',
        '\tdeadline ',
        '\tpassengers ',
        '\tcargo ',
    ):
        if objective in text:
            failures.append(f"unexpected mission objective in state-only lifecycle slice: {objective.strip()}")

    # The slice must stay on stock condition state rather than inventing a new
    # relationship or apprenticeship persistence store.
    forbidden = (
        "relationship database",
        "apprenticeship database",
        "new save schema",
        "sqlite",
    )
    lower = text.lower()
    for token in forbidden:
        if token in lower:
            failures.append(f"forbidden shadow-state/schema marker present: {token}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: B2 Far North Yard Legacy structure validated")
    print(f"PASS: missions={len(MISSIONS)}")
    print(f"PASS: named_characters={len(CHARACTERS)}")
    print(f"PASS: initial_routes={len(ROUTES)} + refusal")
    print("PASS: review_routing=balanced fallthrough + explicit Vale/Pike branches")
    print(f"PASS: terminal_settlements={len(SETTLEMENTS)}")
    print("PASS: later_reader=Vale Remembers")
    print("PASS: persistence_model=stock mission/global conditions")
    print("PASS: lifecycle=state-only dialogue terminals decline cleanly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
