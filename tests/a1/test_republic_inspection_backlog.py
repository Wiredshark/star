from pathlib import Path

TEXT = (
    Path(__file__).resolve().parents[2]
    / "data/human/a1 republic inspection backlog.txt"
).read_text()


def accrue(backlog: int, scrutiny: int):
    if scrutiny < 3 or backlog >= 6:
        return backlog, False
    return min(6, backlog + 1), True


def recover(backlog: int):
    return max(0, backlog - 1)


def surge(backlog: int, scrutiny: int, active: bool):
    if active or backlog < 4:
        return backlog, scrutiny, active, False
    return max(0, backlog - 3), max(0, scrutiny - 1), True, True


def test_contract_tokens_present():
    expected = [
        '"world: republic customs scrutiny" >= 3',
        '"world: republic inspection backlog" < 6',
        '"world: republic inspection backlog" += 1',
        'event "ES A1: Republic Inspection Backlog Recovery" 6 6',
        '"world: republic inspection backlog" >= 4',
        'set "world: republic inspection surge"',
        '"world: republic inspection backlog" -= 3',
        '"world: republic customs scrutiny" -= 1',
        'event "ES A1: Republic Inspection Surge Ends" 5 5',
    ]
    for token in expected:
        assert token in TEXT


def test_backlog_is_bounded_and_requires_elevated_scrutiny():
    backlog = 0
    scheduled = 0
    for _ in range(10):
        backlog, added = accrue(backlog, scrutiny=3)
        scheduled += int(added)
    assert (backlog, scheduled) == (6, 6)
    assert accrue(6, scrutiny=6) == (6, False)
    assert accrue(0, scrutiny=2) == (0, False)


def test_recovery_cannot_underflow():
    backlog = 6
    for _ in range(12):
        backlog = recover(backlog)
    assert backlog == 0


def test_capacity_surge_closes_the_feedback_loop():
    backlog, scrutiny, active, fired = surge(4, 5, False)
    assert (backlog, scrutiny, active, fired) == (1, 4, True, True)

    # Cooldown makes repeat arrivals inert until the surge ends.
    assert surge(6, 6, active) == (6, 6, True, False)

    # Once the cooldown clears, another severe queue can mobilize again.
    backlog, scrutiny, active, fired = surge(6, 4, False)
    assert (backlog, scrutiny, active, fired) == (3, 3, True, True)


def test_seeded_accelerated_horizons_are_deterministic_and_bounded():
    def run(days: int):
        backlog = 0
        scrutiny = 4
        active_until = -1
        recoveries = []
        trace = []
        for day in range(days):
            # Deterministic synthetic arrival pressure: two of every three days.
            if day % 3 != 2:
                backlog, added = accrue(backlog, scrutiny)
                if added:
                    recoveries.append(day + 6)

            due = recoveries.count(day)
            for _ in range(due):
                backlog = recover(backlog)

            active = day < active_until
            backlog, scrutiny, active, fired = surge(backlog, scrutiny, active)
            if fired:
                active_until = day + 5

            assert 0 <= backlog <= 6
            assert 0 <= scrutiny <= 6
            trace.append((day, backlog, scrutiny, active_until))
        return trace

    for horizon in (30, 180, 720):
        first = run(horizon)
        second = run(horizon)
        assert first == second
        assert max(row[1] for row in first) <= 6
        assert min(row[1] for row in first) >= 0
        assert min(row[2] for row in first) >= 0


if __name__ == "__main__":
    test_contract_tokens_present()
    test_backlog_is_bounded_and_requires_elevated_scrutiny()
    test_recovery_cannot_underflow()
    test_capacity_surge_closes_the_feedback_loop()
    test_seeded_accelerated_horizons_are_deterministic_and_bounded()
    print("A1 Republic inspection-backlog contract: PASS")
