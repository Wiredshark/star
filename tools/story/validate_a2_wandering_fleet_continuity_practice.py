#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/avgi/a2 wandering fleet continuity practice.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'B2 Avgi Wandering Fleet Transfer Compact: aftermath seen',
    'A2 Wandering Fleet Continuity Practice: resilience boundary',
    'A2 Wandering Fleet Continuity Practice: dependency provenance',
    'A2 Wandering Fleet Continuity Practice: local only',
    'A2 Wandering Fleet Continuity Practice: refused',
    'A2 Wandering Fleet Continuity Practice: reflection seen',
]
for token in required:
    assert token in text, f"missing required state: {token}"

assert text.count('mission "A2 Wandering Fleet Continuity Practice:') == 2
assert text.count('offer precedence 9') == 2
assert text.count('\n\t\t\tdecline') == 5, "all five state-only terminals must decline"
assert '\n\t\t\taccept' not in text, "state-only A2 dialogue must not accept a mission"
assert 'not "A2 Wandering Fleet Continuity Practice: refused"' in text
assert text.count('has "B2 Avgi Wandering Fleet Transfer Compact: aftermath seen"') == 2
assert not re.search(r'^\s*"world:[^"]+"\s*=', text, re.M), "A2 must not write world state"
assert not re.search(r'^\s*"B2 Avgi Wandering Fleet Transfer Compact:[^"]+"\s*=', text, re.M), "A2 must not write B2 state"

writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, re.M)
assert writes
assert all(w.startswith("A2 Wandering Fleet Continuity Practice:") for w in writes)
for route in ("resilience boundary", "dependency provenance", "local only", "refused"):
    assert text.count(f'"A2 Wandering Fleet Continuity Practice: {route}" = 1') == 1

print(f"PASS: {PATH.relative_to(ROOT)}; lifecycle, precedence, ownership, and route contracts hold")
