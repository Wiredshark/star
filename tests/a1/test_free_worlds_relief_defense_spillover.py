from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RELIEF = ROOT / "data/human/a1 relief demand.txt"
DEFENSE = ROOT / "data/human/a1 free worlds defense strain.txt"
BRIDGE = ROOT / "data/human/a1 free worlds relief defense spillover.txt"


def apply_spillover(defense_strain, relief_demand, latch=False):
    if relief_demand >= 4 and defense_strain < 5 and not latch:
        return min(5, defense_strain + 1), True
    return defense_strain, latch


def recover_defense(defense_strain):
    return max(0, defense_strain - 1)


def test_contract_reuses_authoritative_states_and_keeps_relief_read_only():
    relief = RELIEF.read_text(encoding="utf-8")
    defense = DEFENSE.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert '"world: free worlds relief demand" += 1' in relief
    assert '"world: free worlds defense strain" += 1' in defense
    for token in (
        '"world: free worlds relief demand" >= 4',
        '"world: free worlds defense strain" < 5',
        'not "world: free worlds relief defense spillover active"',
        'set "world: free worlds relief defense spillover active"',
        '"world: free worlds defense strain" += 1',
        '"world: free worlds defense strain" <?= 5',
        'event "ES A1: Free Worlds Defense Strain Recovery" 6 6',
        'event "ES A1: Free Worlds Relief Defense Spillover Latch Ends" 6 6',
        'clear "world: free worlds relief defense spillover active"',
    ):
        assert token in bridge

    assert '"world: free worlds relief demand" +=' not in bridge
    assert '"world: free worlds relief demand" -=' not in bridge


def test_threshold_cap_and_latch_behavior():
    assert apply_spillover(0, 3, False) == (0, False)
    assert apply_spillover(0, 4, False) == (1, True)
    assert apply_spillover(4, 6, False) == (5, True)
    assert apply_spillover(5, 6, False) == (5, False)

    defense, latch = apply_spillover(2, 5, False)
    assert (defense, latch) == (3, True)
    assert apply_spillover(defense, 5, latch) == (3, True)
    assert apply_spillover(defense, 5, False) == (4, True)


def test_quiet_recovery_and_upstream_resolution():
    defense, latch = apply_spillover(0, 5, False)
    assert (defense, latch) == (1, True)
    for _ in range(6):
        defense = recover_defense(defense)
    assert defense == 0
    assert apply_spillover(defense, 2, False) == (0, False)


def test_deterministic_three_year_horizon_is_bounded_and_recovers():
    defense = 0
    latch_days = 0
    for day in range(365 * 3):
        relief = 5 if day % 210 < 84 else 2
        if day % 3 == 0:
            defense, activated = apply_spillover(
                defense,
                relief,
                latch=latch_days > 0,
            )
            if activated and latch_days == 0:
                latch_days = 6
        if day % 6 == 5:
            defense = recover_defense(defense)
        latch_days = max(0, latch_days - 1)
        assert 0 <= defense <= 5

    for _ in range(8):
        defense = recover_defense(defense)
    assert defense == 0


if __name__ == "__main__":
    test_contract_reuses_authoritative_states_and_keeps_relief_read_only()
    test_threshold_cap_and_latch_behavior()
    test_quiet_recovery_and_upstream_resolution()
    test_deterministic_three_year_horizon_is_bounded_and_recovers()
    print("A1 Free Worlds relief -> defense strain spillover: PASS")
