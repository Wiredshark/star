#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 free worlds caregiving leave compact.txt"
text = DATA.read_text(encoding="utf-8")

PREFIX = "B2 Free Worlds Caregiving Leave Compact:"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def block(start: str, next_marker: str | None = None) -> str:
    start_at = text.index(start)
    if next_marker is None:
        return text[start_at:]
    end_at = text.index(next_marker, start_at + len(start))
    return text[start_at:end_at]


# Exact three-mission character arc and one delayed event.
missions = re.findall(r'^mission "([^"]+)"', text, flags=re.MULTILINE)
require(missions == [
    PREFIX + " Offer",
    PREFIX + " Review",
    PREFIX + " Jalen Remembers",
], f"unexpected mission graph: {missions}")
require(text.count('event "' + PREFIX + ' Review Ready"') == 4,
        "expected one event declaration plus three substantive route schedules")
require('event "' + PREFIX + ' Review Ready"\n\t"' + PREFIX + ' review ready" = 1' in text,
        "missing delayed review event payload")

# Character/scope and authoritative A1 dependency.
for token in ("Mira Senn", "Jalen Ro", 'government "Free Worlds"'):
    require(token in text, f"missing character/scope token: {token}")
require(text.count('"world: free worlds defense strain" >= 3') == 1,
        "Offer must consume high defense strain exactly once")
require(text.count('"world: free worlds defense strain" <= 1') == 1,
        "Review must consume recovered defense strain exactly once")
require('"world: free worlds defense strain" =' not in text,
        "B2 must never write authoritative A1 defense strain")

# Split route and lifecycle blocks to prove writes are local rather than aggregate-only.
offer = block('mission "' + PREFIX + ' Offer"', 'mission "' + PREFIX + ' Review"')
review = block('mission "' + PREFIX + ' Review"', 'mission "' + PREFIX + ' Jalen Remembers"')
aftermath = block('mission "' + PREFIX + ' Jalen Remembers"')

route_labels = {
    "availability": PREFIX + " route bounded availability",
    "standby": PREFIX + " route voluntary standby",
    "paired": PREFIX + " route paired records",
}
for label, condition in route_labels.items():
    segment = offer[offer.index(f"\t\t\tlabel {label}"):]
    # stop at the next route/refusal label
    following = [offer.find(f"\t\t\tlabel {x}", offer.index(f"\t\t\tlabel {label}") + 1)
                 for x in ("availability", "standby", "paired", "decline")]
    following = [x for x in following if x != -1]
    if following:
        segment = offer[offer.index(f"\t\t\tlabel {label}"):min(following)]
    require(segment.count('"' + PREFIX + ' introduced" = 1') == 1,
            f"{label} must write introduced exactly once")
    require(segment.count('"' + condition + '" = 1') == 1,
            f"{label} must write its own route exactly once")
    for other in route_labels.values():
        if other != condition:
            require('"' + other + '" = 1' not in segment,
                    f"{label} must not write another route")
    require(segment.count('event "' + PREFIX + ' Review Ready" 7 11') == 1,
            f"{label} must schedule exactly one 7-11 day Review")
    require(segment.count("\n\t\t\tdecline") == 1,
            f"{label} must terminate exactly once with decline")

refusal = offer[offer.index("\t\t\tlabel decline"):]
require('"' + PREFIX + ' declined" = 1' in refusal, "refusal state missing")
require('"' + PREFIX + ' introduced" = 1' not in refusal, "refusal must not introduce arc")
require('event "' + PREFIX + ' Review Ready" 7 11' not in refusal, "refusal must not arm Review")
for condition in route_labels.values():
    require('"' + condition + '" = 1' not in refusal, "refusal must not write substantive route")

# Review lifecycle and terminal settlements.
for gate in (
    'has "' + PREFIX + ' introduced"',
    'has "' + PREFIX + ' review ready"',
    'not "' + PREFIX + ' reviewed"',
):
    require(gate in review, f"Review missing lifecycle gate: {gate}")
settlements = {
    "packet": PREFIX + " settlement portable availability packet",
    "expiry": PREFIX + " settlement expiry plus fresh request",
}
for label, condition in settlements.items():
    start = review.index(f"\t\t\tlabel {label}")
    following = [review.find(f"\t\t\tlabel {x}", start + 1) for x in ("packet", "expiry")]
    following = [x for x in following if x != -1]
    segment = review[start:min(following)] if following else review[start:]
    require(segment.count('"' + PREFIX + ' reviewed" = 1') == 1,
            f"{label} must close Review exactly once")
    require(segment.count('"' + condition + '" = 1') == 1,
            f"{label} must write its own settlement exactly once")
    for other in settlements.values():
        if other != condition:
            require('"' + other + '" = 1' not in segment,
                    f"{label} must not write the other settlement")
    require(segment.count("\n\t\t\tdecline") == 1,
            f"{label} must terminate exactly once")

# One-shot aftermath consumes either settlement.
require('not "' + PREFIX + ' aftermath seen"' in aftermath, "aftermath one-shot gate missing")
for condition in settlements.values():
    require('has "' + condition + '"' in aftermath, f"aftermath missing settlement gate: {condition}")
require(aftermath.count('"' + PREFIX + ' aftermath seen" = 1') == 1,
        "aftermath must write seen exactly once")
require(aftermath.count("\n\t\t\tdecline") == 1, "aftermath must terminate exactly once")

# Ownership / gameplay lifecycle invariants.
writes = re.findall(r'^\s*"([^"]+)"\s*=\s*[-0-9]+\s*$', text, flags=re.MULTILINE)
require(writes, "no persistent writes found")
require(all(name.startswith(PREFIX) for name in writes), f"out-of-namespace writes: {writes}")
require(text.count("\n\t\t\taccept") == 0, "state-only slice must contain zero accept terminals")
require(text.count("\n\t\t\tdecline") == 7, "state-only slice must contain exactly seven decline terminals")
for directive in ("destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passenger ", "deadline ", "timer "):
    require("\n\t" + directive not in text and "\n\t\t" + directive not in text,
            f"unexpected gameplay objective directive: {directive.strip()}")
for forbidden in ("credits", "reputation", "combat rating", "government attitude", "outfit ", "ship ", "fleet "):
    require(forbidden not in "\n".join(line.lower() for line in text.splitlines() if line.startswith("\t\taction") or line.startswith("\t\t\t\t")),
            f"unexpected material/reputation mutation token: {forbidden}")

# Continuity assertions: current availability is not permanent reliability judgment;
# private family detail is not required for ordinary staffing; one local solution is
# not centralized Free Worlds employment law.
semantic_fragments = (
    "current answer, not a biography",
    "family reason stays outside routine staffing copies",
    "volunteering for a defined emergency cannot become an unlimited claim",
    "old leave and standby entries as history rather than current authority",
    "voluntary Free Worlds practice rather than centralized employment law",
)
for fragment in semantic_fragments:
    require(fragment in text, f"missing continuity invariant: {fragment}")

print("B2 Free Worlds Caregiving Leave Compact validation: PASS")
