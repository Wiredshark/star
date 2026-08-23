#!/usr/bin/env python3
"""Validate the B2 Coalition Rescue Handoff Compact story slice."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/coalition/b2 coalition rescue handoff compact.txt")
PREFIX = "B2 Coalition Rescue Handoff Compact:"
MISSIONS = [
    f'{PREFIX} Offer',
    f'{PREFIX} Review',
    f'{PREFIX} Oren Remembers',
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")

    for mission in MISSIONS:
        if f'mission "{mission}"' not in text:
            fail(f"missing mission: {mission}")

    if text.count('\nmission "') != 3:
        fail("expected exactly 3 missions")

    for character in ("Lira Senn", "Oren Vale"):
        if character not in text:
            fail(f"missing recurring character: {character}")

    if 'event "B2 Coalition Rescue Handoff Compact: Review Ready"' not in text:
        fail("missing delayed Review event")
    if text.count('event "B2 Coalition Rescue Handoff Compact: Review Ready" 7 11') != 3:
        fail("expected all three substantive Offer routes to schedule Review in 7-11 days")

    required_states = [
        "route continuity first",
        "route operational first",
        "route paired records",
        "declined",
        "settlement portable survivor packet",
        "settlement expiry reconciliation",
        "aftermath seen",
    ]
    for suffix in required_states:
        if f'"{PREFIX} {suffix}"' not in text:
            fail(f"missing persistent state: {suffix}")

    if re.search(r"^\s+accept\s*$", text, flags=re.MULTILINE):
        fail("state-only dialogue slice must not use terminal accept")
    decline_count = len(re.findall(r"^\s+decline\s*$", text, flags=re.MULTILINE))
    if decline_count != 7:
        fail(f"expected exactly 7 terminal decline commands, found {decline_count}")

    objective_directive = re.compile(
        r"^\t(?:destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b",
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if objective_directive.search(text):
        fail("unexpected gameplay-objective directive in state-only slice")

    writes = re.findall(r'^\s+"([^"]+)"\s*=\s*[-0-9]+\s*$', text, flags=re.MULTILINE)
    if not writes:
        fail("no persistent writes found")
    foreign_writes = sorted({name for name in writes if not name.startswith(PREFIX)})
    if foreign_writes:
        fail(f"writes outside B2 namespace: {foreign_writes}")

    forbidden_mutations = (
        "credits",
        "reputation",
        "combat rating",
        "cargo ",
        "outfit ",
        "ship ",
        "fleet ",
        "world:",
    )
    for write in writes:
        lowered = write.lower()
        if any(token in lowered for token in forbidden_mutations):
            fail(f"forbidden material/upstream write: {write}")

    labels = set(re.findall(r"^\s*label\s+([A-Za-z0-9_-]+)\s*$", text, flags=re.MULTILINE))
    gotos = re.findall(r"^\s*goto\s+([A-Za-z0-9_-]+)\s*$", text, flags=re.MULTILINE)
    missing = sorted({target for target in gotos if target not in labels})
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    continuity_terms = (
        "consent",
        "treatment",
        "contact",
        "unresolved care",
        "update time",
        "scope",
    )
    lowered = text.lower()
    for term in continuity_terms:
        if term not in lowered:
            fail(f"missing rescue-continuity concept: {term}")

    if "centralized Coalition rescue office" not in text:
        fail("missing distributed-authority continuity guard")

    print("PASS: B2 Coalition Rescue Handoff Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: delayed_review=7-11 days")
    print("PASS: lifecycle=7 declines, 0 accepts")
    print("PASS: mutation_surface=B2 conditions only")


if __name__ == "__main__":
    main()
