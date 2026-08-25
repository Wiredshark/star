#!/usr/bin/env python3
"""Focused validation for B2 Republic Household Placement Consent."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/human/b2 republic household placement consent.txt"
TEXT = DATA.read_text(encoding="utf-8")

PREFIX = "B2 Republic Household Placement Consent:"
MISSIONS = [
    f'{PREFIX} Offer',
    f'{PREFIX} Review',
    f'{PREFIX} Owen Remembers',
]
ROUTES = [
    f'{PREFIX} route individual consent',
    f'{PREFIX} route bounded representative',
    f'{PREFIX} route paired placement and consent',
]
SETTLEMENTS = [
    f'{PREFIX} settlement portable consent packet',
    f'{PREFIX} settlement expiry and renewal',
]
A2_STATES = [
    "A2 Republic Resettlement Council: followup seen",
    "A2 Republic Resettlement Council: priority family unity",
    "A2 Republic Resettlement Council: priority work continuity",
    "A2 Republic Resettlement Council: priority distributed placement",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def mission_block(name: str) -> str:
    marker = f'mission "{name}"'
    start = TEXT.find(marker)
    require(start >= 0, f"missing mission {name}")
    next_start = TEXT.find('\nmission "', start + len(marker))
    return TEXT[start:] if next_start < 0 else TEXT[start:next_start]


def label_block(block: str, label: str) -> str:
    marker = f"\t\t\tlabel {label}\n"
    start = block.find(marker)
    require(start >= 0, f"missing label {label}")
    rest = block[start + len(marker):]
    match = re.search(r"\n\t\t\tlabel [^\n]+\n", rest)
    return rest if not match else rest[:match.start()]


require(TEXT.startswith("# Copyright (c) 2026 by the Endless Sky contributors\n"), "missing canonical content header")
require(TEXT.endswith("\n"), "file must end with newline")
require(TEXT.count('\nmission "') == 3, "expected exactly three missions")
for mission in MISSIONS:
    require(f'mission "{mission}"' in TEXT, f"missing {mission}")

require('source "Earth"' in TEXT, "expected Earth source scope")
require(TEXT.count('source "Earth"') == 3, "all three missions must source from Earth")
require('has "A2 Republic Resettlement Council: followup seen"' in TEXT, "missing A2 followup gate")
for state in A2_STATES[1:]:
    require(state in TEXT, f"missing dynamic A2 policy reaction {state}")

# Ownership: A2 and world state are read-only; all assignments belong to B2.
for line in TEXT.splitlines():
    stripped = line.strip()
    if " = " in stripped:
        lhs = stripped.split(" = ", 1)[0].strip().strip('"')
        require(lhs.startswith(PREFIX), f"non-B2 persistent write: {lhs}")
require('"world:' not in TEXT, "new slice must not depend on mutable world state")

# Dialogue-only lifecycle contract.
require(re.search(r"\n\s+accept\s*(?:\n|$)", TEXT) is None, "state-only slice must not accept missions")
require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", TEXT)) == 7, "expected exactly seven decline terminals")
for directive in ("destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passenger ", "deadline ", "timer "):
    require(re.search(rf"^\s*{re.escape(directive)}", TEXT, re.MULTILINE) is None, f"unexpected gameplay objective directive {directive.strip()}")

# Offer route-local persistence and refusal suppression.
offer = mission_block(MISSIONS[0])
route_specs = [
    ("individual", ROUTES[0]),
    ("bounded", ROUTES[1]),
    ("paired", ROUTES[2]),
]
for label, route in route_specs:
    block = label_block(offer, label)
    require(block.count(f'"{PREFIX} introduced" = 1') == 1, f"{label} must introduce exactly once")
    require(block.count(f'"{route}" = 1') == 1, f"{label} must write its route exactly once")
    for other in ROUTES:
        if other != route:
            require(f'"{other}" = 1' not in block, f"{label} must not write another route")
    require(block.count(f'event "{PREFIX} Review Ready" 7 11') == 1, f"{label} must schedule one 7-11 day review")
    require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", block)) == 1, f"{label} must terminate exactly once")

decline = label_block(offer, "decline")
require(f'"{PREFIX} declined" = 1' in decline, "refusal must persist declined state")
require(f'"{PREFIX} introduced" = 1' not in decline, "refusal must not introduce compact")
require("Review Ready" not in decline, "refusal must not schedule Review")
for route in ROUTES:
    require(route not in decline, "refusal must not write a substantive route")

# Review lifecycle, two mutually local settlements, then one-shot aftermath.
review = mission_block(MISSIONS[1])
for gate in (f'{PREFIX} introduced', f'{PREFIX} review ready'):
    require(f'has "{gate}"' in review, f"Review missing gate {gate}")
require(f'not "{PREFIX} reviewed"' in review, "Review must be one-shot")
for label, settlement in (("packet", SETTLEMENTS[0]), ("renewal", SETTLEMENTS[1])):
    block = label_block(review, label)
    require(block.count(f'"{PREFIX} reviewed" = 1') == 1, f"{label} must close Review exactly once")
    require(block.count(f'"{settlement}" = 1') == 1, f"{label} must write its settlement exactly once")
    for other in SETTLEMENTS:
        if other != settlement:
            require(f'"{other}" = 1' not in block, f"{label} must not write another settlement")
    require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", block)) == 1, f"{label} must terminate exactly once")

after = mission_block(MISSIONS[2])
require(f'not "{PREFIX} aftermath seen"' in after, "aftermath must be one-shot")
for settlement in SETTLEMENTS:
    require(f'has "{settlement}"' in after, f"aftermath must consume {settlement}")
require(after.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must write seen exactly once")
require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", after)) == 1, "aftermath must terminate exactly once")

# Character/canon/continuity checks.
for name in ("Lena Orr", "Nadia Kess", "Owen"):
    require(name in TEXT, f"missing recurring character {name}")
for phrase in (
    "emergency coordination and durable consent",
    "history can no longer impersonate present consent",
    "emergency authority expire by default",
    "without pretending I stopped being an adult",
):
    require(phrase in TEXT, f"missing consent/authority continuity phrase: {phrase}")
require("universal Republic rule" in TEXT, "must keep local dispute from becoming universal Republic law")

# No direct material/reputation/gameplay mutation surfaces.
for forbidden in ("credits ", "reputation ", "outfit ", "ship ", "fleet ", "combat rating", "government attitude"):
    require(re.search(rf"^\s*{re.escape(forbidden)}", TEXT, re.MULTILINE) is None, f"unexpected mutation surface {forbidden.strip()}")

print("PASS: B2 Republic Household Placement Consent")
