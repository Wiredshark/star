#!/usr/bin/env python3
"""Focused structural validation for B2 Hai Chosen Family Recognition Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "hai" / "b2 hai chosen family recognition compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Hai Chosen Family Recognition Compact: "

MISSIONS = [
    "B2 Hai Chosen Family Recognition Compact: Offer",
    "B2 Hai Chosen Family Recognition Compact: Review",
    "B2 Hai Chosen Family Recognition Compact: Teren Remembers",
]
ROUTES = (
    "route relationship separate from authority",
    "route purpose specific authority",
    "route paired relationship records",
)
SETTLEMENTS = (
    "settlement portable relationship packet",
    "settlement fresh context renewal",
)


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def label_block(block: str, label: str) -> str:
    marker = f'\n\t\t\tlabel {label}\n'
    start = block.index(marker) + len(marker)
    nxt = block.find('\n\t\t\tlabel ', start)
    return block[start:] if nxt < 0 else block[start:nxt]


def assignments():
    return re.findall(
        r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M
    )


def test_exact_graph_and_delay():
    assert TEXT.count('mission "B2 Hai Chosen Family Recognition Compact:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Hai Chosen Family Recognition Compact: Review Ready"' in TEXT
    offer = mission_block(MISSIONS[0])
    assert offer.count('event "B2 Hai Chosen Family Recognition Compact: Review Ready" 7 11') == 3


def test_scope_and_history_dependency():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Hai"' in block
        assert '\t\tnot attributes "uninhabited"' in block
    offer = mission_block(MISSIONS[0])
    assert 'has "First Contact: Hai: offered"' in offer
    assert 'has "Hai Guest Settlement Register: offered"' in offer


def test_characters_and_local_canon_boundary():
    lowered = TEXT.lower()
    for fragment in (
        "mara hale",
        "teren",
        "call each other siblings",
        "family bond",
        "not universal hai family law",
        "one household's arrangement",
    ):
        assert fragment in lowered, f"missing character/canon boundary: {fragment}"
    assert "socially real without automatically carrying inheritance" in lowered


def test_offer_routes_are_local_and_refusal_suppresses_review():
    offer = mission_block(MISSIONS[0])
    labels = {
        "relationship": ROUTES[0],
        "scope": ROUTES[1],
        "paired": ROUTES[2],
    }
    for label, route in labels.items():
        block = label_block(offer, label)
        assert block.count(f'"{PREFIX}introduced" = 1') == 1
        assert block.count(f'"{PREFIX}{route}" = 1') == 1
        for other in ROUTES:
            if other != route:
                assert f'"{PREFIX}{other}" = 1' not in block
        assert block.count('event "B2 Hai Chosen Family Recognition Compact: Review Ready" 7 11') == 1
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1
    decline = label_block(offer, "decline")
    assert f'"{PREFIX}declined" = 1' in decline
    assert f'"{PREFIX}introduced" = 1' not in decline
    for route in ROUTES:
        assert f'"{PREFIX}{route}" = 1' not in decline
    assert 'Review Ready" 7 11' not in decline


def test_review_and_settlement_lifecycle():
    review = mission_block(MISSIONS[1])
    assert f'has "{PREFIX}introduced"' in review
    assert f'has "{PREFIX}review ready"' in review
    assert f'not "{PREFIX}reviewed"' in review
    for label, settlement in (("packet", SETTLEMENTS[0]), ("renewal", SETTLEMENTS[1])):
        block = label_block(review, label)
        assert block.count(f'"{PREFIX}reviewed" = 1') == 1
        assert block.count(f'"{PREFIX}{settlement}" = 1') == 1
        for other in SETTLEMENTS:
            if other != settlement:
                assert f'"{PREFIX}{other}" = 1' not in block
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1


def test_aftermath_is_one_shot_and_consumes_both_settlements():
    aftermath = mission_block(MISSIONS[2])
    assert f'not "{PREFIX}aftermath seen"' in aftermath
    for settlement in SETTLEMENTS:
        assert f'has "{PREFIX}{settlement}"' in aftermath
    assert aftermath.count(f'"{PREFIX}aftermath seen" = 1') == 1
    assert len(re.findall(r'^\s*decline\s*$', aftermath, re.M)) == 1


def test_state_only_dialogue_lifecycle():
    assert len(re.findall(r'^\s*accept\s*$', TEXT, re.M)) == 0
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    for pattern in (
        r'^\s*destination\b', r'^\s*stopover\b', r'^\s*waypoint\b', r'^\s*npc\b',
        r'^\s*cargo\b', r'^\s*passengers?\b', r'^\s*deadline\b', r'^\s*timer\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"objective directive found: {pattern}"


def test_gotos_are_local_and_resolved():
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name}: missing labels for gotos {missing}"


def test_b2_only_writes_and_no_material_mutation():
    foreign = sorted({name for name in assignments() if not name.startswith(PREFIX)})
    assert not foreign, f"foreign condition writes: {foreign}"
    for pattern in (
        r'^\s*payment\b', r'^\s*combat rating\b', r'^\s*reputation\b',
        r'^\s*give\s+ship\b', r'^\s*give\s+outfit\b', r'^\s*give\s+cargo\b',
        r'^\s*take\s+outfit\b', r'^\s*take\s+cargo\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"material/reputation mutation found: {pattern}"


def test_relationship_authority_boundaries_are_explicit():
    lowered = TEXT.lower()
    for fragment in (
        "family. that does not make every legal power",
        "relationship and authority must be the same thing",
        "does not itself authorize teren",
        "explicit formal powers",
        "different clocks",
        "emergency contact expired",
        "still her sibling today",
    ):
        assert fragment in lowered, f"missing relationship/authority boundary: {fragment}"
    assert "cannot infer one record from the other" in lowered
    assert "fresh consent before it expands" in lowered


def main():
    test_exact_graph_and_delay()
    test_scope_and_history_dependency()
    test_characters_and_local_canon_boundary()
    test_offer_routes_are_local_and_refusal_suppresses_review()
    test_review_and_settlement_lifecycle()
    test_aftermath_is_one_shot_and_consumes_both_settlements()
    test_state_only_dialogue_lifecycle()
    test_gotos_are_local_and_resolved()
    test_b2_only_writes_and_no_material_mutation()
    test_relationship_authority_boundaries_are_explicit()
    print("PASS: B2 Hai Chosen Family Recognition Compact structure validated")
    print("PASS: missions=3 routes=3+refusal settlements=2")
    print("PASS: delayed_review=7-11 days; refusal does not arm review")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: writes=B2 namespace only")
    print("PASS: relationship/formal-authority/expiry boundaries explicit")


if __name__ == "__main__":
    main()
