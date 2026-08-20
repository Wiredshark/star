#!/usr/bin/env python3
"""Focused structural validation for B2 Avgi Dissonance Tax Appeal Compact."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/avgi/b2 avgi dissonance tax appeal compact.txt"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


text = DATA.read_text(encoding="utf-8")
missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
expected = [
    "B2 Avgi Dissonance Tax Appeal Compact: Offer",
    "B2 Avgi Dissonance Tax Appeal Compact: Review",
    "B2 Avgi Dissonance Tax Appeal Compact: Indigo Remembers",
]
if missions != expected:
    fail(f"mission list mismatch: {missions!r}")

for name in ("Indigo", "Sienna"):
    if name not in text:
        fail(f"missing named character {name}")

for route in ("indigo", "sienna", "paired"):
    if text.count(f'"B2 Avgi Dissonance Tax Appeal Compact: route {route}" = 1') != 1:
        fail(f"route {route} must be written exactly once")

if text.count('"B2 Avgi Dissonance Tax Appeal Compact: declined" = 1') != 1:
    fail("decline state must be written exactly once")

for token in (
    '"B2 Avgi Dissonance Tax Appeal Compact: settlement disposition packet" = 1',
    '"B2 Avgi Dissonance Tax Appeal Compact: settlement expiry renewal" = 1',
):
    if text.count(token) != 1:
        fail(f"terminal settlement write mismatch: {token}")

if text.count('"B2 Avgi Dissonance Tax Appeal Compact: reviewed" = 1') != 2:
    fail("reviewed state should be written by exactly two terminal outcomes")
if text.count('"B2 Avgi Dissonance Tax Appeal Compact: aftermath seen" = 1') != 1:
    fail("aftermath one-shot state mismatch")

if text.count('\t\tgovernment "Avgi (Dissonance)"') != 3:
    fail("all three missions must be Dissonance-scoped")
if text.count('\t\thas "language: Avgi (Written)"') != 3:
    fail("all three missions must require Avgi written language")
if text.count('\t\tnot "avgi: lost in twilight"') != 3:
    fail("all three missions must preserve lost-in-twilight gating")

labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE)
missing = sorted(set(gotos) - labels)
if missing:
    fail(f"missing goto labels: {missing}")

if text.count('\t\t\tbranch indigo\n\t\t\t\thas "B2 Avgi Dissonance Tax Appeal Compact: route indigo"') != 1:
    fail("missing Indigo Review branch")
if text.count('\t\t\tbranch sienna\n\t\t\t\thas "B2 Avgi Dissonance Tax Appeal Compact: route sienna"') != 1:
    fail("missing Sienna Review branch")
if '\t\t\tbranch paired' in text:
    fail("paired route should be the intentional Review fallthrough")

for phrase in (
    "memory without turning grievance into proof",
    "complaint can survive copying without becoming a verdict",
    "mere existence of the old objection",
):
    if phrase not in text:
        fail(f"missing evidence-vs-verdict continuity phrase: {phrase}")

for line in text.splitlines():
    stripped = line.strip()
    if re.search(r'^(set|clear)\s+"(avgi:|world:)', stripped):
        fail(f"unexpected upstream state mutation: {stripped}")
    if re.search(r'^"(avgi:|world:)[^"]*"\s*(?:[+\-*/]?=)', stripped):
        fail(f"unexpected upstream state mutation: {stripped}")

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

print("PASS: B2 Avgi Dissonance Tax Appeal Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: review_routing=paired fallthrough + explicit Indigo/Sienna branches")
print("PASS: terminal_settlements=2")
print("PASS: later_reader=Indigo Remembers")
print("PASS: authority=B2 conditions only; Avgi campaign/world state read-only")
print("PASS: continuity=challenge history remains distinct from current verified assessment and disposition")
