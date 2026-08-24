#!/usr/bin/env python3
"""Focused validator for B2 Bunrodea Recusal Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/bunrodea/b2 bunrodea recusal compact.txt")
PREFIX = "B2 Bunrodea Recusal Compact:"


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
    expected = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Nema Remembers"]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for character in ("Tavi Rell", "Nema Oss"):
        if character not in text:
            fail(f"missing character: {character}")

    if text.count('has "B2 Bunrodea Review Queue Compact: aftermath seen"') != 1:
        fail("Offer must consume integrated Bunrodea Review Queue aftermath exactly once")
    if text.count('government "Bunrodea"') != 3:
        fail("all three missions must remain Bunrodea-scoped")

    if text.count('event "B2 Bunrodea Recusal Compact: Review Ready" 7 11') != 3:
        fail("exactly three substantive routes must schedule delayed Review")

    for route in ("route recusal", "route disclosure plus second review", "route layered authority"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["portable recusal record", "tiered conflict screen"]
    if sorted(set(settlements)) != expected_settlements or len(settlements) != 2:
        fail(f"unexpected settlements: {settlements!r}")

    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        fail("state-only slice must not use terminal accept")
    if text.count("\t\t\t\tdecline") != 7:
        fail("all seven state-only terminal paths must decline cleanly")

    objective_directives = (
        "destination ", "stopover ", "waypoint ", "npc ", "cargo ",
        "passenger ", "deadline ", "timer ",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if line.startswith("\t") and any(stripped.startswith(token) for token in objective_directives):
            fail(f"unexpected objective directive: {line.strip()}")

    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE)
    for raw in writes:
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope write: {raw}")

    if '"world:' in text:
        fail("slice must not write or depend on world state")

    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    offer = next(block for block in blocks if block.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("refusal must not enter Review chain")
    if 'Review Ready" 7 11' in decline_block:
        fail("refusal must not schedule Review")

    required_concepts = (
        "conflict of interest", "family tie", "recusal", "disclosure",
        "second reviewer", "evidence handling", "decision authority",
        "independent review", "direct family", "material stakes",
        "active warnings", "permanent suspicion",
    )
    for phrase in required_concepts:
        if phrase not in lower:
            fail(f"missing recusal/authority concept: {phrase}")

    forbidden = (
        "all family ties prove corruption",
        "all bunrodea reviewers must recuse",
        "tavi is corrupt",
        "nema controls the review office",
        "central bunrodea ethics authority",
    )
    for phrase in forbidden:
        if phrase in lower:
            fail(f"asserts unsupported authority or guilt: {phrase}")

    print("PASS: B2 Bunrodea Recusal Compact structure validated")
    print("PASS: missions=3")
    print("PASS: characters=Tavi Rell + Nema Oss")
    print("PASS: dependency=integrated Bunrodea Review Queue aftermath")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Nema Remembers")
    print("PASS: lifecycle=7 state-only terminals decline")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: continuity=evidence work, disclosure, recusal, and final decision authority remain distinct")


if __name__ == "__main__":
    main()
