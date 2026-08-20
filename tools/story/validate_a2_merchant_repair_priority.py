from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a2 merchant repair priority.txt").read_text(encoding="utf-8")


def test_structure_and_routes():
    assert TEXT.count('mission "A2 Merchant Repair Priority:') == 2
    for token in (
        '"world: merchant repair backlog" >= 3',
        '"world: merchant repair backlog" <= 1',
        'has "world: merchant repair surge"',
        '"A2 Merchant Repair Priority: priority safety" = 1',
        '"A2 Merchant Repair Priority: priority freight" = 1',
        '"A2 Merchant Repair Priority: priority queue" = 1',
        '"A2 Merchant Repair Priority: refused" = 1',
        '"A2 Merchant Repair Priority: recovery seen" = 1',
    ):
        assert token in TEXT


def test_six_simulation_sensitive_positive_outcomes_plus_refusal():
    for token in (
        'Cross remembers safety under surge',
        'Cross remembers safety after quiet',
        'Cross remembers freight under surge',
        'Cross remembers freight after quiet',
        'Cross remembers queue under surge',
        'Cross remembers queue after quiet',
        'refusal respected',
    ):
        assert token in TEXT


def test_a1_world_state_is_read_only():
    for name in ('world: merchant repair backlog', 'world: merchant repair surge', 'world: merchant rescue load'):
        assert not re.search(
            rf'^\s*"{re.escape(name)}"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
            TEXT,
            re.M,
        )


def test_persistence_namespace_isolated():
    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', TEXT, re.M)
    assert writes
    assert all(name.startswith('A2 Merchant Repair Priority:') for name in writes)
