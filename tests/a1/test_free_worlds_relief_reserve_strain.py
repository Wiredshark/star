from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 free worlds relief reserve strain.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 4
DEMAND_AT = 4
NOTICE_AT = 3


def arrival(strain, relief_demand):
    if relief_demand < DEMAND_AT or strain >= CAP:
        return strain, 0
    return min(CAP, strain + 1), 1


def recover(strain, contribution):
    return max(0, strain - contribution)


def test_contract_text():
    assert 'event "ES A1: Free Worlds Relief Reserve Recovery"' in TEXT
    assert 'mission "ES A1: Free Worlds Relief Reserve Strain"' in TEXT
    assert 'mission "ES A1: Free Worlds Relief Reserve Notice"' in TEXT
    assert 'government "Free Worlds"' in TEXT
    assert '"world: free worlds relief demand" >= 4' in TEXT
    assert '"world: free worlds relief reserve strain" < 4' in TEXT
    assert '"world: free worlds relief reserve strain" += 1' in TEXT
    assert '"world: free worlds relief reserve strain" <?= 4' in TEXT
    assert 'event "ES A1: Free Worlds Relief Reserve Recovery" 6 6' in TEXT
    assert '"world: free worlds relief reserve strain" >= 3' in TEXT

    forbidden_input_write = r'^\s*"world: free worlds relief demand"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)'
    assert not re.search(forbidden_input_write, TEXT, re.M)


def test_low_demand_never_consumes_reserve_capacity():
    for demand in range(DEMAND_AT):
        assert arrival(0, demand) == (0, 0)
        assert arrival(2, demand) == (2, 0)


def test_sustained_high_demand_saturates_exactly():
    strain = 0
    contributions = []
    trajectory = [strain]
    for _ in range(7):
        strain, contribution = arrival(strain, DEMAND_AT)
        trajectory.append(strain)
        if contribution:
            contributions.append(contribution)
    assert trajectory == [0, 1, 2, 3, 4, 4, 4, 4]
    assert contributions == [1, 1, 1, 1]


def test_exact_recovery_and_re_elevation():
    strain = 0
    contributions = []
    for _ in range(CAP):
        strain, contribution = arrival(strain, 5)
        contributions.append(contribution)
    assert strain == CAP
    assert contributions == [1, 1, 1, 1]

    recovery = [strain]
    for contribution in contributions:
        strain = recover(strain, contribution)
        recovery.append(strain)
    assert recovery == [4, 3, 2, 1, 0]

    strain, contribution = arrival(strain, 5)
    assert (strain, contribution) == (1, 1)


def test_notice_threshold_and_no_underflow():
    strain = 0
    visible = []
    for _ in range(CAP):
        strain, _ = arrival(strain, 5)
        visible.append(strain >= NOTICE_AT)
    assert visible == [False, False, True, True]
    assert recover(0, 1) == 0
    assert recover(1, 2) == 0


if __name__ == "__main__":
    test_contract_text()
    test_low_demand_never_consumes_reserve_capacity()
    test_sustained_high_demand_saturates_exactly()
    test_exact_recovery_and_re_elevation()
    test_notice_threshold_and_no_underflow()
    print("A1 Free Worlds relief-reserve strain contract: PASS")
