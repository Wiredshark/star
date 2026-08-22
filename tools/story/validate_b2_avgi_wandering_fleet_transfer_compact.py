#!/usr/bin/env python3
"""Focused structural validation for B2 Avgi Wandering Fleet Transfer Compact."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/avgi/b2 avgi wandering fleet transfer compact.txt"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


text = DATA.read_text(encoding="utf-8")
missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
expected = [
    "B2 Avgi Wandering Fleet Transfer Compact: Offer",
    "B2 Avgi Wandering Fleet Transfer Compact: Review",
    "B2 Avgi Wandering Fleet Transfer Compact: Loadkeeper Remembers",
]
if missions != expected:
    fail(f"mission list mismatch: {missions!r}")

for token in ("Loadkeeper", "Fitter"):
    if token not in text:
        fail(f"missing recurring character shorthand {token}")

if "private shorthand" not in text:
    fail("must explicitly preserve private-shorthand continuity boundary")

for route in ("reserve", "repair", "paired"):
    if text.count(f'"B2 Avgi Wandering Fleet Transfer Compact: route {route}" = 1') != 1:
        fail(f"route {route} must be written exactly once")

if text.count('"B2 Avgi Wandering Fleet Transfer Compact: declined" = 1') != 1:
    fail("decline state must be written exactly once")

settlements = (
    '"B2 Avgi Wandering Fleet Transfer Compact: settlement portable transfer debt" = 1',
    '"B2 Avgi Wandering Fleet Transfer Compact: settlement dependency reconciliation" = 1',
)
for token in settlements:
    if text.count(token) != 1:
        fail(f"terminal settlement write mismatch: {token}")

if text.count('"B2 Avgi Wandering Fleet Transfer Compact: reviewed" = 1') != 2:
    fail("reviewed state must be written by exactly two terminal settlements")
if text.count('"B2 Avgi Wandering Fleet Transfer Compact: aftermath seen" = 1') != 1:
    fail("aftermath one-shot state mismatch")

# Lifecycle: these missions only persist state. They must close the conversation
# instead of creating objective-less accepted missions.
accept_terminals = len(re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE))
decline_terminals = len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE))
if accept_terminals != 0:
    fail(f"state-only lifecycle must not use accept terminals: found {accept_terminals}")
if decline_terminals != 7:
    fail(f"expected exactly 7 state-only decline terminals, found {decline_terminals}")

objective_directives = (
    r'^\s*destination\b',
    r'^\s*stopover\b',
    r'^\s*waypoint\b',
    r'^\s*npc\b',
    r'^\s*cargo\b',
    r'^\s*passenger\b',
    r'^\s*deadline\b',
    r'^\s*timer\b',
)
for pattern in objective_directives:
    if re.search(pattern, text, flags=re.MULTILINE):
        fail(f"state-only lifecycle assumption invalidated by objective directive: {pattern}")

for gate in (
    '\t\thas "language: Avgi (Written)"',
    '\t\thas "avgi: wandering fleet refit 1"',
    '\t\tnot "avgi: lost in twilight"',
):
    if text.count(gate) != 3:
        fail(f"all three missions must preserve gate: {gate.strip()}")

if text.count('\t\thas "Avgi Wandering Fleet Load and Reserve Ledger: offered"') != 1:
    fail("Offer must depend on the B1 Wandering Fleet load/reserve history")

labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE)
missing = sorted(set(gotos) - labels)
if missing:
    fail(f"missing goto labels: {missing}")

if text.count('\t\t\tbranch reserve\n\t\t\t\thas "B2 Avgi Wandering Fleet Transfer Compact: route reserve"') != 1:
    fail("missing reserve Review branch")
if text.count('\t\t\tbranch repair\n\t\t\t\thas "B2 Avgi Wandering Fleet Transfer Compact: route repair"') != 1:
    fail("missing repair Review branch")
if '\t\t\tbranch paired\n' in text:
    fail("paired route should be the intentional Review fallthrough")

# Ownership: B2 may read Avgi/B1 conditions but must never mutate them.
for line in text.splitlines():
    stripped = line.strip()
    if re.search(r'^(set|clear)\s+"(avgi:|world:|Avgi Wandering Fleet )', stripped):
        fail(f"unexpected upstream state mutation: {stripped}")
    if re.search(r'^"(avgi:|world:|Avgi Wandering Fleet )[^"]*"\s*(?:[+\-*/]?=)', stripped):
        fail(f"unexpected upstream state mutation: {stripped}")
    if re.search(r'^"B2 Avgi Wandering Fleet Transfer Compact:[^"]*"\s*(?:[+\-*/]?=)', stripped):
        continue

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
        fail(f"unexpected material/gameplay mutation: {forbidden.strip()}")

# Continuity semantics inherited from B1.
required_fragments = (
    "compatibility and known provenance",
    "donor reserve",
    "replacement plan",
    "borrowed reserve",
    "successful recipient",
    "fleet is nevertheless more fragile",
    "repair success and restored resilience require different closing conditions",
)
for fragment in required_fragments:
    if fragment.lower() not in text.lower():
        fail(f"missing continuity concept: {fragment}")

# Avoid centralizing Wandering Fleet logistics into a new polity/office.
for forbidden_claim in (
    "centralized wandering fleet authority",
    "wandering fleet government",
    "universal avgi repair law",
):
    if forbidden_claim in text.lower():
        fail(f"unsupported centralization claim: {forbidden_claim}")

print("PASS: B2 Avgi Wandering Fleet Transfer Compact structure validated")
print("PASS: missions=3")
print("PASS: recurring_characters=Loadkeeper + Fitter private shorthand")
print("PASS: initial_routes=3 + refusal")
print("PASS: review_routing=paired fallthrough + explicit reserve/repair branches")
print("PASS: terminal_settlements=2")
print("PASS: later_reader=Loadkeeper Remembers")
print("PASS: lifecycle=7 decline terminals; 0 objective-less accepts")
print("PASS: authority=B2 conditions only; Avgi/B1 state read-only")
print("PASS: continuity=recipient repair != restored fleet resilience")
