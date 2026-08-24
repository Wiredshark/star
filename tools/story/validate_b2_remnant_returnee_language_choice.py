#!/usr/bin/env python3
from pathlib import Path
import re

PATH = Path("data/remnant/b2 remnant returnee language choice.txt")
text = PATH.read_text(encoding="utf-8")

PREFIX = "B2 Remnant Returnee Language Choice:"
missions = [
    "B2 Remnant Returnee Language Choice: Offer",
    "B2 Remnant Returnee Language Choice: Review",
    "B2 Remnant Returnee Language Choice: Mira Remembers",
]

errors = []

def require(cond, message):
    if not cond:
        errors.append(message)

for mission in missions:
    require(text.count(f'mission "{mission}"') == 1, f"expected one mission: {mission}")

require(text.count('event "B2 Remnant Returnee Language Choice: Review Ready"') == 4,
        "expected Review Ready declaration plus three schedules")
require('has "Remnant: Cognizance 4: done"' in text, "missing Cognizance 4 gate")
require('government "Remnant"' in text, "missing Remnant source scope")
require("Mira Pell" in text and "Eren" in text, "missing recurring sibling characters")

route_states = [
    "route communication autonomy",
    "route task context",
    "route paired communication records",
]
for route in route_states:
    require(text.count(f'"{PREFIX} {route}" = 1') == 1, f"route write count wrong: {route}")

require(text.count(f'"{PREFIX} introduced" = 1') == 3, "introduced must be written by exactly three substantive routes")
require(text.count(f'"{PREFIX} declined" = 1') == 1, "refusal must write declined exactly once")
require(text.count('event "B2 Remnant Returnee Language Choice: Review Ready" 7 11') == 3,
        "exactly three substantive routes must schedule 7-11 day Review")
require(text.count("\t\t\t\tdecline") == 7, "expected exactly seven state-only terminal declines")
require("\t\t\t\taccept" not in text, "state-only slice must not use terminal accept")

settlements = [
    "settlement portable communication packet",
    "settlement fresh context renewal",
]
for settlement in settlements:
    require(text.count(f'"{PREFIX} {settlement}" = 1') == 1, f"settlement write count wrong: {settlement}")
require(text.count(f'"{PREFIX} reviewed" = 1') == 2, "each settlement must close Review exactly once")
require(text.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must be one-shot")

for fragment in [
    'has "B2 Remnant Returnee Language Choice: introduced"',
    'has "B2 Remnant Returnee Language Choice: review ready"',
    'not "B2 Remnant Returnee Language Choice: reviewed"',
    'not "B2 Remnant Returnee Language Choice: aftermath seen"',
    'has "B2 Remnant Returnee Language Choice: settlement portable communication packet"',
    'has "B2 Remnant Returnee Language Choice: settlement fresh context renewal"',
]:
    require(fragment in text, f"missing lifecycle gate: {fragment}")

for line in text.splitlines():
    if re.match(r'^\s+"[^\"]+"\s*(?:=|\+=|-=|\+\+|--|\?=|\^=|<\?=|>\?=)', line):
        key = re.search(r'"([^"]+)"', line).group(1)
        require(key.startswith(PREFIX), f"write outside B2 namespace: {key}")

objective_directive = re.compile(r'^\t+(destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer|outfit|ship|fleet|payment|credits|reputation)\b', re.M)
require(not objective_directive.search(text), "state-only slice contains gameplay-objective/material directive")

# Semantic continuity fragments. Keep these formatting-independent so line wrapping
# or comments do not become false negatives.
for fragment in [
    "communication mode as Mira's choice",
    "task requirements",
    "identity or loyalty",
    "less suited to trusted work in general",
    "what the record does not establish",
    "new office",
]:
    require(fragment in text, f"missing continuity fragment: {fragment}")

require("does not define Remnant language" in text, "missing local-not-universal canon boundary")

if errors:
    for error in errors:
        print(f"FAIL: {error}")
    raise SystemExit(1)

print("PASS: B2 Remnant Returnee Language Choice")
