#!/usr/bin/env python3
"""Focused structural validator for B2 Free Worlds Volunteer Command Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 free worlds volunteer command compact.txt")
PREFIX = "B2 Free Worlds Volunteer Command Compact:"
A1_STRAIN = "world: free worlds defense strain"
A1_SURGE = "world: free worlds patrol surge"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    if not path.is_file():
        fail(f"missing content file: {path}")

    text = path.read_text(encoding="utf-8")
    lowered = text.lower()

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    expected = [
        f"{PREFIX} Offer",
        f"{PREFIX} Review",
        f"{PREFIX} Quill Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for name in ("Elia Venn", "Mara Quill"):
        if name not in text:
            fail(f"missing named character {name}")

    if text.count('government "Free Worlds"') != 3:
        fail("all three missions must be scoped to Free Worlds government")

    # A1 owns the live defense simulation. B2 may gate on it but never write it.
    required_reads = (
        f'has "{A1_SURGE}"',
        f'"{A1_STRAIN}" >= 1',
        f'not "{A1_SURGE}"',
        f'"{A1_STRAIN}" <= 1',
    )
    for read in required_reads:
        if read not in text:
            fail(f"missing authoritative A1 read gate: {read}")

    for line in text.splitlines():
        stripped = line.strip()
        if (A1_STRAIN in stripped or A1_SURGE in stripped) and any(
            op in stripped for op in (" += ", " -= ", " = ", "set ", "clear ")
        ):
            fail(f"B2 must not mutate A1-owned Free Worlds defense state: {stripped}")

    for route in (
        "route bounded activation",
        "route captain discretion",
        "route paired records",
    ):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")

    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["expiry and release", "portable activation packet"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("later reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must persist completion")

    # Dialogue/state-only lifecycle: no objective-less accepted missions.
    accepts = re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE)
    declines = re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)
    if accepts:
        fail(f"state-only compact must not contain terminal accept commands: {len(accepts)}")
    if len(declines) != 7:
        fail(f"expected exactly 7 terminal decline commands, found {len(declines)}")

    objective_directives = re.findall(
        r'^\t(?:destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b',
        text,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if objective_directives:
        fail(f"unexpected gameplay-objective directives: {objective_directives}")

    # Every direct B2 persistent write must stay in the compact namespace.
    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    # This is character/institutional content only: no material/combat mutation.
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

    # Validate local conversation goto/label targets inside each mission block.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    # Continuity: temporary militia coordination must not become ownership or
    # permanent service through copied records or historical precedent.
    continuity_terms = (
        "temporary",
        "volunteer",
        "consent",
        "scope",
        "safety",
        "release",
        "closure",
        "fresh activation",
    )
    for term in continuity_terms:
        if term not in lowered:
            fail(f"missing volunteer-command continuity concept: {term}")

    if "permanent control" not in lowered and "permanent command" not in lowered:
        fail("must explicitly preserve the temporary-versus-permanent authority boundary")

    if "centralized navy" in lowered or "centralized command authority" in lowered:
        fail("unexpected centralized Free Worlds command claim")

    print("PASS: B2 Free Worlds Volunteer Command Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: a1_defense_state=read_only")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: later_reader=Quill Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: authority_boundary=temporary volunteer coordination")


if __name__ == "__main__":
    main()
