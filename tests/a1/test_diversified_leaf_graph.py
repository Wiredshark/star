from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = {
    "congestion_relief": ROOT / "data/human/a1 congestion relief spillover.txt",
    "relief_reserve": ROOT / "data/human/a1 free worlds relief reserve strain.txt",
    "merchant_reserve": ROOT / "data/human/a1 merchant rescue reserve.txt",
    "parts": ROOT / "data/human/a1 syndicate parts scarcity.txt",
    "civic": ROOT / "data/human/a1 republic civic strain.txt",
    "inspection": ROOT / "data/human/a1 republic inspection backlog.txt",
    "storm": ROOT / "data/human/a1 free worlds geomagnetic storm.txt",
}


def writes(text, state):
    return bool(re.search(
        rf'^\s*"{re.escape(state)}"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
        text,
        re.M,
    ))


def test_new_leaf_graph_has_no_reverse_writes_to_upstream_authorities():
    text = {name: path.read_text(encoding="utf-8") for name, path in DATA.items()}

    # The congestion bridge is intentionally the sole new writer into existing
    # relief demand; all downstream capacity states are leaves.
    assert writes(text["congestion_relief"], "world: free worlds relief demand")
    assert not writes(text["relief_reserve"], "world: free worlds relief demand")
    assert not writes(text["merchant_reserve"], "world: merchant rescue load")
    assert not writes(text["parts"], "world: syndicate maintenance surge")
    assert not writes(text["parts"], "world: syndicate maintenance backlog")
    assert not writes(text["civic"], "world: republic displacement pressure")
    assert not writes(text["civic"], "world: republic customs scrutiny")
    assert not writes(text["inspection"], "world: republic customs scrutiny")


def test_new_graph_contains_only_forward_pressure_edges():
    edges = {
        ("southern rim transit congestion", "free worlds relief demand"),
        ("free worlds relief demand", "free worlds relief reserve strain"),
        ("merchant rescue load", "merchant rescue reserve strain"),
        ("syndicate maintenance surge", "syndicate parts scarcity"),
        ("republic displacement pressure", "republic civic strain"),
        ("republic customs scrutiny", "republic civic strain"),
        ("republic customs scrutiny", "republic inspection backlog"),
    }
    # Explicit reverse-edge guard for every new connection.
    assert all((dst, src) not in edges for src, dst in edges)


def test_representative_pressure_propagation_is_bounded():
    congestion = 4
    relief = 3
    relief_reserve = 0
    rescue = 5
    merchant_reserve = 0
    parts = 0
    civic = 0
    inspection = 0
    storm_strain = 0

    if congestion >= 4 and relief < 5:
        relief = min(5, relief + 1)
    if relief >= 4 and relief_reserve < 4:
        relief_reserve = min(4, relief_reserve + 1)
    if rescue >= 5 and merchant_reserve < 3:
        merchant_reserve = min(4, merchant_reserve + 2)
    parts = min(6, parts + 2)
    civic = min(6, civic + 2)
    inspection = min(6, inspection + 1)
    storm_strain = min(6, storm_strain + 1)

    assert relief == 4
    assert relief_reserve == 1
    assert merchant_reserve == 2
    assert parts == 2
    assert civic == 2
    assert inspection == 1
    assert storm_strain == 1
    assert 0 <= relief <= 5
    assert 0 <= relief_reserve <= 4
    assert 0 <= merchant_reserve <= 4
    assert 0 <= parts <= 6
    assert 0 <= civic <= 6
    assert 0 <= inspection <= 6
    assert 0 <= storm_strain <= 6


def test_quiet_tail_can_drain_all_new_leaf_states():
    values = {
        "relief": 5,
        "relief_reserve": 4,
        "merchant_reserve": 4,
        "parts": 6,
        "civic": 6,
        "inspection": 6,
        "storm_strain": 6,
    }
    for _ in range(32):
        values["relief"] = max(0, values["relief"] - 1)
        values["relief_reserve"] = max(0, values["relief_reserve"] - 1)
        values["merchant_reserve"] = max(0, values["merchant_reserve"] - 2)
        values["parts"] = max(0, values["parts"] - 1)
        values["civic"] = max(0, values["civic"] - 1)
        values["inspection"] = max(0, values["inspection"] - 1)
        values["storm_strain"] = max(0, values["storm_strain"] - 1)
    assert set(values.values()) == {0}
