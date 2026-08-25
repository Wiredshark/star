#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 syndicate overtime baseline compact.txt"
text = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Syndicate Overtime Baseline Compact:"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def block(start: str, next_marker: str | None = None) -> str:
    start_at = text.index(start)
    if next_marker is None:
        return text[start_at:]
    return text[start_at:text.index(next_marker, start_at + len(start))]


missions = re.findall(r'^mission "([^"]+)"', text, flags=re.MULTILINE)
require(missions == [PREFIX + " Offer", PREFIX + " Review", PREFIX + " Rhea Remembers"],
        f"unexpected mission graph: {missions}")
require(text.count('event "' + PREFIX + ' Review Ready"') == 4,
        "expected one Review event declaration plus three schedules")
require('event "' + PREFIX + ' Review Ready"\n\t"' + PREFIX + ' review ready" = 1' in text,
        "missing Review Ready payload")
for token in ("Kellan Voss", "Rhea Noll", 'government "Syndicate"'):
    require(token in text, f"missing character/scope token: {token}")

# A1/world state is consumed read-only.
for gate in ('"world: syndicate labor strain" >= 3', 'has "world: syndicate labor rotation active"',
             '"world: syndicate labor strain" <= 1', 'not "world: syndicate labor rotation active"'):
    require(gate in text, f"missing live-state gate: {gate}")
require('"world: syndicate labor strain" =' not in text, "B2 must not write labor strain")
require('"world: syndicate labor rotation active" =' not in text, "B2 must not write rotation state")

offer = block('mission "' + PREFIX + ' Offer"', 'mission "' + PREFIX + ' Review"')
review = block('mission "' + PREFIX + ' Review"', 'mission "' + PREFIX + ' Rhea Remembers"')
after = block('mission "' + PREFIX + ' Rhea Remembers"')

routes = {
    "baseline": PREFIX + " route baseline separate",
    "consent": PREFIX + " route current commitment",
    "paired": PREFIX + " route paired records",
}
for label, condition in routes.items():
    start = offer.index(f"\t\t\tlabel {label}")
    positions = [offer.find(f"\t\t\tlabel {x}", start + 1) for x in ("baseline", "consent", "paired", "decline")]
    positions = [p for p in positions if p != -1]
    segment = offer[start:min(positions)] if positions else offer[start:]
    require(segment.count('"' + PREFIX + ' introduced" = 1') == 1, f"{label} must introduce once")
    require(segment.count('"' + condition + '" = 1') == 1, f"{label} must write its route once")
    for other in routes.values():
        if other != condition:
            require('"' + other + '" = 1' not in segment, f"{label} must not write another route")
    require(segment.count('event "' + PREFIX + ' Review Ready" 7 11') == 1,
            f"{label} must schedule one Review")
    require(segment.count("\n\t\t\tdecline") == 1, f"{label} must terminate once")

refusal = offer[offer.index("\t\t\tlabel decline"):]
require(refusal.count('"' + PREFIX + ' declined" = 1') == 1, "refusal state missing")
require('"' + PREFIX + ' introduced" = 1' not in refusal, "refusal must not introduce")
require('event "' + PREFIX + ' Review Ready" 7 11' not in refusal, "refusal must not arm Review")

for gate in ('has "' + PREFIX + ' introduced"', 'has "' + PREFIX + ' review ready"',
             'not "' + PREFIX + ' reviewed"'):
    require(gate in review, f"Review missing lifecycle gate: {gate}")

settlements = {
    "packet": PREFIX + " settlement workload packet",
    "expiry": PREFIX + " settlement expiry and reset",
}
for label, condition in settlements.items():
    start = review.index(f"\t\t\tlabel {label}")
    positions = [review.find(f"\t\t\tlabel {x}", start + 1) for x in settlements]
    positions = [p for p in positions if p != -1]
    segment = review[start:min(positions)] if positions else review[start:]
    require(segment.count('"' + PREFIX + ' reviewed" = 1') == 1, f"{label} must close Review once")
    require(segment.count('"' + condition + '" = 1') == 1, f"{label} must write settlement once")
    for other in settlements.values():
        if other != condition:
            require('"' + other + '" = 1' not in segment, f"{label} must not write other settlement")
    require(segment.count("\n\t\t\tdecline") == 1, f"{label} must terminate once")

require('not "' + PREFIX + ' aftermath seen"' in after, "aftermath one-shot gate missing")
for condition in settlements.values():
    require('has "' + condition + '"' in after, f"aftermath missing settlement gate: {condition}")
require(after.count('"' + PREFIX + ' aftermath seen" = 1') == 1, "aftermath must write seen once")
require(after.count("\n\t\t\tdecline") == 1, "aftermath must terminate once")

writes = re.findall(r'^\s*"([^"]+)"\s*=\s*[-0-9]+\s*$', text, flags=re.MULTILINE)
require(writes and all(name.startswith(PREFIX) for name in writes), f"out-of-namespace writes: {writes}")
require(text.count("\n\t\t\taccept") == 0, "state-only slice must contain zero accept terminals")
require(text.count("\n\t\t\tdecline") == 7, "state-only slice must contain exactly seven decline terminals")
for directive in ("destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passenger ", "deadline ", "timer "):
    require("\n\t" + directive not in text and "\n\t\t" + directive not in text,
            f"unexpected gameplay objective directive: {directive.strip()}")

for fragment in (
    "one voluntary emergency becoming a standing obligation",
    "exceptional output can remain part of Rhea's work history without becoming the denominator",
    "overtime as a fresh commitment rather than inherited availability",
    "historical credit, but a future emergency requires a fresh request and fresh consent",
):
    require(fragment in text, f"missing continuity invariant: {fragment}")

print("B2 Syndicate Overtime Baseline Compact validation: PASS")
