#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/b2 deep unequal means friendship compact.txt"
PREFIX = "B2 Deep Unequal Means Friendship Compact:"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


text = PATH.read_text(encoding="utf-8")
if not text.endswith("\n"):
    fail("production file must end with newline")

missions = re.findall(r'^mission "([^"]+)"$', text, re.M)
expected = {
    PREFIX + " Offer",
    PREFIX + " Review",
    PREFIX + " Mera Remembers",
}
if set(missions) != expected or len(missions) != 3:
    fail(f"expected exact three-mission graph, got {missions}")

for name in ("Ilya Sorn", "Mera Pell"):
    if name not in text:
        fail(f"missing recurring character {name}")

if text.count('government "Deep"') != 3:
    fail("all three missions must be Deep scoped")
if text.count('not attributes "station"') != 3:
    fail("all three missions must exclude stations")

for state in (
    "route gift without debt",
    "route explicit obligation",
    "route paired friendship obligation",
    "settlement broad reciprocity",
    "settlement explicit promises",
):
    if PREFIX + " " + state not in text:
        fail(f"missing state {state}")

# Exactly the three substantive routes arm delayed Review.
if text.count('event "B2 Deep Unequal Means Friendship Compact: Review Ready" 7 11') != 3:
    fail("exactly three substantive routes must schedule 7-11 day Review")
if text.count('"B2 Deep Unequal Means Friendship Compact: introduced" = 1') != 3:
    fail("exactly three substantive routes must introduce the arc")
if 'label decline' not in text or '"B2 Deep Unequal Means Friendship Compact: declined" = 1' not in text:
    fail("refusal path missing")

decline_block = text.split('label decline', 1)[1].split('mission "B2 Deep Unequal Means Friendship Compact: Review"', 1)[0]
if 'introduced" = 1' in decline_block or 'Review Ready" 7 11' in decline_block:
    fail("refusal must not introduce or schedule Review")

# Review lifecycle and settlement closure.
review = text.split('mission "B2 Deep Unequal Means Friendship Compact: Review"', 1)[1].split('mission "B2 Deep Unequal Means Friendship Compact: Mera Remembers"', 1)[0]
for gate in (
    'has "B2 Deep Unequal Means Friendship Compact: introduced"',
    'has "B2 Deep Unequal Means Friendship Compact: review ready"',
    'not "B2 Deep Unequal Means Friendship Compact: reviewed"',
):
    if gate not in review:
        fail(f"Review missing lifecycle gate: {gate}")
if review.count('"B2 Deep Unequal Means Friendship Compact: reviewed" = 1') != 2:
    fail("both Review settlements must close Review exactly once")

# Player wealth is read-only RPG context, never written. Read conditions like
# `credits >= ...` are intentional and must not be mistaken for mutations.
if 'credits >= 50000' not in text or 'credits >= 1000000' not in text:
    fail("missing dynamic player-wealth gates")
if re.search(r'^\s*payment\b', text, re.M) or re.search(r'^\s*credits\s*=\s*', text, re.M):
    fail("slice must not mutate credits/payment")

# All state-only terminals close cleanly.
if len(re.findall(r'^\s*decline\s*$', text, re.M)) != 7:
    fail("expected exactly seven decline terminals")
if re.search(r'^\s*accept\s*$', text, re.M):
    fail("state-only slice must have zero accept terminals")

# No gameplay-objective directives are allowed in this dialogue-only slice.
for directive in ("destination", "stopover", "waypoint", "npc", "cargo", "passengers", "deadline", "timer"):
    if re.search(rf'^\s*{directive}\b', text, re.M | re.I):
        fail(f"unexpected gameplay objective directive: {directive}")

# Persistent writes must remain B2-local.
for line in text.splitlines():
    if " = " not in line:
        continue
    m = re.search(r'"([^"]+)"\s*=\s*', line)
    if m and not m.group(1).startswith(PREFIX):
        fail(f"non-B2 write detected: {m.group(1)}")

# Canon/relationship boundary: material imbalance is not automatic debt or authority.
for fragment in (
    "unequal means do not automatically create a hierarchy",
    "only explicit loans, shared purchases, or promises",
    "reciprocity can be real without being arithmetic",
    "None of those categories silently turns into another",
    "one friendship, not Deep law",
):
    if fragment not in text:
        fail(f"missing continuity boundary fragment: {fragment}")

# Aftermath must consume either settlement and write exactly once.
after = text.split('mission "B2 Deep Unequal Means Friendship Compact: Mera Remembers"', 1)[1]
if after.count('has "B2 Deep Unequal Means Friendship Compact: settlement broad reciprocity"') != 1:
    fail("aftermath must consume broad reciprocity settlement once")
if after.count('has "B2 Deep Unequal Means Friendship Compact: settlement explicit promises"') != 2:
    fail("explicit-promises settlement must gate eligibility and its specific branch")
if after.count('"B2 Deep Unequal Means Friendship Compact: aftermath seen" = 1') != 1:
    fail("aftermath must write exactly once")

print("PASS: B2 Deep Unequal Means Friendship Compact")
