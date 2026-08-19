from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data" / "human" / "a1 free worlds defense strain.txt"
TEXT = DATA.read_text(encoding="utf-8")

CAP = 5
MOBILIZE_AT = 3
MOBILIZE_RELIEF = 2


def assist(strain):
    if strain >= CAP:
        return strain, False
    return min(CAP, strain + 1), True


def recover(strain):
    return max(0, strain - 1)


def mobilize(strain, surge):
    if surge or strain < MOBILIZE_AT:
        return strain, surge, False
    return max(0, strain - MOBILIZE_RELIEF), True, True


def test_contract_text():
    assert 'mission "ES A1: Free Worlds Defense Strain"' in TEXT
    assert 'mission "ES A1: Free Worlds Patrol Mobilization"' in TEXT
    assert 'event "ES A1: Free Worlds Defense Strain Recovery"' in TEXT
    assert 'event "ES A1: Free Worlds Patrol Surge Ends"' in TEXT
    assert 'government "Free Worlds"' in TEXT
    assert '"world: free worlds defense strain" < 5' in TEXT
    assert '"world: free worlds defense strain" += 1' in TEXT
    assert '"world: free worlds defense strain" <?= 5' in TEXT
    assert '"world: free worlds defense strain" >= 3' in TEXT
    assert '"world: free worlds defense strain" -= 2' in TEXT
    assert '"world: free worlds defense strain" >?= 0' in TEXT
    assert 'set "world: free worlds patrol surge"' in TEXT
    assert 'clear "world: free worlds patrol surge"' in TEXT
    assert 'event "ES A1: Free Worlds Defense Strain Recovery" 6 6' in TEXT
    assert 'event "ES A1: Free Worlds Patrol Surge Ends" 5 5' in TEXT


def test_saturation_and_recovery():
    strain = 0
    scheduled = 0
    for _ in range(8):
        strain, accepted = assist(strain)
        scheduled += int(accepted)
    assert strain == 5
    assert scheduled == 5

    path = [strain]
    for _ in range(7):
        strain = recover(strain)
        path.append(strain)
    assert path == [5, 4, 3, 2, 1, 0, 0, 0]


def test_mobilization_feedback():
    strain = 0
    surge = False
    for _ in range(3):
        strain, accepted = assist(strain)
        assert accepted
    assert strain == 3

    strain, surge, fired = mobilize(strain, surge)
    assert fired and surge and strain == 1
    assert mobilize(strain, surge) == (1, True, False)

    surge = False
    for _ in range(2):
        strain, accepted = assist(strain)
        assert accepted
    assert strain == 3
    strain, surge, fired = mobilize(strain, surge)
    assert fired and surge and strain == 1


def test_independent_recovery_events_do_not_underflow():
    strain = 0
    scheduled = []
    for day in [0, 0, 1, 1, 2, 3]:
        strain, accepted = assist(strain)
        if accepted:
            scheduled.append(day + 6)
    assert strain == 5
    assert len(scheduled) == 5

    for day in range(6, 12):
        for due in [d for d in scheduled if d == day]:
            strain = recover(strain)
    assert strain == 0


if __name__ == "__main__":
    test_contract_text()
    test_saturation_and_recovery()
    test_mobilization_feedback()
    test_independent_recovery_events_do_not_underflow()
    print("A1 Free Worlds defense-strain contract: PASS")
