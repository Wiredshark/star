#!/usr/bin/env python3
"""Focused structural validation for B2 Skadenga Living Vow Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 skadenga living vow compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Skadenga Living Vow Compact: "
EVENT = 'event "B2 Skadenga Living Vow Compact: Review Ready"'
MISSIONS = [
    "B2 Skadenga Living Vow Compact: Offer",
    "B2 Skadenga Living Vow Compact: Review",
    "B2 Skadenga Living Vow Compact: Runa Remembers",
]
ROUTES = ["route present consent", "route living renewal", "route paired records"]
SETTLEMENTS = ["settlement vow context", "settlement living recommitment"]


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


def test_header_graph_and_dependency():
    assert TEXT.startswith("# Copyright (c) 2026 by Wiredshark\n")
    assert TEXT.endswith("\n")
    assert TEXT.count('mission "B2 Skadenga Living Vow Compact:') == 3
    for mission in MISSIONS:
        assert f'mission "{mission}"' in TEXT
    assert TEXT.count('\nevent "B2 Skadenga Living Vow Compact: Review Ready"\n') == 1
    assert TEXT.count(EVENT + " 7 11") == 3
    offer_gate = mission_block(MISSIONS[0]).split("\ton offer\n", 1)[0]
    review_gate = mission_block(MISSIONS[1]).split("\ton offer\n", 1)[0]
    assert 'has "Home for Skadenga 4: done"' in offer_gate
    assert 'has "Home for Skadenga 4: done"' in review_gate


def test_characters_scope_and_dependency_read_only():
    assert "Hjlod" in TEXT
    assert "Runa" in TEXT
    for mission in MISSIONS:
        block = mission_block(mission)
        assert "\tsource\n" in block
        assert "\t\tattributes deep\n" in block
        assert '\t\tnot attributes "station"\n' in block
    assert not re.search(
        r'^\s*"Home for Skadenga 4: done"\s*(?:=|\+=|-=|\+\+|--|\?=)',
        TEXT,
        re.M,
    )


def test_offer_route_local_writes_schedule_and_refusal():
    mapping = {
        "consent": "route present consent",
        "renew": "route living renewal",
        "paired": "route paired records",
    }
    for label, own_route in mapping.items():
        block = label_block(MISSIONS[0], label)
        assert assignment_count(block, "introduced") == 1, label
        assert assignment_count(block, own_route) == 1, label
        for other in ROUTES:
            if other != own_route:
                assert assignment_count(block, other) == 0, (label, other)
        assert block.count(EVENT + " 7 11") == 1, label
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1, label
        assert not re.search(r'^\s*accept\s*$', block, re.M), label

    refusal = label_block(MISSIONS[0], "refuse")
    assert assignment_count(refusal, "declined") == 1
    assert assignment_count(refusal, "introduced") == 0
    for route in ROUTES:
        assert assignment_count(refusal, route) == 0
    assert EVENT + " 7 11" not in refusal
    assert len(re.findall(r'^\s*decline\s*$', refusal, re.M)) == 1


def test_review_lifecycle_and_route_wiring():
    review = mission_block(MISSIONS[1])
    gate = review.split("\ton offer\n", 1)[0]
    assert f'has "{PREFIX}introduced"' in gate
    assert f'has "{PREFIX}review ready"' in gate
    assert f'not "{PREFIX}reviewed"' in gate
    assert f'branch renew\n\t\t\t\thas "{PREFIX}route living renewal"' in review
    assert f'branch paired\n\t\t\t\thas "{PREFIX}route paired records"' in review
    # Present-consent is the deliberate default/fallthrough Review presentation.
    assert "branch consent" not in review


def test_settlement_local_closure():
    mapping = {
        "context": "settlement vow context",
        "living": "settlement living recommitment",
    }
    for label, own_settlement in mapping.items():
        block = label_block(MISSIONS[1], label)
        assert assignment_count(block, "reviewed") == 1, label
        assert assignment_count(block, own_settlement) == 1, label
        for other in SETTLEMENTS:
            if other != own_settlement:
                assert assignment_count(block, other) == 0, (label, other)
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1, label
        assert not re.search(r'^\s*accept\s*$', block, re.M), label


def test_aftermath_gate_and_one_shot():
    aftermath = mission_block(MISSIONS[2])
    gate = aftermath.split("\ton offer\n", 1)[0]
    assert f'not "{PREFIX}aftermath seen"' in gate
    assert "\t\tor\n" in gate
    for settlement in SETTLEMENTS:
        assert gate.count(f'has "{PREFIX}{settlement}"') == 1, settlement
    assert f'branch living\n\t\t\t\thas "{PREFIX}settlement living recommitment"' in aftermath
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
        assert not sorted(gotos - labels), (mission, sorted(gotos - labels))


def test_faith_agency_continuity_boundaries():
    lower = TEXT.lower()
    for fragment in (
        "old words can remain important without becoming a permanent staffing order",
        "a living vow can have a living speaker",
        "old words stay true as old words",
        "history issue today's order",
        "practical obligations claimed from an old vow expire unless the living speaker renews them",
        "refusal to renew a work assignment does not become evidence that runa rejected her faith",
        "one skadenga vow",
    ):
        assert fragment in lower, fragment
    assert "universal skadenga law" not in lower
    assert "permanent labor assignment" in lower


def main():
    test_header_graph_and_dependency()
    test_characters_scope_and_dependency_read_only()
    test_offer_route_local_writes_schedule_and_refusal()
    test_review_lifecycle_and_route_wiring()
    test_settlement_local_closure()
    test_aftermath_gate_and_one_shot()
    test_state_only_lifecycle_and_no_objectives()
    test_b2_only_write_ownership_and_no_material_mutation()
    test_local_gotos_resolve()
    test_faith_agency_continuity_boundaries()
    print("PASS: B2 Skadenga Living Vow Compact validated")
    print("PASS: primary_domain=faith/personal agency/community continuity")
    print("PASS: dependency=Home for Skadenga 4 done (read-only)")
    print("PASS: characters=Hjlod,Runa")
    print("PASS: routes=3 + refusal; delayed_review=7-11 days")
    print("PASS: settlements=2; aftermath=one-shot")
    print("PASS: state_only_terminals=7 decline / 0 accept")


if __name__ == "__main__":
    main()
