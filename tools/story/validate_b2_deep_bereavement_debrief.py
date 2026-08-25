#!/usr/bin/env python3
"""Focused validation for B2 Deep Bereavement Debrief Compact."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/human/b2 deep bereavement debrief.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Deep Bereavement Debrief Compact:"
MISSIONS = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Lio Remembers"]
ROUTES = [f"{PREFIX} route operational facts", f"{PREFIX} route purpose bound consent", f"{PREFIX} route paired records"]
SETTLEMENTS = [f"{PREFIX} settlement portable boundary packet", f"{PREFIX} settlement dual purpose archive"]
A2_GATES = [
    "A2 Deep Debrief: venn future field contact",
    "A2 Deep Debrief: venn future security contact",
    "A2 Deep Debrief: venn future review contact",
    "A2 Deep Debrief: refusal respected",
]


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def mission_block(name):
    marker = f'mission "{name}"'
    start = TEXT.find(marker)
    require(start >= 0, f"missing {name}")
    nxt = TEXT.find('\nmission "', start + len(marker))
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def label_block(block, label):
    marker = f"\t\t\tlabel {label}\n"
    start = block.find(marker)
    require(start >= 0, f"missing label {label}")
    rest = block[start + len(marker):]
    match = re.search(r"\n\t\t\tlabel [^\n]+\n", rest)
    return rest if not match else rest[:match.start()]


require(TEXT.startswith("# Copyright (c) 2026 by the Endless Sky contributors\n"), "missing canonical header")
require(TEXT.endswith("\n"), "missing trailing newline")
require(TEXT.count('\nmission "') == 3, "expected exactly three missions")
for mission in MISSIONS:
    require(f'mission "{mission}"' in TEXT, f"missing mission {mission}")
require(TEXT.count('attributes "deep"') == 3, "all missions must use Deep source attributes")

# Writes must remain B2-owned. A2 state is read-only gating only.
for line in TEXT.splitlines():
    stripped = line.strip()
    if " = " in stripped:
        lhs = stripped.split(" = ", 1)[0].strip().strip('"')
        require(lhs.startswith(PREFIX), f"non-B2 write: {lhs}")
require('"world:' not in TEXT, "must not read or write mutable world state")
for gate in A2_GATES:
    require(TEXT.count(f'has "{gate}"') == 1, f"A2 gate must be read exactly once: {gate}")
require(re.search(r"\n\s+accept\s*(?:\n|$)", TEXT) is None, "state-only content must not accept missions")
require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", TEXT)) == 7, "expected seven decline terminals")
for directive in ("destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passenger ", "deadline ", "timer "):
    require(re.search(rf"^\s*{re.escape(directive)}", TEXT, re.MULTILINE) is None, f"unexpected objective directive {directive.strip()}")

# Global persistence cardinality.
require(TEXT.count(f'"{PREFIX} introduced" = 1') == 3, "introduced must be written by exactly three substantive routes")
require(TEXT.count(f'"{PREFIX} declined" = 1') == 1, "refusal must be written exactly once")
require(TEXT.count(f'"{PREFIX} reviewed" = 1') == 2, "review closure must be written by exactly two settlements")
require(TEXT.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must be written exactly once")
require(TEXT.count(f'event "{PREFIX} Review Ready" 7 11') == 3, "exactly three substantive routes must schedule Review")
for route in ROUTES:
    require(TEXT.count(f'"{route}" = 1') == 1, f"route must be written exactly once: {route}")
for settlement in SETTLEMENTS:
    require(TEXT.count(f'"{settlement}" = 1') == 1, f"settlement must be written exactly once: {settlement}")

# Offer routes and refusal suppression.
offer = mission_block(MISSIONS[0])
require(offer.count("\n\t\tor\n") == 1, "offer must use exactly one A2 completion OR gate")
for gate in A2_GATES:
    require(f'has "{gate}"' in offer, f"offer missing A2 gate {gate}")
for label in ("facts", "consent", "paired", "decline"):
    require(offer.count(f"goto {label}") == 1, f"offer must route to {label} exactly once")
for label, route in (("facts", ROUTES[0]), ("consent", ROUTES[1]), ("paired", ROUTES[2])):
    block = label_block(offer, label)
    require(block.count(f'"{PREFIX} introduced" = 1') == 1, f"{label} must introduce once")
    require(block.count(f'"{route}" = 1') == 1, f"{label} must write own route")
    for other in ROUTES:
        if other != route:
            require(f'"{other}" = 1' not in block, f"{label} writes another route")
    require(block.count(f'event "{PREFIX} Review Ready" 7 11') == 1, f"{label} must schedule Review once")
    require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", block)) == 1, f"{label} must terminate exactly once")
refusal = label_block(offer, "decline")
require(refusal.count(f'"{PREFIX} declined" = 1') == 1, "refusal must persist once")
require(f'"{PREFIX} introduced" = 1' not in refusal, "refusal must not introduce")
require("Review Ready" not in refusal, "refusal must not schedule Review")
for route in ROUTES:
    require(route not in refusal, "refusal must not write route state")

# Review lifecycle and settlement-local writes.
review = mission_block(MISSIONS[1])
for gate in (f"{PREFIX} introduced", f"{PREFIX} review ready"):
    require(f'has "{gate}"' in review, f"review missing gate {gate}")
require(f'not "{PREFIX} reviewed"' in review, "review must be one-shot")
for label in ("packet", "dual"):
    require(review.count(f"goto {label}") == 1, f"review must route to {label} once")
for label, settlement in (("packet", SETTLEMENTS[0]), ("dual", SETTLEMENTS[1])):
    block = label_block(review, label)
    require(block.count(f'"{PREFIX} reviewed" = 1') == 1, f"{label} must close Review once")
    require(block.count(f'"{settlement}" = 1') == 1, f"{label} must write own settlement")
    for other in SETTLEMENTS:
        if other != settlement:
            require(f'"{other}" = 1' not in block, f"{label} writes another settlement")
    require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", block)) == 1, f"{label} must terminate once")

# Aftermath must consume either settlement and remain one-shot.
after = mission_block(MISSIONS[2])
require(f'not "{PREFIX} aftermath seen"' in after, "aftermath must be one-shot")
require(after.count("\n\t\tor\n") == 1, "aftermath must use one two-settlement OR gate")
require(after.count(f'has "{SETTLEMENTS[0]}"') == 1, "packet settlement must appear once in aftermath eligibility")
require(after.count(f'has "{SETTLEMENTS[1]}"') == 2, "dual settlement must appear once in eligibility and once for dialogue branching")
require(re.search(rf"\n\t\t\tbranch dual\n\t\t\t\thas \"{re.escape(SETTLEMENTS[1])}\"\n", after) is not None, "dual aftermath dialogue must be settlement-gated")
require(after.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath seen must be written once")
require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", after)) == 1, "aftermath must terminate once")

# Character and canon/evidence boundaries.
for name in ("Mara Venn", "Lio Vos", "Iren"):
    require(name in TEXT, f"missing character {name}")
for phrase in (
    "private last message",
    "does not mean the debrief owns every human thing",
    "without becoming evidence of motive",
    "purpose, audience, expiry, and correction",
    "share the same loss without saying they serve the same purpose",
    "uncertainty about motive is not a defect",
):
    require(phrase in TEXT, f"missing continuity phrase: {phrase}")
require("not a universal Deep Security law" in TEXT or "universal Deep practice" in TEXT, "must keep local practice from becoming universal law")
for forbidden in ("credits ", "reputation ", "outfit ", "ship ", "fleet ", "combat rating", "government attitude"):
    require(re.search(rf"^\s*{re.escape(forbidden)}", TEXT, re.MULTILINE) is None, f"unexpected mutation surface {forbidden.strip()}")

print("PASS: B2 Deep Bereavement Debrief Compact")
