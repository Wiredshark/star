#!/usr/bin/env python3
from pathlib import Path
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 career review.txt")
text = path.read_text(encoding="utf-8")
required = [
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
    '"A2 Career Review: later reader pending" = 1',
    '"A2 Career Review: later reader pending" = 0',
]
errors = [f"missing: {x}" for x in required if x not in text]
for token in ('"start: deep" =', '"start: paradise" =', '"start: syndicate" =', '"combat rating" ='):
    if token in text:
        errors.append(f"forbidden authoritative-state write: {token}")
if text.count('mission "A2 Career Review:') != 2:
    errors.append("expected exactly two missions")
if errors:
    print("FAIL")
    print("\n".join("- " + e for e in errors))
    raise SystemExit(1)
print("PASS")
print("missions=2")
print("named_character=Nia Calder")
print("authoritative_inputs=start:* origin + combat rating")
print("career_principles=margin, force, options")
print("refusal_route=present")
print("later_reader=present")
print("authoritative_input_writes=none")
