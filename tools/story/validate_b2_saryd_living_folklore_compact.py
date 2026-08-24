#!/usr/bin/env python3
from pathlib import Path
import re

PATH = Path("data/coalition/b2 saryd living folklore compact.txt")
text = PATH.read_text(encoding="utf-8")
PREFIX = "B2 Saryd Living Folklore Compact:"
errors = []

def require(cond, message):
    if not cond:
        errors.append(message)

missions = [
    "B2 Saryd Living Folklore Compact: Offer",
    "B2 Saryd Living Folklore Compact: Review",
    "B2 Saryd Living Folklore Compact: Tiri Remembers",
]
for mission in missions:
    require(text.count(f'mission "{mission}"') == 1, f"expected one mission: {mission}")

require(text.count('event "B2 Saryd Living Folklore Compact: Review Ready"') == 4,
        "expected Review Ready declaration plus three schedules")
require(text.count('event "B2 Saryd Living Folklore Compact: Review Ready" 7 11') == 3,
        "exactly three substantive routes must schedule Review")
require(text.count(f'"{PREFIX} introduced" = 1') == 3, "introduced write count wrong")
require(text.count(f'"{PREFIX} declined" = 1') == 1, "refusal write count wrong")
require(text.count("\t\t\t\tdecline") == 7, "expected exactly seven terminal declines")
require("\t\t\t\taccept" not in text, "state-only slice must not use accept")
require('attributes "saryd"' in text and 'attributes "folklore"' in text, "missing Saryd folklore scope")
require("Aven Pell" in text and "Tiri Sen" in text, "missing recurring characters")

for route in [
    "route attributable adaptation",
    "route revision history",
    "route paired lineage and production",
]:
    require(text.count(f'"{PREFIX} {route}" = 1') == 1, f"route write count wrong: {route}")

for settlement in [
    "settlement portable provenance packet",
    "settlement versioned coexistence",
]:
    require(text.count(f'"{PREFIX} {settlement}" = 1') == 1, f"settlement write count wrong: {settlement}")
require(text.count(f'"{PREFIX} reviewed" = 1') == 2, "each settlement must close Review once")
require(text.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must be one-shot")

for fragment in [
    'has "B2 Saryd Living Folklore Compact: introduced"',
    'has "B2 Saryd Living Folklore Compact: review ready"',
    'not "B2 Saryd Living Folklore Compact: reviewed"',
    'not "B2 Saryd Living Folklore Compact: aftermath seen"',
    'has "B2 Saryd Living Folklore Compact: settlement portable provenance packet"',
    'has "B2 Saryd Living Folklore Compact: settlement versioned coexistence"',
]:
    require(fragment in text, f"missing lifecycle gate: {fragment}")

# Refusal must not arm Review or write any substantive route state.
decline_block = text.split("\t\t\tlabel decline", 1)[1].split("\n\n\nmission", 1)[0]
require('event "B2 Saryd Living Folklore Compact: Review Ready" 7 11' not in decline_block,
        "refusal must not schedule Review")
for route in ["route attributable adaptation", "route revision history", "route paired lineage and production"]:
    require(route not in decline_block, f"refusal writes route state: {route}")

# B2-only persistent writes.
for line in text.splitlines():
    if re.match(r'^\s+"[^\"]+"\s*(?:=|\+=|-=|\+\+|--|\?=|\^=|<\?=|>\?=)', line):
        key = re.search(r'"([^"]+)"', line).group(1)
        require(key.startswith(PREFIX), f"write outside B2 namespace: {key}")

objective_directive = re.compile(r'^\t+(destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer|outfit|ship|fleet|payment|credits|reputation)\b', re.M)
require(not objective_directive.search(text), "state-only slice contains gameplay objective/material directive")

for fragment in [
    "Cultural Commons Ledger",
    "does not create centralized Saryd cultural",
    "source lineage",
    "current production authority",
    "no variant becomes official by repetition",
    "Neither fact silently becomes ownership of the whole tradition",
]:
    require(fragment in text, f"missing continuity fragment: {fragment}")

if errors:
    for error in errors:
        print(f"FAIL: {error}")
    raise SystemExit(1)
print("PASS: B2 Saryd Living Folklore Compact")
