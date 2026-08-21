#!/usr/bin/env python3
"""Focused structural/ownership validator for B2 Syndicate Parts Provenance Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT = Path("data/human/b2 syndicate parts provenance compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
text = path.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 Syndicate Parts Provenance Compact: Offer"',
    'mission "B2 Syndicate Parts Provenance Compact: Review"',
    'mission "B2 Syndicate Parts Provenance Compact: Vale Remembers"',
]
for token in required_missions:
    assert token in text, f"missing mission: {token}"
assert text.count('mission "B2 Syndicate Parts Provenance Compact:') == 3

for person in ("Tessa Marr", "Ren Vale"):
    assert person in text, f"missing named character {person}"

# Required A1 gates and strict A1 read-only ownership.
assert '"world: syndicate parts scarcity" >= 3' in text
assert '"world: syndicate parts scarcity" <= 1' in text
assert not re.search(r'^\s*(?:set|clear)\s+"world:', text, re.M)
assert not re.search(r'^\s*"world:[^"]+"\s*(?:\+=|-=|=)', text, re.M)

# Three substantive routes plus refusal.
for route in ("route provenance", "route operational", "route paired", "declined"):
    assert f'"B2 Syndicate Parts Provenance Compact: {route}"' in text

# Exactly two terminal settlements, consumed by the later reader.
settlements = re.findall(
    r'"B2 Syndicate Parts Provenance Compact: settlement ([^"]+)"\s*=\s*1',
    text,
)
assert sorted(set(settlements)) == ["packet", "revalidate"], settlements
for settlement in ("packet", "revalidate"):
    assert text.count(f'has "B2 Syndicate Parts Provenance Compact: settlement {settlement}"') >= 1

# B2 owns only its own persistent conditions.
for line in text.splitlines():
    stripped = line.strip()
    if re.match(r'^(?:set|clear)\s+"', stripped) or re.match(r'^"[^"]+"\s*(?:\+=|-=|=)', stripped):
        condition = re.search(r'"([^"]+)"', stripped)
        assert condition, stripped
        name = condition.group(1)
        assert name.startswith("B2 Syndicate Parts Provenance Compact:"), f"foreign write: {name}"

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

# Continuity concepts from B1 replacement-stock provenance history.
for phrase in (
    "provenance",
    "substitution",
    "compatible",
    "repair",
    "test",
    "uncertainty",
    "portable qualification packet",
    "revalidation",
):
    assert phrase.lower() in text.lower(), f"missing continuity phrase: {phrase}"

# Compatibility must remain bounded by evidence/context rather than universal equivalence.
assert "universal equivalence" in text.lower()
assert "operating" in text.lower() or "duty cycle" in text.lower()
assert "participating syndicate yards" in text.lower() or "participating yards" in text.lower()

# Dialogue-only persistence should not create objective-less accepted missions.
assert not re.search(r'^\s*accept\s*$', text, re.M), "dialogue-only B2 missions should terminate with decline"

print("PASS: B2 Syndicate Parts Provenance Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: a1_parts_scarcity=read_only")
print("PASS: mutation_surface=B2 conditions only")
print("PASS: dialogue_lifecycle=decline")
