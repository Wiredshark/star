#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/b2 deep keepsake friendship.txt"
TEXT = PATH.read_text(encoding="utf-8")

PREFIX = "B2 Deep Keepsake Friendship:"
MISSIONS = [
    "Offer",
    "Review",
    "Sana Remembers",
]
ROUTES = [
    "route shared ritual",
    "route no debt",
    "route gifts separate",
]
SETTLEMENTS = [
    "settlement broad reciprocity",
    "settlement explicit promises",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def mission_block(name: str) -> str:
    marker = f'mission "{PREFIX} {name}"'
    start = TEXT.find(marker)
    require(start >= 0, f"missing mission {name}")
    next_start = TEXT.find('\n\nmission "', start + len(marker))
    return TEXT[start:] if next_start < 0 else TEXT[start:next_start]


def label_block(block: str, label: str, next_labels: list[str]) -> str:
    marker = f"\n\t\t\tlabel {label}\n"
    start = block.find(marker)
    require(start >= 0, f"missing label {label}")
    start += len(marker)
    ends = []
    for candidate in next_labels:
        pos = block.find(f"\n\t\t\tlabel {candidate}\n", start)
        if pos >= 0:
            ends.append(pos)
    return block[start:min(ends)] if ends else block[start:]


require(TEXT.endswith("\n"), "file must end with newline")
require(TEXT.count("mission \"") == 3, "expected exactly three missions")
for mission in MISSIONS:
    mission_block(mission)

require('has "Gift Store Interaction: declined"' in mission_block("Offer"), "Offer must consume the existing Deep gift-store encounter")
require('attributes "deep"' in TEXT, "all content must remain Deep-scoped")
require(TEXT.count('attributes "deep"') == 3, "each mission must be Deep-scoped")
require(TEXT.count('event "B2 Deep Keepsake Friendship: Review Ready" 7 11') == 3, "three substantive routes must schedule one 7-11 day Review")
require(TEXT.count('\n\t\t\t\tdecline\n') == 7, "all seven state-only terminals must decline")
require('\n\t\t\t\taccept\n' not in TEXT, "state-only arc must not accept objective-less missions")

# No gameplay objectives or material rewards are allowed in this dialogue-only slice.
for token in ["\n\tdestination ", "\n\tstopover ", "\n\twaypoint ", "\n\tnpc ", "\n\tcargo ", "\n\tpassengers ", "\n\tdeadline ", "\n\ttimer ", "payment ", "outfit "]:
    require(token not in TEXT, f"unexpected gameplay/material directive: {token.strip()}")

# All persistent writes must stay within the B2 namespace.
for line in TEXT.splitlines():
    stripped = line.strip()
    if stripped.startswith('"') and '" =' in stripped:
        key = stripped.split('"', 2)[1]
        require(key.startswith(PREFIX), f"out-of-namespace persistent write: {key}")
require('"world:' not in TEXT, "must not write or depend on world state")

# Route-local lifecycle checks.
offer = mission_block("Offer")
route_labels = ["ritual", "nodebt", "separate", "decline"]
route_state_by_label = {
    "ritual": "route shared ritual",
    "nodebt": "route no debt",
    "separate": "route gifts separate",
}
for index, label in enumerate(route_labels):
    block = label_block(offer, label, route_labels[index + 1:])
    require(block.count("\n\t\t\t\tdecline\n") == 1, f"Offer {label} must terminate once")
    if label == "decline":
        require(f'"{PREFIX} declined" = 1' in block, "refusal must write declined")
        require(f'"{PREFIX} introduced" = 1' not in block, "refusal must not introduce arc")
        require("Review Ready\" 7 11" not in block, "refusal must not schedule Review")
        for route in ROUTES:
            require(f'"{PREFIX} {route}" = 1' not in block, "refusal must not write route state")
    else:
        route = route_state_by_label[label]
        require(block.count(f'"{PREFIX} introduced" = 1') == 1, f"{label} must introduce once")
        require(block.count(f'"{PREFIX} {route}" = 1') == 1, f"{label} must write own route once")
        for other in ROUTES:
            if other != route:
                require(f'"{PREFIX} {other}" = 1' not in block, f"{label} must not write {other}")
        require(block.count('event "B2 Deep Keepsake Friendship: Review Ready" 7 11') == 1, f"{label} must schedule one Review")

review = mission_block("Review")
require(f'has "{PREFIX} introduced"' in review, "Review requires introduction")
require(f'has "{PREFIX} review ready"' in review, "Review requires delayed readiness")
require(f'not "{PREFIX} reviewed"' in review, "Review must be one-shot")
for settlement_label, settlement in [("broad", SETTLEMENTS[0]), ("explicit", SETTLEMENTS[1])]:
    block = label_block(review, settlement_label, ["explicit"] if settlement_label == "broad" else [])
    require(block.count(f'"{PREFIX} reviewed" = 1') == 1, f"{settlement_label} must close Review once")
    require(block.count(f'"{PREFIX} {settlement}" = 1') == 1, f"{settlement_label} must write its settlement once")
    other = SETTLEMENTS[1] if settlement == SETTLEMENTS[0] else SETTLEMENTS[0]
    require(f'"{PREFIX} {other}" = 1' not in block, f"{settlement_label} must not write other settlement")
    require(block.count("\n\t\t\t\tdecline\n") == 1, f"{settlement_label} must terminate once")

after = mission_block("Sana Remembers")
for settlement in SETTLEMENTS:
    require(f'has "{PREFIX} {settlement}"' in after, f"aftermath must consume {settlement}")
require(f'not "{PREFIX} aftermath seen"' in after, "aftermath must be one-shot")
require(after.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must write seen exactly once")
require(after.count("\n\t\t\t\tdecline\n") == 1, "aftermath must terminate once")

# Character/canon checks: this is deliberately a personal friendship arc, not a new Deep institution.
for phrase in ["Niko Rell", "Sana Vey", "souvenir", "friendship", "gift", "promise"]:
    require(phrase.lower() in TEXT.lower(), f"missing core character/theme phrase: {phrase}")
for forbidden in ["Deep law", "Deep authority", "Deep office", "Republic law", "universal rule"]:
    require(forbidden.lower() not in TEXT.lower(), f"must not invent centralized authority: {forbidden}")

print("PASS: B2 Deep Keepsake Friendship")
