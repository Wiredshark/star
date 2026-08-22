#!/usr/bin/env python3
from pathlib import Path

p = Path("data/human/a2 merchant diversion evidence practice.txt")
s = p.read_text(encoding="utf-8")

required = [
    'mission "A2 Merchant Diversion Evidence Practice: Briefing"',
    'mission "A2 Merchant Diversion Evidence Practice: Recurrence"',
    'has "B2 Merchant Diversion Compact: aftermath seen"',
    'has "B2 Merchant Diversion Compact: settlement ladder"',
    '"world: merchant route diversion pressure" >= 3',
    '"world: merchant route diversion pressure" >= 5',
    '"A2 Merchant Diversion Evidence Practice: expiry" = 1',
    '"A2 Merchant Diversion Evidence Practice: lineage" = 1',
    '"A2 Merchant Diversion Evidence Practice: contradiction" = 1',
    '"A2 Merchant Diversion Evidence Practice: declined" = 1',
    '"A2 Merchant Diversion Evidence Practice: recurrence seen" = 1',
    'centralized Merchant route authority',
]
for token in required:
    assert token in s, token

# A1 and B2 inputs must remain read-only.
for line in s.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') or stripped.startswith('"B2 Merchant Diversion Compact:'):
        assert " = " not in stripped, f"upstream write: {stripped}"

# A2 writes are confined to this slice's namespace.
for line in s.splitlines():
    stripped = line.strip()
    if " = " in stripped and stripped.startswith('"'):
        assert stripped.startswith('"A2 Merchant Diversion Evidence Practice:'), f"foreign write: {stripped}"

# This is a dialogue/state-only slice: it must never create an accepted objective-less mission.
assert s.count("\taccept") == 0, "state-only accept endpoint found"
assert s.count("\t\t\tdecline") == 5, "expected four briefing terminals plus one recurrence terminal"
assert s.count("\toffer precedence 9") == 2, "both state-only missions need current precedence"
for forbidden in ("\tdestination ", "\twaypoint ", "\tstopover ", "\tcargo ", "\tpassengers ", "\tnpc ", "\tdeadline "):
    assert forbidden not in s, f"unexpected gameplay objective directive: {forbidden!r}"

# Three positive practices each receive a moderate and severe recurrence outcome.
assert s.count('label expiry severe') == 1
assert s.count('label lineage severe') == 1
assert s.count('label contradiction severe') == 1
assert s.count('mission "A2 Merchant Diversion Evidence Practice:') == 2
assert s.count('"A2 Merchant Diversion Evidence Practice: introduced" = 1') == 3

# Refusal is a true boundary: it does not introduce/arm recurrence.
decline_block = s.split("\t\t\tlabel decline", 1)[1].split("\n\n\nmission ", 1)[0]
assert '"A2 Merchant Diversion Evidence Practice: declined" = 1' in decline_block
assert '"A2 Merchant Diversion Evidence Practice: introduced" = 1' not in decline_block

print("PASS: Merchant diversion evidence practice structure, ownership, lifecycle, and refusal")
