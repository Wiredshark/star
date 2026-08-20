from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/bunrodea/a1 bunrodea freight review backlog.txt").read_text(encoding="utf-8")
CAP = 6


def arrive(backlog, cross_border=True):
    if not cross_border or backlog >= CAP:
        return backlog, False
    return min(CAP, backlog + 1), True


def recover(backlog):
    return max(0, backlog - 1)


def test_contract_and_narrative_boundary():
    for token in (
        'mission "ES A1: Bunrodea Freight Review Intake"',
        'government "Bunrodea"',
        'not "entered system by: takeoff"',
        'not "previous system government: Bunrodea"',
        '"world: bunrodea freight review backlog" < 6',
        '"world: bunrodea freight review backlog" += 1',
        '"world: bunrodea freight review backlog" <?= 6',
        'event "ES A1: Bunrodea Freight Review Backlog Decay" 4 4',
        '"world: bunrodea freight review backlog" >= 4',
    ):
        assert token in TEXT
    assert not re.search(
        r'^\s*"B2 Bunrodea Freight Petition Compact:[^"]*"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_cross_border_threshold_cap_and_recovery():
    assert arrive(0, cross_border=False) == (0, False)
    backlog = 0
    accepted = 0
    for _ in range(12):
        backlog, added = arrive(backlog)
        accepted += int(added)
    assert (backlog, accepted) == (CAP, CAP)
    for _ in range(accepted + 4):
        backlog = recover(backlog)
    assert backlog == 0


def simulate(days):
    backlog = 0
    recoveries = []
    trace = []
    for day in range(days):
        for _ in range(recoveries.count(day)):
            backlog = recover(backlog)
        recoveries = [due for due in recoveries if due > day]

        # Deterministic cross-border trade seasons alternating with domestic-only movement.
        cross_border = day % 120 < 50
        if day % 2 == 0:
            backlog, added = arrive(backlog, cross_border)
            if added:
                recoveries.append(day + 4)
        assert 0 <= backlog <= CAP
        trace.append(backlog)
    return trace, backlog, recoveries


def test_deterministic_three_year_horizon_and_quiet_tail():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    backlog = first[1]
    recoveries = list(first[2])
    day = 365 * 3
    while recoveries:
        for _ in range(recoveries.count(day)):
            backlog = recover(backlog)
        recoveries = [due for due in recoveries if due > day]
        day += 1
    for _ in range(8):
        backlog = recover(backlog)
    assert backlog == 0


if __name__ == "__main__":
    test_contract_and_narrative_boundary()
    test_cross_border_threshold_cap_and_recovery()
    test_deterministic_three_year_horizon_and_quiet_tail()
    print("A1 Bunrodea freight-review backlog contract: PASS")
