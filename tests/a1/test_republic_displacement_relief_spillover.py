from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DISPLACEMENT = ROOT / "data/human/a1 republic displacement pressure.txt"
RELIEF = ROOT / "data/human/a1 relief demand.txt"
BRIDGE = ROOT / "data/human/a1 republic displacement relief spillover.txt"


def apply_spillover(relief_demand, displacement_pressure, latch=False):
    if displacement_pressure >= 4 and relief_demand < 5 and not latch:
        return min(5, relief_demand + 1), True
    return relief_demand, latch


def recover_relief(relief_demand):
    return max(0, relief_demand - 1)


def test_contract_reuses_authoritative_states_without_mutating_displacement():
    displacement = DISPLACEMENT.read_text(encoding="utf-8")
    relief = RELIEF.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert '"world: republic displacement pressure" += 2' in displacement
    assert '"world: free worlds relief demand" += 1' in relief
    for token in (
        '"world: republic displacement pressure" >= 4',
        '"world: free worlds relief demand" < 5',
        'not "world: republic displacement relief spillover active"',
        'set "world: republic displacement relief spillover active"',
        '"world: free worlds relief demand" += 1',
        '"world: free worlds relief demand" <?= 5',
        'event "ES A1: Free Worlds Relief Demand Recovery" 4 4',
        'event "ES A1: Republic Displacement Relief Spillover Latch Ends" 5 5',
        'clear "world: republic displacement relief spillover active"',
    ):
        assert token in bridge

    # The bridge consumes displacement as a read-only upstream signal.
    assert '"world: republic displacement pressure" +=' not in bridge
    assert '"world: republic displacement pressure" -=' not in bridge


def test_threshold_cap_and_latch_behavior():
    assert apply_spillover(0, 3, False) == (0, False)
    assert apply_spillover(0, 4, False) == (1, True)
    assert apply_spillover(4, 6, False) == (5, True)
    assert apply_spillover(5, 6, False) == (5, False)

    relief, latch = apply_spillover(1, 6, False)
    assert (relief, latch) == (2, True)
    assert apply_spillover(relief, 6, latch) == (2, True)
    assert apply_spillover(relief, 6, False) == (3, True)


def test_quiet_recovery_and_source_resolution():
    relief, latch = apply_spillover(0, 6, False)
    assert (relief, latch) == (1, True)
    # The accepted relief recovery owns decay of the spillover contribution.
    for _ in range(4):
        relief = recover_relief(relief)
    assert relief == 0
    # Once the upstream source recovers below threshold, a released latch does
    # not manufacture fresh downstream demand.
    assert apply_spillover(relief, 2, False) == (0, False)


def test_deterministic_three_year_horizon_is_bounded_and_recovers():
    relief = 0
    latch_days = 0
    for day in range(365 * 3):
        # Deterministic stress seasons: 75 days acute displacement, 105 quiet.
        displacement = 6 if day % 180 < 75 else 2
        # Representative qualifying Free Worlds arrival every third day.
        if day % 3 == 0:
            relief, activated = apply_spillover(
                relief,
                displacement,
                latch=latch_days > 0,
            )
            if activated and latch_days == 0:
                latch_days = 5
        # Model the contribution's accepted four-day recovery horizon.
        if day % 4 == 3:
            relief = recover_relief(relief)
        latch_days = max(0, latch_days - 1)
        assert 0 <= relief <= 5

    # A quiet tail must drain all downstream pressure deterministically.
    for _ in range(8):
        relief = recover_relief(relief)
    assert relief == 0


if __name__ == "__main__":
    test_contract_reuses_authoritative_states_without_mutating_displacement()
    test_threshold_cap_and_latch_behavior()
    test_quiet_recovery_and_source_resolution()
    test_deterministic_three_year_horizon_is_bounded_and_recovers()
    print("A1 Republic displacement -> Free Worlds relief spillover: PASS")
