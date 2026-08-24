#!/usr/bin/env python3
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a2 free worlds joint corridor doctrine.txt"
TEXT = DATA.read_text(encoding="utf-8")


def require(token: str) -> None:
    assert token in TEXT, token


def test_structure_and_routes() -> None:
    assert TEXT.count('mission "A2 Free Worlds Joint Corridor Doctrine:') == 2
    assert TEXT.count('"offer precedence" 9') == 2
    assert TEXT.count('\n\t\t\t\tdecline') == 5
    assert '\n\t\t\t\taccept' not in TEXT
    for token in (
        'mission "A2 Free Worlds Joint Corridor Doctrine: Review"',
        'mission "A2 Free Worlds Joint Corridor Doctrine: Stress Test"',
        'Anika Ro',
        'Rhea Solano',
        'has "A2 Free Worlds Patrol Doctrine: Briefing: done"',
        'not "A2 Free Worlds Patrol Doctrine: later reader pending"',
        'not "A2 Free Worlds Patrol Doctrine: refused"',
        'has "A2 Southern Rim Traffic Coordination: followup seen"',
        'not "A2 Southern Rim Traffic Coordination: refused"',
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
        'label refused',
        'label finish_refusal',
        'label finish',
        '"A2 Free Worlds Joint Corridor Doctrine: refusal respected" = 1',
        '"A2 Free Worlds Joint Corridor Doctrine: stress reader seen" = 1',
    ):
        require(token)


def test_persistent_route_contract() -> None:
    assert TEXT.count('"A2 Free Worlds Joint Corridor Doctrine: review seen" = 1') == 4
    assert TEXT.count('"A2 Free Worlds Joint Corridor Doctrine: stress reader pending" = 1') == 4
    assert TEXT.count(' combined proven" = 1') == 3
    assert TEXT.count(' traffic proven" = 1') == 3
    assert TEXT.count('"A2 Free Worlds Joint Corridor Doctrine: stress reader pending" = 0') == 1
    assert TEXT.count('"A2 Free Worlds Joint Corridor Doctrine: stress reader seen" = 1') == 1


def test_prior_a2_state_is_read_only() -> None:
    forbidden = (
        '"A2 Free Worlds Patrol Doctrine: civilians" =',
        '"A2 Free Worlds Patrol Doctrine: interdiction" =',
        '"A2 Free Worlds Patrol Doctrine: mobility" =',
        '"A2 Free Worlds Patrol Doctrine: refused" =',
        '"A2 Free Worlds Patrol Doctrine: later reader pending" =',
        '"A2 Southern Rim Traffic Coordination: policy emergency corridors" =',
        '"A2 Southern Rim Traffic Coordination: policy staggered clearance" =',
        '"A2 Southern Rim Traffic Coordination: policy distributed routing" =',
        '"A2 Southern Rim Traffic Coordination: followup seen" =',
        '"A2 Southern Rim Traffic Coordination: refused" =',
    )
    for token in forbidden:
        assert token not in TEXT, f"illegal predecessor-A2 state write: {token}"


def test_a1_state_is_read_only() -> None:
    forbidden = (
        '"world: southern rim transit congestion" =',
        '"world: southern rim transit congestion" +=',
        '"world: southern rim transit congestion" -=',
        'set "world: free worlds patrol surge"',
        'clear "world: free worlds patrol surge"',
        '"world: free worlds patrol surge" =',
        '"world: free worlds defense strain" =',
        '"world: free worlds defense strain" +=',
        '"world: free worlds defense strain" -=',
    )
    for token in forbidden:
        assert token not in TEXT, f"illegal A1 state write: {token}"


def test_namespace_isolation() -> None:
    for line in TEXT.splitlines():
        stripped = line.strip()
        if stripped.startswith('"A2 ') and ' = ' in stripped:
            assert stripped.startswith('"A2 Free Worlds Joint Corridor Doctrine:'), stripped


def test_no_gameplay_objectives_or_material_mutation() -> None:
    forbidden_directives = (
        '\n\tdestination ',
        '\n\twaypoint ',
        '\n\tstopover ',
        '\n\tcargo ',
        '\n\tpassengers ',
        '\n\tcredits ',
        '\n\treputation ',
        '\n\toutfit ',
        '\n\tship ',
        '\n\tfleet ',
    )
    for token in forbidden_directives:
        assert token not in TEXT, f"unexpected gameplay/material directive: {token!r}"


if __name__ == "__main__":
    test_structure_and_routes()
    test_persistent_route_contract()
    test_prior_a2_state_is_read_only()
    test_a1_state_is_read_only()
    test_namespace_isolation()
    test_no_gameplay_objectives_or_material_mutation()
    print("A2 Free Worlds joint-corridor doctrine contract: PASS")
    print("missions=2")
    print("named_characters=Anika Ro, Rhea Solano")
    print("prior_a2_inputs=patrol doctrine, southern rim traffic coordination")
    print("authoritative_a1_inputs=southern rim transit congestion, free worlds patrol surge")
    print("joint_protocol_routes=3 + refusal")
    print("stress_test_variants=6 + refusal")
    print("state_only_declines=5")
    print("prior_a2_writes=none")
    print("authoritative_a1_writes=none")
