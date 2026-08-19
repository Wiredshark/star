#!/usr/bin/env python3
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a2 free worlds patrol doctrine.txt"
TEXT = DATA.read_text(encoding="utf-8")


def require(token):
    assert token in TEXT, token


def test_contract():
    for token in (
        'mission "A2 Free Worlds Patrol Doctrine: Briefing"',
        'mission "A2 Free Worlds Patrol Doctrine: After Action"',
        'Anika Ro',
        'has "world: free worlds patrol surge"',
        'not "world: free worlds patrol surge"',
        '"world: free worlds defense strain" >= 3',
        '"world: free worlds defense strain" >= 2',
        '"world: free worlds defense strain" < 2',
        '"A2 Free Worlds Patrol Doctrine: civilians" = 1',
        '"A2 Free Worlds Patrol Doctrine: interdiction" = 1',
        '"A2 Free Worlds Patrol Doctrine: mobility" = 1',
        '"A2 Free Worlds Patrol Doctrine: refused" = 1',
        '"A2 Free Worlds Patrol Doctrine: later reader pending" = 1',
        '"A2 Free Worlds Patrol Doctrine: later reader pending" = 0',
        'label civilians_strained',
        'label civilians_recovered',
        'label interdiction_strained',
        'label interdiction_recovered',
        'label mobility_strained',
        'label mobility_recovered',
        'label refused',
    ):
        require(token)


def test_a1_state_is_read_only():
    forbidden = (
        '"world: free worlds defense strain" =',
        '"world: free worlds defense strain" +=',
        '"world: free worlds defense strain" -=',
        'set "world: free worlds patrol surge"',
        'clear "world: free worlds patrol surge"',
    )
    for token in forbidden:
        assert token not in TEXT, f"illegal A1 state write: {token}"


def test_routes_are_persistent():
    assert TEXT.count('"A2 Free Worlds Patrol Doctrine: later reader pending" = 1') == 4
    assert TEXT.count('future contact" = 1') == 6
    assert '"A2 Free Worlds Patrol Doctrine: refusal respected" = 1' in TEXT


if __name__ == "__main__":
    test_contract()
    test_a1_state_is_read_only()
    test_routes_are_persistent()
    print("A2 Free Worlds patrol-doctrine contract: PASS")
    print("missions=2")
    print("named_character=Anika Ro")
    print("authoritative_a1_inputs=defense strain, patrol surge")
    print("initial_routes=3 + refusal")
    print("after_action_variants=6 + refusal")
    print("authoritative_a1_writes=none")
