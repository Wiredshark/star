from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/remnant/a1 remnant void sprite response strain.txt").read_text(encoding="utf-8")

CAP = 6
OBSERVATION_DAYS = 3
RECOVERY_DAYS = 8
STABILIZATION_DAYS = 5


def observe(strain, response_active, task_force_complete, latched):
    if not response_active or task_force_complete or latched or strain >= CAP:
        return strain, latched, False
    return min(CAP, strain + 1), True, True


def recover(strain):
    return max(0, strain - 1)


def stabilize(strain, task_force_complete, latched):
    if not task_force_complete or strain < 2 or latched:
        return strain, latched, False
    return max(0, strain - 2), True, True


def test_contract_and_campaign_ownership():
    required = [
        'mission "ES A1: Remnant Void Sprite Response Pressure"',
        'mission "ES A1: Remnant Void Sprite Response Stabilization"',
        'mission "ES A1: Remnant Void Sprite Response Advisory"',
        'mission "ES A1: Remnant Void Sprite Response Advisory Reset"',
        'event "ES A1: Remnant Void Sprite Response Recovery"',
        'government "Remnant"',
        'has "Remnant: Cognizance 2: done"',
        'not "Remnant: Cognizance 5: done"',
        'has "Remnant: Cognizance 5: done"',
        '"world: remnant void sprite response strain" < 6',
        '"world: remnant void sprite response strain" += 1',
        '"world: remnant void sprite response strain" <?= 6',
        'event "ES A1: Remnant Void Sprite Response Recovery" 8 8',
        'event "ES A1: Remnant Void Sprite Response Observation Ends" 3 3',
        '"world: remnant void sprite response strain" -= 2',
        'event "ES A1: Remnant Void Sprite Response Stabilization Ends" 5 5',
        '"world: remnant void sprite response strain" >= 3',
        '"world: remnant void sprite response strain" <= 1',
    ]
    for token in required:
        assert token in TEXT

    assert TEXT.count('not "entered system by: takeoff"') == 4

    # Cognizance conditions are stock campaign truth. This A1 slice is allowed to
    # consume them, but never to write or rewrite their progression.
    assert not re.search(
        r'^\s*(?:set|clear)\s+"Remnant: Cognizance [^"]+"',
        TEXT,
        re.M,
    )
    assert not re.search(
        r'^\s*"Remnant: Cognizance [^"]+"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_pressure_is_latched_and_bounded():
    assert observe(0, False, False, False) == (0, False, False)
    assert observe(0, True, True, False) == (0, False, False)

    strain, latch, added = observe(0, True, False, False)
    assert (strain, latch, added) == (1, True, True)
    assert observe(strain, True, False, latch) == (1, True, False)

    strain = 0
    additions = 0
    for _ in range(12):
        strain, _, added = observe(strain, True, False, False)
        additions += int(added)
    assert strain == CAP
    assert additions == CAP


def test_task_force_completion_enables_only_negative_feedback():
    assert stabilize(5, False, False) == (5, False, False)
    assert stabilize(1, True, False) == (1, False, False)
    assert stabilize(5, True, False) == (3, True, True)
    assert stabilize(3, True, True) == (3, True, False)
    assert stabilize(2, True, False) == (0, True, True)


def test_recovery_clamps_at_zero():
    assert recover(1) == 0
    assert recover(0) == 0


def simulate(horizon=365 * 3):
    strain = 0
    observation_days = 0
    stabilization_days = 0
    scheduled_recoveries = []
    trace = []

    for day in range(horizon):
        due = scheduled_recoveries.count(day)
        for _ in range(due):
            strain = recover(strain)
        scheduled_recoveries = [when for when in scheduled_recoveries if when > day]

        response_active = day < 270
        task_force_complete = day >= 210

        if response_active and not task_force_complete:
            strain, new_latch, added = observe(
                strain,
                response_active=True,
                task_force_complete=False,
                latched=observation_days > 0,
            )
            if added:
                observation_days = OBSERVATION_DAYS
                scheduled_recoveries.append(day + RECOVERY_DAYS)
            elif new_latch and observation_days == 0:
                observation_days = OBSERVATION_DAYS

        if task_force_complete:
            strain, new_stabilization, reduced = stabilize(
                strain,
                task_force_complete=True,
                latched=stabilization_days > 0,
            )
            if reduced:
                stabilization_days = STABILIZATION_DAYS
            elif new_stabilization and stabilization_days == 0:
                stabilization_days = STABILIZATION_DAYS

        observation_days = max(0, observation_days - 1)
        stabilization_days = max(0, stabilization_days - 1)
        assert 0 <= strain <= CAP
        trace.append((strain, observation_days, stabilization_days, tuple(scheduled_recoveries)))

    return trace, strain, scheduled_recoveries


def test_deterministic_three_year_horizon_and_quiet_tail():
    first = simulate()
    second = simulate()
    assert first[0] == second[0]

    _, strain, recoveries = first
    day = 365 * 3
    while recoveries:
        due = recoveries.count(day)
        for _ in range(due):
            strain = recover(strain)
        recoveries = [when for when in recoveries if when > day]
        day += 1

    for _ in range(CAP + 4):
        strain = recover(strain)
    assert strain == 0
    assert recoveries == []
