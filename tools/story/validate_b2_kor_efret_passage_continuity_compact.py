#!/usr/bin/env python3
"""Focused structural validator for B2 Kor Efret Passage Continuity Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/korath/b2 kor efret passage continuity compact.txt")
PREFIX = "B2 Kor Efret Passage Continuity Compact:"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    if not path.is_file():
        fail(f"missing content file: {path}")

    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    expected = [
        f"{PREFIX} Offer",
        f"{PREFIX} Review",
        f"{PREFIX} Tracker Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    # Recurring Kor Efreti are player-private shorthands, not invented formal offices.
    for phrase in (
        "started calling this one the Tracker",
        "privately think of that one as the Passage Keeper",
        "Neither label has been offered to you as a Korath name or title",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('attributes "efret"') != 3:
        fail("all three missions must be scoped to Kor Efret worlds")
    if text.count('not attributes "station"') != 3:
        fail("all three missions must exclude stations")

    # Consume the validated B1 family-reunification and passage history explicitly.
    for gate in (
        'has "Kor Efret History: Family Reunification Register: offered"',
        'has "Kor Efret History: Passage Contribution Ledger: offered"',
    ):
        if gate not in text:
            fail(f"missing B1 dependency gate: {gate}")

    for route in ("route reunion", "route passage", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["family packet", "two stage"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("later reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must persist completion")

    # Every persistent write must remain inside this B2 namespace.
    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    forbidden_write_tokens = (
        "credits",
        "reputation:",
        "combat rating",
        "cargo ",
        "outfit ",
        "ship ",
        "fleet ",
        "world:",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if " = " in stripped and any(token in stripped for token in forbidden_write_tokens):
            fail(f"forbidden direct state mutation: {line.strip()}")

    # Validate local goto/label targets per mission.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    # Preserve the B1 social-recovery distinctions this slice exists to deepen.
    for phrase in (
        "family",
        "safe",
        "passage",
        "preferred destination",
        "contact",
        "resettlement",
    ):
        if phrase not in lower:
            fail(f"missing B1 resettlement continuity concept: {phrase}")

    # Core invariant: movement, safety, reunion, and voluntary settlement are
    # related but not interchangeable closure conditions. These are semantic
    # fragments, so compare case-insensitively rather than against capitalization.
    required_fragments = (
        "A safe departure, a family reunion, and a person's preferred destination are not necessarily the same event.",
        "safe location, family contact, and preferred destination",
        "current safe location",
        "whether that location may be shared",
        "current preference",
        "physically safe without being reunited",
        "reunited without choosing to return",
    )
    for phrase in required_fragments:
        if phrase.lower() not in lower:
            fail(f"missing passage/resettlement invariant: {phrase}")

    # Avoid turning practical continuity records into coercive return policy.
    for phrase in (
        "rather than a command to return",
        "voluntarily resolved",
        "person themselves has changed the desired outcome",
    ):
        if phrase.lower() not in lower:
            fail(f"missing voluntary-resettlement safeguard: {phrase}")

    print("PASS: B2 Kor Efret Passage Continuity Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Tracker + Passage Keeper shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Tracker Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=family reunification + passage contribution + voluntary resettlement")


if __name__ == "__main__":
    main()
