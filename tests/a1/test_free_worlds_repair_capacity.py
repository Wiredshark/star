from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 free worlds repair capacity.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 6
STRAINED_AT = 3
MOBILIZED_STRAIN_AT = 1
NOTICE_AT = 3


def intake(backlog, defense_strain, patrol_surge):
    if patrol_surge:
        if defense_strain < MOBILIZED_STRAIN_AT or backlog > CAP - 2:
            return backlog, 0
        return min(CAP, backlog + 2), 2
    if defense_strain < STRAINED_AT or backlog >= CAP:
        return backlog, 0
    return min(CAP, backlog + 1), 1


def recover(backlog, contribution):
    return max(0, backlog - contribution)


def test_contract_text():
    assert 'mission "ES A1: Free Worlds Repair Backlog Strained Intake"' in TEXT
    assert 'mission "ES A1: Free Worlds Repair Backlog Mobilized Intake"' in TEXT
    assert 'mission "ES A1: Free Worlds Repair Backlog Notice"' in TEXT
    assert 'event "ES A1: Free Worlds Repair Backlog Recovery 1"' in TEXT
    assert 'event "ES A1: Free Worlds Repair Backlog Recovery 2"' in TEXT
    assert '"world: free worlds defense strain" >= 3' in TEXT
    assert 'not "world: free worlds patrol surge"' in TEXT
    assert 'has "world: free worlds patrol surge"' in TEXT
    assert '"world: free worlds repair backlog" < 6' in TEXT
    assert '"world: free worlds repair backlog" < 5' in TEXT
    assert '"world: free worlds repair backlog" += 1' in TEXT
    assert '"world: free worlds repair backlog" += 2' in TEXT
    assert TEXT.count('"world: free worlds repair backlog" <?= 6') == 2
    assert 'event "ES A1: Free Worlds Repair Backlog Recovery 1" 7 7' in TEXT
    assert 'event "ES A1: Free Worlds Repair Backlog Recovery 2" 7 7' in TEXT
    assert '"world: free worlds repair backlog" >= 3' in TEXT

    forbidden_writes = (
        r'^\s*"world: free worlds defense strain"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        r'^\s*"world: free worlds patrol surge"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=|clear)',
    )
    for pattern in forbidden_writes:
        assert not re.search(pattern, TEXT, re.M), f"authoritative input write found: {pattern}"


def test_low_strain_does_not_create_backlog():
    for strain in range(STRAINED_AT):
        assert intake(0, strain, False) == (0, 0)
    assert intake(0, 0, True) == (0, 0)


def test_strained_intake_saturates_and_recovers_exactly():
    backlog = 0
    contributions = []
    for _ in range(9):
        backlog, contribution = intake(backlog, STRAINED_AT, False)
        if contribution:
            contributions.append(contribution)
    assert backlog == CAP
    assert contributions == [1, 1, 1, 1, 1, 1]

    for contribution in contributions:
        backlog = recover(backlog, contribution)
    assert backlog == 0


def test_mobilized_intake_uses_two_unit_contributions():
    backlog = 0
    contributions = []
    for _ in range(5):
        backlog, contribution = intake(backlog, MOBILIZED_STRAIN_AT, True)
        if contribution:
            contributions.append(contribution)
    assert backlog == CAP
    assert contributions == [2, 2, 2]

    path = [backlog]
    for contribution in contributions:
        backlog = recover(backlog, contribution)
        path.append(backlog)
    assert path == [6, 4, 2, 0]


def test_mixed_feedback_preserves_bounds_and_notice_threshold():
    backlog, contribution = intake(0, STRAINED_AT, False)
    assert (backlog, contribution) == (1, 1)
    backlog, contribution = intake(backlog, MOBILIZED_STRAIN_AT, True)
    assert (backlog, contribution) == (3, 2)
    assert backlog >= NOTICE_AT
    backlog, contribution = intake(backlog, MOBILIZED_STRAIN_AT, True)
    assert (backlog, contribution) == (5, 2)
    assert intake(backlog, MOBILIZED_STRAIN_AT, True) == (5, 0)
    assert intake(backlog, STRAINED_AT, False) == (6, 1)


def test_recovery_never_underflows():
    assert recover(1, 2) == 0
    assert recover(0, 1) == 0


if __name__ == "__main__":
    test_contract_text()
    test_low_strain_does_not_create_backlog()
    test_strained_intake_saturates_and_recovers_exactly()
    test_mobilized_intake_uses_two_unit_contributions()
    test_mixed_feedback_preserves_bounds_and_notice_threshold()
    test_recovery_never_underflows()
    print("A1 Free Worlds repair-capacity contract: PASS")
