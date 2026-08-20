from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESCUE = ROOT / "data/human/a1 merchant rescue load.txt"
SALVAGE = ROOT / "data/human/a1 merchant salvage demand.txt"


def apply_salvage(demand, rescue_load, latch=False):
    if rescue_load >= 3 and demand < 4 and not latch:
        return min(4, demand + 1), True
    return demand, latch


def recover_salvage(demand):
    return max(0, demand - 1)


def test_contract_consumes_rescue_load_read_only_and_owns_bounded_decay():
    rescue = RESCUE.read_text(encoding="utf-8")
    salvage = SALVAGE.read_text(encoding="utf-8")

    assert '"world: merchant rescue load" += 1' in rescue
    for token in (
        '"world: merchant rescue load" >= 3',
        '"world: merchant salvage demand" < 4',
        'not "world: merchant salvage demand active"',
        'set "world: merchant salvage demand active"',
        '"world: merchant salvage demand" += 1',
        '"world: merchant salvage demand" <?= 4',
        'event "ES A1: Merchant Salvage Demand Recovery" 8 8',
        'event "ES A1: Merchant Salvage Demand Latch Ends" 5 5',
        'clear "world: merchant salvage demand active"',
    ):
        assert token in salvage

    assert '"world: merchant rescue load" +=' not in salvage
    assert '"world: merchant rescue load" -=' not in salvage


def test_threshold_cap_latch_and_recovery_behavior():
    assert apply_salvage(0, 2, False) == (0, False)
    assert apply_salvage(0, 3, False) == (1, True)
    assert apply_salvage(3, 5, False) == (4, True)
    assert apply_salvage(4, 5, False) == (4, False)

    demand, latch = apply_salvage(1, 5, False)
    assert (demand, latch) == (2, True)
    assert apply_salvage(demand, 5, latch) == (2, True)
    assert recover_salvage(2) == 1
    assert recover_salvage(0) == 0


def test_deterministic_three_year_horizon_stays_bounded_and_quiet_tail_recovers():
    demand = 0
    latch_days = 0
    recovery_days = []

    for day in range(365 * 3):
        # Deterministic rescue seasons: 50 days overloaded, 70 days quiet.
        rescue_load = 5 if day % 120 < 50 else 1

        if day % 2 == 0:
            demand, activated = apply_salvage(
                demand,
                rescue_load,
                latch=latch_days > 0,
            )
            if activated and latch_days == 0:
                latch_days = 5
                recovery_days.append(day + 8)

        due = recovery_days.count(day)
        for _ in range(due):
            demand = recover_salvage(demand)

        latch_days = max(0, latch_days - 1)
        assert 0 <= demand <= 4

    # No fresh overload: all outstanding contributions drain deterministically.
    for _ in range(16):
        demand = recover_salvage(demand)
    assert demand == 0


def test_quiet_upstream_does_not_manufacture_demand_after_latch_release():
    demand, latch = apply_salvage(0, 5, False)
    assert (demand, latch) == (1, True)
    demand = recover_salvage(demand)
    assert demand == 0
    assert apply_salvage(demand, 1, False) == (0, False)


if __name__ == "__main__":
    test_contract_consumes_rescue_load_read_only_and_owns_bounded_decay()
    test_threshold_cap_latch_and_recovery_behavior()
    test_deterministic_three_year_horizon_stays_bounded_and_quiet_tail_recovers()
    test_quiet_upstream_does_not_manufacture_demand_after_latch_release()
    print("A1 Merchant salvage demand: PASS")
