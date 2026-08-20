from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRANSIT = ROOT / "data/human/a1 transit congestion.txt"
RELIEF = ROOT / "data/human/a1 relief demand.txt"
BRIDGE = ROOT / "data/human/a1 congestion relief spillover.txt"


def apply_spillover(relief_demand, transit_congestion, latch=False):
    if transit_congestion >= 4 and relief_demand < 5 and not latch:
        return min(5, relief_demand + 1), True
    return relief_demand, latch


def recover_relief(relief_demand):
    return max(0, relief_demand - 1)


def test_contract_reuses_authoritative_states_and_keeps_congestion_read_only():
    transit = TRANSIT.read_text(encoding="utf-8")
    relief = RELIEF.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert '"world: southern rim transit congestion" += 1' in transit
    assert '"world: free worlds relief demand" += 1' in relief
    for token in (
        '"world: southern rim transit congestion" >= 4',
        '"world: free worlds relief demand" < 5',
        'not "world: congestion relief spillover active"',
        'set "world: congestion relief spillover active"',
        '"world: free worlds relief demand" += 1',
        '"world: free worlds relief demand" <?= 5',
        'event "ES A1: Free Worlds Relief Demand Recovery" 4 4',
        'event "ES A1: Congestion Relief Spillover Latch Ends" 7 7',
        'clear "world: congestion relief spillover active"',
    ):
        assert token in bridge

    assert '"world: southern rim transit congestion" +=' not in bridge
    assert '"world: southern rim transit congestion" -=' not in bridge


def test_threshold_cap_and_latch_behavior():
    assert apply_spillover(0, 3, False) == (0, False)
    assert apply_spillover(0, 4, False) == (1, True)
    assert apply_spillover(4, 6, False) == (5, True)
    assert apply_spillover(5, 6, False) == (5, False)

    relief, latch = apply_spillover(1, 6, False)
    assert (relief, latch) == (2, True)
    assert apply_spillover(relief, 6, latch) == (2, True)
    assert apply_spillover(relief, 6, False) == (3, True)


def test_recovery_finishes_before_latch_reopens():
    relief, latch = apply_spillover(0, 6, False)
    assert (relief, latch) == (1, True)
    for _ in range(4):
        relief = recover_relief(relief)
    assert relief == 0
    # The bridge stays latched for seven days even though its downstream
    # contribution has already recovered at day four.
    assert apply_spillover(relief, 6, True) == (0, True)
    # Once congestion itself is below threshold, an expired latch cannot create
    # fresh demand.
    assert apply_spillover(relief, 2, False) == (0, False)


def test_deterministic_three_year_horizon_is_bounded_and_recovers():
    relief = 0
    latch_days = 0
    recovery_days = []

    for day in range(365 * 3):
        # Deterministic traffic seasons: 90 days severe congestion, 90 days quiet.
        congestion = 6 if day % 180 < 90 else 2
        # Representative qualifying border arrival every second day.
        if day % 2 == 0:
            relief, activated = apply_spillover(
                relief,
                congestion,
                latch=latch_days > 0,
            )
            if activated and latch_days == 0:
                latch_days = 7
                recovery_days.append(day + 4)

        # Each accepted spillover contribution schedules its own exact four-day
        # relief recovery. Execute all contributions due today.
        due = recovery_days.count(day)
        for _ in range(due):
            relief = recover_relief(relief)
        recovery_days = [scheduled for scheduled in recovery_days if scheduled > day]

        latch_days = max(0, latch_days - 1)
        assert 0 <= relief <= 5
        assert latch_days >= 0

    # Quiet tail: execute any pending contribution recoveries, then prove no
    # residual downstream pressure or latch survives.
    for day in range(365 * 3, 365 * 3 + 16):
        due = recovery_days.count(day)
        for _ in range(due):
            relief = recover_relief(relief)
        recovery_days = [scheduled for scheduled in recovery_days if scheduled > day]
        latch_days = max(0, latch_days - 1)

    assert relief == 0
    assert latch_days == 0
    assert recovery_days == []


if __name__ == "__main__":
    test_contract_reuses_authoritative_states_and_keeps_congestion_read_only()
    test_threshold_cap_and_latch_behavior()
    test_recovery_finishes_before_latch_reopens()
    test_deterministic_three_year_horizon_is_bounded_and_recovers()
    print("A1 Southern Rim congestion -> Free Worlds relief spillover: PASS")
