#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/incipias/a2 hicemus contact practice.txt"
text = PATH.read_text(encoding="utf-8")
lines = text.splitlines()

required = [
    'mission "A2 Hicemus Contact Practice: Review"',
    'mission "A2 Hicemus Contact Practice: Reflection"',
    'has "Incipias: Help The Stranded 2: done"',
    'set "A2 Hicemus Contact Practice: observation first"',
    'set "A2 Hicemus Contact Practice: revision first"',
    'set "A2 Hicemus Contact Practice: local only"',
    'set "A2 Hicemus Contact Practice: refused"',
    'set "A2 Hicemus Contact Practice: decided"',
    'set "A2 Hicemus Contact Practice: reflection seen"',
    'not "A2 Hicemus Contact Practice: refused"',
    'label done',
    'label observation',
    'label revision',
    'label local',
    'label finish',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('mission "A2 Hicemus Contact Practice:') == 2
assert text.count('government "Hicemus"') == 2
assert text.count('offer precedence 9') == 2
assert text.count('\n\t\t\tdecline') == 2, "expected one converged Review terminal plus one Reflection terminal"
assert '\n\t\t\taccept' not in text, "state-only missions must not accept"
assert 'branch refused' not in text, "refusal must not arm Reflection"
assert text.count('goto done') == 4, "all four Review choices must converge on the declared done label"
assert text.count('goto finish') == 2, "observation and revision reflections must converge on the declared finish label"
assert 'world:' not in text
assert 'set "Incipias:' not in text
assert 'clear "Incipias:' not in text
assert 'set "Hicemus History:' not in text
assert 'clear "Hicemus History:' not in text

for route in (
    'observation first',
    'revision first',
    'local only',
):
    assert f'has "A2 Hicemus Contact Practice: {route}"' in text, f"Reflection missing explicit route gate: {route}"

writes = []
for line in lines:
    stripped = line.strip()
    if stripped.startswith(('set "', 'clear "')):
        writes.append(stripped)
        assert '"A2 Hicemus Contact Practice:' in stripped, f"foreign state write: {stripped}"
    if line.startswith('\t') and stripped.split(' ', 1)[0] in {
        'cargo', 'destination', 'waypoint', 'stopover', 'passenger', 'npc', 'timer'
    }:
        raise AssertionError(f"unexpected gameplay objective in state-only slice: {stripped}")

assert len(writes) == 6, writes
assert 'complete Hicemus language' in text
assert 'Hicemus office, linguistic credential, endorsement, or authority' in text
print("PASS: A2 Hicemus contact practice restage: 2 missions, 4 choices, declared local labels, 3 explicit reflections, refusal suppression, current lifecycle, read-only upstream state")
