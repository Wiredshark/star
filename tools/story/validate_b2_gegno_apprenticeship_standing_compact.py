#!/usr/bin/env python3
"""Focused structural validation for B2 Gegno Apprenticeship Standing Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "gegno" / "b2 gegno apprenticeship standing compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Gegno Apprenticeship Standing Compact: "

MISSIONS = [
    "B2 Gegno Apprenticeship Standing Compact: Offer",
    "B2 Gegno Apprenticeship Standing Compact: Review",
    "B2 Gegno Apprenticeship Standing Compact: Apprentice Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def assignments_for(prefix: str):
    pattern = rf'^\s*"{re.escape(prefix)}[^"\n]*"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)'
    return re.findall(pattern, TEXT, re.M)


def test_exact_graph_and_delay():
    assert TEXT.count('mission "B2 Gegno Apprenticeship Standing Compact:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Gegno Apprenticeship Standing Compact: Review Ready"' in TEXT
    assert 'event "B2 Gegno Apprenticeship Standing Compact: Review Ready" 7 11' in TEXT


def test_dependency_scope_and_characters():
    offer = mission_block(MISSIONS[0])
    assert 'has "Gegno Asteroid Mining Prologue: done"' in offer
    assert 'has "B2 Gegno Claim Records: aftermath seen"' in offer
    for name in MISSIONS:
        assert '\tsource "Tschyss"' in mission_block(name)
    lowered = TEXT.lower()
    assert "mentor" in lowered
    assert "apprentice" in lowered
    assert "player-private shorthand" in lowered
    assert "not gegno offices" in lowered


def test_routes_settlements_and_aftermath():
    for route in (
        "route demonstration first",
        "route bounded reference",
        "route paired portfolio",
    ):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT
    for settlement in (
        "settlement portable skill portfolio",
        "settlement challenge and renewal",
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
    assert f'has "{PREFIX}settlement portable skill portfolio"' in aftermath
    assert f'has "{PREFIX}settlement challenge and renewal"' in aftermath
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
    assert not assignments_for("world:")
    assert not assignments_for("B2 Gegno Claim Records:")
    action_assignments = re.findall(r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M)
    foreign = sorted({name for name in action_assignments if not name.startswith(PREFIX)})
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


def test_mentorship_and_allegiance_boundaries_are_explicit():
    lowered = TEXT.lower()
    for fragment in (
        "demonstrated",
        "mentor lineage",
        "political allegiance",
        "scope",
        "independent corroboration",
        "training lineage is history, not allegiance",
        "not a universal credential",
    ):
        assert fragment in lowered, f"missing mentorship boundary: {fragment}"
    assert "a mentor can vouch for work they actually saw, not for political loyalty" in lowered
    assert "the challenge must be about the work, not the faction of the teacher" in lowered


def main():
    test_exact_graph_and_delay()
    test_dependency_scope_and_characters()
    test_routes_settlements_and_aftermath()
    test_review_and_aftermath_lifecycle()
    test_state_only_dialogue_lifecycle()
    test_gotos_are_local_and_resolved()
    test_b2_only_writes_and_no_material_mutation()
    test_mentorship_and_allegiance_boundaries_are_explicit()
    print("PASS: B2 Gegno Apprenticeship Standing Compact structure validated")
    print("PASS: missions=3")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: delayed_review=7-11 days")
    print("PASS: terminal_settlements=2")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: writes=B2 namespace only")
    print("PASS: mentorship/skill/faction-allegiance boundaries explicit")


if __name__ == "__main__":
    main()
