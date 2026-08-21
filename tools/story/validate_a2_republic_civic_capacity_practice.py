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

if text.count('mission "A2 Republic Civic Capacity Practice') != 2:
    raise SystemExit("expected exactly two A2 civic-capacity missions")
if text.count('"offer precedence" 8') != 2:
    raise SystemExit("both state-only missions must use Republic A2 offer precedence 8")
if text.count("\n\t\t\t\tdecline") != 5:
    raise SystemExit("expected exactly five state-only decline terminals")
if "\n\t\t\t\taccept" in text or "\n\t\t\taccept" in text:
    raise SystemExit("state-only civic-capacity missions must not use accept terminals")

objective_tokens = (
    "\tcargo ", "\tpassengers ", "\twaypoint ", "\tstopover ",
    "\tnpc ", "\tdeadline ", "\tclearance ", "\tstealth"
)
for token in objective_tokens:
    if token in text:
        raise SystemExit("unexpected objective-bearing directive in state-only slice: " + repr(token))

for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') and any(op in stripped for op in (" = ", " += ", " -= ", " <?= ", " >?= ")):
        raise SystemExit("A2 must not write A1 world state: " + stripped)

writes = []
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"A2 ') and any(op in stripped for op in (" = ", " += ", " -= ")):
        writes.append(stripped)
for write in writes:
    if not write.startswith('"A2 Republic Civic Capacity Practice:'):
        raise SystemExit("unexpected A2 persistence namespace: " + write)

print("PASS: Republic civic capacity practice ownership/lifecycle/precedence contract")
