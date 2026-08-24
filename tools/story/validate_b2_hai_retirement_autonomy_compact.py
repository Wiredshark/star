#!/usr/bin/env python3
"""Focused structural validation for B2 Hai Retirement Autonomy Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "hai" / "b2 hai retirement autonomy compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Hai Retirement Autonomy Compact: "

MISSIONS = [
    "B2 Hai Retirement Autonomy Compact: Offer",
    "B2 Hai Retirement Autonomy Compact: Review",
    "B2 Hai Retirement Autonomy Compact: Elena Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def assignments():
    return re.findall(
        r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M
    )


def test_exact_graph_and_delay():
    assert TEXT.count('mission "B2 Hai Retirement Autonomy Compact:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Hai Retirement Autonomy Compact: Review Ready"' in TEXT
    assert 'event "B2 Hai Retirement Autonomy Compact: Review Ready" 7 11' in TEXT


def test_scope_and_b1_dependencies():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Hai"' in block
        assert '\t\tnot attributes "uninhabited"' in block
    offer = mission_block(MISSIONS[0])
    assert 'has "First Contact: Hai: offered"' in offer
    assert 'has "Hai Guest Settlement Register: offered"' in offer
    assert 'has "Hai Stewardship Archive: offered"' in offer


def test_characters_and_local_authority_boundary():
    lowered = TEXT.lower()
    for fragment in (
        "elena voss",
        "retired human merchant",
        "neighbor",
        "player's private notes",
        "not a formal hai title",
        "not universal hai elder-care law",
    ):
        assert fragment in lowered, f"missing character/local-authority boundary: {fragment}"


def test_routes_settlements_and_aftermath():
    for route in (
        "route task specific assistance",
        "route bounded contingency",
        "route paired support records",
    ):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT
    for settlement in (
        "settlement portable support charter",
        "settlement expiry and renewal",
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
    assert f'has "{PREFIX}settlement portable support charter"' in aftermath
    assert f'has "{PREFIX}settlement expiry and renewal"' in aftermath
    assert aftermath.count(f'"{PREFIX}aftermath seen" = 1') == 1


def test_state_only_dialogue_lifecycle():
    assert len(re.findall(r'^\s*accept\s*$', TEXT, re.M)) == 0
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    for pattern in (
        r'^\s*destination\b',
        r'^\s*stopover\b',
        r'^\s*waypoint\b',
        r'^\s*npc\b',
        r'^\s*cargo\b',
        r'^\s*passengers?\b',
        r'^\s*deadline\b',
        r'^\s*timer\b',
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
        r'^\s*payment\b',
        r'^\s*combat rating\b',
        r'^\s*reputation\b',
        r'^\s*give\s+ship\b',
        r'^\s*give\s+outfit\b',
        r'^\s*give\s+cargo\b',
        r'^\s*take\s+outfit\b',
        r'^\s*take\s+cargo\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"material/reputation mutation found: {pattern}"


def test_autonomy_and_support_boundaries_are_explicit():
    lowered = TEXT.lower()
    for fragment in (
        "help into authority",
        "assistance task-specific and revocable",
        "does not transfer decision authority",
        "narrow contingency contact",
        "temporary authority expire by default",
        "age is not used as a substitute",
        "help is just help",
        "asked for it today",
    ):
        assert fragment in lowered, f"missing autonomy/support boundary: {fragment}"
    assert "did not resign from being myself" in lowered
    assert "old emergency cannot become a permanent habit" in lowered


def main():
    test_exact_graph_and_delay()
    test_scope_and_b1_dependencies()
    test_characters_and_local_authority_boundary()
    test_routes_settlements_and_aftermath()
    test_review_and_aftermath_lifecycle()
    test_state_only_dialogue_lifecycle()
    test_gotos_are_local_and_resolved()
    test_b2_only_writes_and_no_material_mutation()
    test_autonomy_and_support_boundaries_are_explicit()
    print("PASS: B2 Hai Retirement Autonomy Compact structure validated")
    print("PASS: missions=3")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: delayed_review=7-11 days")
    print("PASS: terminal_settlements=2")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: writes=B2 namespace only")
    print("PASS: aging/help/contingency/decision-authority boundaries explicit")


if __name__ == "__main__":
    main()
