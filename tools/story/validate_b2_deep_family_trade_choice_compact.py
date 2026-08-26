#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/human/b2 deep family trade choice compact.txt"
text = DATA.read_text(encoding="utf-8")

PREFIX = "B2 Deep Family Trade Choice Compact:"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def block(start: str, end: str | None = None) -> str:
    marker = f'mission "{start}"'
    require(marker in text, f"missing mission {start}")
    body = text.split(marker, 1)[1]
    if end:
        next_marker = f'mission "{end}"'
        require(next_marker in body, f"missing following mission {end}")
        body = body.split(next_marker, 1)[0]
    return body


def label_block(body: str, label: str, next_labels: list[str]) -> str:
    marker = f"\t\t\tlabel {label}\n"
    require(marker in body, f"missing label {label}")
    part = body.split(marker, 1)[1]
    cut = len(part)
    for next_label in next_labels:
        next_marker = f"\t\t\tlabel {next_label}\n"
        pos = part.find(next_marker)
        if pos >= 0:
            cut = min(cut, pos)
    return part[:cut]


require(text.endswith("\n"), "production file must end with newline")
require(text.count('mission "B2 Deep Family Trade Choice Compact:') == 3, "expected exactly three compact missions")
require('event "B2 Deep Family Trade Choice Compact: Review Ready"' in text, "missing delayed Review event")
require('has "A2 Career Review: later reader seen"' in text, "missing read-only A2 Career Review dependency")
require('government "Deep"' in text, "missing Deep source scope")
require("Sela Rook" in text and "Tomas Rook" in text, "missing recurring family characters")

# Persistence ownership: every assignment must stay in the B2 namespace.
for match in re.finditer(r'^\s*"([^"]+)"\s*=\s*-?\d+\s*$', text, re.MULTILINE):
    key = match.group(1)
    require(key.startswith(PREFIX), f"write outside B2 namespace: {key}")

# No gameplay/material objectives or direct economic/reputation mutations.
for line in text.splitlines():
    stripped = line.lstrip("\t")
    if len(line) == len(stripped):
        continue
    lower = stripped.lower()
    forbidden_starts = (
        "destination ", "stopover ", "waypoint ", "npc ", "cargo ",
        "passenger ", "deadline ", "payment ", "reputation ", "ship ",
        "fleet ", "outfit ", "combat rating =", "credits =",
    )
    require(not any(lower.startswith(token) for token in forbidden_starts), f"objective/material directive: {stripped}")

require(text.count("\n\t\t\t\tdecline\n") == 7, "expected seven state-only decline terminals")
require("\n\t\t\t\taccept\n" not in text, "state-only accept terminal is forbidden")

OFFER = "B2 Deep Family Trade Choice Compact: Offer"
REVIEW = "B2 Deep Family Trade Choice Compact: Review"
AFTER = "B2 Deep Family Trade Choice Compact: Tomas Remembers"
offer = block(OFFER, REVIEW)
review = block(REVIEW, AFTER)
after = block(AFTER)

routes = {
    "gift": "route training gift",
    "obligations": "route explicit obligations",
    "paired": "route paired history choice",
}
labels = ["gift", "obligations", "paired", "decline"]
for index, (label, state) in enumerate(routes.items()):
    section = label_block(offer, label, labels[index + 1:])
    require(section.count(f'"{PREFIX} introduced" = 1') == 1, f"{label} must introduce exactly once")
    require(section.count(f'"{PREFIX} {state}" = 1') == 1, f"{label} must write its own route exactly once")
    for other in routes.values():
        if other != state:
            require(f'"{PREFIX} {other}" = 1' not in section, f"{label} writes another route")
    require(section.count(f'event "{PREFIX} Review Ready" 7 11') == 1, f"{label} must schedule one 7-11 day Review")
    require(section.count("\n\t\t\t\tdecline\n") == 1, f"{label} must terminate exactly once")

decline_section = label_block(offer, "decline", [])
require(f'"{PREFIX} declined" = 1' in decline_section, "refusal must persist declined")
require(f'"{PREFIX} introduced" = 1' not in decline_section, "refusal must not introduce arc")
require(f'event "{PREFIX} Review Ready" 7 11' not in decline_section, "refusal must not schedule Review")
for state in routes.values():
    require(f'"{PREFIX} {state}" = 1' not in decline_section, "refusal must not write substantive route")

require(f'has "{PREFIX} introduced"' in review, "Review must require introduction")
require(f'has "{PREFIX} review ready"' in review, "Review must require delayed ready state")
require(f'not "{PREFIX} reviewed"' in review, "Review must be one-shot")
require(f'has "{PREFIX} route explicit obligations"' in review, "Review must branch on obligations route")
require(f'has "{PREFIX} route paired history choice"' in review, "Review must branch on paired route")

settlements = {
    "packet": "settlement portable training choice",
    "renewal": "settlement fresh succession consent",
}
review_labels = ["packet", "renewal"]
for index, (label, state) in enumerate(settlements.items()):
    section = label_block(review, label, review_labels[index + 1:])
    require(section.count(f'"{PREFIX} reviewed" = 1') == 1, f"{label} must close Review exactly once")
    require(section.count(f'"{PREFIX} {state}" = 1') == 1, f"{label} must write its settlement exactly once")
    for other in settlements.values():
        if other != state:
            require(f'"{PREFIX} {other}" = 1' not in section, f"{label} writes another settlement")
    require(section.count("\n\t\t\t\tdecline\n") == 1, f"{label} must terminate exactly once")

require(f'not "{PREFIX} aftermath seen"' in after, "aftermath must be one-shot")
for state in settlements.values():
    require(f'has "{PREFIX} {state}"' in after, f"aftermath must consume {state}")
require(after.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must write seen exactly once")
require(after.count("\n\t\t\t\tdecline\n") == 1, "aftermath must terminate exactly once")

# Continuity/canon boundary.
for fragment in (
    "skill is not the same thing as consent",
    "family history rather than proof of a present obligation",
    "current career choice",
    "fresh agreement",
    "not Deep labor law",
):
    require(fragment in text, f"missing continuity invariant fragment: {fragment}")

print("PASS: B2 Deep Family Trade Choice Compact")
