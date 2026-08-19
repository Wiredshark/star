#!/usr/bin/env python3
"""Focused structural validator for B2 Korath Recovery Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/korath/b2 korath recovery compact.txt")
PREFIX = "B2 Korath Recovery Compact:"


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
        f"{PREFIX} Medic Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for phrase in (
        "calling that one the Medic",
        "privately think of that one as the Analyst",
        "Neither word is a name or title either has given you",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('government "Remnant"') != 3:
        fail("all three missions must remain scoped to existing Remnant government")

    for gate in (
        'has "Remnant: Cognizance 2: done"',
        'has "Remnant History: Korath Exile Raid Ledger: offered"',
        'has "Remnant History: Korath Recovery and Containment Ledger: offered"',
    ):
        if gate not in text:
            fail(f"missing upstream B1/campaign gate: {gate}")

    for route in ("route rescue", "route provenance", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["linked recovery packet", "reconciliation checkpoint"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("later reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must persist completion")

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

    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    for concept in (
        "humanitarian",
        "provenance",
        "restitution",
        "survivor",
        "ownership",
        "evidence",
        "recovery ledger",
    ):
        if concept not in lower:
            fail(f"missing Korath recovery continuity concept: {concept}")

    for phrase in (
        "release several recovered medical supplies",
        "linked recovery packet",
        "reconciliation checkpoint",
        "medical release, an ownership claim, and an evidentiary conclusion",
    ):
        if phrase not in text:
            fail(f"missing recovery-accountability invariant: {phrase}")

    # Preserve B1's epistemic boundary: material shortages may be evidence without
    # becoming a universal excuse or a proven single motive for exile raids.
    forbidden_causation = (
        "the korath raid because",
        "the exiles raid because",
        "all korath exiles need",
        "proves why the korath",
    )
    for phrase in forbidden_causation:
        if phrase in lower:
            fail(f"unsupported universal Korath motive claim: {phrase}")

    if "single centralized policy for all Korath encounters" not in text:
        fail("must explicitly avoid inventing centralized Remnant policy")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")

    print("PASS: B2 Korath Recovery Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Medic + Analyst private shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Medic Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=Korath Exile Raid Ledger + Recovery and Containment Ledger")
    print("PASS: continuity=rescue/provenance/restitution remain distinct")


if __name__ == "__main__":
    main()
