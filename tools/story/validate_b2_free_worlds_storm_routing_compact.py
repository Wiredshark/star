#!/usr/bin/env python3
"""Focused structural validator for B2 Free Worlds Storm Routing Compact."""

from pathlib import Path
import re
import sys

path = Path(
    sys.argv[1]
    if len(sys.argv) > 1
    else "data/human/b2 free worlds storm routing compact.txt"
)
text = path.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 Free Worlds Storm Routing Compact: Offer"',
    'mission "B2 Free Worlds Storm Routing Compact: Review"',
    'mission "B2 Free Worlds Storm Routing Compact: Edden Remembers"',
]
for mission in required_missions:
    assert mission in text, f"missing {mission}"

for character in ("Mara Edden", "Colm Rusk"):
    assert character in text, f"missing recurring character {character}"

for route in ("route verification", "route field", "route paired"):
    assert (
        f'"B2 Free Worlds Storm Routing Compact: {route}" = 1' in text
    ), f"missing persistent route {route}"

assert '"B2 Free Worlds Storm Routing Compact: declined" = 1' in text
assert text.count(
    '"B2 Free Worlds Storm Routing Compact: settlement confidence packet" = 1'
) == 1
assert text.count(
    '"B2 Free Worlds Storm Routing Compact: settlement challenge board" = 1'
) == 1

# All three missions stay within Free Worlds space.
assert text.count('government "Free Worlds"') == 3

# A1 storm/navigation state is consumed read-only.
for signal in (
    "world: free worlds geomagnetic storm active",
    "world: free worlds geomagnetic navigation strain",
):
    assert signal in text, f"missing A1 input {signal}"

# Offer occurs under meaningful live storm pressure; Review waits for recovery.
assert 'has "world: free worlds geomagnetic storm active"' in text
assert '"world: free worlds geomagnetic navigation strain" >= 3' in text
assert 'not "world: free worlds geomagnetic storm active"' in text
assert '"world: free worlds geomagnetic navigation strain" <= 1' in text

# Core B1 continuity concepts stay explicit.
for concept in (
    "calibration",
    "verification",
    "uncertainty",
    "expiry",
    "contradictory",
    "copied",
):
    assert concept in text.lower(), f"missing storm-routing continuity concept: {concept}"

# Preserve distributed Free Worlds authority rather than inventing a central office.
for phrase in (
    "not a centralized Free Worlds navigation office",
    "Each Free Worlds port may still choose its own traffic response",
    "rather than a single authoritative route",
):
    assert phrase in text, f"missing distributed-authority boundary: {phrase}"

# All persistent writes are B2-owned conditions. Read-only A1 conditions may appear
# in to-offer blocks but must never be assigned or cleared.
writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, re.MULTILINE)
assert writes, "no persistent B2 writes found"
foreign = [
    name
    for name in writes
    if not name.startswith("B2 Free Worlds Storm Routing Compact:")
]
assert not foreign, f"foreign condition writes: {foreign}"

for forbidden_world_write in (
    '"world: free worlds geomagnetic storm active" =',
    '"world: free worlds geomagnetic navigation strain" =',
    'clear "world: free worlds geomagnetic storm active"',
    'clear "world: free worlds geomagnetic navigation strain"',
):
    assert forbidden_world_write not in text, f"A1 authority violation: {forbidden_world_write}"

# No direct material, reputation, combat, cargo, outfit, ship, or fleet mutation.
for forbidden in (
    "\tcredits ",
    "\treputation ",
    "\tcargo ",
    "\toutfit ",
    "\tship ",
    "\tfleet ",
    "\tdestroy ",
    "\tcombat ",
):
    assert forbidden not in text, f"forbidden direct mutation token: {forbidden!r}"

# These missions are dialogue/state-only. They must not remain accepted without
# objectives after the conversation closes.
assert re.search(r"^\s*accept\s*$", text, re.MULTILINE) is None, \
    "state-only dialogue must not use terminal accept"
assert len(re.findall(r"^\s*decline\s*$", text, re.MULTILINE)) == 7, \
    "expected exactly seven state-only decline terminals"
for objective in (
    "\tdestination ",
    "\tstopover ",
    "\twaypoint ",
    "\tnpc ",
    "\tcargo ",
    "\tpassenger ",
    "\tdeadline ",
    "\ttimer ",
):
    assert objective not in text, f"unexpected gameplay objective token: {objective!r}"

# Every goto target resolves to a local label.
gotos = set(re.findall(r"^\s*goto ([A-Za-z0-9_ -]+)\s*$", text, re.MULTILINE))
labels = set(re.findall(r"^\s*label ([A-Za-z0-9_ -]+)\s*$", text, re.MULTILINE))
missing = sorted(gotos - labels)
assert not missing, f"goto targets without labels: {missing}"

# Review explicitly branches on verification and field routes, with paired route as
# the intentional fallthrough, and writes exactly one of two terminal settlements.
for route in ("verify", "field"):
    assert f"branch {route}" in text
assert text.count('"B2 Free Worlds Storm Routing Compact: reviewed" = 1') == 2

# Aftermath consumes either terminal settlement once.
for settlement in ("settlement confidence packet", "settlement challenge board"):
    assert f'has "B2 Free Worlds Storm Routing Compact: {settlement}"' in text
assert 'not "B2 Free Worlds Storm Routing Compact: aftermath seen"' in text

print("PASS: B2 Free Worlds Storm Routing Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=Mara Edden + Colm Rusk")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: dialogue_lifecycle=7 decline terminals, 0 accept terminals")
print("PASS: A1 geomagnetic storm/navigation state=read only")
print("PASS: authority=distributed Free Worlds coordination, no central navigation office")
print("PASS: mutation_surface=B2 conditions only")
print("PASS: later_reader=Edden Remembers")
