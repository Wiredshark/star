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
    '"A2 Dirt Belt Resilience Practice: reflection seen" = 1',
]
missing = [x for x in required if x not in s]
assert not missing, f"missing required content: {missing}"
assert '"world:' not in s, "A2 Dirt Belt practice must not read/write A1 world state"
assert "Dirt Belt commands" in s, "authority boundary missing"
assert s.count('\t\t\taction\n') == 5, "expected four decision actions plus reflection action"
print("PASS: Dirt Belt resilience practice structure, persistence, and authority boundary")
