#!/usr/bin/env python3
"""Focused structural validator for B2 Drak Memorial Custody Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/drak/b2 drak memorial custody compact.txt")
PREFIX = "B2 Drak Memorial Custody Compact:"


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
        f"{PREFIX} Custodian Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    # These three missions only record persistent story state. They create no
    # destination, cargo, NPC, waypoint, deadline, timer, or other gameplay
    # objective, so terminal accept would leave an objective-less active mission.
    accepts = re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE)
    declines = re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)
    if accepts:
        fail(f"state-only dialogue must not use terminal accept; found {len(accepts)}")
    if len(declines) != 7:
        fail(f"expected exactly 7 state-only decline terminals, found {len(declines)}")

    objective_directives = (
        "destination ",
        "stopover ",
        "waypoint ",
        "npc ",
        "cargo ",
        "passenger ",
        "deadline ",
        "timer ",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if any(stripped.startswith(token) for token in objective_directives):
            fail(f"unexpected gameplay objective in state-only lifecycle slice: {line.strip()}")

    # The recurring Drak presence is intentionally a player-assigned shorthand,
    # not a new canonical Drak title or named office.
    required_character_phrases = (
        "the Custodian",
        "privately think of the presence as the Custodian",
        "no name or title is offered",
    )
    for phrase in required_character_phrases:
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    for system in ("Sayaiban", "Peresedersi", "Fasitopfar"):
        if f'system "{system}"' not in text:
            fail(f"missing Drak-system scope: {system}")

    for route in ("route intact", "route sever", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")

    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["bounded memorial", "severed function archive"]
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

    # This is narrative/custody content only. It may discuss artifacts and danger,
    # but it must not directly mutate economy, combat, fleets, or A1 world state.
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

    # Validate local conversation goto/label targets within each mission block.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    # Preserve B1's central Drak continuity: stewardship balances extinction
    # prevention, memorial custody, intervention restraint, autonomy, and memory.
    # The autonomy invariant is represented here by restraint/refusal language rather
    # than requiring the literal English word "autonomy" in Drak telepathic prose.
    for phrase in ("extinct", "preserve", "danger", "intervention", "memory"):
        if phrase not in lower:
            fail(f"missing B1 stewardship continuity concept: {phrase}")
    for phrase in (
        "does not give you a rule",
        "refuse to offer a judgment",
        "declining to decide",
    ):
        if phrase not in lower:
            fail(f"missing restraint/autonomy continuity phrase: {phrase}")

    # The two final policies must retain provenance rather than pretending that
    # later safety edits were part of the vanished culture's original design.
    for phrase in ("provenance", "original", "alteration", "intervention record"):
        if phrase not in lower:
            fail(f"missing provenance invariant: {phrase}")

    print("PASS: B2 Drak Memorial Custody Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_character=Custodian shorthand")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Custodian Remembers")
    print("PASS: lifecycle=state-only terminals decline cleanly")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: autonomy_model=restraint + refusal, not invented authority")


if __name__ == "__main__":
    main()
