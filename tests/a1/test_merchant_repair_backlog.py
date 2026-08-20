from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 merchant repair backlog.txt").read_text(encoding="utf-8")
CAP = 6


def escalate(backlog, rescue, active=False):
    if rescue < 3 or active or backlog >= CAP:
        return backlog, active, False
    return min(CAP, backlog + 2), True, True


def recover(backlog):
    return max(0, backlog - 1)


def surge(backlog, rescue, active=False):
    if backlog < 4 or rescue > 1 or active:
        return backlog, active, False
    return max(0, backlog - 2), True, True


def test_contract_upstream_ownership_and_trigger_hygiene():
    for token in (
        '"world: merchant rescue load" >= 3',
        '"world: merchant repair backlog" += 2',
        '"world: merchant repair backlog" <?= 6',
        'event "ES A1: Merchant Repair Backlog Recovery" 6 6',
        'event "ES A1: Merchant Repair Pressure Window Ends" 3 3',
        '"world: merchant rescue load" <= 1',
        '"world: merchant repair backlog" -= 2',
        'event "ES A1: Merchant Repair Surge Ends" 5 5',
    ):
        assert token in TEXT
    assert TEXT.count('not "entered system by: takeoff"') == 4
    assert not re.search(
        r'^\s*"world: merchant rescue load"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_threshold_cap_hysteresis_and_negative_feedback():
    assert escalate(0, 2) == (0, False, False)
    assert escalate(0, 3) == (2, True, True)
    assert escalate(5, 5) == (6, True, True)
    assert surge(4, 3) == (4, False, False)
    assert surge(4, 1) == (2, True, True)
    backlog = 2
    for _ in range(8):
        backlog = recover(backlog)
    assert backlog == 0


def simulate(days):
    backlog = 0
    pressure_days = 0
    surge_days = 0
    recoveries = []
    trace = []
    for day in range(days):
        for _ in range(recoveries.count(day)):
            backlog = recover(backlog)
        recoveries = [due for due in recoveries if due > day]

        rescue = 5 if day % 220 < 90 else 1
        if day % 2 == 0:
            backlog, _, fired = escalate(backlog, rescue, pressure_days > 0)
            if fired:
                pressure_days = 3
                recoveries.append(day + 6)
            backlog, _, fired = surge(backlog, rescue, surge_days > 0)
            if fired:
                surge_days = 5
        pressure_days = max(0, pressure_days - 1)
        surge_days = max(0, surge_days - 1)
        assert 0 <= backlog <= CAP
        trace.append((backlog, pressure_days, surge_days))
    return trace, backlog, recoveries


def test_deterministic_three_year_horizon_and_quiet_tail():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    backlog = first[1]
    for _ in range(16):
        backlog = recover(backlog)
    assert backlog == 0


if __name__ == "__main__":
    test_contract_upstream_ownership_and_trigger_hygiene()
    test_threshold_cap_hysteresis_and_negative_feedback()
    test_deterministic_three_year_horizon_and_quiet_tail()
    print("A1 Merchant repair-backlog contract: PASS")
