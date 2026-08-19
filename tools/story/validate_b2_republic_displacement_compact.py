from pathlib import Path
import re
import sys

DEFAULT_PATH = Path(__file__).resolve().parents[2] / "data/human/b2 republic displacement compact.txt"
PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
TEXT = PATH.read_text()

MISSIONS = [
    "B2 Republic Displacement Compact: Offer",
    "B2 Republic Displacement Compact: Review",
    "B2 Republic Displacement Compact: Hale Remembers",
]

A1_SIGNAL = 'world: republic displacement pressure'
B2_PREFIX = 'B2 Republic Displacement Compact:'


def require(token):
    assert token in TEXT, f"missing required token: {token}"


def mission_blocks():
    starts = list(re.finditer(r'^mission "([^"]+)"', TEXT, re.M))
    blocks = {}
    for i, match in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(TEXT)
        blocks[match.group(1)] = TEXT[match.start():end]
    return blocks


def test_mission_and_character_contract():
    blocks = mission_blocks()
    assert list(blocks) == MISSIONS, f"unexpected mission list: {list(blocks)}"
    require("Lena Ortiz")
    require("Devin Hale")
    require('government "Republic"')
    require(f'"{A1_SIGNAL}" >= 2')
    require(f'"{A1_SIGNAL}" >= 4')
    require(f'"{A1_SIGNAL}" < 2')


def test_persistent_routes_and_refusal():
    for route in ("continuity", "ledger", "compact"):
        require(f'"{B2_PREFIX} route {route}" = 1')
    require(f'"{B2_PREFIX} declined" = 1')
    offer = mission_blocks()[MISSIONS[0]]
    assert offer.count("\n\t\t\tchoice\n") == 1
    assert offer.count("\n\t\t\t\t`\\t") == 4


def test_review_and_terminal_settlements():
    review = mission_blocks()[MISSIONS[1]]
    assert f'"{A1_SIGNAL}" < 2' in review
    require(f'"{B2_PREFIX} reviewed" = 1')
    settlements = [
        f'"{B2_PREFIX} settlement continuity compact" = 1',
        f'"{B2_PREFIX} settlement bounded review" = 1',
    ]
    for settlement in settlements:
        require(settlement)
    assert sum(TEXT.count(x) for x in settlements) == 2


def test_later_reader_consumes_both_outcomes():
    reader = mission_blocks()[MISSIONS[2]]
    require(f'has "{B2_PREFIX} settlement continuity compact"')
    require(f'has "{B2_PREFIX} settlement bounded review"')
    assert reader.count(f'"{B2_PREFIX} aftermath seen" = 1') == 1


def test_a1_signal_is_read_only():
    for line in TEXT.splitlines():
        if A1_SIGNAL not in line:
            continue
        stripped = line.strip()
        assert not any(op in stripped for op in (" += ", " -= ", " = ", "<?=", ">?=")), \
            f"B2 must not mutate A1 world state: {stripped}"


def test_no_material_or_reputation_rewards():
    lower = TEXT.lower()
    forbidden = (
        "payment ",
        "credits ",
        "reputation ",
        "combat rating",
        "cargo ",
        "outfit ",
    )
    for token in forbidden:
        assert token not in lower, f"unexpected material/reputation mutation surface: {token}"


def test_local_goto_labels_resolve():
    for name, block in mission_blocks().items():
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name} has unresolved goto labels: {missing}"


if __name__ == "__main__":
    test_mission_and_character_contract()
    test_persistent_routes_and_refusal()
    test_review_and_terminal_settlements()
    test_later_reader_consumes_both_outcomes()
    test_a1_signal_is_read_only()
    test_no_material_or_reputation_rewards()
    test_local_goto_labels_resolve()
    print("PASS: B2 Republic Displacement Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: a1_signal=read-only")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Hale Remembers")