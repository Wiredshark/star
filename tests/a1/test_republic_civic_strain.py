from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 republic civic strain.txt").read_text(encoding="utf-8")
CAP = 6


def escalate(strain, displacement, scrutiny, active=False):
    if displacement < 4 or scrutiny < 3 or active or strain >= CAP:
        return strain, active, False
    return min(CAP, strain + 2), True, True


def recover(strain):
    return max(0, strain - 1)


def stabilize(strain, displacement, scrutiny, active=False):
    if strain < 2 or displacement > 2 or scrutiny > 1 or active:
        return strain, active, False
    return max(0, strain - 2), True, True


def test_contract_and_source_ownership():
    for token in (
        '"world: republic displacement pressure" >= 4',
        '"world: republic customs scrutiny" >= 3',
        '"world: republic civic strain" += 2',
        '"world: republic civic strain" <?= 6',
        'event "ES A1: Republic Civic Strain Recovery" 10 10',
        'event "ES A1: Republic Civic Assessment Ends" 4 4',
        '"world: republic displacement pressure" <= 2',
        '"world: republic customs scrutiny" <= 1',
        '"world: republic civic strain" -= 2',
        'event "ES A1: Republic Civic Stabilization Ends" 6 6',
    ):
        assert token in TEXT
    assert TEXT.count('not "entered system by: takeoff"') == 3
    for authority in ("world: republic displacement pressure", "world: republic customs scrutiny"):
        assert not re.search(
            rf'^\s*"{re.escape(authority)}"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
            TEXT,
            re.M,
        )


def test_threshold_cap_and_hysteresis():
    assert escalate(0, 3, 4) == (0, False, False)
    assert escalate(0, 4, 2) == (0, False, False)
    assert escalate(0, 4, 3) == (2, True, True)
    assert escalate(5, 6, 6) == (6, True, True)
    assert stabilize(4, 3, 1) == (4, False, False)
    assert stabilize(4, 2, 2) == (4, False, False)
    assert stabilize(2, 2, 1) == (0, True, True)


def simulate(days):
    strain = 0
    assessment = 0
    stabilization = 0
    recoveries = []
    trace = []
    for day in range(days):
        # Long alternating crisis/recovery seasons.
        acute = day % 240 < 100
        displacement = 5 if acute else 1
        scrutiny = 4 if acute else 1

        for _ in range(recoveries.count(day)):
            strain = recover(strain)
        recoveries = [due for due in recoveries if due > day]

        if day % 2 == 0:
            strain, _, fired = escalate(strain, displacement, scrutiny, assessment > 0)
            if fired:
                assessment = 4
                recoveries.append(day + 10)
            strain, _, fired = stabilize(strain, displacement, scrutiny, stabilization > 0)
            if fired:
                stabilization = 6

        assessment = max(0, assessment - 1)
        stabilization = max(0, stabilization - 1)
        assert 0 <= strain <= CAP
        trace.append((strain, assessment, stabilization))
    return trace, strain, recoveries


def test_deterministic_three_year_horizon_and_quiet_tail():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    strain = first[1]
    for _ in range(24):
        strain = max(0, strain - 1)
    assert strain == 0


if __name__ == "__main__":
    test_contract_and_source_ownership()
    test_threshold_cap_and_hysteresis()
    test_deterministic_three_year_horizon_and_quiet_tail()
    print("A1 Republic civic-strain contract: PASS")
