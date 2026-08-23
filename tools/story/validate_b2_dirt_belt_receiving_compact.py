#!/usr/bin/env python3
"""Focused structural/ownership validator for B2 Dirt Belt Receiving Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT = Path("data/human/b2 dirt belt receiving compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
text = path.read_text(encoding="utf-8")
low = text.lower()

required_missions = [
    'mission "B2 Dirt Belt Receiving Compact: Offer"',
    'mission "B2 Dirt Belt Receiving Compact: Review"',
    'mission "B2 Dirt Belt Receiving Compact: Ives Remembers"',
]
for token in required_missions:
    assert token in text, f"missing mission: {token}"
assert text.count('mission "B2 Dirt Belt Receiving Compact:') == 3

for person in ("Dara Ives", "Micah Thorne"):
    assert person in text, f"missing named character {person}"

# Three substantive routes plus refusal.
for route in ("route claim", "route capacity", "route paired", "declined"):
    assert f'"B2 Dirt Belt Receiving Compact: {route}"' in text

# Exactly two terminal settlements and one-shot aftermath state.
settlements = re.findall(
    r'"B2 Dirt Belt Receiving Compact: settlement ([^"]+)"\s*=\s*1',
    text,
)
assert sorted(set(settlements)) == ["packet", "reconcile"], settlements
for settlement in ("packet", "reconcile"):
    assert text.count(f'has "B2 Dirt Belt Receiving Compact: settlement {settlement}"') >= 1
assert '"B2 Dirt Belt Receiving Compact: aftermath seen" = 1' in text

# Dirt Belt / Republic scope and B1 continuity concepts.
assert text.count('attributes "dirt belt"') == 3
assert text.count('government "Republic"') == 3
for phrase in (
    "drought-relief",
    "receiving capacity",
    "warehouse",
    "storage",
    "road",
    "unmet remainder",
    "original need",
    "usable",
    "scarcity",
):
    assert phrase in low, f"missing continuity phrase: {phrase}"

# B2 owns only its namespaced persistent conditions.
for line in text.splitlines():
    stripped = line.strip()
    if re.match(r'^(?:set|clear)\s+"', stripped) or re.match(r'^"[^"]+"\s*(?:\+=|-=|=)', stripped):
        condition = re.search(r'"([^"]+)"', stripped)
        assert condition, stripped
        name = condition.group(1)
        assert name.startswith("B2 Dirt Belt Receiving Compact:"), f"foreign write: {name}"

# This slice must not mutate A1/world or material/reputation state.
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

# Every local goto target must have a label somewhere in the content file.
gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
missing = sorted(gotos - labels)
assert not missing, f"missing labels for gotos: {missing}"

# Dialogue/state-only lifecycle: these missions persist conditions but create no
# gameplay objective, so every terminal must close with decline rather than accept.
assert not re.search(r'^\s*accept\s*$', text, re.M), "state-only mission contains terminal accept"
assert len(re.findall(r'^\s*decline\s*$', text, re.M)) == 7, "expected exactly seven decline terminals"
for objective in (
    r'^\s*destination\b',
    r'^\s*stopover\b',
    r'^\s*waypoint\b',
    r'^\s*npc\b',
    r'^\s*cargo\b',
    r'^\s*passenger\b',
    r'^\s*deadline\b',
    r'^\s*timer\b',
):
    assert not re.search(objective, text, re.M | re.I), f"objective-bearing directive found: {objective}"

# Core continuity invariants from B1's relief-routing history.
assert "a completed shipment is an event" in low
assert "a satisfied need is a condition" in low
assert "completed freight" in low
assert "voluntary coordination" in low
assert "centralized relief authority" in low
assert "scarcity has ended" in low
assert "delivery can be partial" in low
assert "original need vanished" in low

print("PASS: B2 Dirt Belt Receiving Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: dirt_belt_scope=3 missions")
print("PASS: mutation_surface=B2 conditions only")
print("PASS: lifecycle=7 state-only decline terminals")
