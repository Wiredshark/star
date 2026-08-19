from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 republic civic strain.txt").read_text()


def escalate(strain, displacement, scrutiny, active):
    if displacement < 4 or scrutiny < 3 or active or strain >= 6:
        return strain, active, False
    return min(6, strain + 2), True, True


def scheduled_recover(strain):
    return max(0, strain - 1)


def stabilize(strain, displacement, scrutiny, active):
    if strain < 2 or displacement > 2 or scrutiny > 1 or active:
        return strain, active, False
    return max(0, strain - 2), True, True


def test_production_contract_and_authority_boundaries():
    required = [
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
    ]
    for token in required:
        assert token in TEXT

    for authority in (
        "world: republic displacement pressure",
        "world: republic customs scrutiny",
    ):
        writes = re.findall(
            rf'^\s*"{re.escape(authority)}"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
            TEXT,
            flags=re.MULTILINE,
        )
        assert writes == []


def test_escalation_requires_both_sources_and_caps():
    assert escalate(0, 3, 4, False) == (0, False, False)
    assert escalate(0, 5, 2, False) == (0, False, False)
    assert escalate(0, 4, 3, False) == (2, True, True)
    assert escalate(5, 6, 6, False) == (6, True, True)
    assert escalate(6, 6, 6, False) == (6, False, False)
    assert escalate(2, 6, 6, True) == (2, True, False)


def test_stabilization_has_two_source_hysteresis():
    assert stabilize(4, 3, 1, False) == (4, False, False)
    assert stabilize(4, 2, 2, False) == (4, False, False)
    assert stabilize(2, 2, 1, False) == (0, True, True)
    assert stabilize(6, 0, 0, True) == (6, True, False)
    assert stabilize(1, 0, 0, False) == (1, False, False)


def test_deterministic_year_horizon_is_bounded_and_converges():
    strain = 0
    assessment_days = 0
    stabilization_days = 0
    recovery_due = []

    for day in range(365):
        # A prolonged joint crisis is followed by durable source recovery.
        displacement = 5 if day < 150 else 1
        scrutiny = 4 if day < 150 else 1

        strain, _, fired = escalate(
            strain, displacement, scrutiny, assessment_days > 0
        )
        if fired:
            assessment_days = 4
            recovery_due.append(day + 10)

        for due in tuple(recovery_due):
            if due == day:
                strain = scheduled_recover(strain)
                recovery_due.remove(due)

        strain, _, stabilized = stabilize(
            strain, displacement, scrutiny, stabilization_days > 0
        )
        if stabilized:
            stabilization_days = 6

        assessment_days = max(0, assessment_days - 1)
        stabilization_days = max(0, stabilization_days - 1)
        assert 0 <= strain <= 6
        if day < 150:
            assert not stabilized

    assert strain == 0


def test_recovery_cannot_underflow():
    value = 1
    for _ in range(20):
        value = scheduled_recover(value)
    assert value == 0


if __name__ == "__main__":
    test_production_contract_and_authority_boundaries()
    test_escalation_requires_both_sources_and_caps()
    test_stabilization_has_two_source_hysteresis()
    test_deterministic_year_horizon_is_bounded_and_converges()
    test_recovery_cannot_underflow()
    print("A1 Republic civic-strain feedback contract: PASS")
