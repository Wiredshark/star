#!/usr/bin/env python3
"""Focused structural validator for B2 Republic Civic Case Continuity."""

from __future__ import annotations

import pathlib
import re
import sys

DEFAULT_PATH = pathlib.Path("data/human/b2 republic civic case continuity.txt")
PREFIX = "B2 Republic Civic Case Continuity:"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    expected = {
        f"{PREFIX} Offer",
        f"{PREFIX} Review",
        f"{PREFIX} Park Remembers",
    }
    if set(missions) != expected or len(missions) != 3:
        fail(f"expected exactly 3 focused missions, got {missions!r}")

    for name in ("Mara Ellison", "Jun Park"):
        if name not in text:
            fail(f"missing named character {name}")

    required_world_reads = (
        '"world: republic civic strain" >= 4',
        '"world: republic civic strain" <= 1',
    )
    for needle in required_world_reads:
        if needle not in text:
            fail(f"missing authoritative A1 civic-strain read: {needle}")

    # A1 owns world:* simulation state. B2 may read it but never write it.
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('"world:') and re.search(r'\s(?:=|\+=|-=|\?=|>\?=|<\?=)', stripped):
            fail(f"B2 must not write authoritative world state: {stripped}")
        if stripped.startswith('set "world:') or stripped.startswith('clear "world:'):
            fail(f"B2 must not set/clear authoritative world state: {stripped}")

    routes = (
        "route named owner",
        "route accountable handoff",
        "route paired records",
    )
    for route in routes:
        if text.count(f'"{PREFIX} {route}" = 1') != 1:
            fail(f"expected one persistent route write for {route}")

    if text.count(f'"{PREFIX} declined" = 1') != 1:
        fail("missing exactly one refusal persistence write")

    settlements = (
        "settlement portable case packet",
        "settlement reconciliation cycle",
    )
    for settlement in settlements:
        if text.count(f'"{PREFIX} {settlement}" = 1') != 1:
            fail(f"terminal settlement must be written exactly once: {settlement}")

    if text.count(f'"{PREFIX} aftermath seen" = 1') != 1:
        fail("missing one-shot later-reader persistence")

    # Character/state continuity concepts that distinguish this slice from other Republic B2 arcs.
    required_concepts = (
        "resident's current sharing consent",
        "unresolved obligation",
        "current owner",
        "closure evidence",
        "closed appointment",
        "transferred file",
        "reduced queue",
    )
    for needle in required_concepts:
        if needle.lower() not in text.lower():
            fail(f"missing civic-case continuity concept: {needle}")

    # Direct material/combat/reputation changes are outside this B2 slice.
    forbidden = (
        r'^\s*credits\s*[+=-]',
        r'^\s*"reputation:[^"]+"\s*[+=-]',
        r'^\s*"combat rating"\s*[+=-]',
        r'^\s*cargo\s+',
        r'^\s*outfit\s+',
        r'^\s*ship\s+',
        r'^\s*fleet\s+',
    )
    for pattern in forbidden:
        if re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE):
            fail(f"forbidden material/gameplay mutation matched {pattern!r}")

    # All condition writes in action blocks must be owned by this B2 slice.
    for match in re.finditer(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        condition = match.group(1)
        if not condition.startswith(PREFIX):
            fail(f"non-B2 condition write detected: {condition}")

    gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
    labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto targets without labels: {missing}")

    print("PASS: B2 Republic Civic Case Continuity structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: A1 civic strain=read-only")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Park Remembers")
    print("PASS: B2-owned writes only")
    print("PASS: civic continuity=consent + context + owner + obligation + closure evidence")


if __name__ == "__main__":
    main()
