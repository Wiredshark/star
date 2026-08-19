from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RELIEF = ROOT / "data/human/a1 relief demand.txt"
TRANSIT = ROOT / "data/human/a1 transit congestion.txt"
BRIDGE = ROOT / "data/human/a1 free worlds relief transit load.txt"
DISPLACEMENT_BRIDGE = ROOT / "data/human/a1 republic displacement relief spillover.txt"


def apply_relief_transit(congestion, relief_demand, latch=False):
    if relief_demand >= 3 and congestion < 6 and not latch:
        return min(6, congestion + 1), True
    return congestion, latch


def recover_congestion(congestion):
    return max(0, congestion - 1)


def apply_displacement_spillover(relief_demand, displacement_pressure, latch=False):
    if displacement_pressure >= 4 and relief_demand < 5 and not latch:
        return min(5, relief_demand + 1), True
    return relief_demand, latch


def recover_relief(relief_demand):
    return max(0, relief_demand - 1)


def test_contract_reuses_authoritative_states_and_keeps_relief_read_only():
    relief = RELIEF.read_text(encoding="utf-8")
    transit = TRANSIT.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert 'event "ES A1: Free Worlds Relief Demand Recovery" 4 4' in relief
    assert 'event "ES A1: Southern Rim Transit Congestion Decay" 3 3' in transit
    for token in (
        '"world: free worlds relief demand" >= 3',
        'not "world: free worlds relief routing load"',
        'set "world: free worlds relief routing load"',
        '"world: southern rim transit congestion" += 1',
        '"world: southern rim transit congestion" <?= 6',
        'event "ES A1: Southern Rim Transit Congestion Decay" 3 3',
        'event "ES A1: Free Worlds Relief Routing Load Ends" 4 4',
        'clear "world: free worlds relief routing load"',
    ):
        assert token in bridge

    assert '"world: free worlds relief demand" +=' not in bridge
    assert '"world: free worlds relief demand" -=' not in bridge


def test_threshold_cap_and_latch_behavior():
    assert apply_relief_transit(0, 2, False) == (0, False)
    assert apply_relief_transit(0, 3, False) == (1, True)
    assert apply_relief_transit(5, 5, False) == (6, True)
    assert apply_relief_transit(6, 5, False) == (6, False)

    congestion, latch = apply_relief_transit(2, 5, False)
    assert (congestion, latch) == (3, True)
    assert apply_relief_transit(congestion, 5, latch) == (3, True)
    assert apply_relief_transit(congestion, 5, False) == (4, True)


def test_quiet_recovery_and_upstream_resolution():
    congestion, latch = apply_relief_transit(0, 5, False)
    assert (congestion, latch) == (1, True)
    for _ in range(3):
        congestion = recover_congestion(congestion)
    assert congestion == 0
    assert apply_relief_transit(congestion, 1, False) == (0, False)


def test_displacement_relief_transit_chain_is_bounded_and_recovers_for_three_years():
    assert '"world: republic displacement pressure" >= 4' in DISPLACEMENT_BRIDGE.read_text(encoding="utf-8")

    relief = 0
    congestion = 0
    displacement_latch_days = 0
    relief_routing_latch_days = 0

    for day in range(365 * 3):
        displacement = 6 if day % 180 < 75 else 2

        if day % 3 == 0:
            relief, activated = apply_displacement_spillover(
                relief,
                displacement,
                latch=displacement_latch_days > 0,
            )
            if activated and displacement_latch_days == 0:
                displacement_latch_days = 5

        if day % 2 == 0:
            congestion, activated = apply_relief_transit(
                congestion,
                relief,
                latch=relief_routing_latch_days > 0,
            )
            if activated and relief_routing_latch_days == 0:
                relief_routing_latch_days = 4

        if day % 4 == 3:
            relief = recover_relief(relief)
        if day % 3 == 2:
            congestion = recover_congestion(congestion)

        displacement_latch_days = max(0, displacement_latch_days - 1)
        relief_routing_latch_days = max(0, relief_routing_latch_days - 1)
        assert 0 <= relief <= 5
        assert 0 <= congestion <= 6

    for _ in range(8):
        relief = recover_relief(relief)
        congestion = recover_congestion(congestion)
    assert relief == 0
    assert congestion == 0


if __name__ == "__main__":
    test_contract_reuses_authoritative_states_and_keeps_relief_read_only()
    test_threshold_cap_and_latch_behavior()
    test_quiet_recovery_and_upstream_resolution()
    test_displacement_relief_transit_chain_is_bounded_and_recovers_for_three_years()
    print("A1 Free Worlds relief -> transit load feedback: PASS")
