#!/usr/bin/env python3
from pathlib import Path

path = Path("data/coalition/a2 lunarium network practice.txt")
text = path.read_text(encoding="utf-8")

required = [
    'mission "A2 Lunarium Network Practice: Briefing"',
    'mission "A2 Lunarium Network Practice: Reflection"',
    'has "joined the lunarium"',
    'not "joined the heliarchs"',
    'set "A2 Lunarium Network Practice: aid boundary"',
    'set "A2 Lunarium Network Practice: compartmented"',
    'set "A2 Lunarium Network Practice: evidence discipline"',
    'set "A2 Lunarium Network Practice: refused"',
    'set "A2 Lunarium Network Practice: reflected"',
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("missing required contracts: " + repr(missing))

for forbidden in (
    'set "world:',
    'clear "world:',
    'set "joined the lunarium"',
    'clear "joined the lunarium"',
    'set "joined the heliarchs"',
    'clear "joined the heliarchs"',
):
    if forbidden in text:
        raise SystemExit("forbidden ownership mutation: " + forbidden)

if text.count('set "A2 Lunarium Network Practice: decided"') != 4:
    raise SystemExit("each Briefing route must persist a decision")
if text.count("offer precedence 9") != 2:
    raise SystemExit("both state-only missions must use offer precedence 9")
if text.count("\n\t\t\t\tdecline") != 5:
    raise SystemExit("all five state-only terminal paths must decline")
if "\n\t\t\t\taccept" in text:
    raise SystemExit("state-only dialogue must not use accept")
if 'not "A2 Lunarium Network Practice: refused"' not in text:
    raise SystemExit("refusal must suppress Reflection")
if text.count('set "A2 Lunarium Network Practice: reflected"') != 1:
    raise SystemExit("Reflection must be one-shot")

reflection = text.split('mission "A2 Lunarium Network Practice: Reflection"', 1)[1]
for route in (
    'has "A2 Lunarium Network Practice: aid boundary"',
    'has "A2 Lunarium Network Practice: compartmented"',
    'has "A2 Lunarium Network Practice: evidence discipline"',
):
    if route not in reflection:
        raise SystemExit("Reflection missing route gate: " + route)

print("A2 Lunarium Network Practice validator: PASS")
