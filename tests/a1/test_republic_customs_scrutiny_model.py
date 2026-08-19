from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 republic customs scrutiny.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 6
PIRATE_JOBS_AT = 3
ELEVATED_BORDER_AT = 4
NOTICE_AT = 3


def crossing(scrutiny, pirate_jobs, border_pressure):
    if pirate_jobs < PIRATE_JOBS_AT:
        return scrutiny, 0
    if border_pressure >= ELEVATED_BORDER_AT:
        if scrutiny > CAP - 2:
            return scrutiny, 0
        return min(CAP, scrutiny + 2), 2
    if scrutiny >= CAP:
        return scrutiny, 0
    return min(CAP, scrutiny + 1), 1


def recover(scrutiny, contribution):
    return max(0, scrutiny - contribution)


def test_contract_text():
    assert 'mission "ES A1: Republic Customs Scrutiny Routine Crossing"' in TEXT
    assert 'mission "ES A1: Republic Customs Scrutiny Elevated Crossing"' in TEXT
    assert 'mission "ES A1: Republic Customs Scrutiny Notice"' in TEXT
    assert 'event "ES A1: Republic Customs Scrutiny Decay 1"' in TEXT
    assert 'event "ES A1: Republic Customs Scrutiny Decay 2"' in TEXT
    assert 'has "previous system government: Pirate"' in TEXT
    assert '"pirate jobs" >= 3' in TEXT
    assert '"world: republic border pressure" < 4' in TEXT
    assert '"world: republic border pressure" >= 4' in TEXT
    assert '"world: republic customs scrutiny" += 1' in TEXT
    assert '"world: republic customs scrutiny" += 2' in TEXT
    assert TEXT.count('"world: republic customs scrutiny" <?= 6') == 2
    assert 'event "ES A1: Republic Customs Scrutiny Decay 1" 7 7' in TEXT
    assert 'event "ES A1: Republic Customs Scrutiny Decay 2" 7 7' in TEXT
    assert '"world: republic customs scrutiny" >= 3' in TEXT

    forbidden_writes = (
        r'^\s*"pirate jobs"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        r'^\s*"world: republic border pressure"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
    )
    for pattern in forbidden_writes:
        assert not re.search(pattern, TEXT, re.M), f"authoritative input write found: {pattern}"


def test_no_underworld_history_means_no_scrutiny():
    for jobs in range(PIRATE_JOBS_AT):
        for pressure in (0, 3, 4, 6):
            assert crossing(0, jobs, pressure) == (0, 0)


def test_routine_crossings_saturate_and_decay_exactly():
    scrutiny = 0
    contributions = []
    for _ in range(9):
        scrutiny, contribution = crossing(scrutiny, PIRATE_JOBS_AT, 2)
        if contribution:
            contributions.append(contribution)
    assert scrutiny == CAP
    assert contributions == [1, 1, 1, 1, 1, 1]

    for contribution in contributions:
        scrutiny = recover(scrutiny, contribution)
    assert scrutiny == 0


def test_elevated_border_crossings_add_two_and_decay_two():
    scrutiny = 0
    contributions = []
    for _ in range(5):
        scrutiny, contribution = crossing(scrutiny, PIRATE_JOBS_AT, ELEVATED_BORDER_AT)
        if contribution:
            contributions.append(contribution)
    assert scrutiny == CAP
    assert contributions == [2, 2, 2]

    path = [scrutiny]
    for contribution in contributions:
        scrutiny = recover(scrutiny, contribution)
        path.append(scrutiny)
    assert path == [6, 4, 2, 0]


def test_mixed_pressure_preserves_bounds_and_notice_threshold():
    scrutiny, contribution = crossing(0, 5, 1)
    assert (scrutiny, contribution) == (1, 1)
    scrutiny, contribution = crossing(scrutiny, 5, 5)
    assert (scrutiny, contribution) == (3, 2)
    assert scrutiny >= NOTICE_AT
    scrutiny, contribution = crossing(scrutiny, 5, 5)
    assert (scrutiny, contribution) == (5, 2)
    # At 5, an elevated +2 contribution is suppressed instead of saturating and
    # later over-decaying by two.
    assert crossing(scrutiny, 5, 5) == (5, 0)
    # A routine +1 contribution may still fill the final unit exactly.
    assert crossing(scrutiny, 5, 1) == (6, 1)


def test_recovery_never_underflows():
    scrutiny = 1
    assert recover(scrutiny, 2) == 0
    assert recover(0, 1) == 0


if __name__ == "__main__":
    test_contract_text()
    test_no_underworld_history_means_no_scrutiny()
    test_routine_crossings_saturate_and_decay_exactly()
    test_elevated_border_crossings_add_two_and_decay_two()
    test_mixed_pressure_preserves_bounds_and_notice_threshold()
    test_recovery_never_underflows()
    print("A1 Republic customs-scrutiny contract: PASS")
