#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/incipias/b2 incipias family flight consent compact.txt"
text = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Incipias Family Flight Consent Compact:"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def mission_block(name: str, next_name: str | None = None) -> str:
    marker = f'mission "{name}"'
    require(marker in text, f"missing mission {name}")
    body = text.split(marker, 1)[1]
    if next_name:
        next_marker = f'mission "{next_name}"'
        require(next_marker in body, f"missing following mission {next_name}")
        body = body.split(next_marker, 1)[0]
    return body


def label_block(body: str, label: str, following: list[str]) -> str:
    marker = f"\t\t\tlabel {label}\n"
    require(marker in body, f"missing label {label}")
    part = body.split(marker, 1)[1]
    end = len(part)
    for candidate in following:
        pos = part.find(f"\t\t\tlabel {candidate}\n")
        if pos >= 0:
            end = min(end, pos)
    return part[:end]


require(text.endswith("\n"), "production file must end with newline")
require(text.count('mission "B2 Incipias Family Flight Consent Compact:') == 3, "expected exactly three compact missions")
require('event "B2 Incipias Family Flight Consent Compact: Review Ready"' in text, "missing delayed Review event")
require('government "Conlatio"' in text, "missing Conlatio scope")
require('has "B2 Incipias License Compact: aftermath seen"' in text, "missing integrated Incipias license aftermath dependency")
require("Seli Naran" in text and "Tavi Naran" in text, "missing recurring family characters")
require("not universal Incipias law" in text, "missing local-not-universal canon boundary")

for match in re.finditer(r'^\s*"([^"]+)"\s*=\s*-?\d+\s*$', text, re.MULTILINE):
    key = match.group(1)
    require(key.startswith(PREFIX), f"write outside B2 namespace: {key}")

for line in text.splitlines():
    if not line.startswith("\t"):
        continue
    stripped = line.lstrip("\t").lower()
    forbidden = (
        "destination ", "stopover ", "waypoint ", "npc ", "cargo ",
        "passenger ", "deadline ", "payment ", "reputation ", "ship ",
        "fleet ", "outfit ", "combat rating =", "credits =",
    )
    require(not any(stripped.startswith(token) for token in forbidden), f"objective/material directive: {stripped}")

require(text.count("\n\t\t\t\tdecline\n") == 7, "expected seven state-only decline terminals")
require("\n\t\t\t\taccept\n" not in text, "state-only accept terminal is forbidden")

OFFER = "B2 Incipias Family Flight Consent Compact: Offer"
REVIEW = "B2 Incipias Family Flight Consent Compact: Review"
AFTER = "B2 Incipias Family Flight Consent Compact: Seli Remembers"
offer = mission_block(OFFER, REVIEW)
review = mission_block(REVIEW, AFTER)
after = mission_block(AFTER)

routes = {
    "separate": "route contact separate",
    "bounded": "route bounded delegation",
    "paired": "route paired records",
}
route_labels = ["separate", "bounded", "paired", "decline"]
for index, (label, state) in enumerate(routes.items()):
    section = label_block(offer, label, route_labels[index + 1:])
    require(section.count(f'"{PREFIX} introduced" = 1') == 1, f"{label} must introduce exactly once")
    require(section.count(f'"{PREFIX} {state}" = 1') == 1, f"{label} must write route exactly once")
    for other in routes.values():
        if other != state:
            require(f'"{PREFIX} {other}" = 1' not in section, f"{label} writes another route")
    require(section.count(f'event "{PREFIX} Review Ready" 7 11') == 1, f"{label} must schedule exactly one 7-11 day Review")
    require(section.count("\n\t\t\t\tdecline\n") == 1, f"{label} must terminate once")

refusal = label_block(offer, "decline", [])
require(f'"{PREFIX} declined" = 1' in refusal, "refusal must persist declined")
require(f'"{PREFIX} introduced" = 1' not in refusal, "refusal must not introduce arc")
require(f'event "{PREFIX} Review Ready" 7 11' not in refusal, "refusal must not schedule Review")
for state in routes.values():
    require(f'"{PREFIX} {state}" = 1' not in refusal, "refusal must not write substantive route")

require(f'has "{PREFIX} introduced"' in review, "Review must require introduction")
require(f'has "{PREFIX} review ready"' in review, "Review must require delayed ready state")
require(f'not "{PREFIX} reviewed"' in review, "Review must be one-shot")
require(f'has "{PREFIX} route bounded delegation"' in review, "Review must branch on bounded route")
require(f'has "{PREFIX} route paired records"' in review, "Review must branch on paired route")
require(f'has "{PREFIX} route contact separate"' not in review, "contact-separate route should remain deliberate default Review path")

settlements = {
    "packet": "settlement portable family flight packet",
    "renewal": "settlement fresh purpose renewal",
}
settlement_labels = ["packet", "renewal"]
for index, (label, state) in enumerate(settlements.items()):
    section = label_block(review, label, settlement_labels[index + 1:])
    require(section.count(f'"{PREFIX} reviewed" = 1') == 1, f"{label} must close Review exactly once")
    require(section.count(f'"{PREFIX} {state}" = 1') == 1, f"{label} must write settlement exactly once")
    for other in settlements.values():
        if other != state:
            require(f'"{PREFIX} {other}" = 1' not in section, f"{label} writes another settlement")
    require(section.count("\n\t\t\t\tdecline\n") == 1, f"{label} must terminate once")

require(f'not "{PREFIX} aftermath seen"' in after, "aftermath must be one-shot")
for state in settlements.values():
    require(f'has "{PREFIX} {state}"' in after, f"aftermath must consume {state}")
require(after.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must write seen exactly once")
require(after.count("\n\t\t\t\tdecline\n") == 1, "aftermath must terminate exactly once")

for fragment in (
    "being the first person called after an accident is not the same role as approving whether another adult may fly",
    "current authority Seli deliberately delegates",
    "system preserved a true relationship while inventing a present authority",
    "Historical family contacts remain history".lower(),
):
    require(fragment.lower() in text.lower(), f"missing continuity invariant fragment: {fragment}")

print("PASS: B2 Incipias Family Flight Consent Compact")
