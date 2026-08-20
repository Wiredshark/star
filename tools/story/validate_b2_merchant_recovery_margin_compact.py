#!/usr/bin/env python3
"""Focused structural/ownership validator for B2 Merchant Recovery Margin Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT = Path("data/human/b2 merchant recovery margin compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
text = path.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 Merchant Recovery Margin Compact: Offer"',
    'mission "B2 Merchant Recovery Margin Compact: Review"',
    'mission "B2 Merchant Recovery Margin Compact: Vale Remembers"',
]
for token in required_missions:
    assert token in text, f"missing mission: {token}"
assert text.count('mission "B2 Merchant Recovery Margin Compact:') == 3

for person in ("Imani Vale", "Corin Beck"):
    assert person in text, f"missing named character {person}"

# Required upstream gates and strict A1 read-only ownership.
assert 'has "Merchant Recovery Margin Ledger: offered"' in text
assert '"world: merchant repair backlog" >= 3' in text
assert '"world: merchant repair backlog" <= 1' in text
assert not re.search(r'^\s*(?:set|clear)\s+"world:', text, re.M)
assert not re.search(r'^\s*"world:[^"]+"\s*(?:\+=|-=|=)', text, re.M)

# Three substantive routes plus refusal.
for route in (
    'route reserve',
    'route throughput',
    'route paired',
    'declined',
):
    assert f'"B2 Merchant Recovery Margin Compact: {route}"' in text

# Exactly two terminal settlements, consumed by the later reader.
settlements = re.findall(
    r'"B2 Merchant Recovery Margin Compact: settlement ([^"]+)"\s*=\s*1',
    text,
)
assert sorted(set(settlements)) == ["margin packet", "reconciliation"], settlements
for settlement in ("margin packet", "reconciliation"):
    assert text.count(f'has "B2 Merchant Recovery Margin Compact: settlement {settlement}"') >= 1

# B2 owns only its own persistent conditions.
for line in text.splitlines():
    stripped = line.strip()
    if re.match(r'^(?:set|clear)\s+"', stripped) or re.match(r'^"[^"]+"\s*(?:\+=|-=|=)', stripped):
        condition = re.search(r'"([^"]+)"', stripped)
        assert condition, stripped
        name = condition.group(1)
        assert name.startswith("B2 Merchant Recovery Margin Compact:"), f"foreign write: {name}"

# No direct material/reputation/campaign mutation.
for forbidden in (
    r'^\s*payment\b',
    r'^\s*reputation\b',
    r'^\s*cargo\b',
    r'^\s*outfit\b',
    r'^\s*ship\b',
    r'^\s*fleet\b',
):
    assert not re.search(forbidden, text, re.M | re.I), f"forbidden mutation pattern: {forbidden}"

# Every local goto target must have a label somewhere in the same content file.
gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
missing = sorted(gotos - labels)
assert not missing, f"missing labels for gotos: {missing}"

# Continuity concepts from B1/A1 that this slice is expected to preserve.
for phrase in (
    "recovery margin",
    "repair backlog",
    "reserve capacity",
    "restoration",
    "local control",
):
    assert phrase.lower() in text.lower(), f"missing continuity phrase: {phrase}"

# The outcome must remain a voluntary distributed Merchant practice, not a new central authority.
assert "not a centralized Merchant government" in text
assert "participating" in text.lower()

print("PASS: B2 Merchant Recovery Margin Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: a1_repair_backlog=read_only")
print("PASS: mutation_surface=B2 conditions only")
