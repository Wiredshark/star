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
    '"A2 Heliarch Evidence Practice: refused" = 1',
    '"A2 Heliarch Evidence Practice: reflection seen" = 1',
    'branch method',
    'branch challenge',
    'branch local',
    'offer precedence 9',
]
missing = [item for item in required if item not in text]
assert not missing, f"missing required content: {missing}"
assert text.count('mission "A2 Heliarch Evidence Practice:') == 2
assert text.count('"A2 Heliarch Evidence Practice: resolved" = 1') == 3
assert text.count('\tdecline') == 5
assert '\taccept' not in text, "state-only Heliarch practice missions must not accept"
assert text.count('offer precedence 9') == 2
assert 'not "A2 Heliarch Evidence Practice: refused"' in text
assert 'has "A2 Heliarch Evidence Practice: method"' in text
assert 'has "A2 Heliarch Evidence Practice: challenge"' in text
assert 'has "A2 Heliarch Evidence Practice: local"' in text

objective_prefixes = (
    '\tdestination ', '\twaypoint ', '\tstopover ', '\tcargo ', '\tpassengers ',
    '\tnpc ', '\tdeadline ', '\tclearance ', '\tstealth ', '\tassisting ', '\tdisabled '
)
for line in text.splitlines():
    assert not line.startswith(objective_prefixes), f"unexpected gameplay objective directive: {line}"
    stripped = line.strip()
    if stripped.startswith('"B2 Heliarch Evidence Handoff:'):
        assert " = " not in stripped and " += " not in stripped and " -= " not in stripped, f"A2 must not write B2 state: {stripped}"
    if stripped.startswith('"world:'):
        assert " = " not in stripped and " += " not in stripped and " -= " not in stripped, f"A2 must not write world state: {stripped}"

assert "Heliarch representative, investigator, clerk, or procedural authority" in text
assert "grant you any standing" in text
print("PASS: A2 Heliarch Evidence Practice lifecycle, persistence, route gating, refusal suppression, B2/world read-only ownership, and authority boundary")
