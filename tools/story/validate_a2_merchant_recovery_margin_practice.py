from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a2 merchant recovery margin practice.txt").read_text(encoding="utf-8")


def test_structure_routes_and_offer_precedence():
    assert TEXT.count('mission "A2 Merchant Recovery Margin Practice:') == 2
    assert TEXT.count('"offer precedence" 9') == 2
    for token in (
        'has "B2 Merchant Recovery Margin Compact: aftermath seen"',
        '"world: merchant repair backlog" >= 3',
        'has "world: merchant repair surge"',
        '"A2 Merchant Recovery Margin Practice: continuity" = 1',
        '"A2 Merchant Recovery Margin Practice: challenge" = 1',
        '"A2 Merchant Recovery Margin Practice: local" = 1',
        '"A2 Merchant Recovery Margin Practice: declined" = 1',
        '"A2 Merchant Recovery Margin Practice: pressure test seen" = 1',
    ):
        assert token in TEXT


def test_six_simulation_sensitive_outcomes():
    for token in (
        'Vale remembers continuity under surge',
        'Vale remembers continuity under quiet',
        'Vale remembers challenge under surge',
        'Vale remembers challenge under quiet',
        'Vale remembers local under surge',
        'Vale remembers local under quiet',
    ):
        assert token in TEXT


def test_explicit_route_gating_and_one_shot_pressure_test():
    for token in (
        'branch continuity_surge',
        'branch continuity_quiet',
        'branch challenge_surge',
        'branch challenge_quiet',
        'branch local_surge',
        'branch local_quiet',
        'not "A2 Merchant Recovery Margin Practice: pressure test seen"',
    ):
        assert token in TEXT


def test_a1_and_b2_state_are_read_only():
    for name in (
        'world: merchant repair backlog',
        'world: merchant repair surge',
        'B2 Merchant Recovery Margin Compact: aftermath seen',
        'B2 Merchant Recovery Margin Compact: settlement margin packet',
    ):
        assert not re.search(
            rf'^\s*"{re.escape(name)}"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
            TEXT,
            re.M,
        )


def test_persistence_namespace_isolated():
    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', TEXT, re.M)
    assert writes
    assert all(name.startswith('A2 Merchant Recovery Margin Practice:') for name in writes)


def test_state_only_dialogue_lifecycle():
    assert '\taccept\n' not in TEXT
    assert TEXT.count('\t\t\t\tdecline') == 5
    for forbidden in ('\tdestination ', '\twaypoint ', '\tstopover ', '\tcargo ', '\tpassengers '):
        assert forbidden not in TEXT


def test_refusal_does_not_arm_pressure_test():
    assert '"A2 Merchant Recovery Margin Practice: declined" = 1' in TEXT
    assert 'has "A2 Merchant Recovery Margin Practice: introduced"' in TEXT
    assert '"A2 Merchant Recovery Margin Practice: introduced" = 1' not in TEXT.split('label refuse', 1)[1].split('decline', 1)[0]


def test_no_centralized_merchant_authority_claim():
    assert 'centralized Merchant authority' in TEXT
    assert 'voluntary coordination tool' in TEXT
