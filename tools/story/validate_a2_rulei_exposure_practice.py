#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/rulei/a2 rulei exposure practice.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Rulei Exposure Practice: Offer"',
    'mission "A2 Rulei Exposure Practice: Reflection"',
    'has "B2 Rulei Exposure Accountability: aftermath seen"',
    'has "B2 Rulei Exposure Accountability: settlement consent escrow"',
    '"A2 Rulei Exposure Practice: bounded warning" = 1',
    '"A2 Rulei Exposure Practice: consent purpose" = 1',
    '"A2 Rulei Exposure Practice: local only" = 1',
    '"A2 Rulei Exposure Practice: refused" = 1',
    '"A2 Rulei Exposure Practice: reflection seen" = 1',
    'not "A2 Rulei Exposure Practice: refused"',
    '"offer precedence" 9',
]
for token in required:
    assert token in text, f"missing required token: {token}"

assert text.count('mission "A2 Rulei Exposure Practice:') == 2
assert text.count('"offer precedence" 9') == 2
assert text.count('\n\t\t\t\tdecline\n') == 5, "expected five state-only decline terminals"
assert not re.search(r'^\s*accept\s*$', text, re.M), "state-only mission must not accept"

# These missions are dialogue/state-only. Gameplay-objective directives would invalidate
# the lifecycle assumption and require a different mission contract.
for directive in (
    "destination ",
    "waypoint ",
    "npc ",
    "cargo ",
    "passengers ",
    "deadline ",
):
    assert not re.search(rf'^\s*{re.escape(directive)}', text, re.M), directive

# A2 may consume B2 state but must never write it or simulation state.
assert not re.search(r'^\s*"B2 Rulei Exposure Accountability:[^"]+"\s*[+\-*/]?=', text, re.M)
assert not re.search(r'^\s*"world:[^"]+"\s*[+\-*/]?=', text, re.M)

# All writes must stay in the A2 namespace.
for match in re.finditer(r'^\s*"([^"]+)"\s*[+\-*/]?=', text, re.M):
    assert match.group(1).startswith("A2 Rulei Exposure Practice:"), match.group(1)

# Preserve the uncertainty/authority boundary.
for forbidden in (
    "the rulei caused lasting damage",
    "the rulei intended harm",
    "rulei authority",
    "rulei representative",
):
    assert forbidden not in text.lower(), f"unsupported authority/causation phrase: {forbidden}"

# Positive practices must be explicitly gated in the later reflection.
for route in ("bounded warning", "consent purpose", "local only"):
    assert text.count(f'A2 Rulei Exposure Practice: {route}') >= 2, route
    assert f'has "A2 Rulei Exposure Practice: {route}"' in text, route

# Refusal is persistent but must not arm the later reflection.
reflection = text.split('mission "A2 Rulei Exposure Practice: Reflection"', 1)[1]
assert 'not "A2 Rulei Exposure Practice: refused"' in reflection
assert 'label refuse' not in reflection
assert 'has "B2 Rulei Exposure Accountability: aftermath seen"' in reflection

print("PASS: A2 Rulei Exposure Practice lifecycle, persistence, and ownership contract")
