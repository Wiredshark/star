from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 dirt belt drought resource strain.txt").read_text(encoding="utf-8")

DROUGHT_CAP = 6
IRRIGATION_CAP = 4
DROUGHT_LATCH_DAYS = 4
DROUGHT_RECOVERY_DAYS = 10
IRRIGATION_LATCH_DAYS = 6
IRRIGATION_RECOVERY_DAYS = 12


def observe_drought(pressure, drought_job_active, latched):
    if not drought_job_active or latched or pressure >= DROUGHT_CAP:
        return pressure, latched, False
    return min(DROUGHT_CAP, pressure + 1), True, True


def observe_irrigation(strain, drought_pressure, latched):
    if drought_pressure < 3 or latched or strain >= IRRIGATION_CAP:
        return strain, latched, False
    return min(IRRIGATION_CAP, strain + 1), True, True


def recover(value):
    return max(0, value - 1)


def test_contract_and_stock_job_ownership():
    required = [
        'mission "ES A1: Dirt Belt Drought Pressure Observation"',
        'mission "ES A1: Dirt Belt Irrigation Reserve Strain"',
        'mission "ES A1: Dirt Belt Drought Resource Advisory"',
        'mission "ES A1: Dirt Belt Drought Resource Advisory Reset"',
        'government "Republic"',
        'attributes "dirt belt"',
        'attributes "farming"',
        'has "Drought Relief: active"',
        '"world: dirt belt drought pressure" < 6',
        '"world: dirt belt drought pressure" += 1',
        '"world: dirt belt drought pressure" <?= 6',
        'event "ES A1: Dirt Belt Drought Pressure Recovery" 10 10',
        'event "ES A1: Dirt Belt Drought Observation Ends" 4 4',
        '"world: dirt belt drought pressure" >= 3',
        '"world: dirt belt irrigation reserve strain" < 4',
        '"world: dirt belt irrigation reserve strain" += 1',
        '"world: dirt belt irrigation reserve strain" <?= 4',
        'event "ES A1: Dirt Belt Irrigation Reserve Recovery" 12 12',
        'event "ES A1: Dirt Belt Irrigation Observation Ends" 6 6',
        '"world: dirt belt irrigation reserve strain" >= 2',
        '"world: dirt belt drought pressure" <= 1',
        '"world: dirt belt irrigation reserve strain" <= 1',
    ]
    for token in required:
        assert token in TEXT

    assert TEXT.count('not "entered system by: takeoff"') == 4

    # The stock job is an observational input. This A1 slice must not complete,
    # fail, clear, or otherwise mutate it.
    assert not re.search(
        r'^\s*(?:set|clear)\s+"Drought Relief:[^"]+"',
        TEXT,
        re.M,
    )
    assert not re.search(
        r'^\s*"Drought Relief:[^"]+"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_drought_observation_requires_active_stock_job_and_latch():
    assert observe_drought(0, False, False) == (0, False, False)
    assert observe_drought(0, True, False) == (1, True, True)
    assert observe_drought(1, True, True) == (1, True, False)

    pressure = 0
    additions = 0
    for _ in range(12):
        pressure, _, added = observe_drought(pressure, True, False)
        additions += int(added)
    assert pressure == DROUGHT_CAP
    assert additions == DROUGHT_CAP


def test_irrigation_reserve_is_one_way_downstream_and_bounded():
    assert observe_irrigation(0, 2, False) == (0, False, False)
    assert observe_irrigation(0, 3, False) == (1, True, True)
    assert observe_irrigation(1, 6, True) == (1, True, False)

    strain = 0
    additions = 0
    for _ in range(10):
        strain, _, added = observe_irrigation(strain, 6, False)
        additions += int(added)
    assert strain == IRRIGATION_CAP
    assert additions == IRRIGATION_CAP

    # Production only reads drought pressure in the irrigation mission.
    irrigation_block = TEXT.split('mission "ES A1: Dirt Belt Irrigation Reserve Strain"', 1)[1].split(
        'mission "ES A1: Dirt Belt Drought Resource Advisory"', 1
    )[0]
    assert not re.search(
        r'^\s*"world: dirt belt drought pressure"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        irrigation_block,
        re.M,
    )


def simulate(horizon=365 * 3):
    drought_pressure = 0
    irrigation_strain = 0
    drought_latch = 0
    irrigation_latch = 0
    drought_recoveries = []
    irrigation_recoveries = []
    trace = []

    for day in range(horizon):
        for _ in range(drought_recoveries.count(day)):
            drought_pressure = recover(drought_pressure)
        drought_recoveries = [when for when in drought_recoveries if when > day]

        for _ in range(irrigation_recoveries.count(day)):
            irrigation_strain = recover(irrigation_strain)
        irrigation_recoveries = [when for when in irrigation_recoveries if when > day]

        # Deterministic recurring observed drought seasons: 100 stressed days,
        # followed by 100 quiet days. This models the state machine, not climate.
        drought_job_active = day % 200 < 100

        drought_pressure, _, drought_added = observe_drought(
            drought_pressure,
            drought_job_active,
            drought_latch > 0,
        )
        if drought_added:
            drought_latch = DROUGHT_LATCH_DAYS
            drought_recoveries.append(day + DROUGHT_RECOVERY_DAYS)

        irrigation_strain, _, irrigation_added = observe_irrigation(
            irrigation_strain,
            drought_pressure,
            irrigation_latch > 0,
        )
        if irrigation_added:
            irrigation_latch = IRRIGATION_LATCH_DAYS
            irrigation_recoveries.append(day + IRRIGATION_RECOVERY_DAYS)

        drought_latch = max(0, drought_latch - 1)
        irrigation_latch = max(0, irrigation_latch - 1)

        assert 0 <= drought_pressure <= DROUGHT_CAP
        assert 0 <= irrigation_strain <= IRRIGATION_CAP
        trace.append(
            (
                drought_pressure,
                irrigation_strain,
                drought_latch,
                irrigation_latch,
                tuple(drought_recoveries),
                tuple(irrigation_recoveries),
            )
        )

    return trace, drought_pressure, irrigation_strain, drought_recoveries, irrigation_recoveries


def test_deterministic_three_year_chain_is_bounded_and_recovers():
    first = simulate()
    second = simulate()
    assert first[0] == second[0]

    _, drought_pressure, irrigation_strain, drought_recoveries, irrigation_recoveries = first
    day = 365 * 3
    while drought_recoveries or irrigation_recoveries:
        for _ in range(drought_recoveries.count(day)):
            drought_pressure = recover(drought_pressure)
        drought_recoveries = [when for when in drought_recoveries if when > day]

        for _ in range(irrigation_recoveries.count(day)):
            irrigation_strain = recover(irrigation_strain)
        irrigation_recoveries = [when for when in irrigation_recoveries if when > day]
        day += 1

    for _ in range(DROUGHT_CAP + IRRIGATION_CAP + 4):
        drought_pressure = recover(drought_pressure)
        irrigation_strain = recover(irrigation_strain)

    assert drought_pressure == 0
    assert irrigation_strain == 0
    assert drought_recoveries == []
    assert irrigation_recoveries == []
