#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/b2 republic estranged sibling contact compact.txt"
TEXT = PATH.read_text(encoding="utf-8")
PREFIX = "B2 Republic Estranged Sibling Contact Compact:"


def require(fragment: str, message: str) -> None:
    if fragment not in TEXT:
        raise SystemExit(f"FAIL: {message}")


def block(start: str, end: str | None = None) -> str:
    i = TEXT.index(start)
    j = TEXT.index(end, i + len(start)) if end else len(TEXT)
    return TEXT[i:j]


require('mission "B2 Republic Estranged Sibling Contact Compact: Offer"', "Offer mission missing")
require('mission "B2 Republic Estranged Sibling Contact Compact: Review"', "Review mission missing")
require('mission "B2 Republic Estranged Sibling Contact Compact: Mara Remembers"', "aftermath mission missing")
require('event "B2 Republic Estranged Sibling Contact Compact: Review Ready"', "Review event missing")
require('has "world: republic civic strain" >= 2', "Offer must consume elevated Republic civic strain")
require('has "world: republic civic strain" <= 1', "Review must wait for civic-strain recovery")

if TEXT.count('\t\t\t\tevent "B2 Republic Estranged Sibling Contact Compact: Review Ready" 7 11') != 3:
    raise SystemExit("FAIL: exactly three substantive routes must schedule 7-11 day Review")
if TEXT.count("\t\t\t\tdecline") != 7:
    raise SystemExit("FAIL: exactly seven state-only terminal declines required")
if "\t\t\t\taccept" in TEXT:
    raise SystemExit("FAIL: state-only compact must not accept objective-less missions")

OFFER = block('mission "B2 Republic Estranged Sibling Contact Compact: Offer"', 'mission "B2 Republic Estranged Sibling Contact Compact: Review"')
REVIEW = block('mission "B2 Republic Estranged Sibling Contact Compact: Review"', 'mission "B2 Republic Estranged Sibling Contact Compact: Mara Remembers"')
AFTERMATH = block('mission "B2 Republic Estranged Sibling Contact Compact: Mara Remembers"')

routes = {
    "consent": "route current consent",
    "relay": "route neutral relay",
    "paired": "route paired records",
}
for label, state in routes.items():
    seg = block(f"\t\t\tlabel {label}", f"\t\t\tlabel {list(routes)[list(routes).index(label)+1]}" if label != "paired" else "\t\t\tlabel decline")
    require(f'"{PREFIX} introduced" = 1', f"{label} must introduce arc")
    if f'"{PREFIX} {state}" = 1' not in seg:
        raise SystemExit(f"FAIL: {label} route must write only its intended route state")
    if seg.count(f'event "{PREFIX} Review Ready" 7 11') != 1:
        raise SystemExit(f"FAIL: {label} route must schedule Review exactly once")
    if seg.count("\n\t\t\t\tdecline") != 1:
        raise SystemExit(f"FAIL: {label} route must terminate exactly once")

decline = OFFER[OFFER.index("\t\t\tlabel decline"):]
if f'"{PREFIX} introduced"' in decline or f'event "{PREFIX} Review Ready" 7 11' in decline:
    raise SystemExit("FAIL: refusal must not introduce or schedule Review")
if f'"{PREFIX} declined" = 1' not in decline:
    raise SystemExit("FAIL: refusal state missing")

for required in (
    f'has "{PREFIX} introduced"',
    f'has "{PREFIX} review ready"',
    'has "world: republic civic strain" <= 1',
    f'not "{PREFIX} reviewed"',
):
    if required not in REVIEW:
        raise SystemExit(f"FAIL: Review lifecycle gate missing: {required}")

for settlement in ("settlement portable contact packet", "settlement fresh contact renewal"):
    if REVIEW.count(f'"{PREFIX} {settlement}" = 1') != 1:
        raise SystemExit(f"FAIL: {settlement} must be written exactly once")
if REVIEW.count(f'"{PREFIX} reviewed" = 1') != 2:
    raise SystemExit("FAIL: both Review settlements must close Review exactly once")

for settlement in ("settlement portable contact packet", "settlement fresh contact renewal"):
    if f'has "{PREFIX} {settlement}"' not in AFTERMATH:
        raise SystemExit(f"FAIL: aftermath must accept {settlement}")
if AFTERMATH.count(f'"{PREFIX} aftermath seen" = 1') != 1:
    raise SystemExit("FAIL: aftermath must be one-shot")

for line in TEXT.splitlines():
    if line.startswith("\t\t\t\t\"") and "world:" in line:
        raise SystemExit("FAIL: B2 must not write world state")
    if line.startswith("\t\t\t\t\"") and "B2 Republic Estranged Sibling Contact Compact:" not in line:
        raise SystemExit("FAIL: persistent writes must remain in B2 namespace")

for directive in ("\tdestination ", "\tstopover ", "\twaypoint ", "\tnpc ", "\tcargo ", "\tpassenger ", "\tdeadline ", "\ttimer "):
    if directive in TEXT:
        raise SystemExit(f"FAIL: state-only compact unexpectedly contains objective directive {directive.strip()}")

for phrase in (
    "family relationship/history separate from current contact permission and reconciliation status",
    "relationship history, current disclosure permission, relay state, direct-contact consent, reconciliation status",
    "being my brother is permanent history. Access to him is not",
    "not Republic law",
):
    if phrase not in TEXT:
        raise SystemExit(f"FAIL: continuity/canon boundary missing: {phrase}")

print("PASS: B2 Republic Estranged Sibling Contact Compact")
