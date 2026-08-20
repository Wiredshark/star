from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 republic inspection backlog.txt").read_text(encoding="utf-8")
CAP = 6


def accrue(backlog, scrutiny):
    if scrutiny < 3 or backlog >= CAP:
        return backlog, False
    return min(CAP, backlog + 1), True


def recover(backlog):
    return max(0, backlog - 1)


def surge(backlog, active=False):
    if active or backlog < 4:
        return backlog, active, False
    return max(0, backlog - 3), True, True


def test_contract_and_customs_read_only():
    for token in (
        '"world: republic customs scrutiny" >= 3',
        '"world: republic inspection backlog" < 6',
        '"world: republic inspection backlog" += 1',
        'event "ES A1: Republic Inspection Backlog Recovery" 6 6',
        '"world: republic inspection backlog" >= 4',
        '"world: republic inspection backlog" -= 3',
        'event "ES A1: Republic Inspection Surge Ends" 5 5',
    ):
        assert token in TEXT
    assert TEXT.count('not "entered system by: takeoff"') == 4
    assert not re.search(
        r'^\s*"world: republic customs scrutiny"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_threshold_cap_recovery_and_surge():
    assert accrue(0, 2) == (0, False)
    backlog = 0
    accepted = 0
    for _ in range(10):
        backlog, added = accrue(backlog, 5)
        accepted += int(added)
    assert (backlog, accepted) == (CAP, CAP)
    backlog, active, fired = surge(4)
    assert (backlog, active, fired) == (1, True, True)
    assert surge(6, active=True) == (6, True, False)
    for _ in range(10):
        backlog = recover(backlog)
    assert backlog == 0


def simulate(days):
    backlog = 0
    surge_days = 0
    recoveries = []
    trace = []
    for day in range(days):
        for _ in range(recoveries.count(day)):
            backlog = recover(backlog)
        recoveries = [due for due in recoveries if due > day]

        scrutiny = 5 if day % 200 < 80 else 1
        if day % 2 == 0:
            backlog, added = accrue(backlog, scrutiny)
            if added:
                recoveries.append(day + 6)
            backlog, _, fired = surge(backlog, surge_days > 0)
            if fired:
                surge_days = 5
        surge_days = max(0, surge_days - 1)
        assert 0 <= backlog <= CAP
        trace.append((backlog, surge_days))
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
    test_contract_and_customs_read_only()
    test_threshold_cap_recovery_and_surge()
    test_deterministic_three_year_horizon_and_quiet_tail()
    print("A1 Republic inspection-backlog contract: PASS")
