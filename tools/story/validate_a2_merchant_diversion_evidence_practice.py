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
]
for token in required:
    assert token in s, token

# A1 and B2 inputs must remain read-only.
for line in s.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') or stripped.startswith('"B2 Merchant Diversion Compact:'):
        assert " = " not in stripped, f"upstream write: {stripped}"

# Three positive practices each receive a moderate and severe recurrence outcome.
assert s.count('label expiry severe') == 1
assert s.count('label lineage severe') == 1
assert s.count('label contradiction severe') == 1
assert s.count('mission "A2 Merchant Diversion Evidence Practice:') == 2
assert s.count('"A2 Merchant Diversion Evidence Practice: introduced" = 1') == 3
assert 'centralized Merchant route authority' in s
print("PASS: Merchant diversion evidence practice structure and ownership")
