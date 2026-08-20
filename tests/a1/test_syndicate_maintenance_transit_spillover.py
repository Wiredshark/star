from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAINTENANCE = ROOT / "data/human/a1 syndicate maintenance backlog.txt"
CONGESTION = ROOT / "data/human/a1 transit congestion.txt"
BRIDGE = ROOT / "data/human/a1 syndicate maintenance transit spillover.txt"


def apply_spillover(congestion, maintenance_backlog, latch=False):
    if maintenance_backlog >= 4 and congestion < 6 and not latch:
        return min(6, congestion + 1), True
    return congestion, latch


def recover_congestion(congestion):
    return max(0, congestion - 1)


def test_contract_reuses_authoritative_states_and_keeps_upstream_read_only():
    maintenance = MAINTENANCE.read_text(encoding="utf-8")
    congestion = CONGESTION.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert '"world: syndicate maintenance backlog" += 1' in maintenance
    assert '"world: southern rim transit congestion" += 1' in congestion
    for token in (
        '"world: syndicate maintenance backlog" >= 4',
        '"world: southern rim transit congestion" < 6',
        'not "world: syndicate maintenance transit spillover active"',
        'set "world: syndicate maintenance transit spillover active"',
        '"world: southern rim transit congestion" += 1',
        '"world: southern rim transit congestion" <?= 6',
        'event "ES A1: Southern Rim Transit Congestion Decay" 3 3',
        'event "ES A1: Syndicate Maintenance Transit Spillover Latch Ends" 6 6',
        'clear "world: syndicate maintenance transit spillover active"',
    ):
        assert token in bridge

    assert '"world: syndicate maintenance backlog" +=' not in bridge
    assert '"world: syndicate maintenance backlog" -=' not in bridge


def test_threshold_cap_and_latch_behavior():
    assert apply_spillover(0, 3, False) == (0, False)
    assert apply_spillover(0, 4, False) == (1, True)
    assert apply_spillover(5, 6, False) == (6, True)
    assert apply_spillover(6, 6, False) == (6, False)

    congestion, latch = apply_spillover(2, 5, False)
    assert (congestion, latch) == (3, True)
    assert apply_spillover(congestion, 5, latch) == (3, True)


def test_quiet_recovery_and_source_resolution():
    congestion, latch = apply_spillover(0, 6, False)
    assert (congestion, latch) == (1, True)
    for _ in range(3):
        congestion = recover_congestion(congestion)
    assert congestion == 0
    assert apply_spillover(congestion, 2, False) == (0, False)


def test_deterministic_three_year_horizon_is_bounded_and_drains():
    congestion = 0
    latch_days = 0
    for day in range(365 * 3):
        maintenance = 6 if day % 210 < 84 else 2
        if day % 2 == 0:
            congestion, activated = apply_spillover(
                congestion,
                maintenance,
                latch=latch_days > 0,
            )
            if activated and latch_days == 0:
                latch_days = 6
        if day % 3 == 2:
            congestion = recover_congestion(congestion)
        latch_days = max(0, latch_days - 1)
        assert 0 <= congestion <= 6

    for _ in range(12):
        congestion = recover_congestion(congestion)
    assert congestion == 0


if __name__ == "__main__":
    test_contract_reuses_authoritative_states_and_keeps_upstream_read_only()
    test_threshold_cap_and_latch_behavior()
    test_quiet_recovery_and_source_resolution()
    test_deterministic_three_year_horizon_is_bounded_and_drains()
    print("A1 Syndicate maintenance -> Southern Rim transit spillover: PASS")
