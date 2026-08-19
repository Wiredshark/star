from pathlib import Path

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 republic displacement pressure.txt").read_text()


def escalate(displacement, border_pressure, active):
    if border_pressure < 4 or active or displacement >= 6:
        return displacement, active, False
    return min(6, displacement + 2), True, True


def recover(displacement):
    return max(0, displacement - 1)


def resettle(displacement, surge):
    if displacement < 4 or surge:
        return displacement, surge, False
    return max(0, displacement - 2), True, True


def test_contract_tokens():
    required = [
        '"world: republic border pressure" >= 4',
        '"world: republic displacement pressure" += 2',
        '"world: republic displacement pressure" <?= 6',
        'event "ES A1: Republic Displacement Recovery" 8 8',
        'event "ES A1: Republic Displacement Response Ends" 4 4',
        'set "world: republic resettlement surge"',
        '"world: republic displacement pressure" -= 2',
        'event "ES A1: Republic Resettlement Surge Ends" 6 6',
    ]
    for token in required:
        assert token in TEXT


def test_thresholds_caps_and_recovery():
    value, active, fired = escalate(0, 3, False)
    assert (value, active, fired) == (0, False, False)
    value, active, fired = escalate(5, 4, False)
    assert (value, active, fired) == (6, True, True)
    assert escalate(value, 6, True) == (6, True, False)
    for _ in range(9):
        value = recover(value)
    assert value == 0


def test_resettlement_feedback_consumes_backlog():
    value, active, _ = escalate(0, 4, False)
    active = False
    value, active, _ = escalate(value, 5, active)
    assert value == 4
    value, surge, fired = resettle(value, False)
    assert (value, surge, fired) == (2, True, True)
    assert resettle(6, True) == (6, True, False)
    assert resettle(3, False) == (3, False, False)


def test_deterministic_long_horizon_is_bounded():
    value = 0
    active_days = 0
    surge_days = 0
    for day in range(365):
        border_pressure = 4 if day % 11 < 5 else 2
        active = active_days > 0
        value, _, fired = escalate(value, border_pressure, active)
        if fired:
            active_days = 4
        if value >= 4 and surge_days == 0:
            value, _, surge_fired = resettle(value, False)
            if surge_fired:
                surge_days = 6
        if day % 8 == 7:
            value = recover(value)
        active_days = max(0, active_days - 1)
        surge_days = max(0, surge_days - 1)
        assert 0 <= value <= 6
    assert 0 <= value <= 6


if __name__ == "__main__":
    test_contract_tokens()
    test_thresholds_caps_and_recovery()
    test_resettlement_feedback_consumes_backlog()
    test_deterministic_long_horizon_is_bounded()
    print("A1 Republic displacement-pressure contract: PASS")
