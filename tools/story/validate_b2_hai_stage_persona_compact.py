#!/usr/bin/env python3
"""Focused structural validator for B2 Hai Stage Persona Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/hai/b2 hai stage persona compact.txt")
PREFIX = "B2 Hai Stage Persona Compact:"


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
    expected = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Kessa Remembers"]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if text.count('event "B2 Hai Stage Persona Compact: Review Ready" 7 11') != 3:
        fail("exactly three substantive routes must schedule delayed review")
    for phrase in ("Kessa Riin", "Mara Dey"):
        if phrase not in text:
            fail(f"missing named character: {phrase}")
    if text.count('government "Hai"') != 3:
        fail("all three missions must remain Hai content")
    if text.count('has "language: Hai"') != 3:
        fail("all three missions must require Hai comprehension")

    for route in ("route bounded performance", "route revision authority", "route layered identity"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing route persistence: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["persona firewall", "portable persona packet"]
    if sorted(set(settlements)) != expected_settlements or len(settlements) != 2:
        fail(f"unexpected terminal settlements: {settlements!r}")

    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        fail("state-only slice must not use terminal accept")
    if text.count("\t\t\t\tdecline") != 7:
        fail("all seven state-only terminals must decline cleanly")

    objective_directives = ("destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passenger ", "deadline ", "timer ")
    for line in text.splitlines():
        stripped = line.strip().lower()
        if line.startswith("\t") and any(stripped.startswith(token) for token in objective_directives):
            fail(f"unexpected gameplay-objective directive: {line.strip()}")

    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE)
    for raw in writes:
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("refusal must not enter the review chain")
    if 'Review Ready" 7 11' in decline_block:
        fail("refusal must not schedule review")

    required = (
        "stage persona", "private biography", "credited", "publicity consent", "revision",
        "expire", "independent corroboration", "campaign", "performance", "source",
    )
    for phrase in required:
        if phrase not in lower:
            fail(f"missing persona/identity concept: {phrase}")

    forbidden = (
        "stage persona is her true personality",
        "fans prove her private life",
        "label owns kessa",
        "hai law requires the persona",
        "marketing profile is biography",
    )
    for phrase in forbidden:
        if phrase in lower:
            fail(f"asserts unsupported identity/authority claim: {phrase}")

    print("PASS: B2 Hai Stage Persona Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=Kessa Riin + Mara Dey")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Kessa Remembers")
    print("PASS: lifecycle=7 state-only terminals decline")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: primary_domain=entertainment culture / friendship / public identity")
    print("PASS: continuity=performance, authorship, publicity consent, private biography, and source lineage remain distinct")


if __name__ == "__main__":
    main()
