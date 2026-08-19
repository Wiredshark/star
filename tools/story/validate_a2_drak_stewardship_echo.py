#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/drak/a2 drak stewardship echo.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Drak Stewardship Echo: Offer"',
    'mission "A2 Drak Stewardship Echo: Later Reflection"',
    'has "B2 Drak Memorial Custody Compact: aftermath seen"',
    'has "B2 Drak Memorial Custody Compact: settlement severed function archive"',
    '"A2 Drak Stewardship Echo: precedent private" = 1',
    '"A2 Drak Stewardship Echo: precedent bounded advice" = 1',
    '"A2 Drak Stewardship Echo: precedent method only" = 1',
    '"A2 Drak Stewardship Echo: reflection seen" = 1',
]
for token in required:
    assert token in text, f"missing required token: {token}"

assert text.count('mission "A2 Drak Stewardship Echo:') == 2
assert text.count('"A2 Drak Stewardship Echo: precedent private" = 1') == 1
assert text.count('"A2 Drak Stewardship Echo: precedent bounded advice" = 1') == 1
assert text.count('"A2 Drak Stewardship Echo: precedent method only" = 1') == 1

# A2 may read B2 state but must never write it.
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"B2 Drak Memorial Custody Compact:'):
        assert "=" not in stripped, f"illegal B2 state write: {stripped}"
    if stripped.startswith('"world:'):
        raise AssertionError(f"unexpected world-state write/use: {stripped}")

# The content must preserve the non-authority/privacy boundary explicitly.
for phrase in ("private name", "no Drak mandate", "Nobody invokes the Drak"):
    assert phrase in text, f"missing authority boundary: {phrase}"

print("PASS: A2 Drak Stewardship Echo structural and ownership contract")
