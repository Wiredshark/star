from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 merchant route diversion.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 6
HIGH = 3
LOW = 1
RECOVERY_AT = 4


def arrival(pressure, rescue_load, congestion):
    if rescue_load >= HIGH and congestion >= HIGH:
        if pressure > CAP - 2:
            return pressure, 0
        return pressure + 2, 2
    if rescue_load >= HIGH or congestion >= HIGH:
        if pressure >= CAP:
            return pressure, 0
        return pressure + 1, 1
    return pressure, 0


def decay(pressure, contribution):
    return max(0, pressure - contribution)


def recovery(pressure, rescue_load, congestion, active=False):
    if active or pressure < RECOVERY_AT or rescue_load > LOW or congestion > LOW:
        return pressure, False
    return max(0, pressure - 2), True


def test_contract_text_and_read_only_inputs():
    assert 'mission "ES A1: Merchant Route Diversion Moderate"' in TEXT
    assert 'mission "ES A1: Merchant Route Diversion Severe"' in TEXT
    assert 'mission "ES A1: Merchant Route Diversion Recovery"' in TEXT
    assert 'event "ES A1: Merchant Route Diversion Decay 1"' in TEXT
    assert 'event "ES A1: Merchant Route Diversion Decay 2"' in TEXT
    assert '"world: merchant rescue load" >= 3' in TEXT
    assert '"world: southern rim transit congestion" >= 3' in TEXT
    assert '"world: merchant rescue load" <= 1' in TEXT
    assert '"world: southern rim transit congestion" <= 1' in TEXT
    assert '"world: merchant route diversion pressure" += 1' in TEXT
    assert '"world: merchant route diversion pressure" += 2' in TEXT
    assert TEXT.count('"world: merchant route diversion pressure" <?= 6') == 2
    assert 'event "ES A1: Merchant Route Diversion Decay 1" 6 6' in TEXT
    assert 'event "ES A1: Merchant Route Diversion Decay 2" 6 6' in TEXT

    for authority in ("world: merchant rescue load", "world: southern rim transit congestion"):
        pattern = rf'^\s*"{re.escape(authority)}"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)'
        assert not re.search(pattern, TEXT, re.M), authority


def test_severe_pressure_contributes_two_and_recovers_exactly():
    pressure = 0
    contributions = []
    for _ in range(5):
        pressure, contribution = arrival(pressure, 4, 4)
        if contribution:
            contributions.append(contribution)
    assert pressure == CAP
    assert contributions == [2, 2, 2]
    for contribution in contributions:
        pressure = decay(pressure, contribution)
    assert pressure == 0


def test_single_upstream_pressure_contributes_one():
    pressure = 0
    contributions = []
    for rescue, congestion in ((3, 0), (0, 3), (4, 1), (1, 5), (3, 3)):
        pressure, contribution = arrival(pressure, rescue, congestion)
        if contribution:
            contributions.append(contribution)
    assert contributions == [1, 1, 1, 1, 2]
    assert pressure == 6


def test_recovery_hysteresis_requires_both_inputs_low():
    assert recovery(6, 3, 0) == (6, False)
    assert recovery(6, 0, 3) == (6, False)
    assert recovery(6, 2, 1) == (6, False)
    assert recovery(6, 1, 1) == (4, True)
    assert recovery(4, 0, 0, active=True) == (4, False)
    assert recovery(3, 0, 0) == (3, False)


def test_accelerated_horizons_are_bounded_and_converge():
    for days in (30, 180, 720):
        traces = []
        for _ in range(2):
            pressure = 0
            pending = []
            trace = []
            recovery_active_until = -1
            for day in range(days):
                due = [item for item in pending if item[0] == day]
                pending = [item for item in pending if item[0] != day]
                for _, contribution in due:
                    pressure = decay(pressure, contribution)

                acute = day < days // 2
                rescue = 4 if acute and day % 2 == 0 else (3 if acute else 0)
                congestion = 4 if acute and day % 3 else (3 if acute else 0)
                pressure, contribution = arrival(pressure, rescue, congestion)
                if contribution:
                    pending.append((day + 6, contribution))

                active = day < recovery_active_until
                pressure, fired = recovery(pressure, rescue, congestion, active)
                if fired:
                    recovery_active_until = day + 4

                assert 0 <= pressure <= CAP
                trace.append(pressure)
            traces.append(trace)
        assert traces[0] == traces[1]
        if days >= 180:
            assert traces[0][-1] == 0


if __name__ == "__main__":
    test_contract_text_and_read_only_inputs()
    test_severe_pressure_contributes_two_and_recovers_exactly()
    test_single_upstream_pressure_contributes_one()
    test_recovery_hysteresis_requires_both_inputs_low()
    test_accelerated_horizons_are_bounded_and_converge()
    print("A1 Merchant route-diversion contract: PASS")
