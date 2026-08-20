#!/usr/bin/env python3
"""Focused structural validator for B2 Unfettered Maintenance Compact."""

from pathlib import Path
import re
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "data/hai/b2 unfettered maintenance compact.txt")
text = path.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 Unfettered Maintenance Compact: Offer"',
    'mission "B2 Unfettered Maintenance Compact: Review"',
    'mission "B2 Unfettered Maintenance Compact: Keeper Remembers"',
]
for mission in required_missions:
    assert mission in text, f"missing {mission}"

for shorthand in ("Keeper", "Mechanic"):
    assert shorthand in text, f"missing recurring character shorthand {shorthand}"

for route in ("route obligation", "route risk", "route paired ledger"):
    assert f'"B2 Unfettered Maintenance Compact: {route}" = 1' in text, f"missing persistent {route}"

assert '"B2 Unfettered Maintenance Compact: declined" = 1' in text
assert text.count('"B2 Unfettered Maintenance Compact: settlement portable packet" = 1') == 1
assert text.count('"B2 Unfettered Maintenance Compact: settlement reconciliation" = 1') == 1

# Preserve the B1/campaign scope on all three missions.
assert text.count('attributes "unfettered"') == 3
assert text.count('has "First Contact: Unfettered: offered"') == 3
assert text.count('not "event: wanderers: unfettered invasion starts"') == 3

# The core B1 continuity concepts must be explicit.
for concept in (
    "emergency",
    "diversion",
    "obligation",
    "replacement",
    "priority",
):
    assert concept in text.lower(), f"missing maintenance continuity concept: {concept}"

# Character labels are explicitly player shorthand, not canonical offices.
assert "player-facing shorthand" in text
assert "not canonical titles" in text

# Keep the slice narrative/state-only: no direct economy, combat, cargo, outfit, ship, or reputation mutation.
for forbidden in (
    "\tcredits ",
    "\treputation ",
    "\tcargo ",
    "\toutfit ",
    "\tship ",
    "\tfleet ",
    "\tdestroy ",
    "\tcombat ",
    "\tworld:",
):
    assert forbidden not in text, f"forbidden direct mutation token: {forbidden!r}"

# All action writes are B2-owned conditions.
actions = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, re.MULTILINE)
assert actions, "no persistent condition writes found"
foreign = [name for name in actions if not name.startswith("B2 Unfettered Maintenance Compact:")]
assert not foreign, f"foreign condition writes: {foreign}"

# Every local goto target has a label somewhere in the file.
gotos = set(re.findall(r"^\s*goto ([A-Za-z0-9_ -]+)\s*$", text, re.MULTILINE))
labels = set(re.findall(r"^\s*label ([A-Za-z0-9_ -]+)\s*$", text, re.MULTILINE))
missing = sorted(gotos - labels)
assert not missing, f"goto targets without labels: {missing}"

# Review explicitly consumes obligation/risk, with paired-ledger as intended fallthrough.
for route in ("obligation", "risk"):
    assert f"branch {route}" in text
assert text.count('"B2 Unfettered Maintenance Compact: reviewed" = 1') == 2

# Aftermath consumes both terminal settlements once.
for settlement in ("settlement portable packet", "settlement reconciliation"):
    assert f'has "B2 Unfettered Maintenance Compact: {settlement}"' in text
assert 'not "B2 Unfettered Maintenance Compact: aftermath seen"' in text

print("PASS: B2 Unfettered Maintenance Compact structure validated")
print("PASS: missions=3")
print("PASS: recurring_characters=Keeper + Mechanic player shorthand")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: source_scope=Unfettered + first contact + pre-invasion")
print("PASS: mutation_surface=B2 conditions only")
print("PASS: continuity=priority/diversion/unfinished obligation remain distinct")
print("PASS: later_reader=Keeper Remembers")
