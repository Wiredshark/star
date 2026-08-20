from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 deep archaeology security pressure.txt").read_text(encoding="utf-8")

CAP = 4
RECOVERY_DAYS = (4, 8, 12, 16)


def register(pressure, archaeology_complete, registered):
    if not archaeology_complete or registered:
        return pressure, registered, []
    return min(CAP, pressure + CAP), True, list(RECOVERY_DAYS)


def recover(pressure):
    return max(0, pressure - 1)


def test_contract_is_one_shot_and_campaign_read_only():
    required = [
        'mission "ES A1: Deep Archaeology Security Pressure Registration"',
        'mission "ES A1: Deep Archaeology Security Pressure Advisory"',
        'mission "ES A1: Deep Archaeology Security Pressure Advisory Reset"',
        'attributes "deep"',
        'has "Deep Archaeology 5: done"',
        'not "world: deep archaeology security response registered"',
        'set "world: deep archaeology security response registered"',
        '"world: deep archaeology security pressure" += 4',
        '"world: deep archaeology security pressure" <?= 4',
        'event "ES A1: Deep Archaeology Security Pressure Recovery" 4 4',
        'event "ES A1: Deep Archaeology Security Pressure Recovery" 8 8',
        'event "ES A1: Deep Archaeology Security Pressure Recovery" 12 12',
        'event "ES A1: Deep Archaeology Security Pressure Recovery" 16 16',
        '"world: deep archaeology security pressure" >= 3',
        '"world: deep archaeology security pressure" <= 1',
    ]
    for token in required:
        assert token in TEXT

    assert TEXT.count('not "entered system by: takeoff"') == 3

    assert not re.search(
        r'^\s*(?:set|clear)\s+"Deep Archaeology [^"]+"',
        TEXT,
        re.M,
    )
    assert not re.search(
        r'^\s*"Deep Archaeology [^"]+"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_registration_requires_completed_chase_and_cannot_repeat():
    assert register(0, False, False) == (0, False, [])
    pressure, registered, recoveries = register(0, True, False)
    assert pressure == CAP
    assert registered is True
    assert recoveries == list(RECOVERY_DAYS)
    assert register(pressure, True, registered) == (CAP, True, [])


def test_four_matched_recoveries_drain_exactly():
    pressure, _, recoveries = register(0, True, False)
    trace = [pressure]
    for _ in recoveries:
        pressure = recover(pressure)
        trace.append(pressure)
    assert trace == [4, 3, 2, 1, 0]
    assert recover(0) == 0


def simulate(horizon=365 * 3):
    pressure = 0
    registered = False
    scheduled = []
    trace = []

    for day in range(horizon):
        for _ in range(scheduled.count(day)):
            pressure = recover(pressure)
        scheduled = [when for when in scheduled if when > day]

        # The campaign completes once in this deterministic horizon. The player
        # makes a qualifying Deep return on day 60 and subsequent returns cannot
        # create new pressure because the registration flag is permanent.
        archaeology_complete = day >= 50
        qualifying_return = day >= 60 and day % 5 == 0
        if qualifying_return:
            pressure, new_registered, offsets = register(
                pressure,
                archaeology_complete,
                registered,
            )
            if new_registered and not registered:
                registered = True
                scheduled.extend(day + offset for offset in offsets)

        assert 0 <= pressure <= CAP
        trace.append((pressure, registered, tuple(scheduled)))

    return trace, pressure, registered, scheduled


def test_three_year_horizon_is_deterministic_one_shot_and_recovers():
    first = simulate()
    second = simulate()
    assert first[0] == second[0]
    _, pressure, registered, scheduled = first
    assert registered is True
    assert pressure == 0
    assert scheduled == []

    # Only one rise from zero to the full registered response may occur.
    trace = first[0]
    rises = sum(
        1
        for previous, current in zip(trace, trace[1:])
        if previous[0] == 0 and current[0] == CAP
    )
    assert rises == 1
