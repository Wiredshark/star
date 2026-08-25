#!/usr/bin/env python3
from pathlib import Path
import re

PATH = Path("data/human/b2 paradise charity representation compact.txt")
text = PATH.read_text(encoding="utf-8")
PREFIX = "B2 Paradise Charity Representation Compact:"
errors = []


def require(cond, message):
    if not cond:
        errors.append(message)


def mission_block(name):
    marker = f'mission "{name}"'
    require(marker in text, f"missing mission block: {name}")
    if marker not in text:
        return ""
    block = text.split(marker, 1)[1]
    return block.split("\n\n\nmission ", 1)[0]


def label_block(block, label):
    marker = f"\t\t\tlabel {label}"
    require(marker in block, f"missing label: {label}")
    if marker not in block:
        return ""
    tail = block.split(marker, 1)[1]
    next_label = tail.find("\n\t\t\tlabel ")
    if next_label >= 0:
        tail = tail[:next_label]
    return tail


missions = [
    "B2 Paradise Charity Representation Compact: Offer",
    "B2 Paradise Charity Representation Compact: Review",
    "B2 Paradise Charity Representation Compact: Ivo Remembers",
]
for mission in missions:
    require(text.count(f'mission "{mission}"') == 1, f"expected one mission: {mission}")

offer = mission_block(missions[0])
review = mission_block(missions[1])
aftermath = mission_block(missions[2])

require(text.count('event "B2 Paradise Charity Representation Compact: Review Ready"') == 4,
        "expected Review Ready declaration plus three schedules")
require(text.count('event "B2 Paradise Charity Representation Compact: Review Ready" 7 11') == 3,
        "exactly three substantive routes must schedule Review")
require(text.count(f'"{PREFIX} introduced" = 1') == 3, "introduced write count wrong")
require(text.count(f'"{PREFIX} declined" = 1') == 1, "refusal write count wrong")
require(text.count("\t\t\t\tdecline") == 7, "expected exactly seven terminal declines")
require("\t\t\t\taccept" not in text, "state-only slice must not use accept")
require('attributes "paradise"' in text and 'government "Republic"' in text,
        "missing Paradise/Republic source scope")
require("Nara Dey" in text and "Ivo Sen" in text, "missing recurring characters")

route_labels = {
    "purpose": "route purpose bound consent",
    "correction": "route correction right",
    "paired": "route paired evidence and publicity",
}
route_names = list(route_labels.values())
for route in route_names:
    require(text.count(f'"{PREFIX} {route}" = 1') == 1, f"route write count wrong: {route}")

for label, route in route_labels.items():
    block = label_block(offer, label)
    require(block.count(f'"{PREFIX} introduced" = 1') == 1,
            f"{label} must write introduced exactly once")
    require(block.count(f'"{PREFIX} {route}" = 1') == 1,
            f"{label} must write its route exactly once")
    for other in route_names:
        if other != route:
            require(f'"{PREFIX} {other}" = 1' not in block,
                    f"{label} must not write another route: {other}")
    require(block.count('event "B2 Paradise Charity Representation Compact: Review Ready" 7 11') == 1,
            f"{label} must schedule Review exactly once")
    require(block.count("\n\t\t\t\tdecline") == 1,
            f"{label} must terminate exactly once")

decline_block = label_block(offer, "decline")
require(decline_block.count(f'"{PREFIX} declined" = 1') == 1,
        "refusal must write declined exactly once")
require(f'"{PREFIX} introduced" = 1' not in decline_block,
        "refusal must not write introduced")
require('event "B2 Paradise Charity Representation Compact: Review Ready" 7 11' not in decline_block,
        "refusal must not schedule Review")
for route in route_names:
    require(f'"{PREFIX} {route}" = 1' not in decline_block,
            f"refusal writes route state: {route}")
require(decline_block.count("\n\t\t\t\tdecline") == 1,
        "refusal must terminate exactly once")

# Prove lifecycle gates are attached to the Review mission itself, not merely
# present somewhere else in the file.
review_gate_fragments = [
    f'has "{PREFIX} introduced"',
    f'has "{PREFIX} review ready"',
    f'not "{PREFIX} reviewed"',
]
for fragment in review_gate_fragments:
    require(review.count(fragment) == 1,
            f"Review must contain exactly one lifecycle gate: {fragment}")
require(f'has "{PREFIX} declined"' not in review,
        "Review must not be unlocked by refusal state")
require(f'"{PREFIX} introduced" = 1' not in review,
        "Review must not rewrite introduction state")

settlement_labels = {
    "packet": "settlement portable representation packet",
    "renewal": "settlement fresh context renewal",
}
settlement_names = list(settlement_labels.values())
for settlement in settlement_names:
    require(text.count(f'"{PREFIX} {settlement}" = 1') == 1,
            f"settlement write count wrong: {settlement}")
require(text.count(f'"{PREFIX} reviewed" = 1') == 2,
        "each settlement must close Review once")
require(text.count(f'"{PREFIX} aftermath seen" = 1') == 1,
        "aftermath must be one-shot")

for label, settlement in settlement_labels.items():
    block = label_block(review, label)
    require(block.count(f'"{PREFIX} reviewed" = 1') == 1,
            f"{label} must close Review exactly once")
    require(block.count(f'"{PREFIX} {settlement}" = 1') == 1,
            f"{label} must write its settlement exactly once")
    for other in settlement_names:
        if other != settlement:
            require(f'"{PREFIX} {other}" = 1' not in block,
                    f"{label} must not write another settlement: {other}")
    require(block.count("\n\t\t\t\tdecline") == 1,
            f"{label} must terminate exactly once")

require('not "B2 Paradise Charity Representation Compact: aftermath seen"' in aftermath,
        "aftermath must gate on not-yet-seen state")
require(aftermath.count("\n\t\tor\n") == 1,
        "aftermath must contain exactly one OR gate for the two settlements")
# Both settlements must unlock the aftermath. Renewal is also referenced once
# more for route-specific dialogue, while packet is the default dialogue path.
require(aftermath.count(f'has "{PREFIX} settlement portable representation packet"') == 1,
        "aftermath must gate on packet settlement exactly once")
require(aftermath.count(f'has "{PREFIX} settlement fresh context renewal"') == 2,
        "aftermath must gate on renewal and branch renewal dialogue exactly once each")
finish_block = label_block(aftermath, "finish")
require(finish_block.count(f'"{PREFIX} aftermath seen" = 1') == 1,
        "aftermath finish must write aftermath seen exactly once")
require(finish_block.count("\n\t\t\t\tdecline") == 1,
        "aftermath finish must terminate exactly once")

for line in text.splitlines():
    if re.match(r'^\s+"[^\"]+"\s*(?:=|\+=|-=|\+\+|--|\?=|\^=|<\?=|>\?=)', line):
        key = re.search(r'"([^"]+)"', line).group(1)
        require(key.startswith(PREFIX), f"write outside B2 namespace: {key}")

objective_directive = re.compile(
    r'^\t+(destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer|outfit|ship|fleet|payment|credits|reputation)\b',
    re.M,
)
require(not objective_directive.search(text),
        "state-only slice contains gameplay objective/material directive")

# Keep continuity checks semantic and insensitive to source-comment wrapping.
for fragment in [
    "Paradise Charity Circuit Archive",
    "aid facts, fundraising narrative",
    "publicity consent",
    "campaign expiry",
    "centralized Paradise charity law",
    "active reuse requires current permission and current context",
    "accounting evidence no longer silently grants control over his biography",
    "Withdrawal stops future active reuse without pretending the earlier campaign never happened",
]:
    require(fragment in text, f"missing continuity fragment: {fragment}")

if errors:
    for error in errors:
        print(f"FAIL: {error}")
    raise SystemExit(1)
print("PASS: B2 Paradise Charity Representation Compact")
