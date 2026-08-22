#!/usr/bin/env python3
from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/sheragi/b2 sheragi context compact.txt")
path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
text = path.read_text(encoding="utf-8")

PREFIX = "B2 Sheragi Context Compact:"


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


missions = re.findall(r'^mission "([^"]+)"', text, flags=re.M)
require(missions == [
    "B2 Sheragi Context Compact: Offer",
    "B2 Sheragi Context Compact: Review",
    "B2 Sheragi Context Compact: Nadia Remembers",
], "expected exactly the Offer, Review, and Nadia Remembers mission graph")

require('event "B2 Sheragi Context Compact: Review Ready"' in text,
        "missing delayed review event")
require('event "B2 Sheragi Context Compact: Review Ready" 7 11' in text,
        "substantive routes must schedule delayed review")

for name in ("Nadia Rell", "Ivo March"):
    require(name in text, f"missing named character {name}")

for gate in (
    'has "Sheragi Archaeology: Epilogue: done"',
    'has "Sheragi History: Evidence Provenance Register: offered"',
    'has "Sheragi History: Site Context Registry: offered"',
):
    require(gate in text, f"missing B1/campaign gate {gate}")

for route in ("route shelter", "route context", "route paired"):
    require(f'"{PREFIX} {route}" = 1' in text, f"missing persistent route {route}")
require(f'"{PREFIX} declined" = 1' in text, "missing refusal persistence")

settlements = [
    "settlement portable context packet",
    "settlement reversible reconstruction",
]
for settlement in settlements:
    require(f'"{PREFIX} {settlement}" = 1' in text,
            f"missing terminal settlement {settlement}")
require(text.count(f'"{PREFIX} reviewed" = 1') == 2,
        "Review must have exactly two terminal settlement writes")

require(f'"{PREFIX} aftermath seen" = 1' in text,
        "later reader must record one-shot aftermath state")
for settlement in settlements:
    require(f'has "{PREFIX} {settlement}"' in text,
            f"later reader must consume {settlement}")

# State ownership: every assignment in this B2 file must be namespaced to this slice.
assignments = re.findall(r'^\s*"([^"]+)"\s*=\s*[-0-9]+\s*$', text, flags=re.M)
require(assignments, "no persistent state assignments found")
for condition in assignments:
    require(condition.startswith(PREFIX),
            f"writes condition outside B2 namespace: {condition}")

# No direct material/reputation/combat mutations in this character-content slice.
for forbidden in (
    "credits ", "reputation ", "cargo ", "outfit ", "ship ", "fleet ",
    "combat rating", "payment ",
):
    require(forbidden not in text.lower(), f"forbidden direct mutation token: {forbidden.strip()}")

# Lifecycle invariant: these missions only record story state. They do not create a
# gameplay objective, so accepting them would leave objective-less missions active.
require(not re.search(r'^\s*accept\s*$', text, flags=re.M),
        "state-only Sheragi missions must not use terminal accept")
require(len(re.findall(r'^\s*decline\s*$', text, flags=re.M)) == 7,
        "expected exactly seven state-only decline terminals")
for directive in (
    "destination ", "stopover ", "waypoint ", "npc ", "cargo ",
    "passenger ", "deadline ", "timer ",
):
    require(not re.search(rf'^\s*{re.escape(directive)}', text, flags=re.M | re.I),
            f"unexpected objective-bearing directive: {directive.strip()}")

# Conversation local label integrity.
for block in re.split(r'(?=^mission ")', text, flags=re.M)[1:]:
    labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.M))
    gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.M)
    for target in gotos:
        require(target in labels, f"goto target {target} has no local label")

# Continuity invariants from B1: object, context, reconstruction, and interpretation
# must remain distinguishable rather than becoming unsupported Sheragi history claims.
for concept in (
    "site context", "measured", "reconstructed", "uncertainty",
    "original", "interpretation",
):
    require(concept in text.lower(), f"missing continuity concept: {concept}")

unsupported = (
    "the sheragi intended",
    "the sheragi believed",
    "the sheragi government",
    "the sheragi empire required",
)
for phrase in unsupported:
    require(phrase not in text.lower(), f"unsupported ancient-Sheragi claim: {phrase}")

print("PASS: B2 Sheragi Context Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: later_reader=Nadia Remembers")
print("PASS: state_ownership=B2 namespace only")
print("PASS: lifecycle=7 state-only decline terminals, 0 accepts")
print("PASS: continuity=object/context/reconstruction/interpretation remain distinct")
