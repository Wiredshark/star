#!/usr/bin/env python3
"""Focused structural validation for B2 Hai Name Record Continuity Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "hai" / "b2 hai name record continuity compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Hai Name Record Continuity Compact: "

MISSIONS = [
    "B2 Hai Name Record Continuity Compact: Offer",
    "B2 Hai Name Record Continuity Compact: Review",
    "B2 Hai Name Record Continuity Compact: Ari Remembers",
]
ROUTES = (
    "route current display",
    "route purpose bounded",
    "route paired records",
)
SETTLEMENTS = (
    "settlement portable continuity packet",
    "settlement fresh purpose",
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
    return re.findall(r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M)


def test_graph_and_scope():
    assert TEXT.count('mission "B2 Hai Name Record Continuity Compact:') == 3
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Hai"' in block
        assert '\t\tnot attributes "uninhabited"' in block
    offer = mission_block(MISSIONS[0])
    assert 'has "First Contact: Hai: offered"' in offer
    assert offer.count('event "B2 Hai Name Record Continuity Compact: Review Ready" 7 11') == 3


def test_offer_routes_and_refusal():
    offer = mission_block(MISSIONS[0])
    labels = {"current": ROUTES[0], "bounded": ROUTES[1], "paired": ROUTES[2]}
    for label, route in labels.items():
        block = label_block(offer, label)
        assert block.count(f'"{PREFIX}introduced" = 1') == 1
        assert block.count(f'"{PREFIX}{route}" = 1') == 1
        for other in ROUTES:
            if other != route:
                assert f'"{PREFIX}{other}" = 1' not in block
        assert block.count('event "B2 Hai Name Record Continuity Compact: Review Ready" 7 11') == 1
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1
    decline = label_block(offer, "decline")
    assert f'"{PREFIX}declined" = 1' in decline
    assert f'"{PREFIX}introduced" = 1' not in decline
    assert 'Review Ready" 7 11' not in decline
    for route in ROUTES:
        assert f'"{PREFIX}{route}" = 1' not in decline


def test_review_route_gating():
    review = mission_block(MISSIONS[1])
    conversation = review.split("\ton offer\n\t\tconversation\n", 1)[1]
    pre_labels = conversation.split("\n\t\t\tlabel bounded\n", 1)[0]

    assert pre_labels.count("\t\t\tbranch bounded\n") == 1
    assert pre_labels.count(f'\t\t\t\thas "{PREFIX}{ROUTES[1]}"\n') == 1
    assert pre_labels.count("\t\t\tbranch paired\n") == 1
    assert pre_labels.count(f'\t\t\t\thas "{PREFIX}{ROUTES[2]}"\n') == 1
    assert f'has "{PREFIX}{ROUTES[0]}"' not in pre_labels

    bounded = label_block(review, "bounded")
    paired = label_block(review, "paired")
    settle = label_block(review, "settle")
    assert bounded.count("goto settle") == 1
    assert "goto settle" not in paired
    assert "choice" in settle
    assert "goto packet" in settle
    assert "goto renewal" in settle


def test_review_and_aftermath():
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

    aftermath = mission_block(MISSIONS[2])
    offer_gate = aftermath.split("\tto offer\n", 1)[1].split("\ton offer\n", 1)[0]
    assert offer_gate.count(f'not "{PREFIX}aftermath seen"') == 1
    settlement_gates = re.findall(rf'^\s*has "{re.escape(PREFIX)}(settlement [^"]+)"\s*$', offer_gate, re.M)
    assert settlement_gates == list(SETTLEMENTS), f"unexpected aftermath settlement gate: {settlement_gates}"
    assert offer_gate.count("\n\t\tor\n") == 1

    conversation = aftermath.split("\ton offer\n\t\tconversation\n", 1)[1]
    pre_renewal = conversation.split("\n\t\t\tlabel renewal\n", 1)[0]
    assert pre_renewal.count("\t\t\tbranch renewal\n") == 1
    assert pre_renewal.count(f'\t\t\t\thas "{PREFIX}{SETTLEMENTS[1]}"\n') == 1
    assert f'has "{PREFIX}{SETTLEMENTS[0]}"' not in pre_renewal

    assert aftermath.count(f'"{PREFIX}aftermath seen" = 1') == 1
    assert len(re.findall(r'^\s*decline\s*$', aftermath, re.M)) == 1


def test_lifecycle_ownership_and_gotos():
    assert len(re.findall(r'^\s*accept\s*$', TEXT, re.M)) == 0
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    for pattern in (
        r'^\s*destination\b', r'^\s*stopover\b', r'^\s*waypoint\b', r'^\s*npc\b',
        r'^\s*cargo\b', r'^\s*passengers?\b', r'^\s*deadline\b', r'^\s*timer\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"objective directive found: {pattern}"
    foreign = sorted({name for name in assignments() if not name.startswith(PREFIX)})
    assert not foreign, f"foreign condition writes: {foreign}"
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        assert not (set(gotos) - labels), f"{name}: unresolved goto"


def test_identity_continuity_boundaries():
    lowered = TEXT.lower()
    for fragment in (
        "history is permission to use it now",
        "continuity is not publication",
        "current self-identified name",
        "historical aliases",
        "access purpose",
        "current matching need",
        "source lineage",
        "does not travel indefinitely",
        "not universal hai naming law",
    ):
        assert fragment in lowered, f"missing identity/continuity boundary: {fragment}"
    assert "every careless copy creates another source that looks independent" in lowered


def test_no_material_mutation():
    for pattern in (
        r'^\s*payment\b', r'^\s*combat rating\b', r'^\s*reputation\b',
        r'^\s*give\s+ship\b', r'^\s*give\s+outfit\b', r'^\s*give\s+cargo\b',
        r'^\s*take\s+outfit\b', r'^\s*take\s+cargo\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"material/reputation mutation found: {pattern}"


def main():
    test_graph_and_scope()
    test_offer_routes_and_refusal()
    test_review_route_gating()
    test_review_and_aftermath()
    test_lifecycle_ownership_and_gotos()
    test_identity_continuity_boundaries()
    test_no_material_mutation()
    print("PASS: B2 Hai Name Record Continuity Compact structure validated")
    print("PASS: missions=3 routes=3+refusal settlements=2")
    print("PASS: delayed_review=7-11 days; refusal suppresses review")
    print("PASS: review route gates and aftermath settlement gates are exact")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: writes=B2 namespace only")
    print("PASS: current-name/history/access-purpose boundaries explicit")


if __name__ == "__main__":
    main()
