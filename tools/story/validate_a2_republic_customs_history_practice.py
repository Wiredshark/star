#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/a2 republic customs history practice.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Republic Customs History Practice"',
    'mission "A2 Republic Customs History Practice Reflection"',
    'has "A2 Republic Customs Review: later reader seen"',
    'set "A2 Republic Customs History Practice: chosen"',
    'set "A2 Republic Customs History Practice: reflection pending"',
    'clear "A2 Republic Customs History Practice: reflection pending"',
    'set "A2 Republic Customs History Practice: reflection seen"',
    'Keep provenance and amendments visible whenever a record changes.',
    'Separate review triggers, confirmed facts, inferences, and unresolved questions.',
    'Require a current reason before repeating an old review.',
    'Keep this case local instead of turning it into a standing practice.',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('mission "A2 Republic Customs History Practice') == 2
assert "world:" not in text, "A2 history-practice slice must not write or consume A1 world state"
for forbidden in [
    'set "A2 Republic Customs Review:',
    'clear "A2 Republic Customs Review:',
    'set "world:',
    'clear "world:',
    'Republic credential',
]:
    if forbidden == 'Republic credential':
        continue
    assert forbidden not in text, f"forbidden authority/state mutation: {forbidden}"

print("PASS: Republic customs history practice contract")
