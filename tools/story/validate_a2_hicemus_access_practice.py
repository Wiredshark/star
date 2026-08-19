#!/usr/bin/env python3
from pathlib import Path

p = Path("data/incipias/a2 hicemus access practice.txt")
s = p.read_text(encoding="utf-8")
required = [
    'mission "A2 Hicemus Access Practice: Reflection"',
    'mission "A2 Hicemus Access Practice: Later Reflection"',
    'has "B2 Hicemus Access Compact: aftermath seen"',
    '"A2 Hicemus Access Practice: bounded record" = 1',
    '"A2 Hicemus Access Practice: interaction first" = 1',
    '"A2 Hicemus Access Practice: local only" = 1',
    '"A2 Hicemus Access Practice: refused" = 1',
    '"A2 Hicemus Access Practice: reflection seen" = 1',
]
missing = [x for x in required if x not in s]
assert not missing, f"missing required contracts: {missing}"
assert '"B2 Hicemus Access Compact:' not in "\n".join(
    line for line in s.splitlines() if " = " in line or " += " in line or " -= " in line
), "A2 must not write B2 state"
assert '"world:' not in "\n".join(
    line for line in s.splitlines() if " = " in line or " += " in line or " -= " in line
), "A2 must not write world state"
assert s.count('mission "A2 Hicemus Access Practice:') == 2
print("PASS: A2 Hicemus Access Practice contracts")
