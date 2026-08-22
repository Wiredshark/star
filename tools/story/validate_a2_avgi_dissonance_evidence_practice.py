#!/usr/bin/env python3
# Copyright (c) 2026 by Wiredshark
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
PATH = ROOT / "data/avgi/a2 avgi dissonance evidence practice.txt"
TEXT = PATH.read_text(encoding="utf-8")

PREFIX = "A2 Avgi Dissonance Evidence Practice:"

required = [
    'mission "A2 Avgi Dissonance Evidence Practice: Offer"',
    'mission "A2 Avgi Dissonance Evidence Practice: Reflection"',
    'government "Avgi (Dissonance)"',
    'has "language: Avgi (Written)"',
    'not "avgi: lost in twilight"',
    '"offer precedence" 9',
    '"A2 Avgi Dissonance Evidence Practice: full record" = 1',
    '"A2 Avgi Dissonance Evidence Practice: burden separate" = 1',
    '"A2 Avgi Dissonance Evidence Practice: local only" = 1',
    '"A2 Avgi Dissonance Evidence Practice: refused" = 1',
    '"A2 Avgi Dissonance Evidence Practice: reflection seen" = 1',
    'branch full',
    'branch burden',
    'branch local',
    'not "A2 Avgi Dissonance Evidence Practice: refused"',
]
for needle in required:
    assert needle in TEXT, f"missing required contract: {needle}"

assert TEXT.count('mission "A2 Avgi Dissonance Evidence Practice:') == 2
assert TEXT.count('"offer precedence" 9') == 2
assert TEXT.count("\n\t\t\t\tdecline") == 5, "all five state-only terminal paths must decline"
assert "\n\t\t\t\taccept" not in TEXT, "state-only missions must not accept"
assert "world:" not in TEXT, "A2 slice must not consume or own world simulation state"

for line in TEXT.splitlines():
    stripped = line.strip()
    if stripped.startswith('"') and ' = ' in stripped:
        key = stripped.split('"', 2)[1]
        assert key.startswith(PREFIX), f"foreign persistent-state write: {stripped}"

for objective in ("\tcargo ", "\tpassengers ", "\tdestination ", "\twaypoint ", "\tnpc ", "\tstopover "):
    assert objective not in TEXT, f"state-only slice contains gameplay objective directive: {objective.strip()}"

for forbidden in (
    "Dissonance representative authority",
    "Dissonance office",
    "speak for all Dissonance",
    "proof of motive",
):
    assert forbidden not in TEXT, f"authority/evidence boundary violated: {forbidden}"

print("PASS: A2 Avgi Dissonance Evidence Practice contracts")
