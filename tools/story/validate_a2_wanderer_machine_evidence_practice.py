#!/usr/bin/env python3
# Copyright (c) 2026 by the Endless Sky contributors
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

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/wanderer/a2 wanderer machine evidence practice.txt"
text = PATH.read_text(encoding="utf-8")
lines = text.splitlines()

required = [
    'mission "A2 Wanderer Machine Evidence Practice: Choice"',
    'mission "A2 Wanderer Machine Evidence Practice: Reflection"',
    'has "B2 Wanderer Machine Custody Compact: aftermath seen"',
    'has "B2 Wanderer Machine Custody Compact: settlement two-key derivative review"',
    '"A2 Wanderer Machine Evidence Practice: provenance" = 1',
    '"A2 Wanderer Machine Evidence Practice: challenge" = 1',
    '"A2 Wanderer Machine Evidence Practice: local" = 1',
    '"A2 Wanderer Machine Evidence Practice: refused" = 1',
    '"A2 Wanderer Machine Evidence Practice: reflection seen" = 1',
    'has "A2 Wanderer Machine Evidence Practice: provenance"',
    'has "A2 Wanderer Machine Evidence Practice: challenge"',
    'has "A2 Wanderer Machine Evidence Practice: local"',
    'not "A2 Wanderer Machine Evidence Practice: refused"',
]
for token in required:
    assert token in text, f"missing required token: {token}"

assert text.count('mission "A2 Wanderer Machine Evidence Practice:') == 2, "expected exactly two missions"
assert text.count('"offer precedence" 9') == 2, "both missions must use offer precedence 9"
assert text.count("\t\t\t\tdecline") == 5, "expected five state-only decline terminals"
assert "\t\t\t\taccept" not in text, "state-only missions must not accept"
assert text.count('has "B2 Wanderer Machine Custody Compact: aftermath seen"') >= 2, "both stages must recheck B2 aftermath"

# B2 and simulation state are consumers only. All writes must stay in the A2 namespace.
for line in lines:
    stripped = line.strip()
    if stripped.startswith('"B2 Wanderer Machine Custody Compact:'):
        assert " = " not in stripped and " += " not in stripped and " -= " not in stripped, f"illegal B2 write: {stripped}"
    if stripped.startswith('"world:'):
        assert " = " not in stripped and " += " not in stripped and " -= " not in stripped, f"illegal world write: {stripped}"
    if (" = " in stripped or " += " in stripped or " -= " in stripped) and stripped.startswith('"'):
        assert stripped.startswith('"A2 Wanderer Machine Evidence Practice:'), f"write outside A2 namespace: {stripped}"

# These are dialogue/state-only missions. Reject actual objective directives, but ignore prose in backticks.
objective_directives = (
    "cargo ", "passengers ", "destination ", "waypoint ", "stopover ",
    "npc ", "deadline ", "deadline base ", "distance ", "clearance ",
)
for line in lines:
    stripped = line.lstrip("\t")
    if stripped.startswith("`"):
        continue
    indent = len(line) - len(line.lstrip("\t"))
    if indent >= 1:
        assert not any(stripped.startswith(token) for token in objective_directives), f"unexpected gameplay objective directive: {line}"

assert "Curator" in text and "Engineer" in text, "recurring private shorthand characters missing"
assert "player-private shorthand" in text, "private-shorthand authority boundary missing"
assert "not Wanderer offices or titles" in text, "no-Wanderer-authority boundary missing"
assert "borrowed authority" in text, "local-only reflection must preserve authority boundary"
assert "refused" in text, "refusal route missing"

print("PASS: A2 Wanderer Machine Evidence Practice current-main structural/lifecycle contract")
