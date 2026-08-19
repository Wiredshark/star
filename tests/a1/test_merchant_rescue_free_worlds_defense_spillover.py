from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MERCHANT = ROOT / "data/human/a1 merchant rescue load.txt"
DEFENSE = ROOT / "data/human/a1 free worlds defense strain.txt"
BRIDGE = ROOT / "data/human/a1 merchant rescue free worlds defense spillover.txt"


def apply_spillover(defense_strain, merchant_rescue_load, latch=False):
    if merchant_rescue_load >= 3 and defense_strain < 5 and not latch:
        return min(5, defense_strain + 1), True
    return defense_strain, latch


def recover_defense(defense_strain):
    return max(0, defense_strain - 1)


def test_contract_reuses_existing_state_and_preserves_upstream_ownership():
    merchant = MERCHANT.read_text(encoding="utf-8")
    defense = DEFENSE.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert '"world: merchant rescue load" += 1' in merchant
    assert 'event "ES A1: Merchant Rescue Load Recovery" 5 5' in merchant
    assert '"world: free worlds defense strain" += 1' in defense
    assert 'event "ES A1: Free Worlds Defense Strain Recovery" 6 6' in defense

    for token in (
        '"world: merchant rescue load" >= 3',
        '"world: free worlds defense strain" < 5',
        'not "world: merchant rescue free worlds defense spillover active"',
        'set "world: merchant rescue free worlds defense spillover active"',
        '"world: free worlds defense strain" += 1',
        '"world: free worlds defense strain" <?= 5',
        'event "ES A1: Free Worlds Defense Strain Recovery" 6 6',
        'event "ES A1: Merchant Rescue Free Worlds Defense Spillover Latch Ends" 6 6',
        'clear "world: merchant rescue free worlds defense spillover active"',
    ):
        assert token in bridge

    assert '"world: merchant rescue load" +=' not in bridge
    assert '"world: merchant rescue load" -=' not in bridge


def test_threshold_cap_and_latch_behavior():
    assert apply_spillover(0, 2, False) == (0, False)
    assert apply_spillover(0, 3, False) == (1, True)
    assert apply_spillover(4, 5, False) == (5, True)
    assert apply_spillover(5, 5, False) == (5, False)

    defense, latch = apply_spillover(2, 5, False)
    assert (defense, latch) == (3, True)
    assert apply_spillover(defense, 5, latch) == (3, True)


def test_quiet_recovery_and_source_resolution():
    defense, latch = apply_spillover(1, 5, False)
    assert (defense, latch) == (2, True)
    for _ in range(2):
        defense = recover_defense(defense)
    assert defense == 0
    assert apply_spillover(defense, 1, False) == (0, False)


def test_deterministic_three_year_horizon_is_bounded_and_recovers():
    defense = 0
    latch_days = 0
    for day in range(365 * 3):
        rescue_load = 5 if day % 120 < 42 else 1
        if day % 2 == 0:
            defense, activated = apply_spillover(
                defense,
                rescue_load,
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
    test_contract_reuses_existing_state_and_preserves_upstream_ownership()
    test_threshold_cap_and_latch_behavior()
    test_quiet_recovery_and_source_resolution()
    test_deterministic_three_year_horizon_is_bounded_and_recovers()
    print("A1 Merchant rescue -> Free Worlds defense spillover: PASS")
