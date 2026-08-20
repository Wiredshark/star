from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 republic displacement transit load.txt").read_text(encoding="utf-8")
CAP = 6


def crossing(congestion, displacement, latched=False):
    if displacement < 4 or latched or congestion >= CAP:
        return congestion, latched, False
    return min(CAP, congestion + 1), True, True


def decay(congestion):
    return max(0, congestion - 1)


def test_contract_and_displacement_read_only():
    for token in (
        'has "previous system government: Republic"',
        '"world: republic displacement pressure" >= 4',
        'not "world: republic displacement routing load"',
        '"world: southern rim transit congestion" += 1',
        '"world: southern rim transit congestion" <?= 6',
        'event "ES A1: Southern Rim Transit Congestion Decay" 3 3',
        'event "ES A1: Republic Displacement Routing Load Ends" 4 4',
    ):
        assert token in TEXT
    assert 'not "entered system by: takeoff"' in TEXT
    assert not re.search(
        r'^\s*"world: republic displacement pressure"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_threshold_latch_cap_and_recovery():
    assert crossing(2, 3) == (2, False, False)
    assert crossing(2, 4) == (3, True, True)
    assert crossing(3, 6, True) == (3, True, False)
    assert crossing(5, 6) == (6, True, True)
    assert crossing(6, 6) == (6, False, False)
    congestion = 6
    for _ in range(10):
        congestion = decay(congestion)
    assert congestion == 0


def simulate(days):
    congestion = 0
    latch = 0
    recoveries = []
    trace = []
    for day in range(days):
        for _ in range(recoveries.count(day)):
            congestion = decay(congestion)
        recoveries = [due for due in recoveries if due > day]

        displacement = 5 if day % 210 < 80 else 1
        if day % 2 == 0:
            congestion, activated, added = crossing(congestion, displacement, latch > 0)
            if added and latch == 0:
                latch = 4
                recoveries.append(day + 3)
        latch = max(0, latch - 1)
        assert 0 <= congestion <= CAP
        trace.append((congestion, latch))
    return trace, congestion, recoveries


def test_deterministic_three_year_horizon_and_quiet_tail():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    congestion = first[1]
    recoveries = list(first[2])
    day = 365 * 3
    while recoveries:
        for _ in range(recoveries.count(day)):
            congestion = decay(congestion)
        recoveries = [due for due in recoveries if due > day]
        day += 1
    for _ in range(10):
        congestion = decay(congestion)
    assert congestion == 0


if __name__ == "__main__":
    test_contract_and_displacement_read_only()
    test_threshold_latch_cap_and_recovery()
    test_deterministic_three_year_horizon_and_quiet_tail()
    print("A1 Republic displacement-transit load contract: PASS")
