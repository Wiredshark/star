#!/usr/bin/env python3
# Copyright (c) 2026 Wiredshark
#
# Endless Sky is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

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
    '"offer precedence" 9',
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("missing required contract(s): " + ", ".join(missing))

for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') and " = " in stripped:
        raise SystemExit("A2 must not write world state: " + stripped)
    if stripped.startswith('"B2 Wanderer Evacuation Recovery Compact:') and " = " in stripped:
        raise SystemExit("A2 must not write B2 state: " + stripped)

if 'has "A2 Wanderer Evacuation Recovery Practice: declined"' in text:
    raise SystemExit("decline state must not arm recurrence")
if "\n\t\t\taccept\n" in text:
    raise SystemExit("state-only A2 dialogue must not use accept")
if text.count("\n\t\t\tdecline\n") != 5:
    raise SystemExit("expected exactly five state-only decline terminals")
if text.count('"offer precedence" 9') != 2:
    raise SystemExit("both missions must carry deterministic offer precedence")

print("PASS: A2 Wanderer evacuation recovery practice ownership, lifecycle, and recurrence contracts")
