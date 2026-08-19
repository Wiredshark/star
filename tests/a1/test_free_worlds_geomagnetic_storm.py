from pathlib import Path

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 free worlds geomagnetic storm.txt").read_text()


def start_storm(active, cooldown):
    if active or cooldown:
        return active, cooldown, False
    return True, True, True


def add_strain(active, strain):
    if not active or strain >= 6:
        return strain, False
    return min(6, strain + 1), True


def recover_strain(strain):
    return max(0, strain - 1)


def test_contract_and_bounded_feedback_loop():
    required = [
        'government "Free Worlds"',
        'set "world: free worlds geomagnetic storm active"',
        'set "world: free worlds geomagnetic storm cooldown"',
        'event "ES A1: Free Worlds Geomagnetic Storm Ends" 3 3',
        'event "ES A1: Free Worlds Geomagnetic Storm Cooldown Ends" 14 14',
        '"world: free worlds geomagnetic navigation strain" < 6',
        '"world: free worlds geomagnetic navigation strain" += 1',
        'event "ES A1: Free Worlds Navigation Strain Recovery" 2 2',
        '"world: free worlds geomagnetic navigation strain" >?= 0',
        '"world: free worlds geomagnetic navigation strain" >= 3',
        '"world: free worlds geomagnetic navigation strain" <= 1',
    ]
    for token in required:
        assert token in TEXT

    active = False
    cooldown = False
    active, cooldown, started = start_storm(active, cooldown)
    assert (active, cooldown, started) == (True, True, True)
    assert start_storm(active, cooldown) == (True, True, False)

    strain = 0
    scheduled_recoveries = 0
    for _ in range(10):
        strain, added = add_strain(active, strain)
        scheduled_recoveries += int(added)
    assert (strain, scheduled_recoveries) == (6, 6)

    for _ in range(scheduled_recoveries + 4):
        strain = recover_strain(strain)
    assert strain == 0

    active = False
    assert add_strain(active, strain) == (0, False)
    assert start_storm(active, cooldown) == (False, True, False)
    cooldown = False
    assert start_storm(active, cooldown) == (True, True, True)


def test_deterministic_short_medium_long_horizons():
    # Model one system entry per day. A storm lasts three days, then a fourteen-day
    # onset cooldown prevents immediate retriggering. Each storm entry schedules a
    # two-day strain recovery, keeping the derived pressure bounded and convergent.
    for horizon in (30, 180, 720):
        active_days = 0
        cooldown_days = 0
        strain = 0
        recoveries = []
        peak = 0
        starts = 0
        for day in range(horizon):
            due = recoveries.count(day)
            for _ in range(due):
                strain = recover_strain(strain)

            if active_days == 0 and cooldown_days == 0:
                active_days = 3
                cooldown_days = 14
                starts += 1

            if active_days > 0:
                strain, added = add_strain(True, strain)
                if added:
                    recoveries.append(day + 2)
                active_days -= 1

            if cooldown_days > 0:
                cooldown_days -= 1
            peak = max(peak, strain)

        assert 0 <= strain <= 6
        assert peak <= 6
        assert starts >= max(1, horizon // 16)


if __name__ == "__main__":
    test_contract_and_bounded_feedback_loop()
    test_deterministic_short_medium_long_horizons()
    print("A1 Free Worlds geomagnetic-storm contract: PASS")
