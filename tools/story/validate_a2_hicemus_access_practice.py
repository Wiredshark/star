#!/usr/bin/env python3
from pathlib import Path

p = Path("data/incipias/a2 hicemus access practice.txt")
s = p.read_text(encoding="utf-8")
lines = s.splitlines()

required = [
    'mission "A2 Hicemus Access Practice: Reflection"',
    'mission "A2 Hicemus Access Practice: Later Reflection"',
    'has "B2 Hicemus Access Compact: aftermath seen"',
    'has "B2 Hicemus Access Compact: settlement shared conflict table"',
    '"A2 Hicemus Access Practice: bounded record" = 1',
    '"A2 Hicemus Access Practice: interaction first" = 1',
    '"A2 Hicemus Access Practice: local only" = 1',
    '"A2 Hicemus Access Practice: refused" = 1',
    '"A2 Hicemus Access Practice: reflection seen" = 1',
]
missing = [x for x in required if x not in s]
assert not missing, f"missing required contracts: {missing}"

assert s.count('mission "A2 Hicemus Access Practice:') == 2, "expected exactly two A2 missions"
assert s.count('"offer precedence" 9') == 2, "both state-only missions must use precedence 9"
assert s.count("\t\t\tdecline") == 5, "expected four briefing terminals plus one reflection terminal"
assert "\t\t\taccept" not in s and "\t\t\t\t\taccept" not in s, "state-only missions must not accept"

write_lines = [line for line in lines if " = " in line or " += " in line or " -= " in line]
assert not any('"B2 Hicemus Access Compact:' in line for line in write_lines), "A2 must not write B2 state"
assert not any('"world:' in line for line in write_lines), "A2 must not write world state"
assert all('"A2 Hicemus Access Practice:' in line for line in write_lines), "all writes must stay A2 namespaced"

refuse_block = s[s.index("\t\t\tlabel refuse"):s.index('mission "A2 Hicemus Access Practice: Later Reflection"')]
assert '"A2 Hicemus Access Practice: refused" = 1' in refuse_block
assert '"A2 Hicemus Access Practice: chosen" = 1' not in refuse_block, "refusal must not arm later reflection"

later = s[s.index('mission "A2 Hicemus Access Practice: Later Reflection"'):]
assert 'has "A2 Hicemus Access Practice: chosen"' in later
assert 'not "A2 Hicemus Access Practice: refused"' in later
assert later.count('not "A2 Hicemus Access Practice: reflection seen"') == 1
assert 'label refused' not in later, "refusal should suppress later reflection rather than create a pseudo-positive route"

objective_tokens = ("\tcargo ", "\tpassengers ", "\tdestination ", "\twaypoint ", "\tstopover ", "\tnpc ", "\tdeadline ")
assert not any(token in s for token in objective_tokens), "slice is expected to remain dialogue/state-only"

print("PASS: A2 Hicemus Access Practice current-main contracts")
