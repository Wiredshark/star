#!/usr/bin/env python3
from pathlib import Path

p = Path("data/human/a2 merchant recovery margin practice.txt")
s = p.read_text(encoding="utf-8")

required = [
    'mission "A2 Merchant Recovery Margin Practice: Briefing"',
    'mission "A2 Merchant Recovery Margin Practice: Pressure Test"',
    'has "B2 Merchant Recovery Margin Compact: aftermath seen"',
    '"world: merchant repair backlog" >= 3',
    'has "world: merchant repair surge"',
    '"A2 Merchant Recovery Margin Practice: continuity" = 1',
    '"A2 Merchant Recovery Margin Practice: challenge" = 1',
    '"A2 Merchant Recovery Margin Practice: local" = 1',
    '"A2 Merchant Recovery Margin Practice: declined" = 1',
    '"A2 Merchant Recovery Margin Practice: pressure test seen" = 1',
]
for token in required:
    assert token in s, token

# A1 and B2 inputs must remain read-only.
for line in s.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') or stripped.startswith('"B2 Merchant Recovery Margin Compact:'):
        assert " = " not in stripped, f"upstream write: {stripped}"

assert s.count('label continuity surge') == 1
assert s.count('label challenge surge') == 1
assert s.count('label local surge') == 1
assert s.count('mission "A2 Merchant Recovery Margin Practice:') == 2
print("PASS: Merchant recovery margin practice structure and ownership")
