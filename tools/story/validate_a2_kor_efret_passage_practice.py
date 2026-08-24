#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/korath/a2 kor efret passage practice.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Kor Efret Passage Practice: Briefing"',
    'mission "A2 Kor Efret Passage Practice: Reflection"',
    'has "B2 Kor Efret Passage Continuity Compact: aftermath seen"',
    '"A2 Kor Efret Passage Practice: consent current" = 1',
    '"A2 Kor Efret Passage Practice: separate closure" = 1',
    '"A2 Kor Efret Passage Practice: local only" = 1',
    '"A2 Kor Efret Passage Practice: declined" = 1',
    '"A2 Kor Efret Passage Practice: reflection seen" = 1',
    'branch consent', 'branch closure', 'branch local',
    'label consent', 'label closure', 'label local', 'label done',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('offer precedence 9') == 2
assert text.count('\n\t\t\tdecline') == 5
assert '\n\t\t\taccept' not in text
assert text.count('"A2 Kor Efret Passage Practice: introduced" = 1') == 3
assert text.count('"A2 Kor Efret Passage Practice: reflection seen" = 1') == 1
assert text.count('goto done') == 3
assert 'not "A2 Kor Efret Passage Practice: reflection seen"' in text
assert text.count('not "A2 Kor Efret Passage Practice: declined"') == 2

for line in text.splitlines():
    stripped = line.strip()
    if " = " in stripped:
        assert '"A2 Kor Efret Passage Practice:' in stripped, f"foreign state write: {stripped}"
    assert '"world:' not in stripped, f"unexpected world-state dependency: {stripped}"

for forbidden in ('\tdestination ', '\tstopover ', '\twaypoint ', '\tcargo ', '\toutfit ', '\tcredits ', '\treputation '):
    assert forbidden not in text, f"unexpected gameplay objective/mutation directive: {forbidden.strip()}"

assert "no authority" not in text.lower() or "authority" in text.lower()
print("A2 Kor Efret Passage Practice validator: PASS")
