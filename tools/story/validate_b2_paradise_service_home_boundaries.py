#!/usr/bin/env python3
"""Focused structural validation for B2 Paradise Service Home Boundaries."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 paradise service home boundaries.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Paradise Service Home Boundaries: "
MISSIONS = [
    "B2 Paradise Service Home Boundaries: Offer",
    "B2 Paradise Service Home Boundaries: Review",
    "B2 Paradise Service Home Boundaries: Rina Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def label_block(block: str, label: str) -> str:
    start = block.index(f"\n\t\t\tlabel {label}\n")
    nxt = block.find("\n\t\t\tlabel ", start + 1)
    return block[start:] if nxt < 0 else block[start:nxt]


def assignments():
    return re.findall(r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M)


def test_graph_scope_and_history_gate():
    assert TEXT.count('mission "B2 Paradise Service Home Boundaries:') == 3
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Republic"' in block
        assert '\t\tattributes "paradise"' in block
        assert '\t\tnot attributes "station"' in block
    offer = mission_block(MISSIONS[0])
    assert 'has "Paradise Service District Museum: offered"' in offer
    assert offer.count('event "B2 Paradise Service Home Boundaries: Review Ready" 7 11') == 3


def test_offer_routes_and_refusal_boundary():
    offer = mission_block(MISSIONS[0])
    expected_routes = {
        "tenancy": "route tenancy first",
        "transition": "route explicit transition",
        "paired": "route paired records",
    }
    for label, route in expected_routes.items():
        block = label_block(offer, label)
        assert f'"{PREFIX}introduced" = 1' in block
        assert f'"{PREFIX}{route}" = 1' in block
        assert 'event "B2 Paradise Service Home Boundaries: Review Ready" 7 11' in block
        assert re.search(r'^\s*decline\s*$', block, re.M)
    refusal = label_block(offer, "decline")
    assert f'"{PREFIX}declined" = 1' in refusal
    assert f'"{PREFIX}introduced" = 1' not in refusal
    assert 'event "B2 Paradise Service Home Boundaries: Review Ready"' not in refusal
    assert re.search(r'^\s*decline\s*$', refusal, re.M)


def test_characters_routes_and_settlements():
    lowered = TEXT.lower()
    for fragment in (
        "rina vale",
        "tomas keene",
        "service residence",
        "municipal tenancy",
        "employer subsidy",
        "residential access",
    ):
        assert fragment in lowered, f"missing character/home continuity: {fragment}"
    for route in ("route tenancy first", "route explicit transition", "route paired records"):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT
    for settlement in ("settlement portable occupancy packet", "settlement employment housing firewall"):
        assert f'"{PREFIX}{settlement}" = 1' in TEXT


def test_review_and_aftermath_lifecycle():
    review = mission_block(MISSIONS[1])
    assert f'has "{PREFIX}introduced"' in review
    assert f'has "{PREFIX}review ready"' in review
    assert f'not "{PREFIX}reviewed"' in review
    assert f'has "{PREFIX}declined"' not in review
    assert review.count(f'"{PREFIX}reviewed" = 1') == 2
    for settlement in ("packet", "firewall"):
        block = label_block(review, settlement)
        assert f'"{PREFIX}reviewed" = 1' in block
        assert re.search(r'^\s*decline\s*$', block, re.M)
    aftermath = mission_block(MISSIONS[2])
    assert f'not "{PREFIX}aftermath seen"' in aftermath
    assert f'has "{PREFIX}settlement portable occupancy packet"' in aftermath
    assert f'has "{PREFIX}settlement employment housing firewall"' in aftermath
    assert aftermath.count(f'"{PREFIX}aftermath seen" = 1') == 1
    assert re.search(r'^\s*decline\s*$', aftermath, re.M)


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


def test_home_employment_boundaries_are_explicit():
    lowered = TEXT.lower()
    fragments = (
        "i am resigning from a job",
        "i am not resigning from my kitchen",
        "the home from the job",
        "one status can change without pretending the others changed too",
        "the mistake was letting one change propagate into systems that answer different questions",
        "history visible without letting history issue today's orders",
        "employment systems may report employment",
        "housing systems may report occupancy",
        "history is allowed to be true without staying in charge",
        "republic tenancy law",
        "universal paradise rule",
    )
    for fragment in fragments:
        assert fragment in lowered, f"missing employment/home boundary: {fragment}"


def main():
    test_graph_scope_and_history_gate()
    test_offer_routes_and_refusal_boundary()
    test_characters_routes_and_settlements()
    test_review_and_aftermath_lifecycle()
    test_state_only_lifecycle_and_gotos()
    test_state_ownership_and_no_material_mutation()
    test_home_employment_boundaries_are_explicit()
    print("PASS: B2 Paradise Service Home Boundaries structure validated")
    print("PASS: missions=3; routes=3+refusal; settlements=2; aftermath=one-shot")
    print("PASS: delayed_review=3 substantive routes only; refusal cannot arm Review")
    print("PASS: terminals=7 decline / 0 accept; writes=B2 namespace only")
    print("PASS: employment/tenancy/subsidy/access boundaries explicit")


if __name__ == "__main__":
    main()
