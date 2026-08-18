#!/usr/bin/env python3
"""Validate the first A2 modern-dialogue production slice.

This intentionally performs a narrow structural acceptance check without trying to
reimplement Endless Sky's parser. Engine/parser/runtime gates remain authoritative.
"""

from __future__ import annotations

from pathlib import Path
import sys


DEFAULT = Path("data/human/a2 dialogue vertical slice.txt")


def require(text: str, needle: str, failures: list[str], message: str) -> None:
    if needle not in text:
        failures.append(message)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    text = path.read_text(encoding="utf-8")
    failures: list[str] = []

    require(text, 'mission "A2 Dialogue: Rook Mediation"', failures, "missing production mediation mission")
    require(text, 'mission "A2 Dialogue: Rook Remembers"', failures, "missing positive later-reader mission")
    require(text, 'mission "A2 Dialogue: Rook Refusal Reader"', failures, "missing refusal later-reader mission")

    # Player-visible requirement labels paired with authoritative persistent checks.
    require(text, '[Combat experience: convoy command]', failures, "missing combat requirement label")
    require(text, '"combat rating" >= 5', failures, "combat label lacks authoritative condition")
    require(text, '[Prior service: Deep convoy]', failures, "missing prior-service requirement label")
    require(text, 'has "Deep: Syndicate Convoy: done"', failures, "prior-service label lacks authoritative persistent condition")

    # At least three materially distinct selectable approaches plus a refusal route.
    routes = [
        'goto balanced',
        'goto command',
        'goto logistics',
        'goto refuse',
    ]
    for route in routes:
        require(text, route, failures, f"missing route {route}")

    # Choice-specific durable outputs and actual later readers.
    outcomes = [
        '"A2 Dialogue: rook outcome balanced" = 1',
        '"A2 Dialogue: rook outcome command" = 1',
        '"A2 Dialogue: rook outcome logistics" = 1',
        '"A2 Dialogue: rook refused" = 1',
        'has "A2 Dialogue: rook outcome command"',
        'has "A2 Dialogue: rook outcome logistics"',
        'has "A2 Dialogue: rook refused"',
    ]
    for outcome in outcomes:
        require(text, outcome, failures, f"missing persistent outcome/reader: {outcome}")

    # Save compatibility: no schema extension is used; all new state is ordinary conditions.
    forbidden = [
        'dialogue world state',
        'character memory blob',
    ]
    for needle in forbidden:
        if needle in text.lower():
            failures.append(f"forbidden duplicate authority marker present: {needle}")

    if failures:
        print("A2 dialogue slice: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("A2 dialogue slice: PASS")
    print("- named production NPC: Imani Rook")
    print("- selectable approaches: balanced, command, logistics, refusal")
    print("- persistent gated inputs: combat rating, Deep convoy completion")
    print("- later readers: positive outcome reader + refusal reader")
    print("- persistence mechanism: stock mission/global conditions only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
