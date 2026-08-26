#!/usr/bin/env python3
"""Focused structural validation for B2 Rook Confidential Teaching Compact."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 rook confidential teaching compact.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Rook Confidential Teaching Compact: "
EVENT = 'event "B2 Rook Confidential Teaching Compact: Review Ready"'

MISSIONS = [
    "B2 Rook Confidential Teaching Compact: Offer",
    "B2 Rook Confidential Teaching Compact: Review",
    "B2 Rook Confidential Teaching Compact: Bell Remembers",
]
ROUTES = ["route abstract", "route consent", "route paired"]
SETTLEMENTS = ["settlement reidentification review", "settlement consent-bound excerpts"]


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


def test_header_and_graph():
    assert TEXT.startswith("# Copyright (c) 2026 by Wiredshark\n")
    assert TEXT.endswith("\n")
    assert TEXT.count('mission "B2 Rook Confidential Teaching Compact:') == 3
    for mission in MISSIONS:
        assert f'mission "{mission}"' in TEXT
    assert TEXT.count('\nevent "B2 Rook Confidential Teaching Compact: Review Ready"\n') == 1
    assert TEXT.count(EVENT + " 7 11") == 3


def test_characters_and_a2_dependencies_are_read_only():
    assert "Imani Rook" in TEXT
    assert "Nora Bell" in TEXT
    offer = mission_block(MISSIONS[0])
    assert 'has "A2 Rook Mediation: later reader seen"' in offer
    assert 'has "A2 Rook Mediation: outcome command"' in offer
    assert 'has "A2 Rook Mediation: outcome logistics"' in offer
    assert not re.search(r'^\s*"A2 Rook Mediation:[^"\n]*"\s*(?:=|\+=|-=|\+\+|--|\?=)', TEXT, re.M)


def test_offer_route_local_writes_and_schedule():
    offer = MISSIONS[0]
    route_labels = {
        "abstract": "route abstract",
        "consent": "route consent",
        "paired": "route paired",
    }
    for label, own_route in route_labels.items():
        block = label_block(offer, label)
        assert assignment_count(block, "introduced") == 1, label
        assert assignment_count(block, own_route) == 1, label
        for other in ROUTES:
            if other != own_route:
                assert assignment_count(block, other) == 0, (label, other)
        assert block.count(EVENT + " 7 11") == 1, label
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1, label
        assert not re.search(r'^\s*accept\s*$', block, re.M)

    refusal = label_block(offer, "refuse")
    assert assignment_count(refusal, "declined") == 1
    assert assignment_count(refusal, "introduced") == 0
    for route in ROUTES:
        assert assignment_count(refusal, route) == 0
    assert EVENT + " 7 11" not in refusal
    assert len(re.findall(r'^\s*decline\s*$', refusal, re.M)) == 1


def test_review_gates_and_routing():
    review = mission_block(MISSIONS[1])
    to_offer = review.split("\ton offer\n", 1)[0]
    assert f'has "{PREFIX}introduced"' in to_offer
    assert f'has "{PREFIX}review ready"' in to_offer
    assert f'not "{PREFIX}reviewed"' in to_offer
    assert f'branch consent\n\t\t\t\thas "{PREFIX}route consent"' in review
    assert f'branch paired\n\t\t\t\thas "{PREFIX}route paired"' in review
    # The abstract route is intentionally the fallthrough/default Review presentation.
    assert 'branch abstract' not in review


def test_settlement_local_closure():
    review = MISSIONS[1]
    mapping = {
        "audit": "settlement reidentification review",
        "bounded": "settlement consent-bound excerpts",
    }
    for label, own_settlement in mapping.items():
        block = label_block(review, label)
        assert assignment_count(block, "reviewed") == 1, label
        assert assignment_count(block, own_settlement) == 1, label
        for other in SETTLEMENTS:
            if other != own_settlement:
                assert assignment_count(block, other) == 0, (label, other)
        assert len(re.findall(r'^\s*decline\s*$', block, re.M)) == 1, label
        assert not re.search(r'^\s*accept\s*$', block, re.M)


def test_aftermath_gate_and_one_shot():
    aftermath = mission_block(MISSIONS[2])
    to_offer = aftermath.split("\ton offer\n", 1)[0]
    assert f'not "{PREFIX}aftermath seen"' in to_offer
    assert '\t\tor\n' in to_offer
    for settlement in SETTLEMENTS:
        assert to_offer.count(f'has "{PREFIX}{settlement}"') == 1
    assert f'branch bounded\n\t\t\t\thas "{PREFIX}settlement consent-bound excerpts"' in aftermath
    assert assignment_count(aftermath, "aftermath seen") == 1
    assert len(re.findall(r'^\s*decline\s*$', aftermath, re.M)) == 1


def test_state_only_lifecycle_and_no_objectives():
    assert not re.search(r'^\s*accept\s*$', TEXT, re.M)
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    objective_directives = (
        "destination", "stopover", "waypoint", "npc", "cargo", "passengers",
        "deadline", "timer",
    )
    for directive in objective_directives:
        assert not re.search(rf'^\t+{directive}\b', TEXT, re.M | re.I), directive


def test_b2_only_write_ownership_and_no_material_mutation():
    assignments = re.findall(r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=)\s*[^\n]*$', TEXT, re.M)
    for key in assignments:
        assert key.startswith(PREFIX), f"non-B2 assignment: {key}"

    forbidden_actions = (
        r'^\s*payment\b',
        r'^\s*reputation\b',
        r'^\s*combat rating\s*(?:=|\+=|-=)',
        r'^\s*give\s+(?:ship|outfit|cargo)\b',
        r'^\s*take\s+(?:ship|outfit|cargo)\b',
    )
    for pattern in forbidden_actions:
        assert not re.search(pattern, TEXT, re.M | re.I), pattern


def test_local_gotos_resolve():
    for mission in MISSIONS:
        block = mission_block(mission)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = set(re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        missing = sorted(gotos - labels)
        assert not missing, f"{mission}: missing labels {missing}"


def test_continuity_boundaries():
    lower = TEXT.lower()
    for fragment in (
        "confidential",
        "purpose-bound consent",
        "re-identification",
        "audience",
        "expiry",
        "withdrawal",
        "allowed to exist",
        "allowed to circulate",
    ):
        assert fragment in lower, fragment
    assert "redacted is not anonymous" in lower
    assert "consent to settle is not consent to become curriculum" in lower


def main():
    test_header_and_graph()
    test_characters_and_a2_dependencies_are_read_only()
    test_offer_route_local_writes_and_schedule()
    test_review_gates_and_routing()
    test_settlement_local_closure()
    test_aftermath_gate_and_one_shot()
    test_state_only_lifecycle_and_no_objectives()
    test_b2_only_write_ownership_and_no_material_mutation()
    test_local_gotos_resolve()
    test_continuity_boundaries()
    print("PASS: B2 Rook Confidential Teaching Compact validated")
    print("PASS: missions=3 event=1")
    print("PASS: characters=Imani Rook,Nora Bell")
    print("PASS: routes=3 + refusal; delayed_review=7-11 days")
    print("PASS: settlements=2; aftermath=one-shot")
    print("PASS: A2 state=read_only; B2 state=owned")
    print("PASS: state_only_terminals=7 decline / 0 accept")


if __name__ == "__main__":
    main()
