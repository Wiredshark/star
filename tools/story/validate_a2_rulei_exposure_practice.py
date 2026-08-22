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
]
for token in required:
    assert token in text, f"missing required token: {token}"

assert text.count('mission "A2 Rulei Exposure Practice:') == 2
assert text.count('"A2 Rulei Exposure Practice:') >= 10

# A2 may consume B2 state but must never write it.
assert not re.search(r'^\s*"B2 Rulei Exposure Accountability:[^"]+"\s*[+\-*/]?=', text, re.M)
assert not re.search(r'^\s*"world:[^"]+"\s*[+\-*/]?=', text, re.M)

# Preserve the uncertainty boundary: no affirmative causal or motive claims.
for forbidden in (
    "the rulei caused lasting damage",
    "the rulei intended harm",
    "rulei authority",
    "rulei representative",
):
    assert forbidden not in text.lower(), f"unsupported authority/causation phrase: {forbidden}"

# Four persistent routes must all be represented in the later reflection.
for route in ("bounded warning", "consent purpose", "local only", "refused"):
    assert text.count(f'A2 Rulei Exposure Practice: {route}') >= 2, route

print("PASS: A2 Rulei Exposure Practice structural and ownership contract")
