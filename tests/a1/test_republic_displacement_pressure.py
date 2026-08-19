from pathlib import Path

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 republic displacement pressure.txt").read_text()


def escalate(displacement, border_pressure, active):
    if border_pressure < 4 or active or displacement >= 6:
        return displacement, active, False
    return min(6, displacement + 2), True, True


def recover(displacement):
    return max(0, displacement - 1)


def resettle(displacement, border_pressure, surge):
    if displacement < 4 or border_pressure > 2 or surge:
        return displacement, surge, False
    return max(0, displacement - 2), True, True


def test_contract_tokens():
    required = [
        '"world: republic border pressure" >= 4',
        '"world: republic displacement pressure" += 2',
        '"world: republic displacement pressure" <?= 6',
        'event "ES A1: Republic Displacement Recovery" 8 8',
        'event "ES A1: Republic Displacement Response Ends" 4 4',
        '"world: republic border pressure" <= 2',
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


def test_resettlement_waits_for_source_pressure_to_recede():
    value = 4
    assert resettle(value, 4, False) == (4, False, False)
    assert resettle(value, 3, False) == (4, False, False)
    value, surge, fired = resettle(value, 2, False)
    assert (value, surge, fired) == (2, True, True)
    assert resettle(6, 0, True) == (6, True, False)
    assert resettle(3, 0, False) == (3, False, False)


def test_deterministic_long_horizon_is_bounded_and_converges_after_crisis():
    value = 0
    active_days = 0
    surge_days = 0
    for day in range(365):
        # 180-day sustained crisis, then a durable low-pressure recovery period.
        border_pressure = 5 if day < 180 else 1
        active = active_days > 0
        value, _, fired = escalate(value, border_pressure, active)
        if fired:
            active_days = 4
        if value >= 4 and surge_days == 0:
            value, _, surge_fired = resettle(value, border_pressure, False)
            if surge_fired:
                surge_days = 6
        if day % 8 == 7:
            value = recover(value)
        active_days = max(0, active_days - 1)
        surge_days = max(0, surge_days - 1)
        assert 0 <= value <= 6
        if day < 180 and border_pressure >= 4:
            # Acute source pressure blocks the fast recovery path.
            assert not (surge_days > 0)
    assert value == 0


if __name__ == "__main__":
    test_contract_tokens()
    test_thresholds_caps_and_recovery()
    test_resettlement_waits_for_source_pressure_to_recede()
    test_deterministic_long_horizon_is_bounded_and_converges_after_crisis()
    print("A1 Republic displacement-pressure hysteresis contract: PASS")
