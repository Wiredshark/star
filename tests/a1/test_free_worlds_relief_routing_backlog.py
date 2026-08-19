from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 free worlds relief routing backlog.txt"
TEXT = DATA.read_text(encoding="utf-8")
BACKLOG_CAP = 4
RELIEF_CAP = 5


def observe(backlog, relief, congestion, latched=False):
    if latched or relief < 3 or congestion < 3 or backlog >= BACKLOG_CAP:
        return backlog, False
    return min(BACKLOG_CAP, backlog + 1), True


def feedback(relief, backlog, latched=False):
    if latched or backlog < 2 or relief >= RELIEF_CAP:
        return relief, False
    return min(RELIEF_CAP, relief + 1), True


def recover(value, amount=1):
    return max(0, value - amount)


def test_contract_text():
    assert 'mission "ES A1: Free Worlds Relief Routing Backlog"' in TEXT
    assert 'mission "ES A1: Free Worlds Relief Routing Feedback"' in TEXT
    assert 'event "ES A1: Free Worlds Relief Routing Backlog Recovery"' in TEXT
    assert '"world: free worlds relief demand" >= 3' in TEXT
    assert '"world: southern rim transit congestion" >= 3' in TEXT
    assert '"world: free worlds relief routing backlog" < 4' in TEXT
    assert '"world: free worlds relief routing backlog" += 1' in TEXT
    assert 'event "ES A1: Free Worlds Relief Routing Backlog Recovery" 6 6' in TEXT
    assert '"world: free worlds relief routing backlog" >= 2' in TEXT
    assert '"world: free worlds relief demand" < 5' in TEXT
    assert '"world: free worlds relief demand" += 1' in TEXT
    assert 'event "ES A1: Free Worlds Relief Demand Recovery" 4 4' in TEXT


def test_backlog_requires_both_inputs_and_saturates():
    assert observe(0, 2, 5) == (0, False)
    assert observe(0, 5, 2) == (0, False)
    value = 0
    accepted = 0
    for _ in range(8):
        value, did = observe(value, 5, 5)
        accepted += int(did)
    assert value == 4
    assert accepted == 4
    for _ in range(accepted + 2):
        value = recover(value)
    assert value == 0


def test_feedback_is_bounded_and_exactly_recoverable():
    relief = 3
    relief, did = feedback(relief, backlog=1)
    assert (relief, did) == (3, False)
    contributions = 0
    for _ in range(5):
        relief, did = feedback(relief, backlog=3)
        contributions += int(did)
    assert relief == 5
    assert contributions == 2
    for _ in range(contributions):
        relief = recover(relief)
    assert relief == 3


def test_latches_break_same_crossing_retrigger_loops():
    assert observe(1, 4, 4, latched=True) == (1, False)
    assert feedback(4, backlog=3, latched=True) == (4, False)


def test_long_horizon_no_runaway_or_underflow():
    backlog = 0
    relief = 3
    for day in range(365):
        backlog, _ = observe(backlog, relief, 4, latched=(day % 2 == 1))
        relief, _ = feedback(relief, backlog, latched=(day % 3 != 0))
        if day % 6 == 5:
            backlog = recover(backlog)
        if day % 4 == 3:
            relief = recover(relief)
        assert 0 <= backlog <= BACKLOG_CAP
        assert 0 <= relief <= RELIEF_CAP


if __name__ == "__main__":
    test_contract_text()
    test_backlog_requires_both_inputs_and_saturates()
    test_feedback_is_bounded_and_exactly_recoverable()
    test_latches_break_same_crossing_retrigger_loops()
    test_long_horizon_no_runaway_or_underflow()
    print("A1 Free Worlds relief-routing backlog contract: PASS")
