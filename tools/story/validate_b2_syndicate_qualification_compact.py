#!/usr/bin/env python3
"""Focused structural/ownership validator for B2 Syndicate Qualification Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT = Path("data/human/b2 syndicate qualification compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
text = path.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 Syndicate Qualification Compact: Offer"',
    'mission "B2 Syndicate Qualification Compact: Review"',
    'mission "B2 Syndicate Qualification Compact: Venn Remembers"',
]
for token in required_missions:
    assert token in text, f"missing mission: {token}"
assert text.count('mission "B2 Syndicate Qualification Compact:') == 3

for person in ("Mara Venn", "Ilias Rook"):
    assert person in text, f"missing named character {person}"

# Required A1 gates and strict A1 read-only ownership.
assert '"world: syndicate labor strain" >= 2' in text
assert 'has "world: syndicate labor rotation active"' in text
assert '"world: syndicate labor strain" <= 1' in text
assert 'not "world: syndicate labor rotation active"' in text
assert not re.search(r'^\s*(?:set|clear)\s+"world:', text, re.M)
assert not re.search(r'^\s*"world:[^"]+"\s*(?:\+=|-=|=)', text, re.M)

# Three substantive routes plus refusal.
for route in ("route local", "route portable", "route paired", "declined"):
    assert f'"B2 Syndicate Qualification Compact: {route}"' in text

# Exactly two terminal settlements, consumed by the later reader.
settlements = re.findall(
    r'"B2 Syndicate Qualification Compact: settlement ([^"]+)"\s*=\s*1',
    text,
)
assert sorted(set(settlements)) == ["packet", "renewal"], settlements
for settlement in ("packet", "renewal"):
    assert text.count(f'has "B2 Syndicate Qualification Compact: settlement {settlement}"') >= 1

# These are dialogue/state-only missions. They create no gameplay objective, so every
# terminal path must close with decline instead of leaving an accepted objective-less
# mission active in the player's mission list.
accepts = re.findall(r'^\s*accept\s*$', text, re.M)
declines = re.findall(r'^\s*decline\s*$', text, re.M)
assert not accepts, f"state-only lifecycle must not use accept terminals: {len(accepts)}"
assert len(declines) == 7, f"expected 7 decline terminals, found {len(declines)}"
for objective in (
    r'^\s*destination\b',
    r'^\s*stopover\b',
    r'^\s*waypoint\b',
    r'^\s*npc\b',
    r'^\s*cargo\b',
    r'^\s*passengers?\b',
    r'^\s*deadline\b',
    r'^\s*timer\b',
):
    assert not re.search(objective, text, re.M | re.I), (
        f"objective-bearing directive invalidates state-only lifecycle assumption: {objective}"
    )

# B2 owns only its own persistent conditions.
for line in text.splitlines():
    stripped = line.strip()
    if re.match(r'^(?:set|clear)\s+"', stripped) or re.match(r'^"[^"]+"\s*(?:\+=|-=|=)', stripped):
        condition = re.search(r'"([^"]+)"', stripped)
        assert condition, stripped
        name = condition.group(1)
        assert name.startswith("B2 Syndicate Qualification Compact:"), f"foreign write: {name}"

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

# Continuity concepts from the B1 dockyard-labor history.
for phrase in (
    "qualification",
    "labor strain",
    "rotation",
    "supervision",
    "local endorsement",
    "portable qualification packet",
):
    assert phrase.lower() in text.lower(), f"missing continuity phrase: {phrase}"

# Transferred qualification must not become blanket authority or universal labor law.
assert "not a universal" in text.lower()
assert "participating yards" in text.lower()
assert "local" in text.lower()

print("PASS: B2 Syndicate Qualification Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: lifecycle=7 decline terminals, 0 accept terminals")
print("PASS: a1_labor_state=read_only")
print("PASS: mutation_surface=B2 conditions only")
