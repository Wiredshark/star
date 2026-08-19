from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRANSIT = ROOT / "data/human/a1 transit congestion.txt"
PATROL = ROOT / "data/human/a1 free worlds defense strain.txt"
BRIDGE = ROOT / "data/human/a1 free worlds patrol transit load.txt"


def apply_crossing(congestion, patrol_surge=False, routing_load=False):
    # Existing Southern Rim crossing contributes one point.
    congestion = min(6, congestion + 1)
    # New bridge contributes one additional point only while the accepted
    # patrol-surge signal is active and its short routing latch is clear.
    if patrol_surge and not routing_load and congestion < 6:
        congestion = min(6, congestion + 1)
        routing_load = True
    return congestion, routing_load


def decay(congestion):
    return max(0, congestion - 1)


def test_contract_tokens_and_authoritative_signal_reuse():
    transit = TRANSIT.read_text(encoding="utf-8")
    patrol = PATROL.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert 'set "world: free worlds patrol surge"' in patrol
    assert '"world: southern rim transit congestion" += 1' in transit
    for token in (
        'has "world: free worlds patrol surge"',
        'not "world: free worlds military routing load"',
        '"world: southern rim transit congestion" += 1',
        '"world: southern rim transit congestion" <?= 6',
        'event "ES A1: Southern Rim Transit Congestion Decay" 3 3',
        'event "ES A1: Free Worlds Military Routing Load Ends" 2 2',
        'clear "world: free worlds military routing load"',
    ):
        assert token in bridge


def test_patrol_surge_adds_bounded_extra_routing_load():
    assert apply_crossing(0, patrol_surge=False, routing_load=False) == (1, False)
    assert apply_crossing(0, patrol_surge=True, routing_load=False) == (2, True)
    assert apply_crossing(5, patrol_surge=True, routing_load=False) == (6, False)


def test_routing_latch_blocks_repeat_amplification_until_released():
    congestion, latch = apply_crossing(0, patrol_surge=True, routing_load=False)
    assert (congestion, latch) == (2, True)
    congestion, latch = apply_crossing(congestion, patrol_surge=True, routing_load=latch)
    assert (congestion, latch) == (3, True)
    # After the two-day latch ends, a later qualifying crossing can again add
    # the military-routing contribution while the surge remains active.
    latch = False
    congestion, latch = apply_crossing(congestion, patrol_surge=True, routing_load=latch)
    assert (congestion, latch) == (5, True)


def test_deterministic_year_horizon_remains_bounded_and_recovers():
    congestion = 0
    latch_days = 0
    for day in range(365):
        patrol_surge = day < 90
        # Representative border crossing every four days.
        if day % 4 == 0:
            congestion, latched = apply_crossing(
                congestion,
                patrol_surge=patrol_surge,
                routing_load=latch_days > 0,
            )
            if latched and latch_days == 0:
                latch_days = 2
        # Each crossing contribution schedules the accepted three-day decay;
        # this compact model applies one decay every three days for horizon QA.
        if day % 3 == 2:
            congestion = decay(congestion)
        latch_days = max(0, latch_days - 1)
        assert 0 <= congestion <= 6

    # A quiet recovery tail must be capable of draining the bounded state.
    for _ in range(18):
        congestion = decay(congestion)
    assert congestion == 0


if __name__ == "__main__":
    test_contract_tokens_and_authoritative_signal_reuse()
    test_patrol_surge_adds_bounded_extra_routing_load()
    test_routing_latch_blocks_repeat_amplification_until_released()
    test_deterministic_year_horizon_remains_bounded_and_recovers()
    print("A1 Free Worlds patrol-transit feedback contract: PASS")
