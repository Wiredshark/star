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
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

# A2 may read B2 state but must never mutate B2/world state.
for line in text.splitlines():
    stripped = line.strip()
    if " = " in stripped:
        assert '"A2 Kor Efret Passage Practice:' in stripped, f"foreign state write: {stripped}"
    assert '"world:' not in stripped, f"unexpected world-state dependency: {stripped}"

assert text.count('"A2 Kor Efret Passage Practice: introduced" = 1') == 3
assert text.count('"A2 Kor Efret Passage Practice: reflection seen" = 1') == 1
assert 'not "A2 Kor Efret Passage Practice: reflection seen"' in text
assert 'not "A2 Kor Efret Passage Practice: declined"' in text
print("A2 Kor Efret Passage Practice validator: PASS")
