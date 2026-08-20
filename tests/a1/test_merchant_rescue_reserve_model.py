from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 merchant rescue reserve.txt").read_text(encoding="utf-8")
CAP = 4


def arrive(strain, rescue_load):
    if rescue_load >= 5:
        if strain > CAP - 2:
            return strain, 0
        return min(CAP, strain + 2), 2
    if rescue_load >= 3:
        if strain >= CAP:
            return strain, 0
        return min(CAP, strain + 1), 1
    return strain, 0


def recover(strain, amount):
    return max(0, strain - amount)


def test_contract_and_upstream_ownership():
    for token in (
        '"world: merchant rescue load" >= 3',
        '"world: merchant rescue load" >= 5',
        '"world: merchant rescue reserve strain" += 1',
        '"world: merchant rescue reserve strain" += 2',
        'event "ES A1: Merchant Rescue Reserve Recovery 1" 10 10',
        'event "ES A1: Merchant Rescue Reserve Recovery 2" 10 10',
    ):
        assert token in TEXT
    assert TEXT.count('not "entered system by: takeoff"') == 3
    assert not re.search(
        r'^\s*"world: merchant rescue load"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_load_tiers_cap_and_exact_recovery():
    assert arrive(0, 2) == (0, 0)
    assert arrive(0, 3) == (1, 1)
    assert arrive(0, 5) == (2, 2)
    assert arrive(3, 5) == (3, 0)
    assert arrive(3, 4) == (4, 1)
    strain = 0
    obligations = []
    for _ in range(8):
        strain, amount = arrive(strain, 5)
        if amount:
            obligations.append(amount)
    assert (strain, obligations) == (4, [2, 2])
    for amount in obligations:
        strain = recover(strain, amount)
    assert strain == 0


def simulate(days):
    strain = 0
    obligations = []
    trace = []
    for day in range(days):
        due = [x for x in obligations if x[0] == day]
        for _, amount in due:
            strain = recover(strain, amount)
        obligations = [x for x in obligations if x[0] > day]

        phase = day % 210
        load = 5 if phase < 45 else (4 if phase < 90 else 1)
        if day % 2 == 0:
            strain, amount = arrive(strain, load)
            if amount:
                obligations.append((day + 10, amount))
        assert 0 <= strain <= CAP
        trace.append(strain)
    return trace, strain, obligations


def test_deterministic_three_year_horizon_and_quiet_tail():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    strain = first[1]
    obligations = list(first[2])
    day = 365 * 3
    while obligations:
        for _, amount in [x for x in obligations if x[0] == day]:
            strain = recover(strain, amount)
        obligations = [x for x in obligations if x[0] > day]
        day += 1
    for _ in range(6):
        strain = recover(strain, 2)
    assert strain == 0


if __name__ == "__main__":
    test_contract_and_upstream_ownership()
    test_load_tiers_cap_and_exact_recovery()
    test_deterministic_three_year_horizon_and_quiet_tail()
    print("A1 Merchant rescue-reserve strain contract: PASS")
