#!/usr/bin/env python3
# Copyright (c) 2026 by the Endless Sky contributors
#
# Endless Sky is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/wanderer/a2 wanderer machine evidence practice.txt"
text = PATH.read_text(encoding="utf-8")

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
]
for token in required:
    assert token in text, f"missing required token: {token}"

# B2 and simulation state are consumers only.
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"B2 Wanderer Machine Custody Compact:'):
        assert " = " not in stripped, f"illegal B2 write: {stripped}"
    if stripped.startswith('"world:'):
        assert " = " not in stripped and " += " not in stripped and " -= " not in stripped, f"illegal world write: {stripped}"

assert text.count('mission "A2 Wanderer Machine Evidence Practice:') == 2
assert "Curator" in text and "Engineer" in text
assert "private" in text
print("PASS: A2 Wanderer Machine Evidence Practice structural contract")
