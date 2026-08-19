from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 merchant rescue reserve.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 4
ELEVATED_LOAD = 3
CRITICAL_LOAD = 5
NOTICE_AT = 3


def arrival(strain, rescue_load):
    if rescue_load >= CRITICAL_LOAD:
        if strain > CAP - 2:
            return strain, 0
        return min(CAP, strain + 2), 2
    if rescue_load >= ELEVATED_LOAD:
        if strain >= CAP:
            return strain, 0
        return min(CAP, strain + 1), 1
    return strain, 0


def recover(strain, contribution):
    return max(0, strain - contribution)


def test_contract_text():
    assert 'mission "ES A1: Merchant Rescue Reserve Elevated Load"' in TEXT
    assert 'mission "ES A1: Merchant Rescue Reserve Critical Load"' in TEXT
    assert 'mission "ES A1: Merchant Rescue Reserve Notice"' in TEXT
    assert 'event "ES A1: Merchant Rescue Reserve Recovery 1"' in TEXT
    assert 'event "ES A1: Merchant Rescue Reserve Recovery 2"' in TEXT
    assert 'government "Merchant"' in TEXT
    assert '"world: merchant rescue load" >= 3' in TEXT
    assert '"world: merchant rescue load" >= 5' in TEXT
    assert '"world: merchant rescue reserve strain" < 3' in TEXT
    assert '"world: merchant rescue reserve strain" += 1' in TEXT
    assert '"world: merchant rescue reserve strain" += 2' in TEXT
    assert TEXT.count('"world: merchant rescue reserve strain" <?= 4') == 2
    assert 'event "ES A1: Merchant Rescue Reserve Recovery 1" 10 10' in TEXT
    assert 'event "ES A1: Merchant Rescue Reserve Recovery 2" 10 10' in TEXT
    assert '"world: merchant rescue reserve strain" >= 3' in TEXT

    # The new slice consumes but never mutates the upstream A1 authority.
    assert not re.search(
        r'^\s*"world: merchant rescue load"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_low_load_does_not_create_reserve_strain():
    for load in range(ELEVATED_LOAD):
        assert arrival(0, load) == (0, 0)
        assert arrival(2, load) == (2, 0)


def test_elevated_load_accumulates_and_recovers_exactly():
    strain = 0
    contributions = []
    for _ in range(7):
        strain, contribution = arrival(strain, 4)
        if contribution:
            contributions.append(contribution)
    assert strain == CAP
    assert contributions == [1, 1, 1, 1]
    path = [strain]
    for contribution in contributions:
        strain = recover(strain, contribution)
        path.append(strain)
    assert path == [4, 3, 2, 1, 0]


def test_critical_load_uses_exact_two_point_contributions():
    strain = 0
    contributions = []
    for _ in range(4):
        strain, contribution = arrival(strain, 5)
        if contribution:
            contributions.append(contribution)
    assert strain == CAP
    assert contributions == [2, 2]
    assert recover(recover(strain, 2), 2) == 0


def test_mixed_load_preserves_bounds_and_notice_threshold():
    strain, contribution = arrival(0, 3)
    assert (strain, contribution) == (1, 1)
    strain, contribution = arrival(strain, 5)
    assert (strain, contribution) == (3, 2)
    assert strain >= NOTICE_AT
    # Critical +2 is suppressed at 3 to avoid scheduling an over-decay.
    assert arrival(strain, 5) == (3, 0)
    # Elevated +1 may still fill the final unit exactly.
    assert arrival(strain, 4) == (4, 1)


def test_recovery_clamps_and_long_horizon_converges():
    assert recover(0, 1) == 0
    assert recover(1, 2) == 0

    strain = 0
    scheduled = []
    # Representative sustained-pressure horizon: 24 arrivals at critical load.
    for _ in range(24):
        strain, contribution = arrival(strain, 5)
        if contribution:
            scheduled.append(contribution)
    assert strain == CAP
    assert scheduled == [2, 2]
    for contribution in scheduled:
        strain = recover(strain, contribution)
    assert strain == 0


if __name__ == "__main__":
    test_contract_text()
    test_low_load_does_not_create_reserve_strain()
    test_elevated_load_accumulates_and_recovers_exactly()
    test_critical_load_uses_exact_two_point_contributions()
    test_mixed_load_preserves_bounds_and_notice_threshold()
    test_recovery_clamps_and_long_horizon_converges()
    print("A1 Merchant rescue-reserve strain contract: PASS")
