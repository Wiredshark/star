#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/a2 syndicate qualification practice.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Syndicate Qualification Practice: Adopt"',
    'mission "A2 Syndicate Qualification Practice: Pressure Test"',
    'B2 Syndicate Qualification Compact: aftermath seen',
    'B2 Syndicate Qualification Compact: settlement renewal',
    'A2 Syndicate Qualification Practice: evidence first',
    'A2 Syndicate Qualification Practice: boundaries travel',
    'A2 Syndicate Qualification Practice: local only',
    'A2 Syndicate Qualification Practice: refused',
    'world: syndicate labor strain',
    'world: syndicate labor rotation active',
    'A2 Syndicate Qualification Practice: pressure test seen',
]
for token in required:
    assert token in text, f"missing required token: {token}"

assert text.count('mission "A2 Syndicate Qualification Practice:') == 2
assert text.count('"A2 Syndicate Qualification Practice: adopted" = 1') == 3
assert text.count('"A2 Syndicate Qualification Practice: refused" = 1') == 1
assert text.count('"A2 Syndicate Qualification Practice: pressure test seen" = 1') == 1

# Upstream A1/B2 authority is read-only. Conditions may appear, assignments may not.
for forbidden in [
    '"world: syndicate labor strain" =',
    '"world: syndicate labor rotation active" =',
    '"B2 Syndicate Qualification Compact:',
]:
    if forbidden.startswith('"B2'):
        for line in text.splitlines():
            assert not (forbidden in line and "=" in line), f"illegal B2 write: {line}"
    else:
        assert forbidden not in text, f"illegal upstream write: {forbidden}"

# Refusal must not arm the later pressure test.
refusal = text.split('label refuse', 1)[1].split('mission "A2 Syndicate Qualification Practice: Pressure Test"', 1)[0]
assert '"A2 Syndicate Qualification Practice: adopted" = 1' not in refusal

print("PASS: A2 Syndicate Qualification Practice; 2 missions; 3 positive practices + refusal; A1/B2 read-only")
