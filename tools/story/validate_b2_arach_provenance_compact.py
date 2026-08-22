#!/usr/bin/env python3
"""Focused structural validation for B2 Arach Provenance Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "coalition" / "b2 arach provenance compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Arach Provenance Compact: "

MISSIONS = [
    "B2 Arach Provenance Compact: Offer",
    "B2 Arach Provenance Compact: Review",
    "B2 Arach Provenance Compact: Assayer Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def test_exact_graph():
    assert TEXT.count('mission "B2 Arach Provenance Compact:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Arach Provenance Compact: Review Ready"' in TEXT
    assert 'event "B2 Arach Provenance Compact: Review Ready" 5 7' in TEXT


def test_b1_continuity_and_character_boundary():
    for phrase in (
        "mine maps",
        "assay",
        "freight",
        "handoff",
        "provenance",
        "custody",
    ):
        assert phrase.lower() in TEXT.lower(), phrase
    assert "privately think of one as the Assayer" in TEXT
    assert "Carrier in your mind" in TEXT
    assert "not canonical Arach names, titles, or offices" in TEXT


def test_routes_and_settlements():
    for route in (
        "route portable provenance",
        "route bounded custody",
        "route paired histories",
    ):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT
    for settlement in (
        "settlement provenance packet",
        "settlement portable dispute ledger",
    ):
        assert f'"{PREFIX}{settlement}" = 1' in TEXT
    assert f'"{PREFIX}aftermath seen" = 1' in TEXT


def test_scope_and_lifecycle():
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tgovernment "Coalition"' in block
        assert '\t\tattributes "arach"' in block
        assert '\ton offer\n\t\tconversation' in block
        assert '\ton complete' not in block

    # These missions only persist dialogue/global state. They do not create a
    # gameplay objective, so every terminal conversation path must close with
    # decline rather than accepting an objective-less active mission.
    assert not re.search(r'^\s*accept\s*$', TEXT, re.M), "state-only path uses accept"
    declines = re.findall(r'^\s*decline\s*$', TEXT, re.M)
    assert len(declines) == 7, f"expected 7 state-only decline terminals, got {len(declines)}"

    objective_directives = (
        "destination",
        "stopover",
        "waypoint",
        "npc",
        "cargo",
        "passengers",
        "deadline",
        "timer",
    )
    for directive in objective_directives:
        assert not re.search(rf'^\s*{re.escape(directive)}\b', TEXT, re.M | re.I), (
            f"state-only lifecycle assumption invalidated by objective directive: {directive}"
        )


def test_local_gotos_resolve():
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name}: missing labels for gotos {missing}"


def test_b2_write_ownership_and_no_material_rewards():
    assignments = re.findall(r'^\s*"([^"]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M)
    assert assignments
    assert all(key.startswith(PREFIX) for key in assignments), assignments

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
        assert not re.search(pattern, TEXT, re.M | re.I), pattern


def test_record_semantics_and_later_reader():
    review = mission_block(MISSIONS[1])
    assert "observation" in review.lower()
    assert "inferred" in review.lower()
    assert "uncertainty" in review.lower()
    assert "contradiction" in review.lower()
    aftermath = mission_block(MISSIONS[2])
    assert f'has "{PREFIX}settlement provenance packet"' in aftermath
    assert f'has "{PREFIX}settlement portable dispute ledger"' in aftermath


def main():
    test_exact_graph()
    test_b1_continuity_and_character_boundary()
    test_routes_and_settlements()
    test_scope_and_lifecycle()
    test_local_gotos_resolve()
    test_b2_write_ownership_and_no_material_rewards()
    test_record_semantics_and_later_reader()
    print("PASS: B2 Arach Provenance Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=2 player-private shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: dialogue_lifecycle=7/7 state-only terminals decline")
    print("PASS: write_surface=B2 prefix only")
    print("PASS: later_reader=Assayer Remembers")


if __name__ == "__main__":
    main()
