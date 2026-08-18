from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 relief demand.txt"
TEXT = DATA.read_text(encoding="utf-8")

CONDITION = "world: free worlds relief demand"
CAP = 5
NOTICE = 3

def arrival(value):
    if value >= CAP:
        return value, False
    return min(CAP, value + 1), True

def recover(value):
    return max(0, value - 1)

def test_contract_text():
    assert 'event "ES A1: Free Worlds Relief Demand Recovery"' in TEXT
    assert 'mission "ES A1: Free Worlds Relief Demand"' in TEXT
    assert 'mission "ES A1: Free Worlds Relief Demand Notice"' in TEXT
    assert 'government "Free Worlds"' in TEXT
    assert 'has "previous system government: Pirate"' in TEXT
    assert f'"{CONDITION}" < 5' in TEXT
    assert f'"{CONDITION}" += 1' in TEXT
    assert f'"{CONDITION}" <?= 5' in TEXT
    assert f'"{CONDITION}" -= 1' in TEXT
    assert f'"{CONDITION}" >?= 0' in TEXT
    assert 'event "ES A1: Free Worlds Relief Demand Recovery" 4 4' in TEXT
    assert f'"{CONDITION}" >= 3' in TEXT

def test_saturation_and_one_to_one_recovery():
    value = 0
    scheduled = 0
    trajectory = [value]
    for _ in range(8):
        value, accepted = arrival(value)
        scheduled += int(accepted)
        trajectory.append(value)
    assert trajectory == [0, 1, 2, 3, 4, 5, 5, 5, 5]
    assert scheduled == CAP
    recovery = [value]
    for _ in range(scheduled + 2):
        value = recover(value)
        recovery.append(value)
    assert recovery == [5, 4, 3, 2, 1, 0, 0, 0]

def test_notice_threshold_and_re_elevation():
    value = 0
    visible = []
    for _ in range(5):
        value, _ = arrival(value)
        visible.append(value >= NOTICE)
    assert visible == [False, False, True, True, True]
    for _ in range(4):
        value = recover(value)
    assert value == 1
    assert value < NOTICE
    value, accepted = arrival(value)
    assert accepted and value == 2
    value, accepted = arrival(value)
    assert accepted and value == 3
    assert value >= NOTICE

if __name__ == "__main__":
    test_contract_text()
    test_saturation_and_one_to_one_recovery()
    test_notice_threshold_and_re_elevation()
    print("A1 relief-demand contract: PASS")
