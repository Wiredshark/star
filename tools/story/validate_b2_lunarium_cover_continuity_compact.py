#!/usr/bin/env python3
"""Focused structural/ownership validator for B2 Lunarium Cover Continuity Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT = Path("data/coalition/b2 lunarium cover continuity compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
text = path.read_text(encoding="utf-8")
low = text.lower()

required_missions = [
    'mission "B2 Lunarium Cover Continuity Compact: Offer"',
    'mission "B2 Lunarium Cover Continuity Compact: Review"',
    'mission "B2 Lunarium Cover Continuity Compact: Niree Remembers"',
]
for token in required_missions:
    assert token in text, f"missing mission: {token}"
assert text.count('mission "B2 Lunarium Cover Continuity Compact:') == 3

for person in ("Chiree", "Niree"):
    assert person in text, f"missing character: {person}"

# B1/campaign state is read-only and controls eligibility.
for token in (
    'has "joined the lunarium"',
    'not "joined the heliarchs"',
    'has "Lunarium Cover Network Archive: offered"',
):
    assert token in text, f"missing required gate: {token}"

# Three substantive routes plus refusal.
for route in ("route aid", "route continuity", "route paired", "declined"):
    assert f'"B2 Lunarium Cover Continuity Compact: {route}"' in text

# Exactly two terminal settlements and a one-shot aftermath reader.
settlements = re.findall(
    r'"B2 Lunarium Cover Continuity Compact: settlement ([^"]+)"\s*=\s*1',
    text,
)
assert sorted(set(settlements)) == ["receipt", "reconciliation"], settlements
for settlement in ("receipt", "reconciliation"):
    assert text.count(f'has "B2 Lunarium Cover Continuity Compact: settlement {settlement}"') >= 1
assert '"B2 Lunarium Cover Continuity Compact: aftermath seen" = 1' in text

# B2 owns only its own persistent writes.
for line in text.splitlines():
    stripped = line.strip()
    if re.match(r'^(?:set|clear)\s+"', stripped) or re.match(r'^"[^"]+"\s*(?:\+=|-=|=)', stripped):
        match = re.search(r'"([^"]+)"', stripped)
        assert match, stripped
        name = match.group(1)
        assert name.startswith("B2 Lunarium Cover Continuity Compact:"), f"foreign write: {name}"

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

# Every local goto target must exist.
gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
missing = sorted(gotos - labels)
assert not missing, f"missing labels for gotos: {missing}"

# B1 continuity: genuine aid remains genuine; covert use remains compartmented.
for phrase in (
    "real civic institution",
    "real beneficiaries",
    "civilian obligations",
    "covert",
    "displaced",
    "closure status",
    "compartmented",
    "public charity manifest",
):
    assert phrase in low, f"missing continuity phrase: {phrase}"

# Guard against collapsing the charity into a fake front or exposing covert details.
assert "charity remains a real civic institution" in low
assert "civilian manifests must not become a disguised record of clandestine operations" in low
assert "keep the cover real" in low
assert "keep the secret secret" in low
assert "contains no description of the covert cargo" in low
assert "without exposing the clandestine cargo" in low

print("PASS: B2 Lunarium Cover Continuity Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: b1_campaign_state=read_only")
print("PASS: mutation_surface=B2 conditions only")
