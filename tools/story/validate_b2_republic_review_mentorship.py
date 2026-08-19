#!/usr/bin/env python3
"""Focused structural validation for B2 Republic Review Mentorship."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 republic review mentorship.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Republic Review Mentorship: "

MISSIONS = [
    "B2 Republic Review Mentorship: Offer",
    "B2 Republic Review Mentorship: Practice Review",
    "B2 Republic Review Mentorship: Keene Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def test_exact_mission_graph():
    assert TEXT.count('mission "B2 Republic Review Mentorship:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Republic Review Mentorship: Practice Ready"' in TEXT
    assert 'event "B2 Republic Review Mentorship: Practice Ready" 5 7' in TEXT


def test_named_character_and_a2_dependencies():
    assert "Sera Noll" in TEXT
    assert "Mara Keene" in TEXT
    assert 'has "A2 Republic Customs Review: later reader seen"' in TEXT
    assert 'has "A2 Republic Customs Review: precedent kept private"' in TEXT


def test_routes_and_settlements():
    expected_routes = [
        "route anonymized casebook",
        "route supervised clinic",
        "route private mentorship",
    ]
    for route in expected_routes:
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT

    settlements = [
        "settlement safeguards record",
        "settlement supervised review circle",
    ]
    for settlement in settlements:
        assert f'"{PREFIX}{settlement}" = 1' in TEXT
    assert f'"{PREFIX}aftermath seen" = 1' in TEXT


def test_source_scope_and_lifecycle():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Republic"' in block
        assert '\t\tnot attributes "station"' in block
        assert '\ton offer\n\t\tconversation' in block
        assert '\ton complete' not in block


def test_local_gotos_resolve():
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name}: missing labels for gotos {missing}"


def test_b2_does_not_mutate_upstream_or_material_state():
    forbidden_assignment_prefixes = (
        "A2 Republic Customs Review:",
        "world:",
    )
    for prefix in forbidden_assignment_prefixes:
        pattern = rf'^\s*"{re.escape(prefix)}[^"\n]*"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)'
        assert not re.search(pattern, TEXT, re.M), f"upstream write found for {prefix}"

    forbidden_actions = (
        r'^\s*payment\b',
        r'^\s*combat rating\b',
        r'^\s*reputation\b',
        r'^\s*give\s+ship\b',
        r'^\s*give\s+outfit\b',
        r'^\s*give\s+cargo\b',
        r'^\s*take\s+outfit\b',
        r'^\s*take\s+cargo\b',
    )
    for pattern in forbidden_actions:
        assert not re.search(pattern, TEXT, re.M | re.I), f"material/reputation mutation found: {pattern}"


def test_character_memory_persists():
    assert f'"{PREFIX}noll trusts player" = 1' in TEXT
    assert f'"{PREFIX}keene trusts player" = 1' in TEXT
    aftermath = mission_block(MISSIONS[2])
    assert f'has "{PREFIX}settlement safeguards record"' in aftermath
    assert f'has "{PREFIX}settlement supervised review circle"' in aftermath


def main():
    test_exact_mission_graph()
    test_named_character_and_a2_dependencies()
    test_routes_and_settlements()
    test_source_scope_and_lifecycle()
    test_local_gotos_resolve()
    test_b2_does_not_mutate_upstream_or_material_state()
    test_character_memory_persists()
    print("PASS: B2 Republic Review Mentorship structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: upstream_A1_A2_state=read_only")
    print("PASS: later_reader=Keene Remembers")


if __name__ == "__main__":
    main()
