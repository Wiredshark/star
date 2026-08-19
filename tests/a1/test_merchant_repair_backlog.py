from pathlib import Path

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 merchant repair backlog.txt").read_text()

CAP = 6


def escalate(backlog, rescue_load, pressure_active):
    if rescue_load < 3 or pressure_active or backlog >= CAP:
        return backlog, pressure_active, False
    return min(CAP, backlog + 2), True, True


def recover(backlog):
    return max(0, backlog - 1)


def surge(backlog, rescue_load, surge_active):
    if backlog < 4 or rescue_load > 1 or surge_active:
        return backlog, surge_active, False
    return max(0, backlog - 2), True, True


def test_contract_tokens():
    required = [
        'mission "ES A1: Merchant Repair Backlog Escalation"',
        '"world: merchant rescue load" >= 3',
        'set "world: merchant repair pressure active"',
        '"world: merchant repair backlog" += 2',
        '"world: merchant repair backlog" <?= 6',
        'event "ES A1: Merchant Repair Backlog Recovery" 6 6',
        'event "ES A1: Merchant Repair Pressure Window Ends" 3 3',
        'mission "ES A1: Merchant Repair Surge"',
        '"world: merchant rescue load" <= 1',
        '"world: merchant repair backlog" -= 2',
        'event "ES A1: Merchant Repair Surge Ends" 5 5',
    ]
    for token in required:
        assert token in TEXT


def test_escalation_cap_and_source_threshold():
    assert escalate(0, 2, False) == (0, False, False)
    assert escalate(0, 3, False) == (2, True, True)
    assert escalate(5, 5, False) == (6, True, True)
    assert escalate(6, 5, False) == (6, False, False)
    assert escalate(2, 5, True) == (2, True, False)


def test_repair_surge_waits_for_rescue_recovery():
    assert surge(4, 3, False) == (4, False, False)
    assert surge(4, 2, False) == (4, False, False)
    assert surge(4, 1, False) == (2, True, True)
    assert surge(6, 0, True) == (6, True, False)
    assert surge(3, 0, False) == (3, False, False)


def test_recovery_never_goes_negative():
    value = 2
    for _ in range(10):
        value = recover(value)
    assert value == 0


def test_deterministic_year_horizon_is_bounded_and_converges():
    backlog = 0
    pressure_days = 0
    surge_days = 0
    for day in range(365):
        # Sustained rescue crisis for 180 days, then durable recovery.
        rescue_load = 4 if day < 180 else 1
        pressure_active = pressure_days > 0
        backlog, _, fired = escalate(backlog, rescue_load, pressure_active)
        if fired:
            pressure_days = 3

        if backlog >= 4 and surge_days == 0:
            backlog, _, surge_fired = surge(backlog, rescue_load, False)
            if surge_fired:
                surge_days = 5

        if day % 6 == 5:
            backlog = recover(backlog)

        pressure_days = max(0, pressure_days - 1)
        surge_days = max(0, surge_days - 1)
        assert 0 <= backlog <= CAP
        if day < 180:
            assert surge_days == 0

    assert backlog == 0


if __name__ == "__main__":
    test_contract_tokens()
    test_escalation_cap_and_source_threshold()
    test_repair_surge_waits_for_rescue_recovery()
    test_recovery_never_goes_negative()
    test_deterministic_year_horizon_is_bounded_and_converges()
    print("A1 Merchant repair-backlog hysteresis contract: PASS")
