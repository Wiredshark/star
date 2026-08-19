#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / "data/coalition/a2 heliarch evidence practice.txt"
text = path.read_text(encoding="utf-8")

required = [
    'mission "A2 Heliarch Evidence Practice: Reflection"',
    'mission "A2 Heliarch Evidence Practice: Later Reflection"',
    'has "B2 Heliarch Evidence Handoff: aftermath seen"',
    'has "B2 Heliarch Evidence Handoff: settlement provenance packet"',
    '"A2 Heliarch Evidence Practice: method" = 1',
    '"A2 Heliarch Evidence Practice: challenge" = 1',
    '"A2 Heliarch Evidence Practice: local" = 1',
    '"A2 Heliarch Evidence Practice: reflection seen" = 1',
]
missing = [item for item in required if item not in text]
assert not missing, f"missing required content: {missing}"
assert text.count('mission "A2 Heliarch Evidence Practice:') == 2
assert text.count('"A2 Heliarch Evidence Practice: resolved" = 1') == 3
assert '"B2 Heliarch Evidence Handoff:' in text
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"B2 Heliarch Evidence Handoff:'):
        assert " = " not in stripped, f"A2 must not write B2 state: {stripped}"
    if stripped.startswith('"world:'):
        assert " = " not in stripped and " += " not in stripped and " -= " not in stripped, f"A2 must not write world state: {stripped}"
assert "Heliarch representative, investigator, clerk, or procedural authority" in text
print("PASS: A2 Heliarch Evidence Practice structure, persistence, B2 read-only ownership, and authority boundary")
