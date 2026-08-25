#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 merchant partnership dissolution compact.txt"
text = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Merchant Partnership Dissolution Compact:"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def block(start: str, end: str | None = None) -> str:
    start_at = text.index(start)
    return text[start_at:] if end is None else text[start_at:text.index(end, start_at + len(start))]


missions = re.findall(r'^mission "([^"]+)"', text, flags=re.MULTILINE)
require(missions == [PREFIX + " Offer", PREFIX + " Review", PREFIX + " Damin Remembers"],
        f"unexpected mission graph: {missions}")
require(text.count('event "' + PREFIX + ' Review Ready"') == 4,
        "expected one Review event declaration plus three substantive schedules")
require('event "' + PREFIX + ' Review Ready"\n\t"' + PREFIX + ' review ready" = 1' in text,
        "missing Review Ready payload")
require('has "B2 Merchant Recovery Margin Compact: aftermath seen"' in text,
        "missing integrated Merchant Recovery Margin aftermath dependency")
require(text.count('government "Merchant"') == 3, "all three missions must be Merchant-scoped")

OFFER = block('mission "' + PREFIX + ' Offer"', 'mission "' + PREFIX + ' Review"')
REVIEW = block('mission "' + PREFIX + ' Review"', 'mission "' + PREFIX + ' Damin Remembers"')
AFTERMATH = block('mission "' + PREFIX + ' Damin Remembers"')

routes = {
    "authority": PREFIX + " route fresh authority",
    "reference": PREFIX + " route bounded reference",
    "paired": PREFIX + " route paired records",
}
next_route = {"authority": "reference", "reference": "paired", "paired": "decline"}
for label, condition in routes.items():
    section = block('\t\t\tlabel ' + label, '\t\t\tlabel ' + next_route[label])
    require(section.count('"' + PREFIX + ' introduced" = 1') == 1,
            f"{label} route must introduce exactly once")
    require(section.count('"' + condition + '" = 1') == 1,
            f"{label} route missing own state")
    for other in routes.values():
        if other != condition:
            require('"' + other + '" = 1' not in section, f"{label} writes another route state")
    require(section.count('event "' + PREFIX + ' Review Ready" 7 11') == 1,
            f"{label} must schedule one 7-11 day Review")
    require(section.count('\n\t\t\tdecline') == 1, f"{label} must terminate once with decline")

decline = block('\t\t\tlabel decline', 'mission "' + PREFIX + ' Review"')
require('"' + PREFIX + ' declined" = 1' in decline, "refusal missing declined state")
require('"' + PREFIX + ' introduced" = 1' not in decline, "refusal must not introduce arc")
require('Review Ready" 7 11' not in decline, "refusal must not arm Review")
for condition in routes.values():
    require('"' + condition + '" = 1' not in decline, "refusal must not write substantive route")

for token in ('has "' + PREFIX + ' introduced"', 'has "' + PREFIX + ' review ready"',
              'not "' + PREFIX + ' reviewed"'):
    require(token in REVIEW, f"Review missing lifecycle gate: {token}")

settlements = {
    "packet": PREFIX + " settlement portable partnership status",
    "renewal": PREFIX + " settlement fresh acknowledgement",
}
for label, condition in settlements.items():
    end = '\t\t\tlabel renewal' if label == "packet" else 'mission "' + PREFIX + ' Damin Remembers"'
    section = block('\t\t\tlabel ' + label, end)
    require(section.count('"' + PREFIX + ' reviewed" = 1') == 1,
            f"{label} settlement must close Review exactly once")
    require(section.count('"' + condition + '" = 1') == 1,
            f"{label} settlement missing own state")
    for other in settlements.values():
        if other != condition:
            require('"' + other + '" = 1' not in section, f"{label} writes other settlement")
    require(section.count('\n\t\t\tdecline') == 1, f"{label} settlement must terminate once")

require('not "' + PREFIX + ' aftermath seen"' in AFTERMATH, "aftermath must be one-shot")
for condition in settlements.values():
    require('has "' + condition + '"' in AFTERMATH, "aftermath must consume both settlements")
require(AFTERMATH.count('"' + PREFIX + ' aftermath seen" = 1') == 1,
        "aftermath must write seen exactly once")
require(AFTERMATH.count('\n\t\t\tdecline') == 1, "aftermath must terminate once")

require(text.count('\n\t\t\tdecline') == 7, "expected exactly seven state-only decline terminals")
require('\n\t\t\taccept' not in text, "state-only compact must not use accept terminals")
for directive in ('\n\tdestination ', '\n\tstopover ', '\n\twaypoint ', '\n\tnpc ', '\n\tcargo ', '\n\tpassenger ', '\n\tdeadline ', '\n\ttimer '):
    require(directive not in text, f"unexpected gameplay objective directive: {directive.strip()}")

assignments = re.findall(r'^\s*"([^"]+)"\s*[+\-*/]?=', text, flags=re.MULTILINE)
require(assignments, "expected persistent writes")
require(all(name.startswith(PREFIX) for name in assignments),
        f"non-B2 state write found: {[name for name in assignments if not name.startswith(PREFIX)]}")
for banned in ('credits', 'reputation', 'outfit ', 'cargo ', 'fleet ', 'combat rating'):
    require(banned not in text.lower(), f"unexpected material/reputation mutation surface: {banned}")

for phrase in (
    "historical partnership can remain fully true without granting either person standing authority",
    "former partner may give a dated reference",
    "Neither record silently overwrites the other",
    "partnership records expire as authority after the separation date",
):
    require(phrase in text, f"missing continuity boundary: {phrase}")
require("general Merchant rule" in text, "missing local-not-universal authority boundary")
require("sponsor, guarantor, co-owner, or responsible party" in text,
        "missing explicit present-authority separation")

print("B2 Merchant Partnership Dissolution Compact validation: PASS")
