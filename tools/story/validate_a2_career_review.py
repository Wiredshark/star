#!/usr/bin/env python3
from pathlib import Path
import re
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 career review.txt")
text = path.read_text(encoding="utf-8")
errors = []

required = [
    '# Copyright (c) 2026 by the Endless Sky contributors',
    'mission "A2 Career Review: First Meeting"',
    'mission "A2 Career Review: Later Reader"',
    'Nia Calder',
    '"combat rating" >= 25',
    '"combat rating" >= 80',
    'has "start: deep"',
    'has "start: paradise"',
    'has "start: syndicate"',
    '"A2 Career Review: principle margin" = 1',
    '"A2 Career Review: principle force" = 1',
    '"A2 Career Review: principle options" = 1',
    '"A2 Career Review: refused" = 1',
    '"A2 Career Review: refusal respected" = 1',
    '"A2 Career Review: later reader pending" = 1',
    '"A2 Career Review: later reader pending" = 0',
    '"A2 Career Review: Calder remembers margin" = 1',
    '"A2 Career Review: Calder remembers force" = 1',
    '"A2 Career Review: Calder remembers options" = 1',
]
errors.extend(f"missing: {item}" for item in required if item not in text)

if text.count('mission "A2 Career Review:') != 2:
    errors.append("expected exactly two A2 Career Review missions")
if text.count('"offer precedence" 8') != 2:
    errors.append("expected offer precedence 8 on both missions")
if text.count('\n\t\t\t\tdecline') != 8:
    errors.append("expected exactly eight state-only decline terminals")
if re.search(r'^\s*accept\s*$', text, re.MULTILINE):
    errors.append("state-only Career Review must not accept objective-less missions")

for token in ('"start: deep" =', '"start: paradise" =', '"start: syndicate" =', '"combat rating" ='):
    if token in text:
        errors.append(f"forbidden authoritative-state write: {token}")

for match in re.finditer(r'^\s*"([^\"]+)"\s*=\s*[-0-9]+\s*$', text, re.MULTILINE):
    key = match.group(1)
    if not key.startswith("A2 Career Review:"):
        errors.append(f"write escapes A2 Career Review namespace: {key}")

for route in ("margin", "force", "options"):
    if f'branch {route}\n\t\t\t\thas "A2 Career Review: principle {route}"' not in text:
        errors.append(f"later reader missing explicit {route} route gate")

if '"A2 Career Review: refused" = 1' not in text or '"A2 Career Review: refusal respected" = 1' not in text:
    errors.append("refusal route must persist and remain explicitly respected")

for directive in ("cargo ", "passenger ", "destination ", "waypoint ", "npc ", "outfit ", "payment ", "reputation "):
    if re.search(rf'^\s*{re.escape(directive)}', text, re.MULTILINE):
        errors.append(f"unexpected gameplay/material directive: {directive.strip()}")

if not text.endswith("\n"):
    errors.append("file must end with newline")

if errors:
    print("FAIL")
    print("\n".join("- " + error for error in errors))
    raise SystemExit(1)

print("PASS")
print("missions=2")
print("named_character=Nia Calder")
print("authoritative_inputs=start:* origin + combat rating (read-only)")
print("career_principles=margin, force, options")
print("refusal_route=persistent_and_respected")
print("later_reader=route_explicit")
print("offer_precedence=8,8")
print("state_only_accepts=0")
print("state_only_declines=8")
print("persistent_write_namespace=A2 Career Review only")
