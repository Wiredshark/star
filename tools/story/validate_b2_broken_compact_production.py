#!/usr/bin/env python3
"""Focused structural validation for the B2 Broken Compact production slice.

This intentionally does not replace Endless Sky's own parser/runtime validation.
It checks the persistence/branching contract that B2 owns.
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 broken compact.txt"

MISSIONS = (
    'mission "B2 Broken Compact: Notice"',
    'mission "B2 Broken Compact: Senn Evidence"',
    'mission "B2 Broken Compact: Dorne Evidence"',
    'mission "B2 Broken Compact: Settlement"',
    'mission "B2 Broken Compact: Kelm Aftermath"',
)

CHARACTERS = ("Nadia Kelm", "Elias Dorne", "Mara Senn")

TERMINAL_STATES = (
    "ES-STORY-0002: settlement operating partnership",
    "ES-STORY-0002: settlement estate sale",
    "ES-STORY-0002: settlement arbitration",
    "ES-STORY-0002: settlement player acquisition",
)

EVIDENCE_STATES = (
    "ES-STORY-0002: found private message",
    "ES-STORY-0002: found senn annotation",
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
        require(text, mission, failures, f"missing production mission: {mission}")

    for character in CHARACTERS:
        require(text, character, failures, f"missing named character: {character}")

    for state in TERMINAL_STATES:
        require(text, f'"{state}" = 1', failures, f"terminal state is never written: {state}")

    for state in EVIDENCE_STATES:
        require(text, f'"{state}" = 1', failures, f"evidence state is never written: {state}")
        require(text, f'has "{state}"', failures, f"evidence state is never consumed: {state}")

    require(
        text,
        "[Evidence: private message + Senn annotation]",
        failures,
        "missing player-visible evidence requirement label",
    )

    arbitration_block = text.split("[Evidence: private message + Senn annotation]", 1)[-1][:500]
    if 'has "ES-STORY-0002: found private message"' not in arbitration_block:
        failures.append("evidence-labeled arbitration route is not gated by private-message state")
    if 'has "ES-STORY-0002: found senn annotation"' not in arbitration_block:
        failures.append("evidence-labeled arbitration route is not gated by Senn-annotation state")

    require(
        text,
        'mission "B2 Broken Compact: Kelm Aftermath"',
        failures,
        "missing later-reader mission",
    )
    require(
        text,
        '"ES-STORY-0002: kelm aftermath seen" = 1',
        failures,
        "later reader does not persist its own one-shot state",
    )

    # Refusal/compromised content must remain a valid state, not a dead reload path.
    require(
        text,
        '"ES-STORY-0002: unresolved at departure" = 1',
        failures,
        "missing durable refusal/unresolved outcome",
    )

    # B2 must not invent a second relationship store or new engine schema.
    forbidden = (
        "relationship database",
        "character_memory_table",
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

    print("PASS: B2 Broken Compact production structure validated")
    print(f"PASS: missions={len(MISSIONS)}")
    print(f"PASS: named_characters={len(CHARACTERS)}")
    print(f"PASS: terminal_outcomes={len(TERMINAL_STATES)}")
    print(f"PASS: evidence_states={len(EVIDENCE_STATES)}")
    print("PASS: later_reader=Kelm Aftermath")
    return 0


if __name__ == "__main__":
    sys.exit(main())
