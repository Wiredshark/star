#!/usr/bin/env python3
"""Focused structural validator for B2 Hicemus Access Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/incipias/b2 hicemus access compact.txt")
PREFIX = "B2 Hicemus Access Compact:"


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
    expected = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Maintainer Remembers"]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for phrase in (
        "calling that one the Dispatcher",
        "privately think of that one as the Maintainer",
        "Neither word is a name or title they have given you",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('government "Hicemus"') != 3:
        fail("all three missions must be scoped to existing Hicemus government")

    for gate in (
        'has "Incipias: Help The Stranded 2: done"',
        'has "Hicemus History: Station Access Archive: offered"',
    ):
        if gate not in text:
            fail(f"missing B1/contact gate: {gate}")

    for route in ("route emergency", "route conditional", "route compact"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["portable access record", "shared conflict table"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text or f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must be one-shot and persist completion")

    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    forbidden_write_tokens = (
        "credits", "reputation:", "combat rating", "cargo ", "outfit ", "ship ", "fleet ", "world:"
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

    for phrase in ("station", "emergency route", "freight", "temporary", "capacity", "privacy"):
        if phrase not in lower:
            fail(f"missing Hicemus station-access continuity concept: {phrase}")

    for phrase in (
        "purpose, capacity, emergency priority, expiry",
        "shared conflict table",
        "local discretion",
        "why they exist and when they should end",
    ):
        if phrase not in text:
            fail(f"missing access-accountability invariant: {phrase}")

    if "Hicemus/Conlatio division" not in text:
        fail("must preserve uncertainty around Hicemus/Conlatio political division")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")

    # Lifecycle invariant: these three missions only persist dialogue/global state.
    # They create no destination, cargo, NPC, waypoint, timer, stopover, or other
    # gameplay objective, so every terminal path must close with decline rather
    # than leave an objective-less accepted mission in the player's active list.
    accepts = re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE)
    declines = re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)
    if accepts:
        fail(f"state-only dialogue slice must not contain terminal accept commands: {len(accepts)} found")
    if len(declines) != 7:
        fail(f"expected exactly 7 state-only decline terminals, found {len(declines)}")

    objective_directives = re.findall(
        r'^\s*(destination|stopover|waypoint|npc|cargo|passengers|deadline|timer)\b',
        text,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if objective_directives:
        fail(f"state-only lifecycle assumption invalidated by objective directives: {objective_directives}")

    print("PASS: B2 Hicemus Access Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Dispatcher + Maintainer private shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Maintainer Remembers")
    print("PASS: lifecycle=7 decline terminals, 0 accepts, no objectives")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_input=Hicemus Station Access Archive")


if __name__ == "__main__":
    main()
