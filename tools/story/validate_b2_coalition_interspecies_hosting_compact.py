#!/usr/bin/env python3
from pathlib import Path
import re

P = Path("data/coalition/b2 coalition interspecies hosting compact.txt")
text = P.read_text(encoding="utf-8")
missions = re.findall(r'^mission "([^"]+)"', text, re.M)
expected = [
    "B2 Coalition Interspecies Hosting Compact: Offer",
    "B2 Coalition Interspecies Hosting Compact: Review",
    "B2 Coalition Interspecies Hosting Compact: Settler Remembers",
]
assert missions == expected, missions
assert text.count('\n\t\t\tdecline') == 7, text.count('\n\t\t\tdecline')
assert '\n\t\t\taccept' not in text
for token in ('\tdestination\n','\tstopover\n','\twaypoint ','\tnpc ','\tcargo ','\tpassengers ','\tdeadline ','\ttimer '):
    assert token not in text, token
for route in ('route consent floor','route named adaptation','route paired'):
    assert f'"B2 Coalition Interspecies Hosting Compact: {route}" = 1' in text
assert '"B2 Coalition Interspecies Hosting Compact: declined" = 1' in text
assert text.count('event "B2 Coalition Interspecies Hosting Compact: Review Ready" 7 11') == 3
assert 'has "B2 Coalition Interspecies Hosting Compact: review ready"' in text
for settlement in ('settlement household charter','settlement periodic renewal'):
    assert f'"B2 Coalition Interspecies Hosting Compact: {settlement}" = 1' in text
    assert f'has "B2 Coalition Interspecies Hosting Compact: {settlement}"' in text
assert text.count('"B2 Coalition Interspecies Hosting Compact: reviewed" = 1') == 2
assert text.count('"B2 Coalition Interspecies Hosting Compact: aftermath seen" = 1') == 1
assert 'not "B2 Coalition Interspecies Hosting Compact: aftermath seen"' in text
assert 'has "known to the heliarchs"' in text
# Every direct persistent write belongs to B2.
for line in text.splitlines():
    if re.search(r'"[^"]+"\s*(?:=|\+\+|--)', line):
        assert '"B2 Coalition Interspecies Hosting Compact:' in line, line
# Canon/continuity concepts must be explicit.
for phrase in ('privacy', 'guests', 'right to leave', 'consent', 'optional', 'universal template'):
    assert phrase.lower() in text.lower(), phrase
print("B2 Coalition Interspecies Hosting Compact validator: PASS")
