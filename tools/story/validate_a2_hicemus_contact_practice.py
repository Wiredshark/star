#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/incipias/a2 hicemus contact practice.txt"
text = PATH.read_text(encoding="utf-8")

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
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('mission "A2 Hicemus Contact Practice:') == 2
assert text.count('government "Hicemus"') == 2
assert 'world:' not in text
assert 'set "Incipias:' not in text
assert 'clear "Incipias:' not in text
assert 'set "Hicemus History:' not in text
assert 'clear "Hicemus History:' not in text

writes = []
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith(('set "', 'clear "')):
        writes.append(stripped)
        assert '"A2 Hicemus Contact Practice:' in stripped, f"foreign state write: {stripped}"

assert len(writes) == 6, writes
print("PASS: A2 Hicemus contact practice: 2 missions, 4 routes, read-only upstream state, no world-state writes")
