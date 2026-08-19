#!/usr/bin/env python3
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a2 free worlds joint corridor doctrine.txt"
TEXT = DATA.read_text(encoding="utf-8")


def require(token):
    assert token in TEXT, token


def test_contract():
    for token in (
        'mission "A2 Free Worlds Joint Corridor Doctrine: Review"',
        'mission "A2 Free Worlds Joint Corridor Doctrine: Stress Test"',
        'Anika Ro',
        'Rhea Solano',
        'has "A2 Free Worlds Patrol Doctrine: Briefing: done"',
        'not "A2 Free Worlds Patrol Doctrine: later reader pending"',
        'has "A2 Southern Rim Traffic Coordination: followup seen"',
        '"A2 Free Worlds Joint Corridor Doctrine: protected capacity" = 1',
        '"A2 Free Worlds Joint Corridor Doctrine: synchronized windows" = 1',
        '"A2 Free Worlds Joint Corridor Doctrine: delegated authority" = 1',
        '"A2 Free Worlds Joint Corridor Doctrine: refused" = 1',
        '"world: southern rim transit congestion" >= 4',
        'has "world: free worlds patrol surge"',
        'not "world: free worlds patrol surge"',
        'label protected_combined',
        'label protected_traffic',
        'label synchronized_combined',
        'label synchronized_traffic',
        'label delegated_combined',
        'label delegated_traffic',
        '"A2 Free Worlds Joint Corridor Doctrine: stress reader seen" = 1',
    ):
        require(token)


def test_prior_a2_state_is_read_only():
    forbidden = (
        '"A2 Free Worlds Patrol Doctrine: civilians" =',
        '"A2 Free Worlds Patrol Doctrine: interdiction" =',
        '"A2 Free Worlds Patrol Doctrine: mobility" =',
        '"A2 Southern Rim Traffic Coordination: policy emergency corridors" =',
        '"A2 Southern Rim Traffic Coordination: policy staggered clearance" =',
        '"A2 Southern Rim Traffic Coordination: policy distributed routing" =',
        '"A2 Southern Rim Traffic Coordination: followup seen" =',
    )
    for token in forbidden:
        assert token not in TEXT, f"illegal prior-A2 state write: {token}"


def test_a1_state_is_read_only():
    forbidden = (
        '"world: southern rim transit congestion" =',
        '"world: southern rim transit congestion" +=',
        '"world: southern rim transit congestion" -=',
        'set "world: free worlds patrol surge"',
        'clear "world: free worlds patrol surge"',
        '"world: free worlds defense strain" =',
        '"world: free worlds defense strain" +=',
        '"world: free worlds defense strain" -=',
    )
    for token in forbidden:
        assert token not in TEXT, f"illegal A1 state write: {token}"


def test_persistent_routes():
    assert TEXT.count('"A2 Free Worlds Joint Corridor Doctrine: stress reader pending" = 1') == 4
    assert TEXT.count(' combined proven" = 1') == 3
    assert TEXT.count(' traffic proven" = 1') == 3
    assert '"A2 Free Worlds Joint Corridor Doctrine: refusal respected" = 1' in TEXT
    assert TEXT.count('"A2 Free Worlds Joint Corridor Doctrine: stress reader pending" = 0') == 1


if __name__ == "__main__":
    test_contract()
    test_prior_a2_state_is_read_only()
    test_a1_state_is_read_only()
    test_persistent_routes()
    print("A2 Free Worlds joint-corridor doctrine contract: PASS")
    print("missions=2")
    print("named_characters=Anika Ro, Rhea Solano")
    print("prior_a2_inputs=patrol doctrine, southern rim traffic coordination")
    print("authoritative_a1_inputs=southern rim transit congestion, free worlds patrol surge")
    print("joint_protocol_routes=3 + refusal")
    print("stress_test_variants=6 + refusal")
    print("prior_a2_writes=none")
    print("authoritative_a1_writes=none")
