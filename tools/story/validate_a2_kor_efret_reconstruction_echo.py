#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/korath/a2 kor efret reconstruction echo.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Kor Efret Reconstruction Echo: Practice"',
    'mission "A2 Kor Efret Reconstruction Echo: Reflection"',
    'has "B2 Kor Efret Reconstruction Compact: aftermath seen"',
    'has "B2 Kor Efret Reconstruction Compact: settlement restoration priority"',
    '"A2 Kor Efret Reconstruction Echo: route local" = 1',
    '"A2 Kor Efret Reconstruction Echo: route method" = 1',
    '"A2 Kor Efret Reconstruction Echo: route example" = 1',
    '"A2 Kor Efret Reconstruction Echo: reflection seen" = 1',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('mission "A2 Kor Efret Reconstruction Echo:') == 2
assert text.count('"A2 Kor Efret Reconstruction Echo: route ') == 6, "each route should be written once and read once"

# This consumer may read B2 state, but never write it.
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"B2 Kor Efret Reconstruction Compact:'):
        assert "=" not in stripped and "+=" not in stripped and "-=" not in stripped, f"illegal B2 write: {stripped}"
    if stripped.startswith('"world:'):
        raise AssertionError(f"A2 reconstruction echo must not use world-state authority: {stripped}")

for forbidden in ["credits", "reputation", "government reputation", "cargo ", "outfit ", "ship ", "fleet "]:
    assert forbidden not in text.lower(), f"forbidden gameplay mutation surface: {forbidden}"

for phrase in [
    "does not make me an authority",
    "borrowed authority",
    "evidence, not command",
    "neither title nor standing authority",
]:
    assert phrase in text, f"missing authority-boundary phrase: {phrase}"

print("PASS: A2 Kor Efret Reconstruction Echo contracts")
