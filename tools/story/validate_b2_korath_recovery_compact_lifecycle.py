#!/usr/bin/env python3
"""Lifecycle validator for B2 Korath Recovery Compact."""

from __future__ import annotations

import re
from pathlib import Path

PATH = Path("data/korath/b2 korath recovery compact.txt")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


text = PATH.read_text(encoding="utf-8")

accepts = len(re.findall(r"^\s*accept\s*$", text, flags=re.MULTILINE))
declines = len(re.findall(r"^\s*decline\s*$", text, flags=re.MULTILINE))
if accepts:
    fail(f"state-only Korath recovery slice must not use terminal accept; found {accepts}")
if declines != 7:
    fail(f"expected exactly 7 terminal decline commands, found {declines}")

objective_directives = re.findall(
    r"^\s*(destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b",
    text,
    flags=re.MULTILINE | re.IGNORECASE,
)
if objective_directives:
    fail(f"state-only lifecycle assumption invalidated by objectives: {objective_directives}")

required = (
    'mission "B2 Korath Recovery Compact: Offer"',
    'mission "B2 Korath Recovery Compact: Review"',
    'mission "B2 Korath Recovery Compact: Medic Remembers"',
    '"B2 Korath Recovery Compact: settlement linked recovery packet" = 1',
    '"B2 Korath Recovery Compact: settlement reconciliation checkpoint" = 1',
    '"B2 Korath Recovery Compact: aftermath seen" = 1',
)
for token in required:
    if token not in text:
        fail(f"missing expected lifecycle/state token: {token}")

print("PASS: B2 Korath Recovery Compact lifecycle validated")
print("PASS: state_only_terminals=7 decline / 0 accept")
print("PASS: objective_directives=0")
