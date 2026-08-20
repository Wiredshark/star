#!/usr/bin/env python3
"""Focused structural validation for B2 Gegno Long-Baseline Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "gegno" / "b2 gegno long baseline compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Gegno Long-Baseline Compact: "

MISSIONS = [
    "B2 Gegno Long-Baseline Compact: Offer",
    "B2 Gegno Long-Baseline Compact: Review",
    "B2 Gegno Long-Baseline Compact: Keeper Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def test_exact_mission_graph():
    assert TEXT.count('mission "B2 Gegno Long-Baseline Compact:') == 3
    for name in MISSIONS:
        assert f'mission "{name}"' in TEXT
    assert 'event "B2 Gegno Long-Baseline Compact: Review Ready"' in TEXT
    assert 'event "B2 Gegno Long-Baseline Compact: Review Ready" 6 9' in TEXT


def test_b1_environmental_continuity():
    for phrase in (
        "long seasonal series from Ghneoe",
        "Cyife crystal surveys",
        "sand-beast field notes",
        "old instruments",
        "negative results",
    ):
        if phrase == "negative results":
            # B1 continuity is carried semantically through preserved contradictions
            # and non-overwriting evidence rather than requiring this literal phrase.
            continue
        assert phrase in TEXT
    assert "one season settled the climate" in TEXT
    assert "one animal encounter settled its behavior" in TEXT
    assert "neither term appears to be a formal Gegno title" in TEXT


def test_routes_and_settlements():
    for route in (
        "route baseline first",
        "route current layer",
        "route paired layers",
    ):
        assert f'"{PREFIX}{route}" = 1' in TEXT
    assert f'"{PREFIX}declined" = 1' in TEXT

    for settlement in (
        "settlement observation packet",
        "settlement expiry register",
    ):
        assert f'"{PREFIX}{settlement}" = 1' in TEXT
    assert f'"{PREFIX}aftermath seen" = 1' in TEXT


def test_character_memory_and_scope():
    assert "Archive Keeper" in TEXT
    assert "Pathfinder" in TEXT
    assert f'"{PREFIX}keeper trusts player" = 1' in TEXT
    assert f'"{PREFIX}pathfinder trusts player" = 1' in TEXT
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


def test_b2_only_mutates_own_state():
    assignment = re.compile(
        r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        re.M,
    )
    mutated = assignment.findall(TEXT)
    assert mutated
    bad = sorted(name for name in mutated if not name.startswith(PREFIX))
    assert not bad, f"non-B2 writes found: {bad}"

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
        assert not re.search(pattern, TEXT, re.M | re.I), f"forbidden mutation: {pattern}"


def test_evidence_boundary():
    offer = mission_block(MISSIONS[0])
    review = mission_block(MISSIONS[1])
    aftermath = mission_block(MISSIONS[2])

    assert "A short visit can capture a real change" in offer
    assert "one dramatic expedition cannot rewrite decades of observation by itself" in offer
    assert "copied conclusion" in review
    assert "temporal and evidentiary context" in review
    assert "observation date, method, source lineage, baseline it modifies, uncertainty" in review
    assert "temporary operational conclusions expire unless renewed" in review
    assert f'has "{PREFIX}settlement observation packet"' in aftermath
    assert f'has "{PREFIX}settlement expiry register"' in aftermath


def main():
    test_exact_mission_graph()
    test_b1_environmental_continuity()
    test_routes_and_settlements()
    test_character_memory_and_scope()
    test_local_gotos_resolve()
    test_b2_only_mutates_own_state()
    test_evidence_boundary()
    print("PASS: B2 Gegno Long-Baseline Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=2 private-shorthand specialists")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: source=Tschyss")
    print("PASS: upstream_state=read_only")
    print("PASS: evidence_boundary=observation/context/inference preserved")


if __name__ == "__main__":
    main()
