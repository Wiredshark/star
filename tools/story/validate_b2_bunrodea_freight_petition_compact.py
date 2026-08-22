#!/usr/bin/env python3
"""Focused structural validator for B2 Bunrodea Freight Petition Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/bunrodea/b2 bunrodea freight petition compact.txt")
PREFIX = "B2 Bunrodea Freight Petition Compact:"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    if not path.is_file():
        fail(f"missing content file: {path}")

    text = path.read_text(encoding="utf-8")

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    expected = [
        f"{PREFIX} Offer",
        f"{PREFIX} Review",
        f"{PREFIX} Sedi Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for name in ("Sedi Var", "Iral Kes"):
        if name not in text:
            fail(f"missing named character {name}")

    if text.count('government "Bunrodea"') != 3:
        fail("all three missions must be scoped to Bunrodea government")

    for route in ("route sedi", "route iral", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")

    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    if sorted(set(settlements)) != ["dual ledger", "portable docket"]:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("later reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must persist completion")

    # This slice is dialogue/state-only. Accepting one of these missions would
    # create an objective-less active mission, so every terminal path must close
    # with decline after persisting its state.
    accept_count = len(re.findall(r"^\s*accept\s*$", text, flags=re.MULTILINE))
    decline_count = len(re.findall(r"^\s*decline\s*$", text, flags=re.MULTILINE))
    if accept_count != 0:
        fail(f"state-only slice must not use terminal accept; found {accept_count}")
    if decline_count != 7:
        fail(f"expected exactly 7 terminal decline commands, found {decline_count}")

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
        if stripped.startswith(objective_directives):
            fail(f"state-only lifecycle assumption invalidated by objective directive: {line.strip()}")

    # Every persistent write must remain inside this B2 namespace.
    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    # The slice is institutional/character content only; it must not directly
    # mutate material or combat state.
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

    # The content must retain the central continuity distinction established by B1:
    # common freight facts do not erase petition/authority review.
    continuity_phrases = ("petition", "freight", "Megasa", "Erabu")
    for phrase in continuity_phrases:
        if phrase not in text:
            fail(f"missing continuity concept: {phrase}")

    print("PASS: B2 Bunrodea Freight Petition Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Sedi Remembers")
    print("PASS: mutation_surface=B2 conditions only")


if __name__ == "__main__":
    main()
