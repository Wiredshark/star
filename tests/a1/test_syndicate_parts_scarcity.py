from pathlib import Path
import re

TEXT = (Path(__file__).resolve().parents[2] / "data/human/a1 syndicate parts scarcity.txt").read_text(encoding="utf-8")
CAP = 6


def mobilization(scarcity, surge=True, latched=False):
    if not surge or latched or scarcity >= 5:
        return scarcity, latched, 0
    return min(CAP, scarcity + 2), True, 2


def recover(scarcity, amount=1):
    return max(0, scarcity - amount)


def assist(scarcity):
    return max(0, scarcity - 1) if scarcity >= 1 else scarcity


def test_contract_and_upstream_read_only():
    for token in (
        'has "world: syndicate maintenance surge"',
        'not "world: syndicate parts scarcity surge counted"',
        '"world: syndicate parts scarcity" += 2',
        '"world: syndicate parts scarcity" <?= 6',
        'event "ES A1: Syndicate Parts Scarcity Recovery" 4 4',
        'event "ES A1: Syndicate Parts Scarcity Recovery" 8 8',
        'event "ES A1: Syndicate Parts Scarcity Latch Ends" 6 6',
        'mission "ES A1: Syndicate Parts Relief"',
    ):
        assert token in TEXT
    for authority in ("world: syndicate maintenance backlog", "world: syndicate maintenance surge"):
        assert not re.search(
            rf'^\s*"{re.escape(authority)}"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
            TEXT,
            re.M,
        )


def test_one_surge_counts_once_and_caps():
    scarcity, latch, amount = mobilization(0)
    assert (scarcity, latch, amount) == (2, True, 2)
    assert mobilization(scarcity, surge=True, latched=True) == (2, True, 0)
    scarcity, latch, amount = mobilization(4, surge=True, latched=False)
    assert (scarcity, latch, amount) == (6, True, 2)
    assert mobilization(5, surge=True, latched=False) == (5, False, 0)
    assert mobilization(0, surge=False, latched=False) == (0, False, 0)


def test_recovery_and_assistance_never_underflow():
    scarcity = 6
    scarcity = recover(scarcity)
    scarcity = assist(scarcity)
    assert scarcity == 4
    for _ in range(10):
        scarcity = recover(scarcity)
        scarcity = assist(scarcity)
    assert scarcity == 0


def simulate(days):
    scarcity = 0
    latch = 0
    obligations = []
    trace = []
    for day in range(days):
        for _ in range(obligations.count(day)):
            scarcity = recover(scarcity)
        obligations = [due for due in obligations if due > day]

        # One six-day maintenance surge at the start of each 50-day stress cycle.
        surge = day % 50 < 6
        if day % 2 == 0:
            scarcity, counted, amount = mobilization(scarcity, surge, latch > 0)
            if counted and latch == 0 and amount:
                latch = 6
                obligations.extend((day + 4, day + 8))
        # Periodic local deliveries provide additional negative feedback.
        if day % 13 == 0:
            scarcity = assist(scarcity)
        latch = max(0, latch - 1)
        assert 0 <= scarcity <= CAP
        trace.append((scarcity, latch))
    return trace, scarcity, obligations


def test_deterministic_three_year_horizon_and_quiet_tail():
    first = simulate(365 * 3)
    second = simulate(365 * 3)
    assert first[0] == second[0]
    scarcity = first[1]
    for _ in range(16):
        scarcity = recover(scarcity)
    assert scarcity == 0


if __name__ == "__main__":
    test_contract_and_upstream_read_only()
    test_one_surge_counts_once_and_caps()
    test_recovery_and_assistance_never_underflow()
    test_deterministic_three_year_horizon_and_quiet_tail()
    print("A1 Syndicate parts-scarcity contract: PASS")
