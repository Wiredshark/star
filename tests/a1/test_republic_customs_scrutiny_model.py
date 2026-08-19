from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 republic customs scrutiny.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 6
PIRATE_JOBS_AT = 3
ELEVATED_BORDER_AT = 4
NOTICE_AT = 3
COOLDOWN_DAYS = 4
DECAY_DAYS = 7


def crossing(scrutiny, pirate_jobs, border_pressure, cooldown=False):
    if pirate_jobs < PIRATE_JOBS_AT:
        return scrutiny, 0, cooldown
    if border_pressure >= ELEVATED_BORDER_AT:
        if cooldown or scrutiny > CAP - 2:
            return scrutiny, 0, cooldown
        return min(CAP, scrutiny + 2), 2, True
    if scrutiny >= CAP:
        return scrutiny, 0, cooldown
    return min(CAP, scrutiny + 1), 1, cooldown


def recover(scrutiny, contribution):
    return max(0, scrutiny - contribution)


def test_contract_text():
    assert 'mission "ES A1: Republic Customs Scrutiny Routine Crossing"' in TEXT
    assert 'mission "ES A1: Republic Customs Scrutiny Elevated Crossing"' in TEXT
    assert 'mission "ES A1: Republic Customs Scrutiny Notice"' in TEXT
    assert 'event "ES A1: Republic Customs Scrutiny Decay 1"' in TEXT
    assert 'event "ES A1: Republic Customs Scrutiny Decay 2"' in TEXT
    assert 'event "ES A1: Republic Customs Review Cooldown"' in TEXT
    assert 'has "previous system government: Pirate"' in TEXT
    assert '"pirate jobs" >= 3' in TEXT
    assert '"world: republic border pressure" < 4' in TEXT
    assert '"world: republic border pressure" >= 4' in TEXT
    assert '"world: republic customs scrutiny" < 5' in TEXT
    assert 'not "world: republic customs review cooldown"' in TEXT
    assert 'set "world: republic customs review cooldown"' in TEXT
    assert 'clear "world: republic customs review cooldown"' in TEXT
    assert 'event "ES A1: Republic Customs Review Cooldown" 4 4' in TEXT
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
            assert crossing(0, jobs, pressure) == (0, 0, False)


def test_routine_crossings_still_saturate_and_decay_exactly():
    scrutiny = 0
    contributions = []
    for _ in range(9):
        scrutiny, contribution, cooldown = crossing(scrutiny, PIRATE_JOBS_AT, 2)
        assert not cooldown
        if contribution:
            contributions.append(contribution)
    assert scrutiny == CAP
    assert contributions == [1, 1, 1, 1, 1, 1]

    for contribution in contributions:
        scrutiny = recover(scrutiny, contribution)
    assert scrutiny == 0


def test_elevated_crossing_sets_cooldown_and_blocks_restack():
    scrutiny, contribution, cooldown = crossing(0, PIRATE_JOBS_AT, ELEVATED_BORDER_AT)
    assert (scrutiny, contribution, cooldown) == (2, 2, True)
    assert crossing(scrutiny, PIRATE_JOBS_AT, ELEVATED_BORDER_AT, cooldown) == (2, 0, True)
    scrutiny, contribution, cooldown = crossing(scrutiny, PIRATE_JOBS_AT, ELEVATED_BORDER_AT, False)
    assert (scrutiny, contribution, cooldown) == (4, 2, True)


def test_mixed_pressure_preserves_bounds_and_notice_threshold():
    scrutiny, contribution, cooldown = crossing(0, 5, 1)
    assert (scrutiny, contribution, cooldown) == (1, 1, False)
    scrutiny, contribution, cooldown = crossing(scrutiny, 5, 5, cooldown)
    assert (scrutiny, contribution, cooldown) == (3, 2, True)
    assert scrutiny >= NOTICE_AT
    assert crossing(scrutiny, 5, 5, cooldown) == (3, 0, True)
    # A later elevated crossing can proceed only after the four-day cooldown clears.
    scrutiny, contribution, cooldown = crossing(scrutiny, 5, 5, False)
    assert (scrutiny, contribution, cooldown) == (5, 2, True)
    # Routine pressure remains independent and may fill the final unit exactly.
    assert crossing(scrutiny, 5, 1, cooldown) == (6, 1, True)


def test_three_year_daily_elevated_attempts_remain_bounded_and_quiet_tail_recovers():
    scrutiny = 0
    cooldown = 0
    scheduled = []

    for day in range(365 * 3):
        due = [amount for due_day, amount in scheduled if due_day == day]
        scheduled = [(due_day, amount) for due_day, amount in scheduled if due_day != day]
        for amount in due:
            scrutiny = recover(scrutiny, amount)

        if cooldown:
            cooldown -= 1
        scrutiny, contribution, active = crossing(
            scrutiny,
            PIRATE_JOBS_AT,
            ELEVATED_BORDER_AT,
            cooldown > 0,
        )
        if contribution:
            scheduled.append((day + DECAY_DAYS, contribution))
            cooldown = COOLDOWN_DAYS
        assert active == (cooldown > 0) or contribution == 0
        assert 0 <= scrutiny <= CAP

    # No new crossings: let every pending contribution and cooldown drain.
    for day in range(365 * 3, 365 * 3 + DECAY_DAYS + COOLDOWN_DAYS + 2):
        due = [amount for due_day, amount in scheduled if due_day == day]
        scheduled = [(due_day, amount) for due_day, amount in scheduled if due_day != day]
        for amount in due:
            scrutiny = recover(scrutiny, amount)
        if cooldown:
            cooldown -= 1
        assert 0 <= scrutiny <= CAP

    assert scrutiny == 0
    assert cooldown == 0
    assert not scheduled


def test_recovery_never_underflows():
    assert recover(1, 2) == 0
    assert recover(0, 1) == 0


if __name__ == "__main__":
    test_contract_text()
    test_no_underworld_history_means_no_scrutiny()
    test_routine_crossings_still_saturate_and_decay_exactly()
    test_elevated_crossing_sets_cooldown_and_blocks_restack()
    test_mixed_pressure_preserves_bounds_and_notice_threshold()
    test_three_year_daily_elevated_attempts_remain_bounded_and_quiet_tail_recovers()
    test_recovery_never_underflows()
    print("A1 Republic customs-scrutiny cooldown contract: PASS")
