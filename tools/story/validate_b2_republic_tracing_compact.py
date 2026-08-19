#!/usr/bin/env python3
"""Focused structural validator for B2 Republic Tracing Compact."""

from __future__ import annotations

import pathlib
import re
import sys

DEFAULT_PATH = pathlib.Path("data/human/b2 republic tracing compact.txt")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    expected_missions = {
        "B2 Republic Tracing Compact: Offer",
        "B2 Republic Tracing Compact: Review",
        "B2 Republic Tracing Compact: Saye Remembers",
    }
    if set(missions) != expected_missions or len(missions) != 3:
        fail(f"expected exactly 3 focused missions, got {missions!r}")

    for name in ("Anika Saye", "Corin Vell"):
        if name not in text:
            fail(f"missing named character {name}")

    required_inputs = (
        'has "world: republic resettlement surge"',
        '"world: republic displacement pressure" >= 2',
        '"world: republic displacement pressure" < 2',
        'not "world: republic resettlement surge"',
    )
    for needle in required_inputs:
        if needle not in text:
            fail(f"missing authoritative A1 read: {needle}")

    # B2 may read world:* state but must never write it in an action block.
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('"world:') and re.search(r'\s(?:=|\+=|-=|\?=|>\?=|<\?=)', stripped):
            fail(f"B2 must not write authoritative world state: {stripped}")
        if stripped.startswith('set "world:') or stripped.startswith('clear "world:'):
            fail(f"B2 must not set/clear authoritative world state: {stripped}")

    route_flags = (
        "route portable tracing",
        "route accountable registry",
        "route dual track",
    )
    for route in route_flags:
        if f'"B2 Republic Tracing Compact: {route}" = 1' not in text:
            fail(f"missing persistent route {route}")

    if '"B2 Republic Tracing Compact: declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = (
        "settlement portable family file",
        "settlement consent ledger",
    )
    for settlement in settlements:
        if text.count(f'"B2 Republic Tracing Compact: {settlement}" = 1') != 1:
            fail(f"terminal settlement must be written exactly once: {settlement}")

    if '"B2 Republic Tracing Compact: aftermath seen" = 1' not in text:
        fail("missing one-shot later-reader persistence")

    # Guard this story slice against direct material/combat/reputation mutation.
    forbidden_write_patterns = (
        r'^\s*credits\s*[+=-]',
        r'^\s*"reputation:[^"]+"\s*[+=-]',
        r'^\s*"combat rating"\s*[+=-]',
        r'^\s*cargo\s+',
        r'^\s*outfit\s+',
    )
    for pattern in forbidden_write_patterns:
        if re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE):
            fail(f"forbidden material/gameplay mutation matched {pattern!r}")

    # Every local goto must have a matching local label somewhere in the file.
    gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
    labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
    missing_labels = sorted(gotos - labels)
    if missing_labels:
        fail(f"goto targets without labels: {missing_labels}")

    print("PASS: B2 Republic Tracing Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: authoritative_A1_inputs=displacement pressure + resettlement surge (read-only)")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Saye Remembers")
    print("PASS: world_state_writes=none")


if __name__ == "__main__":
    main()
