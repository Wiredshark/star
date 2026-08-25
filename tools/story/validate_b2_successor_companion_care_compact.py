#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "successors" / "b2 successor companion care compact.txt"
text = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Successor Companion Care Compact:"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def block(start: str, next_marker: str | None = None) -> str:
    start_at = text.index(start)
    if next_marker is None:
        return text[start_at:]
    end_at = text.index(next_marker, start_at + len(start))
    return text[start_at:end_at]


missions = re.findall(r'^mission "([^"]+)"', text, flags=re.MULTILINE)
require(missions == [
    PREFIX + " Offer",
    PREFIX + " Review",
    PREFIX + " Sona Remembers",
], f"unexpected mission graph: {missions}")
require(text.count('event "' + PREFIX + ' Review Ready"') == 4,
        "expected one event declaration plus three substantive route schedules")
require('event "' + PREFIX + ' Review Ready"\n\t"' + PREFIX + ' review ready" = 1' in text,
        "missing delayed review event payload")

for token in ("Ryii Vael", "Sona Mii", "Palu", 'attributes "successor"'):
    require(token in text, f"missing character/scope token: {token}")
require(text.count('has "known to the successors"') == 1,
        "Offer must consume Successor recognition exactly once")
require(text.count('has "Successors: First Contact 2: done"') == 1,
        "Offer must require completed Successor first contact exactly once")
require('"known to the successors" =' not in text, "B2 must not write recognition state")
require('"Successors: First Contact 2: done" =' not in text, "B2 must not write first-contact state")

offer = block('mission "' + PREFIX + ' Offer"', 'mission "' + PREFIX + ' Review"')
review = block('mission "' + PREFIX + ' Review"', 'mission "' + PREFIX + ' Sona Remembers"')
aftermath = block('mission "' + PREFIX + ' Sona Remembers"')

route_labels = {
    "tasks": PREFIX + " route task specific",
    "consent": PREFIX + " route current consent",
    "paired": PREFIX + " route paired records",
}
for label, condition in route_labels.items():
    start = offer.index(f"\t\t\tlabel {label}")
    following = [offer.find(f"\t\t\tlabel {x}", start + 1)
                 for x in ("tasks", "consent", "paired", "decline")]
    following = [x for x in following if x != -1]
    segment = offer[start:min(following)] if following else offer[start:]
    require(segment.count('"' + PREFIX + ' introduced" = 1') == 1,
            f"{label} must write introduced exactly once")
    require(segment.count('"' + condition + '" = 1') == 1,
            f"{label} must write its route exactly once")
    for other in route_labels.values():
        if other != condition:
            require('"' + other + '" = 1' not in segment,
                    f"{label} must not write another route")
    require(segment.count('event "' + PREFIX + ' Review Ready" 7 11') == 1,
            f"{label} must schedule exactly one Review")
    require(segment.count("\n\t\t\tdecline") == 1,
            f"{label} must terminate exactly once with decline")

refusal = offer[offer.index("\t\t\tlabel decline"):]
require('"' + PREFIX + ' declined" = 1' in refusal, "refusal state missing")
require('"' + PREFIX + ' introduced" = 1' not in refusal, "refusal must not introduce arc")
require('event "' + PREFIX + ' Review Ready" 7 11' not in refusal, "refusal must not arm Review")
for condition in route_labels.values():
    require('"' + condition + '" = 1' not in refusal, "refusal must not write a substantive route")

for gate in (
    'has "' + PREFIX + ' introduced"',
    'has "' + PREFIX + ' review ready"',
    'not "' + PREFIX + ' reviewed"',
):
    require(gate in review, f"Review missing lifecycle gate: {gate}")

settlements = {
    "packet": PREFIX + " settlement portable care packet",
    "renewal": PREFIX + " settlement expiry and renewal",
}
for label, condition in settlements.items():
    start = review.index(f"\t\t\tlabel {label}")
    following = [review.find(f"\t\t\tlabel {x}", start + 1) for x in ("packet", "renewal")]
    following = [x for x in following if x != -1]
    segment = review[start:min(following)] if following else review[start:]
    require(segment.count('"' + PREFIX + ' reviewed" = 1') == 1,
            f"{label} must close Review exactly once")
    require(segment.count('"' + condition + '" = 1') == 1,
            f"{label} must write its settlement exactly once")
    for other in settlements.values():
        if other != condition:
            require('"' + other + '" = 1' not in segment,
                    f"{label} must not write the other settlement")
    require(segment.count("\n\t\t\tdecline") == 1,
            f"{label} must terminate exactly once")

require('not "' + PREFIX + ' aftermath seen"' in aftermath, "aftermath one-shot gate missing")
for condition in settlements.values():
    require('has "' + condition + '"' in aftermath, f"aftermath missing settlement gate: {condition}")
require(aftermath.count('"' + PREFIX + ' aftermath seen" = 1') == 1,
        "aftermath must write seen exactly once")
require(aftermath.count("\n\t\t\tdecline") == 1, "aftermath must terminate exactly once")

writes = re.findall(r'^\s*"([^"]+)"\s*=\s*[-0-9]+\s*$', text, flags=re.MULTILINE)
require(writes, "no persistent writes found")
require(all(name.startswith(PREFIX) for name in writes), f"out-of-namespace writes: {writes}")
require(text.count("\n\t\t\taccept") == 0, "state-only slice must contain zero accept terminals")
require(text.count("\n\t\t\tdecline") == 7, "state-only slice must contain exactly seven decline terminals")
for directive in ("destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passenger ", "deadline ", "timer "):
    require("\n\t" + directive not in text and "\n\t\t" + directive not in text,
            f"unexpected gameplay objective directive: {directive.strip()}")

forbidden_action_tokens = ("credits", "reputation", "combat rating", "government attitude", "outfit ", "ship ", "fleet ")
actionish = "\n".join(line.lower() for line in text.splitlines()
                      if line.startswith("\t\taction") or line.startswith("\t\t\t\t"))
for forbidden in forbidden_action_tokens:
    require(forbidden not in actionish, f"unexpected material/reputation mutation token: {forbidden}")

semantic_fragments = (
    "routine help remain easy while major non-emergency decisions require a current, explicit grant",
    "History stays visible without becoming a standing order",
    "history of useful work should remain credit for the work, not become ownership by accumulation",
    "authority that once existed can remain historically true without remaining active",
    "one household's arrangement, not centralized Successor law",
)
for fragment in semantic_fragments:
    require(fragment in text, f"missing continuity invariant: {fragment}")

print("B2 Successor Companion Care Compact validation: PASS")
