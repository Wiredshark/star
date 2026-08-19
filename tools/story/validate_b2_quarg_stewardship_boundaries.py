#!/usr/bin/env python3
"""Focused structural validation for B2 Quarg Stewardship Boundaries."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "quarg" / "b2 quarg stewardship boundaries.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Quarg Stewardship Boundaries: "

MISSIONS = [
    "B2 Quarg Stewardship Boundaries: Offer",
    "B2 Quarg Stewardship Boundaries: Review",
    "B2 Quarg Stewardship Boundaries: Steward Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def test_exact_mission_graph():
    assert TEXT.count('mission "B2 Quarg Stewardship Boundaries:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Quarg Stewardship Boundaries: Review Ready"' in TEXT
    assert 'event "B2 Quarg Stewardship Boundaries: Review Ready" 6 9' in TEXT


def test_history_dependency_and_character_continuity():
    offer = mission_block(MISSIONS[0])
    assert 'has "First Contact: Quarg: offered"' in offer
    assert 'has "Quarg History: Protected Community Ledger: offered"' in offer
    assert offer.lower().count("steward") >= 4
    review = mission_block(MISSIONS[1])
    aftermath = mission_block(MISSIONS[2])
    assert "steward" in review.lower()
    assert "steward" in aftermath.lower()


def test_routes_and_settlements():
    for route in (
        "route local autonomy",
        "route accountable protection",
        "route dual ledger",
    ):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT

    for settlement in (
        "settlement narrow covenant",
        "settlement paired duty register",
    ):
        assert f'"{PREFIX}{settlement}" = 1' in TEXT
    assert f'"{PREFIX}aftermath seen" = 1' in TEXT
    assert f'"{PREFIX}steward trusts player" = 1' in TEXT


def test_quarg_scope_and_lifecycle():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Quarg"' in block
        assert '\ton offer\n\t\tconversation' in block
        assert '\ton complete' not in block


def test_local_gotos_resolve():
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name}: missing labels for gotos {missing}"


def test_b2_owns_only_its_state():
    assignments = re.findall(
        r'^\s*"([^"]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )
    unexpected = sorted(name for name in assignments if not name.startswith(PREFIX))
    assert not unexpected, f"non-B2 condition writes: {unexpected}"

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


def test_aftermath_reads_both_terminal_states():
    aftermath = mission_block(MISSIONS[2])
    assert f'has "{PREFIX}settlement narrow covenant"' in aftermath
    assert f'has "{PREFIX}settlement paired duty register"' in aftermath
    assert f'"{PREFIX}aftermath seen" = 1' in aftermath


def main():
    test_exact_mission_graph()
    test_history_dependency_and_character_continuity()
    test_routes_and_settlements()
    test_quarg_scope_and_lifecycle()
    test_local_gotos_resolve()
    test_b2_owns_only_its_state()
    test_aftermath_reads_both_terminal_states()
    print("PASS: B2 Quarg Stewardship Boundaries structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_character=Quarg refuge steward")
    print("PASS: B1_history_dependency=Protected Community Ledger")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: later_reader=Steward Remembers")


if __name__ == "__main__":
    main()
