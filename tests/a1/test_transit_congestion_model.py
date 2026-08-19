from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 transit congestion.txt"
TEXT = DATA.read_text(encoding="utf-8")

CONDITION = "world: southern rim transit congestion"
CAP = 6
DECAY = 1

def cross(value):
    if value >= CAP:
        return value, False
    return min(CAP, value + 1), True

def decay(value):
    return max(0, value - DECAY)

def test_contract_text():
    assert 'mission "ES A1: Southern Rim Transit Congestion"' in TEXT
    assert 'event "ES A1: Southern Rim Transit Congestion Decay"' in TEXT
    assert 'government "Free Worlds"' in TEXT
    assert 'neighbor government "Republic" "Neutral" "Independent"' in TEXT
    assert 'has "previous system government: Republic"' in TEXT
    assert 'has "previous system government: Neutral"' in TEXT
    assert 'has "previous system government: Independent"' in TEXT
    assert f'"{CONDITION}" < 6' in TEXT
    assert f'"{CONDITION}" += 1' in TEXT
    assert f'"{CONDITION}" <?= 6' in TEXT
    assert f'"{CONDITION}" -= 1' in TEXT
    assert f'"{CONDITION}" >?= 0' in TEXT
    assert 'event "ES A1: Southern Rim Transit Congestion Decay" 3 3' in TEXT
    assert f'"{CONDITION}" >= 4' in TEXT

def test_saturation_and_decay():
    value = 0
    scheduled = 0
    for _ in range(10):
        value, did_schedule = cross(value)
        scheduled += int(did_schedule)
    assert value == 6
    assert scheduled == 6

    trajectory = [value]
    for _ in range(8):
        value = decay(value)
        trajectory.append(value)

    assert trajectory == [6, 5, 4, 3, 2, 1, 0, 0, 0]

def test_recovery_matches_accepted_crossings():
    value = 0
    scheduled = []
    for day in [0, 0, 1, 1, 2, 2, 2, 2]:
        value, accepted = cross(value)
        if accepted:
            scheduled.append(day + 3)

    assert value == 6
    assert len(scheduled) == 6

    for day in range(3, 7):
        for due in [d for d in scheduled if d == day]:
            value = decay(value)
    assert value == 0

if __name__ == "__main__":
    test_contract_text()
    test_saturation_and_decay()
    test_recovery_matches_accepted_crossings()
    print("A1 transit congestion contract: PASS")
