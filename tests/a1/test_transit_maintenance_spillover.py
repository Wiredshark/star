from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRANSIT = ROOT / "data/human/a1 transit congestion.txt"
MAINTENANCE = ROOT / "data/human/a1 syndicate maintenance backlog.txt"
BRIDGE = ROOT / "data/human/a1 transit maintenance spillover.txt"


def apply_spillover(backlog, congestion, latch=False):
    if congestion >= 4 and backlog < 6 and not latch:
        return min(6, backlog + 1), True
    return backlog, latch


def recover_backlog(backlog):
    return max(0, backlog - 1)


def test_contract_reuses_authoritative_states_and_keeps_congestion_read_only():
    transit = TRANSIT.read_text(encoding="utf-8")
    maintenance = MAINTENANCE.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")
    assert '"world: southern rim transit congestion" += 1' in transit
    assert '"world: syndicate maintenance backlog" += 1' in maintenance
    for token in (
        '"world: southern rim transit congestion" >= 4',
        '"world: syndicate maintenance backlog" < 6',
        'not "world: syndicate transit wear active"',
        'set "world: syndicate transit wear active"',
        '"world: syndicate maintenance backlog" += 1',
        '"world: syndicate maintenance backlog" <?= 6',
        'event "ES A1: Syndicate Maintenance Backlog Recovery" 7 7',
        'event "ES A1: Syndicate Transit Wear Latch Ends" 4 4',
        'clear "world: syndicate transit wear active"',
    ):
        assert token in bridge
    assert '"world: southern rim transit congestion" +=' not in bridge
    assert '"world: southern rim transit congestion" -=' not in bridge


def test_threshold_cap_and_latch_behavior():
    assert apply_spillover(0, 3, False) == (0, False)
    assert apply_spillover(0, 4, False) == (1, True)
    assert apply_spillover(5, 6, False) == (6, True)
    assert apply_spillover(6, 6, False) == (6, False)
    backlog, latch = apply_spillover(2, 6, False)
    assert (backlog, latch) == (3, True)
    assert apply_spillover(backlog, 6, latch) == (3, True)
    assert apply_spillover(backlog, 6, False) == (4, True)


def test_quiet_recovery_and_source_resolution():
    backlog, latch = apply_spillover(0, 5, False)
    assert (backlog, latch) == (1, True)
    backlog = recover_backlog(backlog)
    assert backlog == 0
    assert apply_spillover(backlog, 2, False) == (0, False)


def test_deterministic_three_year_horizon_is_bounded_and_drains():
    backlog = 0
    latch_days = 0
    recovery_days = []
    for day in range(365 * 3):
        congestion = 6 if day % 120 < 45 else 2
        if day % 3 == 0:
            before = backlog
            backlog, activated = apply_spillover(backlog, congestion, latch=latch_days > 0)
            if activated and backlog > before:
                latch_days = 4
                recovery_days.append(day + 7)
        due = recovery_days.count(day)
        for _ in range(due):
            backlog = recover_backlog(backlog)
        recovery_days = [scheduled for scheduled in recovery_days if scheduled != day]
        latch_days = max(0, latch_days - 1)
        assert 0 <= backlog <= 6
    for _ in range(12):
        backlog = recover_backlog(backlog)
    assert backlog == 0


if __name__ == "__main__":
    test_contract_reuses_authoritative_states_and_keeps_congestion_read_only()
    test_threshold_cap_and_latch_behavior()
    test_quiet_recovery_and_source_resolution()
    test_deterministic_three_year_horizon_is_bounded_and_drains()
    print("A1 transit congestion -> Syndicate maintenance spillover: PASS")
