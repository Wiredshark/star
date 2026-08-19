#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/coalition/a2 saryd seed practice echo.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Saryd Seed Practice Echo: Offer"',
    'mission "A2 Saryd Seed Practice Echo: Reflection"',
    'has "B2 Saryd Seed Stewardship: aftermath seen"',
    'has "B2 Saryd Seed Stewardship: settlement local reserve covenant"',
    '"A2 Saryd Seed Practice Echo: route local" = 1',
    '"A2 Saryd Seed Practice Echo: route method" = 1',
    '"A2 Saryd Seed Practice Echo: route bounded example" = 1',
    '"A2 Saryd Seed Practice Echo: declined" = 1',
    '"A2 Saryd Seed Practice Echo: reflection seen" = 1',
]
for needle in required:
    assert needle in text, f"missing required content: {needle}"

assert text.count('mission "A2 Saryd Seed Practice Echo:') == 2
assert text.count('"A2 Saryd Seed Practice Echo: route ') >= 6
assert '"B2 Saryd Seed Stewardship:' not in "\n".join(
    line for line in text.splitlines() if " = " in line
), "A2 must not write B2 stewardship state"
assert '"world:' not in "\n".join(
    line for line in text.splitlines() if " = " in line
), "A2 must not write world state"
assert "not Saryd names or offices" in text
assert "without treating your silence as permission" in text
print("PASS: A2 Saryd Seed Practice Echo structural contract")
