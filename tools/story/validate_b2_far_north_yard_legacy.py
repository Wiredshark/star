#!/usr/bin/env python3
"""Focused structural validation for the B2 Far North Yard Legacy slice."""

from __future__ import annotations

from pathlib import Path
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
        require(text, f'has "{route}"', failures, f"route never read: {route}")
    for settlement in SETTLEMENTS:
        require(text, f'"{settlement}" = 1', failures, f"settlement never written: {settlement}")
        require(text, f'has "{settlement}"', failures, f"settlement never read: {settlement}")

    require(text, '"B2 Far North Yard Legacy: declined" = 1', failures,
            "decline route is not persisted")
    require(text, '"B2 Far North Yard Legacy: aftermath seen" = 1', failures,
            "later reader is not one-shot persisted")
    require(text, 'source "Prime"', failures,
            "production slice is not anchored at Prime")

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
    print(f"PASS: initial_routes={len(ROUTES)}")
    print(f"PASS: terminal_settlements={len(SETTLEMENTS)}")
    print("PASS: later_reader=Vale Remembers")
    print("PASS: persistence_model=stock mission/global conditions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
