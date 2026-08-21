#!/usr/bin/env python3
# Copyright (c) 2026 by Wiredshark
#
# Endless Sky is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.

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
    assert not stripped.startswith('"B2 Kor Efret Passage Continuity Compact:') or " = " not in stripped, f"B2 state write: {stripped}"

assert text.count('"A2 Kor Efret Passage Practice: introduced" = 1') == 3
assert text.count('"A2 Kor Efret Passage Practice: reflection seen" = 1') == 1
assert 'not "A2 Kor Efret Passage Practice: reflection seen"' in text
assert 'not "A2 Kor Efret Passage Practice: declined"' in text

# Both missions are state-only conversations. They must close rather than become
# objective-less accepted missions.
assert "\n\t\t\taccept\n" not in text, "state-only dialogue must not use accept"
assert text.count("\n\t\t\tdecline\n") == 5, "expected four briefing terminals plus one reflection terminal"

# Current A2 integration convention: explicit stable precedence on both offers.
assert text.count("\toffer precedence 9\n") == 2, "both missions must declare offer precedence 9"

# Refusal must not arm the positive reflection path.
refuse_block = text.split("\t\t\tlabel refuse\n", 1)[1].split("\n\nmission ", 1)[0]
assert '"A2 Kor Efret Passage Practice: introduced" = 1' not in refuse_block
assert '"A2 Kor Efret Passage Practice: declined" = 1' in refuse_block

print("A2 Kor Efret Passage Practice validator: PASS")
