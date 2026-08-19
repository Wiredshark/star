from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 syndicate labor strain.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 6
BACKLOG_AT = 3
ROTATION_AT = 5


def accumulate(strain, backlog, rotating=False):
    if backlog < BACKLOG_AT or rotating or strain >= CAP:
        return strain, 0
    return min(CAP, strain + 1), 1


def rotate(strain, rotating=False):
    if rotating or strain < ROTATION_AT:
        return strain, rotating
    return max(0, strain - 2), True


def recover(strain, contribution=1):
    return max(0, strain - contribution)


def test_contract_text():
    assert 'mission "ES A1: Syndicate Labor Strain Accumulation"' in TEXT
    assert 'mission "ES A1: Syndicate Labor Rotation"' in TEXT
    assert 'mission "ES A1: Syndicate Labor Rotation Notice"' in TEXT
    assert 'event "ES A1: Syndicate Labor Strain Recovery"' in TEXT
    assert 'event "ES A1: Syndicate Labor Rotation Ends"' in TEXT
    assert '"world: syndicate maintenance backlog" >= 3' in TEXT
    assert '"world: syndicate labor strain" < 6' in TEXT
    assert '"world: syndicate labor strain" += 1' in TEXT
    assert '"world: syndicate labor strain" <?= 6' in TEXT
    assert 'event "ES A1: Syndicate Labor Strain Recovery" 8 8' in TEXT
    assert '"world: syndicate labor strain" >= 5' in TEXT
    assert '"world: syndicate labor strain" -= 2' in TEXT
    assert 'event "ES A1: Syndicate Labor Rotation Ends" 5 5' in TEXT

    # Existing maintenance backlog is input authority only.
    assert not re.search(
        r'^\s*"world: syndicate maintenance backlog"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        TEXT,
        re.M,
    )


def test_backlog_threshold_and_cap():
    for backlog in range(BACKLOG_AT):
        assert accumulate(0, backlog) == (0, 0)
    strain = 0
    contributions = []
    for _ in range(10):
        strain, contribution = accumulate(strain, BACKLOG_AT)
        if contribution:
            contributions.append(contribution)
    assert strain == CAP
    assert contributions == [1, 1, 1, 1, 1, 1]


def test_rotation_is_bounded_feedback():
    strain = 0
    for _ in range(5):
        strain, _ = accumulate(strain, BACKLOG_AT)
    assert strain == 5
    strain, rotating = rotate(strain)
    assert (strain, rotating) == (3, True)
    # Lock prevents immediate re-accumulation while crews rotate.
    assert accumulate(strain, BACKLOG_AT, rotating=True) == (3, 0)
    assert rotate(strain, rotating=True) == (3, True)


def test_recovery_horizons_do_not_underflow():
    # Short horizon: three strained arrivals.
    strain = 0
    contributions = []
    for _ in range(3):
        strain, contribution = accumulate(strain, 4)
        contributions.append(contribution)
    assert strain == 3
    # Medium horizon: all scheduled eight-day contributions recover exactly.
    for contribution in contributions:
        strain = recover(strain, contribution)
    assert strain == 0
    # Long horizon / stale-event safety: extra recovery remains clamped.
    for _ in range(32):
        strain = recover(strain)
    assert strain == 0


def test_repeated_pressure_rotation_cycle_converges():
    strain = 0
    for _cycle in range(12):
        # Pressure can build to the rotation threshold but rotation cuts two units.
        while strain < ROTATION_AT:
            strain, _ = accumulate(strain, 6)
        strain, rotating = rotate(strain)
        assert rotating
        assert 0 <= strain <= 3
        # Simulate rotation ending plus two scheduled recoveries landing.
        rotating = False
        strain = recover(recover(strain))
        assert 0 <= strain <= 1
    assert 0 <= strain <= 1


if __name__ == "__main__":
    test_contract_text()
    test_backlog_threshold_and_cap()
    test_rotation_is_bounded_feedback()
    test_recovery_horizons_do_not_underflow()
    test_repeated_pressure_rotation_cycle_converges()
    print("A1 Syndicate labor-strain contract: PASS")
