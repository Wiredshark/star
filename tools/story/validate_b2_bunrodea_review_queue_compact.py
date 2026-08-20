#!/usr/bin/env python3
"""Focused structural validator for B2 Bunrodea Review Queue Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/bunrodea/b2 bunrodea review queue compact.txt")
PREFIX = "B2 Bunrodea Review Queue Compact:"
A1_SIGNAL = "world: bunrodea freight review backlog"


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
        f"{PREFIX} Iral Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for name in ("Sedi Var", "Iral Kes"):
        if name not in text:
            fail(f"missing established named character {name}")

    if text.count('government "Bunrodea"') != 3:
        fail("all three missions must be scoped to Bunrodea government")

    # This slice is a sequel to the prior freight/petition compact, not a duplicate.
    prior_settlements = (
        'has "B2 Bunrodea Freight Petition Compact: settlement portable docket"',
        'has "B2 Bunrodea Freight Petition Compact: settlement dual ledger"',
    )
    for gate in prior_settlements:
        if gate not in text:
            fail(f"missing prerequisite gate: {gate}")

    # A1 owns the live review-backlog signal. B2 must only read it.
    if f'"{A1_SIGNAL}" >= 4' not in text:
        fail("Offer must react to high authoritative A1 review backlog")
    if f'"{A1_SIGNAL}" <= 1' not in text:
        fail("Review must wait for authoritative A1 backlog recovery")

    for line in text.splitlines():
        stripped = line.strip()
        if A1_SIGNAL in stripped and any(op in stripped for op in (" += ", " -= ", " = ")):
            fail(f"B2 must not mutate A1-owned backlog state: {stripped}")

    for route in ("route age first", "route risk first", "route paired lanes"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")

    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["portable delay history", "reconciliation cycle"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("later reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must persist completion")

    # Every direct persistent write must remain inside the B2 namespace.
    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    # This is character/institutional content only; no direct material/combat mutation.
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

    # Continuity: queue recovery and individual petition recovery are different facts.
    continuity_terms = (
        "backlog",
        "urgent",
        "deferr",
        "original arrival",
        "reconciliation",
        "petition",
    )
    lowered = text.lower()
    for term in continuity_terms:
        if term not in lowered:
            fail(f"missing queue-continuity concept: {term}")

    # The compact must not reinterpret the prior freight/petition settlement as a
    # centralized Bunrodea bureaucracy; it only adds queue-management discipline.
    if "centralized" in lowered and "not" not in lowered:
        fail("unexpected centralized-authority claim")

    print("PASS: B2 Bunrodea Review Queue Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: prior_compact_dependency=present")
    print("PASS: a1_backlog_signal=read_only")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Iral Remembers")
    print("PASS: mutation_surface=B2 conditions only")


if __name__ == "__main__":
    main()
