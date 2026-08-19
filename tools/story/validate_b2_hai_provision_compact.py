#!/usr/bin/env python3
"""Focused structural validator for B2 Hai Provision Compact."""

from pathlib import Path
import re
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "data/hai/b2 hai provision compact.txt")
text = path.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 Hai Provision Compact: Offer"',
    'mission "B2 Hai Provision Compact: Review"',
    'mission "B2 Hai Provision Compact: Marr Remembers"',
]
for mission in required_missions:
    assert mission in text, f"missing {mission}"

for name in ("Tami", "Leah Marr"):
    assert name in text, f"missing named character {name}"

for route in ("route threshold", "route manifest", "route dual ledger"):
    assert f'"B2 Hai Provision Compact: {route}" = 1' in text, f"missing persistent {route}"

assert '"B2 Hai Provision Compact: declined" = 1' in text
assert text.count('"B2 Hai Provision Compact: settlement dual ledger" = 1') == 1
assert text.count('"B2 Hai Provision Compact: settlement bounded review" = 1') == 1

for settlement in ("settlement dual ledger", "settlement bounded review"):
    assert f'has "B2 Hai Provision Compact: {settlement}"' in text

# All three missions remain scoped to inhabited Hai-controlled sources.
assert text.count('government "Hai"') == 3
assert text.count('not attributes "uninhabited"') == 3

# Keep the slice narrative/state-only: no direct economy, combat, cargo, or reputation rewards.
for forbidden in (
    "\tcredits ",
    "\treputation ",
    "\tcargo ",
    "\toutfit ",
    "\tship ",
    "\tdestroy ",
    "\tcombat ",
):
    assert forbidden not in text, f"forbidden direct mutation token: {forbidden!r}"

# Every local goto target must have a corresponding label somewhere in the file.
gotos = set(re.findall(r"^\s*goto ([A-Za-z0-9_ -]+)\s*$", text, re.MULTILINE))
labels = set(re.findall(r"^\s*label ([A-Za-z0-9_ -]+)\s*$", text, re.MULTILINE))
missing = sorted(gotos - labels)
assert not missing, f"goto targets without labels: {missing}"

# Review consumes threshold/manifest explicitly; dual-ledger is the intended fallthrough path.
for route in ("threshold", "manifest"):
    assert f"branch {route}" in text
assert text.count('"B2 Hai Provision Compact: reviewed" = 1') == 2

# The aftermath reader must consume both mutually exclusive terminal settlements.
assert 'has "B2 Hai Provision Compact: settlement dual ledger"' in text
assert 'has "B2 Hai Provision Compact: settlement bounded review"' in text
assert 'not "B2 Hai Provision Compact: aftermath seen"' in text

print("PASS: B2 Hai Provision Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: review_routing=threshold/manifest branches + dual-ledger fallthrough")
print("PASS: terminal_settlements=2")
print("PASS: source_scope=inhabited Hai government")
print("PASS: later_reader=Marr Remembers")
print("PASS: persistence_model=stock mission/global conditions")
