from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CUSTOMS = ROOT / "data/human/a1 republic customs scrutiny.txt"
TRANSIT = ROOT / "data/human/a1 transit congestion.txt"
BRIDGE = ROOT / "data/human/a1 republic customs transit spillover.txt"


def apply_border_crossing(congestion, scrutiny, diversion_latched=False):
    """Compact deterministic model of the new bridge only."""
    if scrutiny >= 3 and not diversion_latched and congestion < 6:
        congestion = min(6, congestion + 1)
        diversion_latched = True
    return congestion, diversion_latched


def decay(congestion):
    return max(0, congestion - 1)


def test_contract_reuses_existing_authoritative_states():
    customs = CUSTOMS.read_text(encoding="utf-8")
    transit = TRANSIT.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")

    assert '"world: republic customs scrutiny" += 1' in customs
    assert '"world: southern rim transit congestion" += 1' in transit
    for token in (
        'has "previous system government: Republic"',
        '"world: republic customs scrutiny" >= 3',
        'not "world: republic customs diversion load"',
        '"world: southern rim transit congestion" += 1',
        '"world: southern rim transit congestion" <?= 6',
        'event "ES A1: Southern Rim Transit Congestion Decay" 3 3',
        'event "ES A1: Republic Customs Diversion Load Ends" 2 2',
        'clear "world: republic customs diversion load"',
    ):
        assert token in bridge


def test_scrutiny_threshold_and_capacity_bound():
    assert apply_border_crossing(0, scrutiny=2, diversion_latched=False) == (0, False)
    assert apply_border_crossing(0, scrutiny=3, diversion_latched=False) == (1, True)
    assert apply_border_crossing(5, scrutiny=6, diversion_latched=False) == (6, True)
    assert apply_border_crossing(6, scrutiny=6, diversion_latched=False) == (6, False)


def test_two_day_latch_blocks_rapid_repeat_amplification():
    congestion, latch = apply_border_crossing(1, scrutiny=4, diversion_latched=False)
    assert (congestion, latch) == (2, True)
    congestion, latch = apply_border_crossing(congestion, scrutiny=4, diversion_latched=latch)
    assert (congestion, latch) == (2, True)
    latch = False
    congestion, latch = apply_border_crossing(congestion, scrutiny=4, diversion_latched=latch)
    assert (congestion, latch) == (3, True)


def test_deterministic_year_horizon_is_bounded_and_recovers():
    congestion = 0
    latch_days = 0
    # Fixed scrutiny phases and crossing cadence make this a reproducible horizon
    # check without introducing a second simulation implementation.
    for day in range(365):
        scrutiny = 5 if day < 120 else (3 if day < 240 else 0)
        if day % 4 == 0:
            before_latch = latch_days > 0
            congestion, latched = apply_border_crossing(
                congestion,
                scrutiny=scrutiny,
                diversion_latched=before_latch,
            )
            if latched and not before_latch:
                latch_days = 2
        if day % 3 == 2:
            congestion = decay(congestion)
        latch_days = max(0, latch_days - 1)
        assert 0 <= congestion <= 6

    for _ in range(12):
        congestion = decay(congestion)
    assert congestion == 0


if __name__ == "__main__":
    test_contract_reuses_existing_authoritative_states()
    test_scrutiny_threshold_and_capacity_bound()
    test_two_day_latch_blocks_rapid_repeat_amplification()
    test_deterministic_year_horizon_is_bounded_and_recovers()
    print("A1 Republic customs transit spillover contract: PASS")
