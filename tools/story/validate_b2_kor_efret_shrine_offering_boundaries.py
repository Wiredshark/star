#!/usr/bin/env python3
"""Focused structural validation for B2 Kor Efret Shrine Offering Boundaries."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "korath" / "b2 kor efret shrine offering boundaries.txt"
TEXT = DATA.read_text(encoding="utf-8")
PREFIX = "B2 Kor Efret Shrine Offering Boundaries: "
MISSIONS = [
    "B2 Kor Efret Shrine Offering Boundaries: Offer",
    "B2 Kor Efret Shrine Offering Boundaries: Review",
    "B2 Kor Efret Shrine Offering Boundaries: Caretaker Remembers",
]


def mission_block(name: str) -> str:
    start = TEXT.index(f'mission "{name}"')
    nxt = TEXT.find('\nmission "', start + 1)
    return TEXT[start:] if nxt < 0 else TEXT[start:nxt]


def label_block(block: str, label: str) -> str:
    start = block.index(f"\n\t\t\tlabel {label}\n")
    nxt = block.find("\n\t\t\tlabel ", start + 1)
    return block[start:] if nxt < 0 else block[start:nxt]


def assignments():
    return re.findall(r'^\s*"([^"\n]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)', TEXT, re.M)


def test_graph_scope_and_dependencies():
    assert TEXT.count('mission "B2 Kor Efret Shrine Offering Boundaries:') == 3
    for name in MISSIONS:
        block = mission_block(name)
        assert '\t\tattributes "efret"' in block
        assert '\t\tnot attributes "station"' in block
    offer = mission_block(MISSIONS[0])
    assert 'has "Korath Far\'en Lai Prayer: offered"' in offer
    assert 'has "B2 Kor Efret Passage Continuity Compact: aftermath seen"' in offer
    assert offer.count('event "B2 Kor Efret Shrine Offering Boundaries: Review Ready" 7 11') == 3


def test_offer_routes_and_refusal():
    offer = mission_block(MISSIONS[0])
    expected = {
        "intent": "route intent first",
        "reuse": "route family reuse",
        "paired": "route paired status",
    }
    for label, route in expected.items():
        block = label_block(offer, label)
        assert f'"{PREFIX}introduced" = 1' in block
        assert f'"{PREFIX}{route}" = 1' in block
        assert 'event "B2 Kor Efret Shrine Offering Boundaries: Review Ready" 7 11' in block
        assert re.search(r'^\s*decline\s*$', block, re.M)
    refusal = label_block(offer, "decline")
    assert f'"{PREFIX}declined" = 1' in refusal
    assert f'"{PREFIX}introduced" = 1' not in refusal
    assert 'Review Ready" 7 11' not in refusal
    assert re.search(r'^\s*decline\s*$', refusal, re.M)


def test_review_and_settlements():
    review = mission_block(MISSIONS[1])
    assert f'has "{PREFIX}introduced"' in review
    assert f'has "{PREFIX}review ready"' in review
    assert f'not "{PREFIX}reviewed"' in review
    assert review.count(f'"{PREFIX}reviewed" = 1') == 2
    history = label_block(review, "history")
    dual = label_block(review, "dual")
    assert f'"{PREFIX}settlement portable offering history" = 1' in history
    assert f'"{PREFIX}settlement dual closure" = 1' in dual
    assert re.search(r'^\s*decline\s*$', history, re.M)
    assert re.search(r'^\s*decline\s*$', dual, re.M)


def test_aftermath_is_one_shot_and_reachable_from_both_settlements():
    aftermath = mission_block(MISSIONS[2])
    assert f'not "{PREFIX}aftermath seen"' in aftermath
    assert f'has "{PREFIX}settlement portable offering history"' in aftermath
    assert f'has "{PREFIX}settlement dual closure"' in aftermath
    assert aftermath.count(f'"{PREFIX}aftermath seen" = 1') == 1
    assert re.search(r'^\s*decline\s*$', aftermath, re.M)


def test_state_only_lifecycle_and_gotos():
    assert len(re.findall(r'^\s*accept\s*$', TEXT, re.M)) == 0
    assert len(re.findall(r'^\s*decline\s*$', TEXT, re.M)) == 7
    for pattern in (
        r'^\s*destination\b', r'^\s*stopover\b', r'^\s*waypoint\b', r'^\s*npc\b',
        r'^\s*cargo\b', r'^\s*passengers?\b', r'^\s*deadline\b', r'^\s*timer\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"objective directive found: {pattern}"
    for name in MISSIONS:
        block = mission_block(name)
        labels = set(re.findall(r'^\s*label\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M))
        gotos = re.findall(r'^\s*goto\s+([A-Za-z][A-Za-z0-9_-]*)\s*$', block, re.M)
        missing = sorted(set(gotos) - labels)
        assert not missing, f"{name}: unresolved goto(s) {missing}"


def test_state_ownership_and_no_material_mutation():
    foreign = sorted({name for name in assignments() if not name.startswith(PREFIX)})
    assert not foreign, f"foreign condition writes: {foreign}"
    for pattern in (
        r'^\s*payment\b', r'^\s*reputation\b', r'^\s*combat rating\b',
        r'^\s*give\s+(?:ship|outfit|cargo)\b', r'^\s*take\s+(?:outfit|cargo)\b',
    ):
        assert not re.search(pattern, TEXT, re.M | re.I), f"material mutation found: {pattern}"


def test_ritual_property_boundaries_are_explicit():
    lowered = TEXT.lower()
    for fragment in (
        "far'en lai remembrance",
        "not a universal korath rule for sacred property",
        "use intent first",
        "do not invent permanent surrender or automatic retrieval",
        "ritual status and physical custody separately",
        "moving the object can change custody without erasing its ritual history",
        "physical value, family ownership history, ritual meaning, donor intent, and current custodian are not the same thing",
        "one true fact and turned it into a rule the original record never stated",
        "the whole chain rather than a single word",
        "both can remain true",
    ):
        assert fragment in lowered, f"missing ritual/property boundary: {fragment}"


def test_player_private_shorthand_is_bounded():
    lowered = TEXT.lower()
    assert "in your own thoughts you have started calling this one the caretaker" in lowered
    assert "nobody has offered that as a korath title" in lowered


def main():
    test_graph_scope_and_dependencies()
    test_offer_routes_and_refusal()
    test_review_and_settlements()
    test_aftermath_is_one_shot_and_reachable_from_both_settlements()
    test_state_only_lifecycle_and_gotos()
    test_state_ownership_and_no_material_mutation()
    test_ritual_property_boundaries_are_explicit()
    test_player_private_shorthand_is_bounded()
    print("PASS: B2 Kor Efret Shrine Offering Boundaries structure validated")
    print("PASS: missions=3; routes=3+refusal; settlements=2; aftermath=one-shot")
    print("PASS: delayed_review=3 substantive routes only; refusal cannot arm Review")
    print("PASS: terminals=7 decline / 0 accept; writes=B2 namespace only")
    print("PASS: ritual meaning / donor intent / family claim / physical custody remain distinct")


if __name__ == "__main__":
    main()
