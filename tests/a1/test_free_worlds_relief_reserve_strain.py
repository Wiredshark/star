from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 free worlds relief reserve strain.txt").read_text(encoding="utf-8")
CAP = 4


def arrive(strain, relief):
    if relief < 4 or strain >= CAP:
        return strain, False
    return min(CAP, strain + 1), True


def recover(strain):
    return max(0, strain - 1)


def test_contract_and_read_only_relief():
    for token in (
        '"world: free worlds relief demand" >= 4',
        '"world: free worlds relief reserve strain" < 4',
        '"world: free worlds relief reserve strain" += 1',
        '"world: free worlds relief reserve strain" <?= 4',
        'event "ES A1: Free Worlds Relief Reserve Recovery" 6 6',
        '"world: free worlds relief reserve strain" >= 3',
    ):
        assert token in TEXT
    assert TEXT.count('not "entered system by: takeoff"') == 2
    assert not re.search(
        r'^\s*"world: free worlds relief demand"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_threshold_cap_and_recovery():
    assert arrive(0, 3) == (0, False)
    strain = 0
    accepted = 0
    for _ in range(8):
        strain, added = arrive(strain, 5)
        accepted += int(added)
    assert (strain, accepted) == (CAP, CAP)
    for _ in range(accepted + 3):
        strain = recover(strain)
    assert strain == 0


def simulate(days):
    strain = 0
    recoveries = []
    trace = []
    for day in range(days):
        for _ in range(recoveries.count(day)):
            strain = recover(strain)
        recoveries = [due for due in recoveries if due > day]

        relief = 5 if day % 180 < 70 else 1
        if day % 2 == 0:
            strain, added = arrive(strain, relief)
            if added:
                recoveries.append(day + 6)
        assert 0 <= strain <= CAP
        trace.append(strain)
    return trace, strain, recoveries


def test_deterministic_three_year_horizon_and_quiet_tail():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    strain = first[1]
    recoveries = list(first[2])
    day = 365 * 3
    while recoveries:
        for _ in range(recoveries.count(day)):
            strain = recover(strain)
        recoveries = [due for due in recoveries if due > day]
        day += 1
    for _ in range(8):
        strain = recover(strain)
    assert strain == 0


if __name__ == "__main__":
    test_contract_and_read_only_relief()
    test_threshold_cap_and_recovery()
    test_deterministic_three_year_horizon_and_quiet_tail()
    print("A1 Free Worlds relief-reserve strain contract: PASS")
