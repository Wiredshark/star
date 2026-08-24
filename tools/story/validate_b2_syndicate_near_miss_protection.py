#!/usr/bin/env python3
from pathlib import Path
import re
import sys

DATA = Path("data/human/b2 syndicate near miss protection compact.txt")
text = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Syndicate Near-Miss Protection Compact:"
errors = []

def need(condition, message):
    if not condition:
        errors.append(message)

need(text.count('mission "B2 Syndicate Near-Miss Protection Compact:') == 3, "expected exactly three missions")
for name in ("Tessa Marr", "Niko Renn"):
    need(name in text, f"missing recurring character {name}")
for route in ("route protected", "route accountable", "route paired"):
    need(PREFIX + " " + route in text, f"missing {route}")
need(PREFIX + " declined" in text, "missing refusal state")
for settlement in ("settlement packet", "settlement expiry"):
    need(PREFIX + " " + settlement in text, f"missing {settlement}")
need(text.count('event "B2 Syndicate Near-Miss Protection Compact: Review Ready" 7 11') == 3, "review must be scheduled by exactly three substantive routes")
need('has "A2 Syndicate Maintenance Triage: followup seen"' in text, "missing A2 Tessa Marr dependency")
need('"world: syndicate labor strain" >= 2' in text and '"world: syndicate labor strain" <= 1' in text, "missing A1 labor-strain gates")
need('has "world: syndicate labor rotation active"' in text and 'not "world: syndicate labor rotation active"' in text, "missing A1 labor-rotation gates")
need(text.count("\n\t\t\tdecline\n") == 7, "expected exactly seven state-only decline terminals")
need("\n\t\t\taccept\n" not in text, "objective-less state-only missions must not accept")
for directive in ("destination", "stopover", "waypoint", "npc", "cargo", "passengers", "deadline", "timer"):
    need(not re.search(rf'^\t{directive}\b', text, re.M), f"unexpected gameplay-objective directive: {directive}")

for match in re.finditer(r'^\s*"([^"]+)"\s*=\s*[-0-9]+\s*$', text, re.M):
    need(match.group(1).startswith(PREFIX), f"non-B2 condition write: {match.group(1)}")

for command in ("credits", "reputation", "combat rating", "outfit", "ship", "fleet"):
    need(not re.search(rf'^\s*{re.escape(command)}\b', text, re.M | re.I), f"unexpected material/reputation command: {command}")

for phrase in (
    "identity behind a narrow access gate",
    "identity from discipline",
    "retaliation cannot hide inside ordinary scheduling",
    "A suspicious sequence is a review trigger, not a verdict",
    "closure without amnesia",
):
    need(phrase in text, f"missing continuity concept: {phrase}")

labels = set(re.findall(r'^\s*label\s+([^\n]+)$', text, re.M))
for target in re.findall(r'^\s*goto\s+([^\n]+)$', text, re.M):
    need(target in labels, f"goto without label: {target}")

need('not "B2 Syndicate Near-Miss Protection Compact: reviewed"' in text, "review missing one-shot gate")
need('not "B2 Syndicate Near-Miss Protection Compact: aftermath seen"' in text, "aftermath missing one-shot gate")
need(text.count('"B2 Syndicate Near-Miss Protection Compact: aftermath seen" = 1') == 1, "aftermath write must occur exactly once")
need(text.count('has "B2 Syndicate Near-Miss Protection Compact: settlement packet"') >= 1 and text.count('has "B2 Syndicate Near-Miss Protection Compact: settlement expiry"') >= 2, "both settlements must feed aftermath")

if errors:
    print("FAIL: B2 Syndicate Near-Miss Protection Compact")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("PASS: B2 Syndicate Near-Miss Protection Compact structure validated")
print("PASS: missions=3 routes=3+refusal settlements=2 terminals=7-decline")
print("PASS: A1/A2 inputs read-only; B2 writes only")
