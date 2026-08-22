#!/usr/bin/env python3
"""Focused structural validator for B2 Kor Efret Reconstruction Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/korath/b2 kor efret reconstruction compact.txt")
PREFIX = "B2 Kor Efret Reconstruction Compact:"


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
        f"{PREFIX} Recorder Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    # The two recurring Kor Efreti are player-assigned role shorthands, not new
    # canonical names or formal offices.
    for phrase in (
        "privately think of that one as the Repairer",
        "started calling this one the Recorder",
        "Neither term is something the Korath have offered as a name or title",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('attributes "efret"') != 3:
        fail("all three missions must be scoped to Kor Efret worlds")
    if text.count('not attributes "station"') != 3:
        fail("all three missions must exclude stations")

    for route in ("route record", "route repair", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["provenance bond", "restoration priority"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("later reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must persist completion")

    # These missions only record persistent dialogue state. They do not create
    # gameplay objectives, so every terminal conversation path must decline
    # after writing state instead of accepting an objective-less mission.
    accept_count = sum(1 for line in text.splitlines() if line.strip() == "accept")
    decline_count = sum(1 for line in text.splitlines() if line.strip() == "decline")
    if accept_count:
        fail(f"state-only slice must not leave accepted missions: accept={accept_count}")
    if decline_count != 7:
        fail(f"expected exactly 7 state-only decline terminals, found {decline_count}")

    objective_directives = re.compile(
        r'^\s*(destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b',
        flags=re.MULTILINE | re.IGNORECASE,
    )
    objective_hits = objective_directives.findall(text)
    if objective_hits:
        fail(f"unexpected gameplay-objective directives in state-only slice: {objective_hits}")

    # Every persistent write must remain inside this B2 namespace.
    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    # Narrative-only slice: no direct material, reputation, combat, or world-state writes.
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

    # Preserve all four B1 reconstruction institutions as explicit content concepts.
    for phrase in (
        "provenance",
        "sealed district",
        "restoration obligation",
        "ecological recovery",
    ):
        if phrase not in lower:
            fail(f"missing B1 reconstruction continuity concept: {phrase}")

    # The resulting policy must keep immediate repair and historical accountability
    # simultaneously visible rather than treating salvage as simple resource loot.
    for phrase in (
        "origin, damage history, repairs, and destination",
        "donor district keeps an open obligation",
        "habitability",
        "environmental recovery",
        "responsibility does not vanish",
    ):
        if phrase not in text:
            fail(f"missing reconstruction-accountability invariant: {phrase}")

    print("PASS: B2 Kor Efret Reconstruction Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Recorder + Repairer shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Recorder Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=provenance + sealed habitat + obligations + recovery")


if __name__ == "__main__":
    main()
