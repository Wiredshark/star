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
assert text.count('\toffer precedence 9') == 2, "both state-only missions must use precedence 9"
assert text.count('"A2 Syndicate Qualification Practice: adopted" = 1') == 3
assert text.count('"A2 Syndicate Qualification Practice: refused" = 1') == 1
assert text.count('"A2 Syndicate Qualification Practice: pressure test seen" = 1') == 1

# State-only dialogue must not leave objective-less missions accepted.
assert '\n\t\t\taccept\n' not in text, "state-only A2 dialogue may not terminate with accept"
assert text.count('\n\t\t\tdecline\n') == 5, "expected four Adopt terminals plus one Pressure Test terminal"

# Upstream A1/B2 authority is read-only. Conditions may appear, assignments may not.
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world: syndicate labor strain"') or stripped.startswith('"world: syndicate labor rotation active"'):
        assert " = " not in stripped, f"illegal A1 write: {line}"
    if stripped.startswith('"B2 Syndicate Qualification Compact:'):
        assert " = " not in stripped, f"illegal B2 write: {line}"

# Only A2 namespaced state may be assigned.
for line in text.splitlines():
    stripped = line.strip()
    if ' = ' in stripped:
        assert stripped.startswith('"A2 Syndicate Qualification Practice:'), f"unexpected state write: {line}"

adopt, pressure = text.split('mission "A2 Syndicate Qualification Practice: Pressure Test"', 1)

# Refusal must be a terminal boundary and must not arm the later pressure test.
refusal = adopt.split('label refuse', 1)[1]
assert '"A2 Syndicate Qualification Practice: adopted" = 1' not in refusal
assert '"A2 Syndicate Qualification Practice: refused" = 1' in refusal
assert '\n\t\t\tdecline\n' in refusal

# The later reader is genuinely tied to live A1 labor pressure and is one-shot.
assert '"world: syndicate labor strain" >= 2' in pressure
assert 'has "world: syndicate labor rotation active"' in pressure
assert 'not "A2 Syndicate Qualification Practice: pressure test seen"' in pressure
assert pressure.count('"A2 Syndicate Qualification Practice: pressure test seen" = 1') == 1

# Positive routes remain distinct and exhaustive.
for condition in [
    'A2 Syndicate Qualification Practice: evidence first',
    'A2 Syndicate Qualification Practice: boundaries travel',
    'A2 Syndicate Qualification Practice: local only',
]:
    assert text.count(condition) >= 1

print("PASS: A2 Syndicate Qualification Practice restage; 2 state-only missions; 3 positive practices + refusal; A1/B2 read-only; lifecycle decline enforced")
