#!/usr/bin/env python3
"""Focused validator for B2 Free Worlds Memorial Boundaries."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 free worlds memorial boundaries.txt")
PREFIX = "B2 Free Worlds Memorial Boundaries:"


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
    expected = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Mika Remembers"]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if text.count('government "Free Worlds"') != 3:
        fail("all three missions must remain Free Worlds content")
    if '"world: free worlds defense strain" >= 3' not in text:
        fail("Offer must react to elevated A1 Free Worlds defense strain")
    if '"world: free worlds defense strain" <= 2' not in text:
        fail("Review must wait for A1 defense strain to ease")
    if re.search(r'^\s*"world:[^"]+"\s*=\s*', text, flags=re.MULTILINE):
        fail("B2 must not write world state")

    for name in ("Tess Morrow", "Mika Rowe", "Niko Rowe"):
        if name not in text:
            fail(f"missing character/reference: {name}")

    if text.count('event "B2 Free Worlds Memorial Boundaries: Review Ready" 7 11') != 3:
        fail("exactly three substantive routes must schedule delayed Review")
    for route in ("route family privacy", "route attributed memory", "route plural remembrance"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing route persistence: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["layered memorial", "living remembrance"]
    if sorted(set(settlements)) != expected_settlements or len(settlements) != 2:
        fail(f"unexpected settlements: {settlements!r}")

    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        fail("state-only slice must not use terminal accept")
    if text.count("\t\t\t\tdecline") != 7:
        fail("all seven state-only terminals must decline cleanly")

    objective_directives = (
        "destination ", "stopover ", "waypoint ", "npc ", "cargo ",
        "passenger ", "deadline ", "timer ",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if line.startswith("\t") and any(stripped.startswith(token) for token in objective_directives):
            fail(f"unexpected gameplay-objective directive: {line.strip()}")

    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE)
    for raw in writes:
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    mission_blocks = {missions[0]: blocks[-3], missions[1]: blocks[-2], missions[2]: blocks[-1]}
    for block in mission_blocks.values():
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    offer_block = mission_blocks[f"{PREFIX} Offer"]
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("refusal must not enter the Review chain")
    if 'Review Ready" 7 11' in decline_block:
        fail("refusal must not schedule Review")

    review_block = mission_blocks[f"{PREFIX} Review"]
    review_requirements = (
        f'has "{PREFIX} introduced"',
        f'has "{PREFIX} review ready"',
        '"world: free worlds defense strain" <= 2',
        f'not "{PREFIX} reviewed"',
    )
    for requirement in review_requirements:
        if requirement not in review_block:
            fail(f"Review missing lifecycle gate: {requirement}")
    if review_block.count(f'"{PREFIX} reviewed" = 1') != 2:
        fail("both Review settlements must close the Review exactly once")
    for settlement in expected_settlements:
        if f'"{PREFIX} settlement {settlement}" = 1' not in review_block:
            fail(f"Review missing settlement write: {settlement}")

    aftermath_block = mission_blocks[f"{PREFIX} Mika Remembers"]
    if f'not "{PREFIX} aftermath seen"' not in aftermath_block:
        fail("aftermath reader must remain one-shot")
    for settlement in expected_settlements:
        if f'has "{PREFIX} settlement {settlement}"' not in aftermath_block:
            fail(f"aftermath reader must consume settlement: {settlement}")
    if aftermath_block.count(f'"{PREFIX} aftermath seen" = 1') != 1:
        fail("aftermath reader must mark aftermath exactly once")

    required = (
        "private message", "crew memories", "family", "public memorial",
        "attributed", "incident report", "fear", "privacy", "corroboration",
        "disagreement", "corrections", "grief",
    )
    for phrase in required:
        if phrase not in lower:
            fail(f"missing grief/memory concept: {phrase}")

    forbidden = (
        "fear proves cowardice",
        "family owns every memory",
        "crew memory is official fact",
        "memorial proves motive",
        "free worlds law requires",
        "one true version",
    )
    for phrase in forbidden:
        if phrase in lower:
            fail(f"asserts unsupported memorial/authority claim: {phrase}")

    print("PASS: B2 Free Worlds Memorial Boundaries structure validated")
    print("PASS: missions=3")
    print("PASS: characters=Tess Morrow + Mika Rowe; memorial subject=Niko Rowe")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: review_gating=introduced + delayed-ready + recovered A1 strain + one-shot")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Mika Remembers; both settlements consumed one-shot")
    print("PASS: lifecycle=7 state-only terminals decline")
    print("PASS: mutation_surface=B2 conditions only; A1 defense strain read-only")
    print("PASS: primary_domain=grief / friendship / family relationships / public memory")
    print("PASS: continuity=facts, attributed memories, privacy, disagreement, and public memorial claims remain distinct")


if __name__ == "__main__":
    main()
