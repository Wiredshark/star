#!/usr/bin/env python3
"""Focused structural validation for B2 Deep Research Credit Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 deep research credit compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Deep Research Credit Compact: "

MISSIONS = [
    "B2 Deep Research Credit Compact: Offer",
    "B2 Deep Research Credit Compact: Review",
    "B2 Deep Research Credit Compact: Ilyas Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def assignments_for(prefix: str):
    pattern = rf'^\s*"{re.escape(prefix)}[^"\n]*"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)'
    return re.findall(pattern, TEXT, re.M)


def test_exact_graph_and_delay():
    assert TEXT.count('mission "B2 Deep Research Credit Compact:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Deep Research Credit Compact: Review Ready"' in TEXT
    assert 'event "B2 Deep Research Credit Compact: Review Ready" 7 11' in TEXT


def test_characters_and_a2_dependencies():
    assert "Selene Arcos" in TEXT
    assert "Toren Ilyas" in TEXT
    for condition in (
        "A2 Deep Field Review: arcos future methods contact",
        "A2 Deep Field Review: arcos future anomaly contact",
        "A2 Deep Field Review: arcos future field contact",
        "A2 Deep Field Review: refusal respected",
    ):
        assert f'has "{condition}"' in TEXT


def test_routes_settlements_and_aftermath():
    for route in (
        "route contribution roles",
        "route claim attribution",
        "route paired consent",
    ):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT
    for settlement in (
        "settlement portable contribution packet",
        "settlement versioned claim custody",
    ):
        assert f'"{PREFIX}{settlement}" = 1' in TEXT
    assert f'"{PREFIX}aftermath seen" = 1' in TEXT


def test_review_requires_introduction_delay_and_one_shot_state():
    review = mission_block(MISSIONS[1])
    assert f'has "{PREFIX}introduced"' in review
    assert f'has "{PREFIX}review ready"' in review
    assert f'not "{PREFIX}reviewed"' in review
    assert review.count(f'"{PREFIX}reviewed" = 1') == 2

    aftermath = mission_block(MISSIONS[2])
    assert f'not "{PREFIX}aftermath seen"' in aftermath
    assert f'has "{PREFIX}settlement portable contribution packet"' in aftermath
    assert f'has "{PREFIX}settlement versioned claim custody"' in aftermath
    assert aftermath.count(f'"{PREFIX}aftermath seen" = 1') == 1


def test_state_only_dialogue_lifecycle():
    assert len(re.findall(r'^\s*accept\s*$', TEXT, re.M)) == 0
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    forbidden_objectives = (
        r'^\s*destination\b',
        r'^\s*stopover\b',
        r'^\s*waypoint\b',
        r'^\s*npc\b',
        r'^\s*cargo\b',
        r'^\s*passengers?\b',
        r'^\s*deadline\b',
        r'^\s*timer\b',
    )
    for pattern in forbidden_objectives:
        assert not re.search(pattern, TEXT, re.M | re.I), f"objective directive found: {pattern}"


def test_source_scope_and_gotos():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tattributes "deep"' in block
        assert '\t\tnot attributes "station"' in block
        assert '\ton offer\n\t\tconversation' in block
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name}: missing labels for gotos {missing}"


def test_b2_only_writes_and_no_material_mutation():
    assert not assignments_for("A2 Deep Field Review:")
    assert not assignments_for("world:")
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


def test_scientific_credit_boundaries_are_explicit():
    lowered = TEXT.lower()
    for fragment in (
        "field observation",
        "analytical",
        "interpret",
        "consent",
        "correction",
        "uncertainty",
        "contribution",
        "version",
    ):
        assert fragment in lowered, f"missing scientific-credit boundary: {fragment}"
    assert "nobody gets ownership of the parts they did not do" in lowered
    assert "credit becomes evidence lineage, not ceremony" in lowered


def main():
    test_exact_graph_and_delay()
    test_characters_and_a2_dependencies()
    test_routes_settlements_and_aftermath()
    test_review_requires_introduction_delay_and_one_shot_state()
    test_state_only_dialogue_lifecycle()
    test_source_scope_and_gotos()
    test_b2_only_writes_and_no_material_mutation()
    test_scientific_credit_boundaries_are_explicit()
    print("PASS: B2 Deep Research Credit Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=Selene Arcos + Toren Ilyas")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: delayed_review=7-11 days")
    print("PASS: terminal_settlements=2")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: A2 inputs=read_only; B2 writes=namespaced")
    print("PASS: scientific_credit_boundaries=observation/analysis/interpretation/consent/correction")


if __name__ == "__main__":
    main()
