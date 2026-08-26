#!/usr/bin/env python3
"""Focused structural validation for B2 Republic Former Smuggler Cooperation Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 republic former smuggler cooperation compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Republic Former Smuggler Cooperation Compact: "
EVENT = 'event "B2 Republic Former Smuggler Cooperation Compact: Review Ready"'

MISSIONS = [
    "B2 Republic Former Smuggler Cooperation Compact: Offer",
    "B2 Republic Former Smuggler Cooperation Compact: Review",
    "B2 Republic Former Smuggler Cooperation Compact: Davin Remembers",
]
ROUTES = ["route completed history", "route fresh agreement", "route paired status"]
SETTLEMENTS = ["settlement fresh cause", "settlement bounded cooperation"]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def label_block(mission: str, label: str) -> str:
    block = mission_block(mission)
    marker = f"\t\t\tlabel {label}\n"
    start = block.index(marker)
    nxt = block.find("\n\t\t\tlabel ", start + len(marker))
    return block[start:] if nxt < 0 else block[start:nxt]


def assignment_count(block: str, suffix: str) -> int:
    return len(re.findall(
        rf'^\s*"{re.escape(PREFIX + suffix)}"\s*=\s*1\s*$', block, re.M
    ))


def test_header_graph_and_inputs():
    assert TEXT.startswith("# Copyright (c) 2026 by Wiredshark\n")
    assert TEXT.endswith("\n")
    assert TEXT.count('mission "B2 Republic Former Smuggler Cooperation Compact:') == 3
    for mission in MISSIONS:
        assert f'mission "{mission}"' in TEXT
    assert TEXT.count('\nevent "B2 Republic Former Smuggler Cooperation Compact: Review Ready"\n') == 1
    assert TEXT.count(EVENT + " 7 11") == 3

    offer = mission_block(MISSIONS[0]).split("\ton offer\n", 1)[0]
    assert '"pirate jobs" >= 3' in offer
    assert '"world: republic customs scrutiny" >= 3' in offer
    assert '"world: republic border pressure" >= 3' in offer


def test_characters_scope_and_read_only_inputs():
    assert "Rhea Markel" in TEXT
    assert "Davin Sorn" in TEXT
    for mission in MISSIONS:
        block = mission_block(mission)
        assert '\tsource "Earth"\n' in block

    # Inputs are conditions only; B2 must not take ownership of them.
    for key in (
        "pirate jobs",
        "world: republic customs scrutiny",
        "world: republic border pressure",
    ):
        assert not re.search(
            rf'^\s*"{re.escape(key)}"\s*(?:=|\+=|-=|\+\+|--|\?=|>\?=|<\?=)',
            TEXT,
            re.M,
        ), key


def test_offer_route_local_writes_schedule_and_refusal():
    offer = MISSIONS[0]
    mapping = {
        "closed": "route completed history",
        "fresh": "route fresh agreement",
        "paired": "route paired status",
    }
    for label, own_route in mapping.items():
        block = label_block(offer, label)
        assert assignment_count(block, "introduced") == 1, label
        assert assignment_count(block, own_route) == 1, label
        for other in ROUTES:
            if other != own_route:
                assert assignment_count(block, other) == 0, (label, other)
        assert block.count(EVENT + " 7 11") == 1, label
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1, label
        assert not re.search(r'^\s*accept\s*$', block, re.M), label

    refusal = label_block(offer, "refuse")
    assert assignment_count(refusal, "declined") == 1
    assert assignment_count(refusal, "introduced") == 0
    for route in ROUTES:
        assert assignment_count(refusal, route) == 0
    assert EVENT + " 7 11" not in refusal
    assert len(re.findall(r'^\s*decline\s*$', refusal, re.M)) == 1


def test_review_lifecycle_and_route_wiring():
    review = mission_block(MISSIONS[1])
    to_offer = review.split("\ton offer\n", 1)[0]
    assert f'has "{PREFIX}introduced"' in to_offer
    assert f'has "{PREFIX}review ready"' in to_offer
    assert f'not "{PREFIX}reviewed"' in to_offer

    assert f'branch fresh\n\t\t\t\thas "{PREFIX}route fresh agreement"' in review
    assert f'branch paired\n\t\t\t\thas "{PREFIX}route paired status"' in review
    # Completed-history is intentionally the default/fallthrough Review presentation.
    assert "branch closed" not in review


def test_settlement_local_closure():
    review = MISSIONS[1]
    mapping = {
        "cause": "settlement fresh cause",
        "bounded": "settlement bounded cooperation",
    }
    for label, own_settlement in mapping.items():
        block = label_block(review, label)
        assert assignment_count(block, "reviewed") == 1, label
        assert assignment_count(block, own_settlement) == 1, label
        for other in SETTLEMENTS:
            if other != own_settlement:
                assert assignment_count(block, other) == 0, (label, other)
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1, label
        assert not re.search(r'^\s*accept\s*$', block, re.M), label


def test_aftermath_gate_and_one_shot():
    aftermath = mission_block(MISSIONS[2])
    to_offer = aftermath.split("\ton offer\n", 1)[0]
    assert f'not "{PREFIX}aftermath seen"' in to_offer
    assert '\t\tor\n' in to_offer
    for settlement in SETTLEMENTS:
        assert to_offer.count(f'has "{PREFIX}{settlement}"') == 1, settlement
    assert f'branch bounded\n\t\t\t\thas "{PREFIX}settlement bounded cooperation"' in aftermath
    assert assignment_count(aftermath, "aftermath seen") == 1
    assert len(re.findall(r'^\s*decline\s*$', aftermath, re.M)) == 1


def test_state_only_lifecycle_and_no_objectives():
    assert not re.search(r'^\s*accept\s*$', TEXT, re.M)
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    for directive in (
        "destination", "stopover", "waypoint", "npc", "cargo", "passengers",
        "deadline", "timer",
    ):
        assert not re.search(rf'^\t+{directive}\b', TEXT, re.M | re.I), directive


def test_b2_only_write_ownership_and_no_material_mutation():
    assignments = re.findall(
        r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=)\s*[^\n]*$', TEXT, re.M
    )
    for key in assignments:
        assert key.startswith(PREFIX), f"non-B2 assignment: {key}"

    for pattern in (
        r'^\s*payment\b',
        r'^\s*reputation\b',
        r'^\s*combat rating\s*(?:=|\+=|-=)',
        r'^\s*give\s+(?:ship|outfit|cargo)\b',
        r'^\s*take\s+(?:ship|outfit|cargo)\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), pattern


def test_local_gotos_resolve():
    for mission in MISSIONS:
        block = mission_block(mission)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = set(re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        missing = sorted(gotos - labels)
        assert not missing, f"{mission}: missing labels {missing}"


def test_crime_investigation_continuity_boundaries():
    lower = TEXT.lower()
    for fragment in (
        "former smuggler",
        "old cooperation",
        "closed cooperation",
        "standing informant duty",
        "permanent active suspicion",
        "fresh case-specific",
        "current evidence",
        "current consent",
        "fresh-cause",
        "explicit closure",
    ):
        assert fragment in lower, fragment
    assert "neither fact alone makes him an active informant or an active suspect today" in lower
    assert "one former smuggler's history" in lower
    # The production text may explicitly discuss whether to make a general office
    # practice; only a positive universal-law claim would violate the local scope.
    assert "universal republic law" not in lower


def main():
    test_header_graph_and_inputs()
    test_characters_scope_and_read_only_inputs()
    test_offer_route_local_writes_schedule_and_refusal()
    test_review_lifecycle_and_route_wiring()
    test_settlement_local_closure()
    test_aftermath_gate_and_one_shot()
    test_state_only_lifecycle_and_no_objectives()
    test_b2_only_write_ownership_and_no_material_mutation()
    test_local_gotos_resolve()
    test_crime_investigation_continuity_boundaries()
    print("PASS: B2 Republic Former Smuggler Cooperation Compact validated")
    print("PASS: primary_domain=crime/investigation/law")
    print("PASS: missions=3 event=1")
    print("PASS: characters=Rhea Markel,Davin Sorn")
    print("PASS: systemic_inputs=pirate jobs + Republic customs scrutiny + border pressure (read-only)")
    print("PASS: routes=3 + refusal; delayed_review=7-11 days")
    print("PASS: settlements=2; aftermath=one-shot")
    print("PASS: state_only_terminals=7 decline / 0 accept")


if __name__ == "__main__":
    main()
