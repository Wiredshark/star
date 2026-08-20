from pathlib import Path

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 free worlds geomagnetic storm.txt").read_text(encoding="utf-8")

CAP = 6
STORM_DAYS = 3
COOLDOWN_DAYS = 14
RECOVERY_DAYS = 2


def start_storm(active, cooldown):
    if active or cooldown:
        return active, cooldown, False
    return True, True, True


def add_strain(active, strain):
    if not active or strain >= CAP:
        return strain, False
    return min(CAP, strain + 1), True


def recover_strain(strain):
    return max(0, strain - 1)


def test_contract_and_trigger_hygiene():
    required = [
        'government "Free Worlds"',
        'set "world: free worlds geomagnetic storm active"',
        'set "world: free worlds geomagnetic storm cooldown"',
        'event "ES A1: Free Worlds Geomagnetic Storm Ends" 3 3',
        'event "ES A1: Free Worlds Geomagnetic Storm Cooldown Ends" 14 14',
        '"world: free worlds geomagnetic navigation strain" < 6',
        '"world: free worlds geomagnetic navigation strain" += 1',
        '"world: free worlds geomagnetic navigation strain" <?= 6',
        'event "ES A1: Free Worlds Navigation Strain Recovery" 2 2',
        '"world: free worlds geomagnetic navigation strain" >?= 0',
        '"world: free worlds geomagnetic navigation strain" >= 3',
        '"world: free worlds geomagnetic navigation strain" <= 1',
    ]
    for token in required:
        assert token in TEXT

    # All five entering missions must ignore takeoff so leaving a planet does not
    # manufacture a storm onset, exposure contribution, or advisory transition.
    assert TEXT.count('not "entered system by: takeoff"') == 5


def test_bounded_feedback_loop():
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
    assert (strain, scheduled_recoveries) == (CAP, CAP)

    for _ in range(scheduled_recoveries + 4):
        strain = recover_strain(strain)
    assert strain == 0

    active = False
    assert add_strain(active, strain) == (0, False)
    assert start_storm(active, cooldown) == (False, True, False)
    cooldown = False
    assert start_storm(active, cooldown) == (True, True, True)


def simulate(horizon):
    active_days = 0
    cooldown_days = 0
    strain = 0
    recoveries = []
    starts = 0
    trace = []

    for day in range(horizon):
        due = recoveries.count(day)
        for _ in range(due):
            strain = recover_strain(strain)
        recoveries = [scheduled for scheduled in recoveries if scheduled > day]

        # Representative qualifying system entry each day.
        if active_days == 0 and cooldown_days == 0:
            active_days = STORM_DAYS
            cooldown_days = COOLDOWN_DAYS
            starts += 1

        if active_days > 0:
            strain, added = add_strain(True, strain)
            if added:
                recoveries.append(day + RECOVERY_DAYS)

        active_days = max(0, active_days - 1)
        cooldown_days = max(0, cooldown_days - 1)
        assert 0 <= strain <= CAP
        trace.append((active_days, cooldown_days, strain))

    return trace, strain, recoveries, starts


def test_deterministic_three_year_horizon_is_bounded_and_quiet_tail_recovers():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    assert first[3] == second[3]
    assert first[3] >= 365 * 3 // 16

    _, strain, recoveries, _ = first
    day = 365 * 3
    while recoveries:
        due = recoveries.count(day)
        for _ in range(due):
            strain = recover_strain(strain)
        recoveries = [scheduled for scheduled in recoveries if scheduled > day]
        day += 1

    for _ in range(8):
        strain = recover_strain(strain)
    assert strain == 0
    assert recoveries == []


if __name__ == "__main__":
    test_contract_and_trigger_hygiene()
    test_bounded_feedback_loop()
    test_deterministic_three_year_horizon_is_bounded_and_quiet_tail_recovers()
    print("A1 Free Worlds geomagnetic-storm contract: PASS")
