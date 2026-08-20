from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONGESTION = ROOT / "data/human/a1 transit congestion.txt"
RESCUE = ROOT / "data/human/a1 merchant rescue load.txt"
BRIDGE = ROOT / "data/human/a1 southern rim rescue spillover.txt"


def apply_spillover(rescue_load, congestion, latch=False):
    if congestion >= 4 and rescue_load < 5 and not latch:
        return min(5, rescue_load + 1), True
    return rescue_load, latch


def recover_rescue(rescue_load):
    return max(0, rescue_load - 1)


def test_contract_reuses_authoritative_states_without_mutating_congestion():
    congestion = CONGESTION.read_text(encoding="utf-8")
    rescue = RESCUE.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert '"world: southern rim transit congestion" += 1' in congestion
    assert '"world: merchant rescue load" += 1' in rescue
    for token in (
        '"world: southern rim transit congestion" >= 4',
        '"world: merchant rescue load" < 5',
        'not "world: southern rim rescue spillover active"',
        'set "world: southern rim rescue spillover active"',
        '"world: merchant rescue load" += 1',
        '"world: merchant rescue load" <?= 5',
        'event "ES A1: Merchant Rescue Load Recovery" 5 5',
        'event "ES A1: Southern Rim Rescue Spillover Latch Ends" 6 6',
        'clear "world: southern rim rescue spillover active"',
    ):
        assert token in bridge

    assert '"world: southern rim transit congestion" +=' not in bridge
    assert '"world: southern rim transit congestion" -=' not in bridge


def test_threshold_cap_and_latch_behavior():
    assert apply_spillover(0, 3, False) == (0, False)
    assert apply_spillover(0, 4, False) == (1, True)
    assert apply_spillover(4, 6, False) == (5, True)
    assert apply_spillover(5, 6, False) == (5, False)
    assert apply_spillover(2, 6, True) == (2, True)


def test_quiet_recovery():
    rescue, latch = apply_spillover(0, 6, False)
    assert (rescue, latch) == (1, True)
    rescue = recover_rescue(rescue)
    assert rescue == 0
    assert apply_spillover(rescue, 2, False) == (0, False)


def test_deterministic_three_year_horizon_is_bounded_and_recovers():
    rescue = 0
    latch_days = 0
    for day in range(365 * 3):
        congestion = 6 if day % 150 < 45 else 2
        if day % 2 == 0:
            rescue, activated = apply_spillover(
                rescue,
                congestion,
                latch=latch_days > 0,
            )
            if activated and latch_days == 0:
                latch_days = 6
        if day % 5 == 4:
            rescue = recover_rescue(rescue)
        latch_days = max(0, latch_days - 1)
        assert 0 <= rescue <= 5

    for _ in range(6):
        rescue = recover_rescue(rescue)
    assert rescue == 0


if __name__ == "__main__":
    test_contract_reuses_authoritative_states_without_mutating_congestion()
    test_threshold_cap_and_latch_behavior()
    test_quiet_recovery()
    test_deterministic_three_year_horizon_is_bounded_and_recovers()
    print("A1 Southern Rim congestion -> Merchant rescue spillover: PASS")
