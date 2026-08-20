#!/usr/bin/env python3
from pathlib import Path
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/wanderer/a2 wanderer evacuation recovery practice.txt")
text = path.read_text(encoding="utf-8")
required = [
    'mission "A2 Wanderer Evacuation Recovery Practice: Briefing"',
    'mission "A2 Wanderer Evacuation Recovery Practice: Recurrence"',
    'has "B2 Wanderer Evacuation Recovery Compact: aftermath seen"',
    '"world: wanderer evacuation logistics strain" <= 1',
    '"world: wanderer evacuation logistics strain" >= 3',
    '"A2 Wanderer Evacuation Recovery Practice: closure evidence" = 1',
    '"A2 Wanderer Evacuation Recovery Practice: current capacity" = 1',
    '"A2 Wanderer Evacuation Recovery Practice: local only" = 1',
    '"A2 Wanderer Evacuation Recovery Practice: declined" = 1',
    '"A2 Wanderer Evacuation Recovery Practice: recurrence seen" = 1',
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("missing required contract(s): " + ", ".join(missing))
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') and " = " in stripped:
        raise SystemExit("A2 must not write world state: " + stripped)
if 'has "A2 Wanderer Evacuation Recovery Practice: declined"' in text:
    raise SystemExit("decline state must not arm recurrence")
print("PASS: A2 Wanderer evacuation recovery practice structural contracts")
