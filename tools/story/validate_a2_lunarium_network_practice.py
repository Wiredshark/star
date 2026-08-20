#!/usr/bin/env python3
from pathlib import Path

p = Path("data/coalition/a2 lunarium network practice.txt")
s = p.read_text(encoding="utf-8")
required = [
    'mission "A2 Lunarium Network Practice: briefing"',
    'mission "A2 Lunarium Network Practice: reflection"',
    'has "joined the lunarium"',
    'not "joined the heliarchs"',
    'set "A2 Lunarium Network Practice: aid boundary"',
    'set "A2 Lunarium Network Practice: compartmented"',
    'set "A2 Lunarium Network Practice: evidence discipline"',
    'set "A2 Lunarium Network Practice: refused"',
    'set "A2 Lunarium Network Practice: reflected"',
]
missing = [x for x in required if x not in s]
if missing:
    raise SystemExit("missing required contracts: " + repr(missing))
for forbidden in ('set "world:', 'clear "world:', 'set "joined the lunarium"', 'set "joined the heliarchs"'):
    if forbidden in s:
        raise SystemExit("forbidden ownership mutation: " + forbidden)
if s.count('set "A2 Lunarium Network Practice: decided"') != 4:
    raise SystemExit("each briefing route must persist a decision")
if 'not "A2 Lunarium Network Practice: refused"' not in s:
    raise SystemExit("refusal must suppress reflection")
print("A2 Lunarium Network Practice validator: PASS")
