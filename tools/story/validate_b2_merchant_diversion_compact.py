#!/usr/bin/env python3
"""Focused structural/ownership validator for B2 Merchant Diversion Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT = Path("data/human/b2 merchant diversion compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
text = path.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 Merchant Diversion Compact: Offer"',
    'mission "B2 Merchant Diversion Compact: Review"',
    'mission "B2 Merchant Diversion Compact: Ward Remembers"',
]
for token in required_missions:
    assert token in text, f"missing mission: {token}"
assert text.count('mission "B2 Merchant Diversion Compact:') == 3

for person in ("Nessa Ward", "Cal Harker"):
    assert person in text, f"missing named character {person}"

# A1 route-diversion state is read-only and controls high/low-pressure phases.
assert '"world: merchant route diversion pressure" >= 3' in text
assert '"world: merchant route diversion pressure" <= 1' in text
assert not re.search(r'^\s*(?:set|clear)\s+"world:', text, re.M)
assert not re.search(r'^\s*"world:[^"]+"\s*(?:\+=|-=|=)', text, re.M)

# Three substantive routes plus refusal.
for route in ("route expiry", "route field", "route paired", "declined"):
    assert f'"B2 Merchant Diversion Compact: {route}"' in text

# Exactly two terminal settlements and a later one-shot reader.
settlements = re.findall(
    r'"B2 Merchant Diversion Compact: settlement ([^"]+)"\s*=\s*1',
    text,
)
assert sorted(set(settlements)) == ["docket", "ladder"], settlements
for settlement in ("docket", "ladder"):
    assert text.count(f'has "B2 Merchant Diversion Compact: settlement {settlement}"') >= 1
assert '"B2 Merchant Diversion Compact: aftermath seen" = 1' in text

# B2 owns only its own persistent conditions.
for line in text.splitlines():
    stripped = line.strip()
    if re.match(r'^(?:set|clear)\s+"', stripped) or re.match(r'^"[^"]+"\s*(?:\+=|-=|=)', stripped):
        condition = re.search(r'"([^"]+)"', stripped)
        assert condition, stripped
        name = condition.group(1)
        assert name.startswith("B2 Merchant Diversion Compact:"), f"foreign write: {name}"

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

# Every local goto target must have a label somewhere in the content file.
gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
missing = sorted(gotos - labels)
assert not missing, f"missing labels for gotos: {missing}"

# Continuity concepts from B1 Merchant Diversion Dispatch Archive.
for phrase in (
    "temporary",
    "diversion",
    "expiry",
    "fuel",
    "repair margin",
    "independent",
    "source",
    "review",
):
    assert phrase.lower() in text.lower(), f"missing continuity phrase: {phrase}"

# Diversion practice must remain voluntary and cannot become permanent route truth.
assert "not a centralized merchant route authority" in text.lower()
assert "not a declaration that an old route is permanently unsafe" in text.lower()
assert "participating merchant carriers" in text.lower()
assert "direct observation" in text.lower()
assert "relayed report" in text.lower()
assert "inference" in text.lower()
assert "contradiction" in text.lower()

print("PASS: B2 Merchant Diversion Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: a1_route_diversion_state=read_only")
print("PASS: mutation_surface=B2 conditions only")
