#!/usr/bin/env python3
"""Focused structural validation for B2 Arach Courtship Boundaries."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "coalition" / "b2 arach courtship boundaries.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Arach Courtship Boundaries: "
MISSIONS = [
    "B2 Arach Courtship Boundaries: Offer",
    "B2 Arach Courtship Boundaries: Review",
    "B2 Arach Courtship Boundaries: Selka Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def assignments():
    return re.findall(r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M)


def test_graph_and_delay():
    assert TEXT.count('mission "B2 Arach Courtship Boundaries:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Arach Courtship Boundaries: Review Ready"' in TEXT
    assert TEXT.count('event "B2 Arach Courtship Boundaries: Review Ready" 7 11') == 3


def test_scope_and_characters():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Coalition"' in block
        assert '\t\tattributes "arach"' in block
    offer = mission_block(MISSIONS[0])
    assert 'has "known to the heliarchs"' in offer
    lowered = TEXT.lower()
    for fragment in (
        "selka meren",
        "neri vass",
        "theater",
        "patron",
        "local relationship practice",
        "arach law",
        "coalition law",
        "universal description of arach courtship",
    ):
        assert fragment in lowered, fragment


def test_routes_and_settlements():
    for route in (
        "route mutual acknowledgement",
        "route private by default",
        "route scoped boundaries",
    ):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT
    for settlement in (
        "settlement shared public boundary",
        "settlement privacy firewall",
    ):
        assert f'"{PREFIX}{settlement}" = 1' in TEXT
    assert f'"{PREFIX}aftermath seen" = 1' in TEXT


def test_review_and_aftermath_lifecycle():
    review = mission_block(MISSIONS[1])
    assert f'has "{PREFIX}introduced"' in review
    assert f'has "{PREFIX}review ready"' in review
    assert f'not "{PREFIX}reviewed"' in review
    assert review.count(f'"{PREFIX}reviewed" = 1') == 2
    aftermath = mission_block(MISSIONS[2])
    assert f'not "{PREFIX}aftermath seen"' in aftermath
    assert f'has "{PREFIX}settlement shared public boundary"' in aftermath
    assert f'has "{PREFIX}settlement privacy firewall"' in aftermath
    assert aftermath.count(f'"{PREFIX}aftermath seen" = 1') == 1


def test_state_only_lifecycle():
    assert len(re.findall(r'^\s*accept\s*$', TEXT, re.M)) == 0
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    for pattern in (
        r'^\s*destination\b', r'^\s*stopover\b', r'^\s*waypoint\b',
        r'^\s*npc\b', r'^\s*cargo\b', r'^\s*passengers?\b',
        r'^\s*deadline\b', r'^\s*timer\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), pattern


def test_gotos_local():
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        assert not (set(gotos) - labels), (name, sorted(set(gotos) - labels))


def test_state_ownership_and_no_rewards():
    foreign = sorted({name for name in assignments() if not name.startswith(PREFIX)})
    assert not foreign, foreign
    for pattern in (
        r'^\s*payment\b', r'^\s*reputation\b', r'^\s*combat rating\b',
        r'^\s*give\s+(?:ship|outfit|cargo)\b', r'^\s*take\s+(?:outfit|cargo)\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), pattern


def test_relationship_boundaries_explicit():
    lowered = TEXT.lower()
    for fragment in (
        "fresh direct consent",
        "public relationship status",
        "gift",
        "guest list",
        "patronage",
        "privacy",
        "revision history",
        "withdrawal status",
        "older copies remain history, not permanent authority",
        "declining to provide it cannot be treated as evidence of conflict",
        "their solution is local relationship practice, not",
        "a universal description of arach courtship",
    ):
        assert fragment in lowered, fragment


def main():
    test_graph_and_delay()
    test_scope_and_characters()
    test_routes_and_settlements()
    test_review_and_aftermath_lifecycle()
    test_state_only_lifecycle()
    test_gotos_local()
    test_state_ownership_and_no_rewards()
    test_relationship_boundaries_explicit()
    print("PASS: B2 Arach Courtship Boundaries validated")
    print("PASS: missions=3; routes=3+refusal; settlements=2")
    print("PASS: delayed_review=7-11 days; aftermath=one-shot")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: writes=B2 namespace only; no material/reputation mutations")
    print("PASS: relationship/publicity/patronage/consent boundaries explicit")


if __name__ == "__main__":
    main()
