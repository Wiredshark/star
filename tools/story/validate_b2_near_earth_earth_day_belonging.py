#!/usr/bin/env python3
"""Focused structural validation for B2 Near Earth Earth Day Belonging."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 near earth earth day belonging.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Near Earth Earth Day Belonging: "
MISSIONS = [
    "B2 Near Earth Earth Day Belonging: Offer",
    "B2 Near Earth Earth Day Belonging: Review",
    "B2 Near Earth Earth Day Belonging: Leo Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def assignments():
    return re.findall(r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M)


def test_graph_scope_and_delay():
    assert TEXT.count('mission "B2 Near Earth Earth Day Belonging:') == 3
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Republic"' in block
        assert '\t\tattributes "near earth"' in block
        assert '\t\tnot attributes "station"' in block
    offer = mission_block(MISSIONS[0])
    assert 'has "Near Earth Earth Day Archive: offered"' in offer
    assert 'event "B2 Near Earth Earth Day Belonging: Review Ready" 7 11' in offer


def test_characters_routes_and_settlements():
    lowered = TEXT.lower()
    for fragment in ("mara quill", "adult son leo", "new boston", "family", "pilgrimage"):
        assert fragment in lowered, f"missing character/family continuity: {fragment}"
    for route in ("route heritage invitation", "route self authored belonging", "route layered belonging"):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT
    for settlement in ("settlement voluntary heritage statement", "settlement plural belonging"):
        assert f'"{PREFIX}{settlement}" = 1' in TEXT


def test_review_and_aftermath_lifecycle():
    review = mission_block(MISSIONS[1])
    assert f'has "{PREFIX}introduced"' in review
    assert f'has "{PREFIX}review ready"' in review
    assert f'not "{PREFIX}reviewed"' in review
    assert review.count(f'"{PREFIX}reviewed" = 1') == 2
    aftermath = mission_block(MISSIONS[2])
    assert f'not "{PREFIX}aftermath seen"' in aftermath
    assert f'has "{PREFIX}settlement voluntary heritage statement"' in aftermath
    assert f'has "{PREFIX}settlement plural belonging"' in aftermath
    assert aftermath.count(f'"{PREFIX}aftermath seen" = 1') == 1


def test_state_only_lifecycle_and_gotos():
    assert len(re.findall(r'^\s*accept\s*$', TEXT, re.M)) == 0
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    for pattern in (
        r'^\s*destination\b', r'^\s*stopover\b', r'^\s*waypoint\b', r'^\s*npc\b',
        r'^\s*cargo\b', r'^\s*passengers?\b', r'^\s*deadline\b', r'^\s*timer\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"objective directive found: {pattern}"
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name}: unresolved goto(s) {missing}"


def test_state_ownership_and_no_material_mutation():
    foreign = sorted({name for name in assignments() if not name.startswith(PREFIX)})
    assert not foreign, f"foreign condition writes: {foreign}"
    for pattern in (
        r'^\s*payment\b', r'^\s*reputation\b', r'^\s*combat rating\b',
        r'^\s*give\s+(?:ship|outfit|cargo)\b', r'^\s*take\s+(?:outfit|cargo)\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"material mutation found: {pattern}"


def test_belonging_boundaries_are_explicit():
    lowered = TEXT.lower()
    for fragment in (
        "heritage invitation, not an inherited obligation",
        "it is home",
        "earth to become a loyalty test",
        "refusing it does not threaten his place in the family",
        "can all be true without proving one another",
        "a living person's identity statement must come from that person",
        "attendance into proof of loyalty",
        "absence into proof of rejection",
        "not republic policy",
        "universal definition of human identity",
    ):
        assert fragment in lowered, f"missing identity/belonging boundary: {fragment}"


def main():
    test_graph_scope_and_delay()
    test_characters_routes_and_settlements()
    test_review_and_aftermath_lifecycle()
    test_state_only_lifecycle_and_gotos()
    test_state_ownership_and_no_material_mutation()
    test_belonging_boundaries_are_explicit()
    print("PASS: B2 Near Earth Earth Day Belonging structure validated")
    print("PASS: missions=3; routes=3+refusal; settlements=2; aftermath=one-shot")
    print("PASS: delayed_review=7-11 days; terminals=7 decline / 0 accept")
    print("PASS: writes=B2 namespace only; no material/reputation mutation")
    print("PASS: ancestry/tradition/home/public-observance boundaries explicit")


if __name__ == "__main__":
    main()
