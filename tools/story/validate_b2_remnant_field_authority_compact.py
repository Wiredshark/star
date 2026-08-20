#!/usr/bin/env python3
"""Focused structural/ownership validator for B2 Remnant Field Authority Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT = Path("data/remnant/b2 remnant field authority compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
text = path.read_text(encoding="utf-8")
low = text.lower()

required_missions = [
    'mission "B2 Remnant Field Authority Compact: Offer"',
    'mission "B2 Remnant Field Authority Compact: Review"',
    'mission "B2 Remnant Field Authority Compact: Plume Remembers"',
]
for token in required_missions:
    assert token in text, f"missing mission: {token}"
assert text.count('mission "B2 Remnant Field Authority Compact:') == 3

assert 'event "B2 Remnant Field Authority Compact: Review Ready"' in text
assert 'event "B2 Remnant Field Authority Compact: Review Ready" 7 11' in text
assert text.count('event "B2 Remnant Field Authority Compact: Review Ready" 7 11') == 3

for person in ("Plume", "Prefect Chilia"):
    assert person in text, f"missing canonical character: {person}"

# Do not pre-empt Chilia's established introduction, and consume the B1 authority history.
assert 'has "Remnant: Cognizance 4: done"' in text
assert 'has "Remnant Qualification Ledger Archive: offered"' in text

for route in ("route authority map", "route adjudication", "route paired", "declined"):
    assert f'"B2 Remnant Field Authority Compact: {route}"' in text

settlements = re.findall(
    r'"B2 Remnant Field Authority Compact: settlement ([^"]+)"\s*=\s*1',
    text,
)
assert sorted(set(settlements)) == ["authority packet", "layered ledger"], settlements
for settlement in ("authority packet", "layered ledger"):
    assert f'has "B2 Remnant Field Authority Compact: settlement {settlement}"' in text
assert '"B2 Remnant Field Authority Compact: aftermath seen" = 1' in text

# Offer and Review remain Remnant-scoped; aftermath returns to Plume on Aventine.
assert text.count('government "Remnant"') == 2
assert 'source "Aventine"' in text

# Continuity: specialist evidence/authority and cross-discipline response stay distinct.
for phrase in (
    "threat is not an order",
    "competence could create authority inside a field",
    "without turning that authority into a universal chain of command",
    "designation does not automatically",
    "expertise is transferable",
    "cross-discipline",
    "specialist findings remain immutable evidence records",
    "response can balance my evidence. it cannot rewrite it",
    "a prefect may reconcile priorities without converting the reconciliation into new scientific evidence",
    "that does not mean the prefect changes what we observed",
):
    assert phrase in low, f"missing continuity phrase: {phrase}"

# Preserve Plume's established Cognizance authority boundary: threat designation is not
# blanket tactical/resource authority, and prefect adjudication is not omniscience.
for concept in (
    "routing",
    "force",
    "logistics",
    "engineering",
    "review",
    "qualified domain",
    "binding scope",
    "excluded decisions",
    "unresolved objections",
):
    assert concept in low, f"missing authority-boundary concept: {concept}"

# B2 owns only namespaced writes.
for line in text.splitlines():
    stripped = line.strip()
    if re.match(r'^(?:set|clear)\s+"', stripped) or re.match(r'^"[^"]+"\s*(?:\+=|-=|=)', stripped):
        condition = re.search(r'"([^"]+)"', stripped)
        assert condition, stripped
        name = condition.group(1)
        assert name.startswith("B2 Remnant Field Authority Compact:"), f"foreign write: {name}"

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

# The refusal path must not schedule the delayed Review or set introduced state.
decline_block = text.split("\t\t\tlabel decline", 1)[1].split("\n\n\nmission", 1)[0]
assert '"B2 Remnant Field Authority Compact: declined" = 1' in decline_block
assert 'Review Ready' not in decline_block
assert '"B2 Remnant Field Authority Compact: introduced" = 1' not in decline_block

print("PASS: B2 Remnant Field Authority Compact structure validated")
print("PASS: missions=3")
print("PASS: canonical_characters=Plume + Prefect Chilia")
print("PASS: initial_routes=3 + refusal")
print("PASS: delayed_review=7-11 days")
print("PASS: terminal_settlements=2")
print("PASS: authority_boundary=specialist finding != cross-discipline response")
print("PASS: mutation_surface=B2 conditions only")
