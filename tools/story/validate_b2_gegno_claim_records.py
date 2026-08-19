#!/usr/bin/env python3
"""Focused structural validation for B2 Gegno Claim Records."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "gegno" / "b2 gegno claim records.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Gegno Claim Records: "

MISSIONS = [
    "B2 Gegno Claim Records: Offer",
    "B2 Gegno Claim Records: Review",
    "B2 Gegno Claim Records: Tchei Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def test_exact_mission_graph():
    assert TEXT.count('mission "B2 Gegno Claim Records:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Gegno Claim Records: Review Ready"' in TEXT
    assert 'event "B2 Gegno Claim Records: Review Ready" 5 7' in TEXT


def test_b1_and_mining_dependencies():
    assert "Tchei Ess" in TEXT
    assert "Duei Ciech" in TEXT
    assert 'has "Gegno Asteroid Mining Prologue: done"' in TEXT
    assert "Claim Marker Archive" in TEXT
    assert "Ore Measure Ledger" in TEXT


def test_routes_and_settlements():
    routes = [
        "route custody chain",
        "route current assay",
        "route paired ledger",
    ]
    for route in routes:
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT

    settlements = [
        "settlement transferable record",
        "settlement two-signature handoff",
    ]
    for settlement in settlements:
        assert f'"{PREFIX}{settlement}" = 1' in TEXT
    assert f'"{PREFIX}aftermath seen" = 1' in TEXT


def test_source_scope_and_lifecycle():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\tsource "Tschyss"' in block
        assert '\ton offer\n\t\tconversation' in block
        assert '\ton complete' not in block


def test_local_gotos_resolve():
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name}: missing labels for gotos {missing}"


def test_b2_only_mutates_own_story_state():
    assignment = re.compile(
        r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        re.M,
    )
    mutated = assignment.findall(TEXT)
    assert mutated, "expected B2 story-state assignments"
    bad = sorted(name for name in mutated if not name.startswith(PREFIX))
    assert not bad, f"non-B2 condition writes found: {bad}"

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


def test_continuity_boundary_and_character_memory():
    assert "without implying political unification or friendship" in TEXT
    assert f'"{PREFIX}tchei trusts player" = 1' in TEXT
    assert f'"{PREFIX}duei trusts player" = 1' in TEXT

    aftermath = mission_block(MISSIONS[2])
    assert f'has "{PREFIX}settlement transferable record"' in aftermath
    assert f'has "{PREFIX}settlement two-signature handoff"' in aftermath
    assert "The record crossed the dispute without asking the dispute to end." in aftermath


def main():
    test_exact_mission_graph()
    test_b1_and_mining_dependencies()
    test_routes_and_settlements()
    test_source_scope_and_lifecycle()
    test_local_gotos_resolve()
    test_b2_only_mutates_own_story_state()
    test_continuity_boundary_and_character_memory()
    print("PASS: B2 Gegno Claim Records structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: source=Tschyss")
    print("PASS: upstream_state=read_only")
    print("PASS: later_reader=Tchei Remembers")


if __name__ == "__main__":
    main()
