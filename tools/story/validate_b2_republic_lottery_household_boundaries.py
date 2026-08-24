#!/usr/bin/env python3
"""Focused structural validation for B2 Republic Lottery Household Boundaries."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 republic lottery household boundaries.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Republic Lottery Household Boundaries: "
MISSIONS = [
    "B2 Republic Lottery Household Boundaries: Offer",
    "B2 Republic Lottery Household Boundaries: Review",
    "B2 Republic Lottery Household Boundaries: Elias Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def assignments():
    return re.findall(r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M)


def test_graph_and_delay():
    assert TEXT.count('mission "B2 Republic Lottery Household Boundaries:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Republic Lottery Household Boundaries: Review Ready"' in TEXT
    assert TEXT.count('event "B2 Republic Lottery Household Boundaries: Review Ready" 7 11') == 3


def test_scope_and_characters():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Republic"' in block
        assert '\t\tattributes "near earth"' in block
        assert '\t\tnot attributes "station"' in block
    lowered = TEXT.lower()
    for fragment in (
        "elias penn",
        "mara",
        "lottery",
        "rent",
        "household",
        "personal spending",
        "not a diagnosis",
        "not a claim that",
        "civic strain causes gambling behavior",
    ):
        assert fragment in lowered, fragment


def test_routes_and_settlements():
    for route in (
        "route household floor",
        "route voluntary limit",
        "route paired records",
    ):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT
    for settlement in (
        "settlement portable household boundary",
        "settlement expiry and fresh cause",
    ):
        assert f'"{PREFIX}{settlement}" = 1' in TEXT
    assert f'"{PREFIX}aftermath seen" = 1' in TEXT


def test_review_and_aftermath_lifecycle():
    review = mission_block(MISSIONS[1])
    assert f'has "{PREFIX}introduced"' in review
    assert f'has "{PREFIX}review ready"' in review
    assert f'not "{PREFIX}reviewed"' in review
    assert review.count(f'"{PREFIX}reviewed" = 1') == 2
    assert '"world: republic civic strain" >= 3' in review
    aftermath = mission_block(MISSIONS[2])
    assert f'not "{PREFIX}aftermath seen"' in aftermath
    assert f'has "{PREFIX}settlement portable household boundary"' in aftermath
    assert f'has "{PREFIX}settlement expiry and fresh cause"' in aftermath
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
    assert '"world: republic civic strain" >= 3' in TEXT
    assert not re.search(r'^\s*"world: republic civic strain"\s*(?:=|\+=|-=)', TEXT, re.M)
    for pattern in (
        r'^\s*payment\b', r'^\s*reputation\b', r'^\s*combat rating\b',
        r'^\s*give\s+(?:ship|outfit|cargo)\b', r'^\s*take\s+(?:outfit|cargo)\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), pattern


def test_household_agency_boundaries_explicit():
    lowered = TEXT.lower()
    for fragment in (
        "household floor",
        "voluntary limit",
        "cooling-off",
        "not turn mara into his financial guardian",
        "personal spending",
        "current household obligations",
        "explicit loans",
        "closure evidence",
        "repaid loan does not keep acting like a debt",
        "expired voluntary limit does not keep acting like a judgment of competence",
        "new missed obligation",
        "legal personal spending",
        "universal republic policy",
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
    test_household_agency_boundaries_explicit()
    print("PASS: B2 Republic Lottery Household Boundaries validated")
    print("PASS: missions=3; routes=3+refusal; settlements=2")
    print("PASS: delayed_review=7-11 days; aftermath=one-shot")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: A1 republic civic strain is read-only")
    print("PASS: household obligation / personal agency / voluntary-limit boundaries explicit")


if __name__ == "__main__":
    main()
