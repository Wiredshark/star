#!/usr/bin/env python3
"""Focused structural/ownership validator for B2 Deep Escort Capacity Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT = Path("data/human/b2 deep escort capacity compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
text = path.read_text(encoding="utf-8")
low = text.lower()

required_missions = [
    'mission "B2 Deep Escort Capacity Compact: Offer"',
    'mission "B2 Deep Escort Capacity Compact: Review"',
    'mission "B2 Deep Escort Capacity Compact: Kest Remembers"',
]
for token in required_missions:
    assert token in text, f"missing mission: {token}"
assert text.count('mission "B2 Deep Escort Capacity Compact:') == 3

for person in ("Mara Kest", "Elias Trent"):
    assert person in text, f"missing named character {person}"

assert 'has "Deep Research Convoy Reserve Ledger: offered"' in text

for route in ("route obligation", "route outcome", "route paired", "declined"):
    assert f'"B2 Deep Escort Capacity Compact: {route}"' in text

settlements = re.findall(
    r'"B2 Deep Escort Capacity Compact: settlement ([^"]+)"\s*=\s*1',
    text,
)
assert sorted(set(settlements)) == ["packet", "reconcile"], settlements
for settlement in ("packet", "reconcile"):
    assert f'has "B2 Deep Escort Capacity Compact: settlement {settlement}"' in text
assert '"B2 Deep Escort Capacity Compact: aftermath seen" = 1' in text

assert text.count('attributes "deep"') == 3
assert text.count('government "Republic"') == 3
for phrase in (
    "research convoy",
    "borrowed capacity",
    "patrol",
    "rescue",
    "inspection",
    "maintenance",
    "displaced duty",
    "restored reserve",
    "replacement",
):
    assert phrase in low, f"missing continuity phrase: {phrase}"

# B2 owns only its namespaced writes.
for line in text.splitlines():
    stripped = line.strip()
    if re.match(r'^(?:set|clear)\s+"', stripped) or re.match(r'^"[^"]+"\s*(?:\+=|-=|=)', stripped):
        condition = re.search(r'"([^"]+)"', stripped)
        assert condition, stripped
        name = condition.group(1)
        assert name.startswith("B2 Deep Escort Capacity Compact:"), f"foreign write: {name}"

assert not re.search(r'^\s*(?:set|clear)\s+"world:', text, re.M)
assert not re.search(r'^\s*"world:[^"]+"\s*(?:\+=|-=|=)', text, re.M)
for forbidden in (
    r'^\s*payment\b',
    r'^\s*reputation\b',
    r'^\s*cargo\b',
    r'^\s*outfit\b',
    r'^\s*ship\b',
    r'^\s*fleet\b',
):
    assert not re.search(forbidden, text, re.M | re.I), f"forbidden mutation pattern: {forbidden}"

# Every local goto target must exist as a label somewhere in the file.
gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
missing = sorted(gotos - labels)
assert not missing, f"missing labels for gotos: {missing}"

# Core continuity invariants inherited from B1's reserve ledger.
assert "borrowed escort capacity as an obligation rather than free reinforcement" in low
assert "a convoy arriving safely is an event" in low
assert "a restored reserve is a condition" in low
assert "replacement promise is not the same thing as a patrol actually sailing" in low
assert "safe arrival cannot counterfeit a healthy reserve" in low
assert "finished convoy is not the same thing as a recovered reserve" in low
assert "practical coordination" in low
assert "unlimited reserve capacity" in low

print("PASS: B2 Deep Escort Capacity Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: deep_scope=3 missions")
print("PASS: mutation_surface=B2 conditions only")
