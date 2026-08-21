#!/usr/bin/env python3
"""Focused structural validation for B2 Core Repair Reciprocity."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/human/b2 core repair reciprocity.txt"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


text = DATA.read_text(encoding="utf-8")

missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
expected_missions = [
    "B2 Core Repair Reciprocity: Offer",
    "B2 Core Repair Reciprocity: Review",
    "B2 Core Repair Reciprocity: Renn Remembers",
]
if missions != expected_missions:
    fail(f"mission list mismatch: {missions!r}")

for name in ("Asha Renn", "Jalen Cross"):
    if name not in text:
        fail(f"missing named character {name}")

for route in ("renn", "cross", "provisional"):
    token = f'"B2 Core Repair Reciprocity: route {route}" = 1'
    if text.count(token) != 1:
        fail(f"expected exactly one write for route {route}")

if text.count('"B2 Core Repair Reciprocity: declined" = 1') != 1:
    fail("decline state must be written exactly once")

settlements = (
    '"B2 Core Repair Reciprocity: settlement reciprocal credential" = 1',
    '"B2 Core Repair Reciprocity: settlement portable endorsement" = 1',
)
for token in settlements:
    if text.count(token) != 1:
        fail(f"expected exactly one terminal settlement write: {token}")

if text.count('"B2 Core Repair Reciprocity: reviewed" = 1') != 2:
    fail("reviewed state should be written by exactly the two terminal outcomes")

if text.count('"B2 Core Repair Reciprocity: aftermath seen" = 1') != 1:
    fail("aftermath reader must record one-shot completion exactly once")

required_scope = '\t\tgovernment "Republic"\n\t\tattributes core factory'
if text.count(required_scope) != 3:
    fail("all three missions must be scoped to Republic core factory sources")

labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE)
missing = sorted(set(gotos) - labels)
if missing:
    fail(f"goto target(s) missing labels: {missing}")

# Review intentionally uses route provisional as conversation fallthrough; only
# the two polarized initial routes branch to specialized review text.
if text.count('\t\t\tbranch renn\n\t\t\t\thas "B2 Core Repair Reciprocity: route renn"') != 1:
    fail("missing Renn review branch")
if text.count('\t\t\tbranch cross\n\t\t\t\thas "B2 Core Repair Reciprocity: route cross"') != 1:
    fail("missing Cross review branch")
if '\t\t\tbranch provisional' in text:
    fail("provisional route should remain the intentional Review fallthrough")

for forbidden in (
    '\tcredits ',
    '\tpayment ',
    '\treputation ',
    '\tcargo ',
    '\toutfit ',
    '\tship ',
    '\tfleet ',
):
    if forbidden in text:
        fail(f"unexpected direct material/gameplay reward mutation: {forbidden.strip()}")

# These three missions are dialogue/state-only. Accepting a terminal branch would
# leave an objective-less mission active after the conversation closes, so every
# terminal path must decline after persisting its state.
if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
    fail("state-only Core Repair Reciprocity missions must not leave accepted missions active")

if len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)) != 7:
    fail("expected exactly seven state-only dialogue terminals to decline")

for objective in (
    '\tdestination ',
    '\tstopover ',
    '\twaypoint ',
    '\tnpc ',
    '\tdeadline ',
    '\tpassengers ',
    '\tcargo ',
):
    if objective in text:
        fail(f"unexpected mission objective in state-only lifecycle slice: {objective.strip()}")

print("PASS: B2 Core Repair Reciprocity structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: review_routing=provisional fallthrough + explicit Renn/Cross branches")
print("PASS: terminal_settlements=2")
print("PASS: later_reader=Renn Remembers")
print("PASS: persistence_model=stock mission/global conditions")
print("PASS: lifecycle=state-only dialogue terminals decline cleanly")
