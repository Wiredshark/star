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
    '"A2 Drak Stewardship Echo: introduced" = 1',
    '"A2 Drak Stewardship Echo: precedent private" = 1',
    '"A2 Drak Stewardship Echo: precedent bounded advice" = 1',
    '"A2 Drak Stewardship Echo: precedent method only" = 1',
    '"A2 Drak Stewardship Echo: reflection seen" = 1',
    'private name',
    'no Drak mandate',
    'Nobody invokes the Drak',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('mission "A2 Drak Stewardship Echo:') == 2
assert text.count('\toffer precedence 9') == 2, "both state-only missions must use offer precedence 9"
assert text.count('\n\t\t\tdecline') == 4, "all four state-only terminals must decline"
assert '\n\t\t\taccept' not in text, "state-only A2 missions must not leave objective-less accepted missions"
assert '\n\tobjective' not in text and '\n\twaypoint' not in text and '\n\tstopover' not in text
assert 'world:' not in text, "Drak stewardship echo must not consume or write A1 world state"

for forbidden in [
    'set "B2 Drak Memorial Custody Compact:',
    'clear "B2 Drak Memorial Custody Compact:',
    '"B2 Drak Memorial Custody Compact: aftermath seen" =',
    '"B2 Drak Memorial Custody Compact: settlement severed function archive" =',
]:
    assert forbidden not in text, f"forbidden upstream mutation: {forbidden}"

for route in ["precedent private", "precedent bounded advice", "precedent method only"]:
    assert f'has "A2 Drak Stewardship Echo: {route}"' in text, f"reflection missing explicit route gate: {route}"

assert text.count('"A2 Drak Stewardship Echo: precedent private" = 1') == 1
assert text.count('"A2 Drak Stewardship Echo: precedent bounded advice" = 1') == 1
assert text.count('"A2 Drak Stewardship Echo: precedent method only" = 1') == 1
assert "does not make you a Drak representative" in text
assert "no new authority is inferred" in text

print("PASS: A2 Drak Stewardship Echo current-main restage contract")
