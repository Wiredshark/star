#!/usr/bin/env python3
"""Focused structural validator for B2 Incipias License Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/incipias/b2 incipias license compact.txt")
PREFIX = "B2 Incipias License Compact:"


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
        f"{PREFIX} Registrar Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    # Preserve the recurring pair without inventing unsupported Incipias names or titles.
    for phrase in (
        "started calling that one the Registrar",
        "privately think of that one as the Pilot",
        "Neither word is a name or title they have given you",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('government "Conlatio"') != 3:
        fail("all three missions must be scoped to existing Conlatio government")

    for route in ("route standard", "route experience", "route provisional"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["portable endorsement", "tiered renewal"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("later reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must persist completion")

    # Every assignment-style persistent write stays inside the B2 namespace.
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

    # Validate local goto/label integrity for every mission.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    # Consume B1's early-spaceflight institutions as explicit concepts.
    for phrase in (
        "crew-license",
        "private ships",
        "formal categories",
        "experience",
    ):
        if phrase not in lower:
            fail(f"missing B1 licensing continuity concept: {phrase}")

    # Preserve the intended dynamic-content invariant: practical judgment can be
    # recognized without silently replacing common standards with unwritten custom.
    for phrase in (
        "evidence and limits travel with the license",
        "temporary local endorsement",
        "second independent review",
        "temporary convenience from becoming invisible precedent",
    ):
        if phrase not in text:
            fail(f"missing license-accountability invariant: {phrase}")

    # The refusal path must not enter the Review chain.
    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")

    print("PASS: B2 Incipias License Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Registrar + Pilot private shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Registrar Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=crew licensing + private-spaceflight growth")


if __name__ == "__main__":
    main()
