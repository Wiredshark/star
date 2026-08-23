#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/coalition/a2 saryd seed practice echo.txt"
text = PATH.read_text(encoding="utf-8")
lines = text.splitlines()

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
    'has "A2 Saryd Seed Practice Echo: route local"',
    'has "A2 Saryd Seed Practice Echo: route method"',
    'has "A2 Saryd Seed Practice Echo: route bounded example"',
    'not Saryd names or offices',
    'without treating your silence as permission',
]
for needle in required:
    assert needle in text, f"missing required content: {needle}"

assert text.count('mission "A2 Saryd Seed Practice Echo:') == 2
assert text.count("offer precedence 9") == 2, "both state-only missions need precedence 9"
assert text.count("\n\t\t\tdecline") == 5, "all five state-only terminal paths must decline"
assert "\n\t\t\taccept" not in text, "state-only A2 missions must not accept"

writes = "\n".join(line for line in lines if " = " in line)
assert '"B2 Saryd Seed Stewardship:' not in writes, "A2 must not write B2 stewardship state"
assert '"world:' not in writes, "A2 must not write world state"
assert all(
    '"A2 Saryd Seed Practice Echo:' in line
    for line in lines
    if " = " in line and line.lstrip().startswith('"')
), "persistent writes must remain in the A2 Saryd namespace"

assert text.count('has "B2 Saryd Seed Stewardship: aftermath seen"') == 2, (
    "Offer and Reflection must both recheck B2 aftermath"
)
assert text.count('has "A2 Saryd Seed Practice Echo: route local"') == 1
assert text.count('has "A2 Saryd Seed Practice Echo: route method"') == 1
assert text.count('has "A2 Saryd Seed Practice Echo: route bounded example"') == 1

objective_prefixes = ("cargo ", "passengers ", "destination ", "waypoint ", "stopover ")
for line in lines:
    stripped = line.lstrip("\t")
    if len(line) - len(stripped) >= 1 and not stripped.startswith("`"):
        assert not stripped.startswith(objective_prefixes), f"unexpected gameplay objective directive: {line}"

assert '"A2 Saryd Seed Practice Echo: introduced" = 1' not in text.split('label refuse', 1)[1].split('mission "A2 Saryd Seed Practice Echo: Reflection"', 1)[0], (
    "refusal must not arm Reflection"
)

print("PASS: A2 Saryd Seed Practice Echo restage structural contract")
