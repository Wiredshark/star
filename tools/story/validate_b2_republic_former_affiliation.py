#!/usr/bin/env python3
"""Focused validation for B2 Republic Former Affiliation Compact."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/human/b2 republic former affiliation.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Republic Former Affiliation Compact:"
MISSIONS = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Devon Remembers"]
ROUTES = [f"{PREFIX} route dated affiliation", f"{PREFIX} route bounded reference", f"{PREFIX} route paired history and present"]
SETTLEMENTS = [f"{PREFIX} settlement portable affiliation packet", f"{PREFIX} settlement expiry and acknowledgement"]


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
require(TEXT.count('source "Earth"') == 3, "all missions must source from Earth")

for line in TEXT.splitlines():
    stripped = line.strip()
    if " = " in stripped:
        lhs = stripped.split(" = ", 1)[0].strip().strip('"')
        require(lhs.startswith(PREFIX), f"non-B2 write: {lhs}")
require('"world:' not in TEXT, "must not read or write mutable world state")
require(re.search(r"\n\s+accept\s*(?:\n|$)", TEXT) is None, "state-only content must not accept missions")
require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", TEXT)) == 7, "expected seven decline terminals")
for directive in ("destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passenger ", "deadline ", "timer "):
    require(re.search(rf"^\s*{re.escape(directive)}", TEXT, re.MULTILINE) is None, f"unexpected objective directive {directive.strip()}")

# Route-local persistence and refusal suppression.
offer = mission_block(MISSIONS[0])
for label, route in (("dated", ROUTES[0]), ("reference", ROUTES[1]), ("paired", ROUTES[2])):
    block = label_block(offer, label)
    require(block.count(f'"{PREFIX} introduced" = 1') == 1, f"{label} must introduce once")
    require(block.count(f'"{route}" = 1') == 1, f"{label} must write own route")
    for other in ROUTES:
        if other != route:
            require(f'"{other}" = 1' not in block, f"{label} writes another route")
    require(block.count(f'event "{PREFIX} Review Ready" 7 11') == 1, f"{label} must schedule review once")
    require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", block)) == 1, f"{label} must terminate once")
refusal = label_block(offer, "decline")
require(f'"{PREFIX} declined" = 1' in refusal, "refusal must persist")
require(f'"{PREFIX} introduced" = 1' not in refusal, "refusal must not introduce")
require("Review Ready" not in refusal, "refusal must not schedule review")
for route in ROUTES:
    require(route not in refusal, "refusal must not write route state")

# Review and aftermath lifecycle.
review = mission_block(MISSIONS[1])
for gate in (f'{PREFIX} introduced', f'{PREFIX} review ready'):
    require(f'has "{gate}"' in review, f"review missing gate {gate}")
require(f'not "{PREFIX} reviewed"' in review, "review must be one-shot")
for label, settlement in (("packet", SETTLEMENTS[0]), ("renewal", SETTLEMENTS[1])):
    block = label_block(review, label)
    require(block.count(f'"{PREFIX} reviewed" = 1') == 1, f"{label} must close review once")
    require(block.count(f'"{settlement}" = 1') == 1, f"{label} must write settlement once")
    for other in SETTLEMENTS:
        if other != settlement:
            require(f'"{other}" = 1' not in block, f"{label} writes another settlement")
    require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", block)) == 1, f"{label} must terminate once")
after = mission_block(MISSIONS[2])
require(f'not "{PREFIX} aftermath seen"' in after, "aftermath must be one-shot")
for settlement in SETTLEMENTS:
    require(f'has "{settlement}"' in after, f"aftermath missing {settlement}")
require(after.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must write seen once")
require(len(re.findall(r"\n\s+decline\s*(?:\n|$)", after)) == 1, "aftermath must terminate once")

for name in ("Mira Sol", "Devon Pryce", "Devon"):
    require(name in TEXT, f"missing character {name}")
for phrase in (
    "history into a current relationship",
    "reference\" and \"current sponsor",
    "old crew can remain part of the story without remaining in control of the present",
    "old roster remains searchable evidence",
    "Same history",
):
    require(phrase in TEXT, f"missing continuity phrase: {phrase}")
require("universal Republic rule" in TEXT or "Republic-wide practice" in TEXT, "must keep local case from becoming universal law")
for forbidden in ("credits ", "reputation ", "outfit ", "ship ", "fleet ", "combat rating", "government attitude"):
    require(re.search(rf"^\s*{re.escape(forbidden)}", TEXT, re.MULTILINE) is None, f"unexpected mutation surface {forbidden.strip()}")

print("PASS: B2 Republic Former Affiliation Compact")
