#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/a2 republic customs history practice.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Republic Customs History Practice"',
    'mission "A2 Republic Customs History Practice Reflection"',
    'has "A2 Republic Customs Review: later reader seen"',
    '"offer precedence" 8',
    '"A2 Republic Customs History Practice: decided" = 1',
    '"A2 Republic Customs History Practice: provenance" = 1',
    '"A2 Republic Customs History Practice: basis separation" = 1',
    '"A2 Republic Customs History Practice: current reason" = 1',
    '"A2 Republic Customs History Practice: local only" = 1',
    '"A2 Republic Customs History Practice: reflection pending" = 1',
    '"A2 Republic Customs History Practice: reflection pending" = 0',
    '"A2 Republic Customs History Practice: reflection seen" = 1',
    'Keep provenance and amendments visible whenever a record changes.',
    'Separate review triggers, confirmed facts, inferences, and unresolved questions.',
    'Require a current reason before repeating an old review.',
    'Keep this case local instead of turning it into a standing practice.',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('mission "A2 Republic Customs History Practice') == 2
assert text.count('"offer precedence" 8') == 2
assert text.count('\n\t\t\t\tdecline') == 5, "all five state-only terminals must decline"
assert '\n\t\t\t\taccept' not in text, "state-only A2 missions must not leave objective-less accepted missions"
assert '\n\tobjective' not in text and '\n\twaypoint' not in text and '\n\tstopover' not in text
assert "world:" not in text, "this history-practice slice must not consume or write A1 world state"

for forbidden in [
    '"A2 Republic Customs Review:' + ' later reader seen" =',
    'set "A2 Republic Customs Review:',
    'clear "A2 Republic Customs Review:',
    'set "world:',
    'clear "world:',
]:
    assert forbidden not in text, f"forbidden upstream/world mutation: {forbidden}"

for route in ["provenance", "basis separation", "current reason", "local only"]:
    assert f'has "A2 Republic Customs History Practice: {route}"' in text, f"reflection missing route gate: {route}"

assert "Republic credential" in text, "authority disclaimer must remain explicit"
assert "procedure itself guarantees correctness" in text, "epistemic boundary must remain explicit"

print("PASS: Republic customs history practice restage contract")
