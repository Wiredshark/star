#!/usr/bin/env python3
from pathlib import Path

p = Path("data/human/a2 republic civic capacity practice.txt")
text = p.read_text(encoding="utf-8")
required = [
    'mission "A2 Republic Civic Capacity Practice"',
    'mission "A2 Republic Civic Capacity Practice Recovery"',
    '"world: republic civic strain" >= 2',
    '"world: republic civic strain" <= 1',
    '"A2 Republic Civic Capacity Practice: continuity" = 1',
    '"A2 Republic Civic Capacity Practice: capacity" = 1',
    '"A2 Republic Civic Capacity Practice: exceptions" = 1',
    '"A2 Republic Civic Capacity Practice: refused" = 1',
    '"A2 Republic Civic Capacity Practice: recovery seen" = 1',
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("missing required civic-capacity contract: " + repr(missing))
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') and any(op in stripped for op in (" = ", " += ", " -= ", " <?= ", " >?= ")):
        raise SystemExit("A2 must not write A1 world state: " + stripped)
if text.count('mission "A2 Republic Civic Capacity Practice') != 2:
    raise SystemExit("expected exactly two A2 civic-capacity missions")
print("PASS: Republic civic capacity practice contract")
