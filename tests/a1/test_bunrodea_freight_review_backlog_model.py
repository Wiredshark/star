from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "bunrodea" / "a1 bunrodea freight review backlog.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 6
NOTICE_AT = 4


def arrival(backlog, cross_border=True):
    if not cross_border or backlog >= CAP:
        return backlog, 0
    return min(CAP, backlog + 1), 1


def recover(backlog, contribution):
    return max(0, backlog - contribution)


def test_contract_text():
    assert 'mission "ES A1: Bunrodea Freight Review Intake"' in TEXT
    assert 'mission "ES A1: Bunrodea Freight Review Backlog Notice"' in TEXT
    assert 'event "ES A1: Bunrodea Freight Review Backlog Decay"' in TEXT
    assert 'government "Bunrodea"' in TEXT
    assert 'not "entered system by: takeoff"' in TEXT
    assert 'not "previous system government: Bunrodea"' in TEXT
    assert '"world: bunrodea freight review backlog" < 6' in TEXT
    assert '"world: bunrodea freight review backlog" += 1' in TEXT
    assert '"world: bunrodea freight review backlog" <?= 6' in TEXT
    assert 'event "ES A1: Bunrodea Freight Review Backlog Decay" 4 4' in TEXT
    assert '"world: bunrodea freight review backlog" >= 4' in TEXT
    assert '"world: bunrodea freight review backlog" >?= 0' in TEXT

    forbidden_writes = (
        r'^\s*"B2 Bunrodea Freight Petition Compact:[^"]*"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
    )
    for pattern in forbidden_writes:
        assert not re.search(pattern, TEXT, re.M), f"narrative-owned state write found: {pattern}"


def test_same_jurisdiction_arrival_does_not_add_load():
    for backlog in range(CAP + 1):
        assert arrival(backlog, cross_border=False) == (backlog, 0)


def test_cross_border_arrivals_saturate_exactly():
    backlog = 0
    contributions = []
    for _ in range(12):
        backlog, contribution = arrival(backlog)
        if contribution:
            contributions.append(contribution)
    assert backlog == CAP
    assert contributions == [1] * CAP


def test_contribution_matched_recovery_returns_to_zero():
    backlog = 0
    contributions = []
    for _ in range(CAP):
        backlog, contribution = arrival(backlog)
        contributions.append(contribution)
    assert backlog == CAP
    for contribution in contributions:
        backlog = recover(backlog, contribution)
    assert backlog == 0


def test_notice_threshold_is_reached_but_not_required_for_state():
    backlog = 0
    for _ in range(NOTICE_AT):
        backlog, _ = arrival(backlog)
    assert backlog == NOTICE_AT
    assert backlog >= NOTICE_AT


def test_recovery_never_underflows():
    assert recover(1, 1) == 0
    assert recover(0, 1) == 0


if __name__ == "__main__":
    test_contract_text()
    test_same_jurisdiction_arrival_does_not_add_load()
    test_cross_border_arrivals_saturate_exactly()
    test_contribution_matched_recovery_returns_to_zero()
    test_notice_threshold_is_reached_but_not_required_for_state()
    test_recovery_never_underflows()
    print("A1 Bunrodea freight-review backlog contract: PASS")
