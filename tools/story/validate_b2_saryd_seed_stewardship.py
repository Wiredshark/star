#!/usr/bin/env python3
"""Focused structural validator for B2 Saryd Seed Stewardship."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/coalition/b2 saryd seed stewardship.txt")
PREFIX = "B2 Saryd Seed Stewardship:"


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
        f"{PREFIX} Keeper Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for phrase in (
        "privately you have started thinking of that one as the Keeper",
        "in your own head you call that one the Grower",
        "Neither word is a name or office they have given you",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('government "Coalition"') != 3:
        fail("all three missions must use existing Coalition government")
    if text.count('attributes "saryd"') != 3:
        fail("all three missions must be scoped to existing saryd attribute")

    for route in ("route provenance", "route access", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["local reserve covenant", "portable seed passport"]
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

    # Lifecycle contract: these missions only write persistent story state and do
    # not create gameplay objectives. They must close with decline instead of
    # leaving objective-less accepted missions in the active mission list.
    terminal_accepts = re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE)
    terminal_declines = re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)
    if terminal_accepts:
        fail(f"state-only dialogue must not use terminal accept: count={len(terminal_accepts)}")
    if len(terminal_declines) != 7:
        fail(f"expected exactly 7 terminal decline commands, found {len(terminal_declines)}")

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
            fail(f"unexpected objective-bearing directive in state-only slice: {line.strip()}")

    for phrase in (
        "seed-exchange",
        "lineage",
        "local variety",
        "ecological",
        "climate",
    ):
        if phrase not in lower:
            fail(f"missing B1 seed/ecology continuity concept: {phrase}")

    for phrase in (
        "portable seed passport",
        "origin, known crosses, field performance, retained local reserve, and uncertainty",
        "local reserve covenant",
        "uncrossed reference population",
        "adaptation does not erase its own history",
    ):
        if phrase not in text:
            fail(f"missing seed-stewardship invariant: {phrase}")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")

    print("PASS: B2 Saryd Seed Stewardship structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Keeper + Grower private shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Keeper Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=seed lineage exchange + ecological recovery")
    print("PASS: lifecycle=7 declines + 0 accepts + no gameplay objectives")


if __name__ == "__main__":
    main()
