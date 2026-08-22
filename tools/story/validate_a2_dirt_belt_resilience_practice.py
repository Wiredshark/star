#!/usr/bin/env python3
from pathlib import Path

p = Path("data/human/a2 dirt belt resilience practice.txt")
s = p.read_text(encoding="utf-8")

required = [
    'mission "A2 Dirt Belt Resilience Practice"',
    'mission "A2 Dirt Belt Resilience Practice Reflection"',
    '"A2 Dirt Belt Resilience Practice: obligations" = 1',
    '"A2 Dirt Belt Resilience Practice: capacity" = 1',
    '"A2 Dirt Belt Resilience Practice: redundancy" = 1',
    '"A2 Dirt Belt Resilience Practice: local" = 1',
    'has "A2 Dirt Belt Resilience Practice: obligations"',
    'has "A2 Dirt Belt Resilience Practice: capacity"',
    'has "A2 Dirt Belt Resilience Practice: redundancy"',
    'has "A2 Dirt Belt Resilience Practice: local"',
    '"A2 Dirt Belt Resilience Practice: reflection seen" = 1',
    '"offer precedence" 9',
    'Dirt Belt commands',
]
missing = [x for x in required if x not in s]
assert not missing, f"missing required content: {missing}"
assert s.count('mission "A2 Dirt Belt Resilience Practice') == 2, "expected exactly two A2 missions"
assert '"world:' not in s, "A2 Dirt Belt practice must not read/write A1 world state"
assert '\t\t\t\taccept\n' not in s, "state-only A2 missions must not remain accepted"
assert s.count('\t\t\t\tdecline\n') == 5, "expected four decisions plus reflection to decline"
assert s.count('"offer precedence" 9') == 2, "both missions must use current A2 precedence"
assert s.count('\t\t\taction\n') == 5, "expected four decision actions plus reflection action"
for forbidden in ('cargo ', 'passenger ', 'waypoint ', 'stopover ', 'destination ', 'deadline '):
    assert forbidden not in s, f"unexpected gameplay objective directive: {forbidden.strip()}"
assert 'abundance' in s, "scarcity/abundance boundary missing"
assert 'authority traveled with it' in s, "local authority boundary missing"
print("PASS: Dirt Belt resilience persistence, explicit routes, lifecycle, and authority boundary")
