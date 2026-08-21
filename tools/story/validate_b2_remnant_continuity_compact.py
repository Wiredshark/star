from pathlib import Path
import re
import sys

DEFAULT_PATH = Path(__file__).resolve().parents[2] / "data/remnant/b2 remnant continuity compact.txt"
PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
TEXT = PATH.read_text()

MISSIONS = [
    "B2 Remnant Continuity Compact: Offer",
    "B2 Remnant Continuity Compact: Review",
    "B2 Remnant Continuity Compact: Taal Remembers",
]
B2_PREFIX = "B2 Remnant Continuity Compact:"


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
    require("Nera Venn")
    require("Corin Taal")
    require('government "Remnant"')
    require("reserve")
    require("provenance")


def test_persistent_routes_and_refusal():
    for route in ("continuity", "provenance", "compact"):
        require(f'"{B2_PREFIX} route {route}" = 1')
    require(f'"{B2_PREFIX} declined" = 1')
    offer = mission_blocks()[MISSIONS[0]]
    assert offer.count("\n\t\t\tchoice\n") == 1
    for target in ("continuity", "provenance", "compact", "decline"):
        assert offer.count(f"goto {target}") == 1, f"Offer route {target} is missing or duplicated"


def test_review_and_terminal_settlements():
    review = mission_blocks()[MISSIONS[1]]
    require(f'"{B2_PREFIX} reviewed" = 1')
    settlements = [
        f'"{B2_PREFIX} settlement custody reconciliation" = 1',
        f'"{B2_PREFIX} settlement two key reserve" = 1',
    ]
    for settlement in settlements:
        require(settlement)
    assert sum(TEXT.count(x) for x in settlements) == 2
    assert review.count("goto custodysettlement") == 3
    assert review.count("goto twokeysettlement") == 3


def test_later_reader_consumes_both_outcomes():
    reader = mission_blocks()[MISSIONS[2]]
    require(f'has "{B2_PREFIX} settlement custody reconciliation"')
    require(f'has "{B2_PREFIX} settlement two key reserve"')
    assert reader.count(f'"{B2_PREFIX} aftermath seen" = 1') == 1


def test_state_only_dialogue_lifecycle():
    # These missions only record persistent dialogue/global state; they do not
    # create cargo, destination, NPC, waypoint, timer, or other playable objectives.
    # Terminal paths must therefore close with decline rather than accept, otherwise
    # an objective-less mission can remain active after its conversation ends.
    assert not re.search(r'^\s*accept\s*$', TEXT, re.M), "state-only B2 slice must not leave accepted missions active"
    declines = re.findall(r'^\s*decline\s*$', TEXT, re.M)
    assert len(declines) == 7, f"expected 7 state-only decline terminals, found {len(declines)}"

    objective_directives = re.compile(
        r'^\s*(?:destination|waypoint|stopover|cargo|passengers|npc|deadline|distance|job|assisting|boarding)\b',
        re.I | re.M,
    )
    assert not objective_directives.search(TEXT), "lifecycle assumption invalidated by objective-bearing mission directives"


def test_no_world_or_material_mutation():
    # Inspect executable data lines, not comments/dialogue prose. B2 may discuss
    # resources in text but must not issue material/reputation/world-state commands.
    forbidden_commands = re.compile(
        r'^\s*(?:payment|credits|reputation|combat rating|cargo|outfit)\b',
        re.I,
    )
    world_write = re.compile(
        r'^\s*"world:[^"]+"\s*(?:=|\+\+|--|\+=|-=|\?=|<\?=|>\?=)',
        re.I,
    )
    for line in TEXT.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("`"):
            continue
        assert not forbidden_commands.match(line), f"unexpected material/reputation command: {stripped}"
        assert not world_write.match(line), f"unexpected world-state mutation: {stripped}"


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
    test_state_only_dialogue_lifecycle()
    test_no_world_or_material_mutation()
    test_local_goto_labels_resolve()
    print("PASS: B2 Remnant Continuity Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Taal Remembers")
    print("PASS: lifecycle=7 state-only decline terminals")
    print("PASS: mutation_surface=B2 conditions only")
