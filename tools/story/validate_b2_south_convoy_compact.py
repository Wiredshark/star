#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/human/b2 south convoy compact.txt"
text = DATA.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 South Convoy Compact: Offer"',
    'mission "B2 South Convoy Compact: Review"',
    'mission "B2 South Convoy Compact: Reeve Remembers"',
]
required_characters = ["Mira Dane", "Tomas Reeve"]
required_routes = [
    '"B2 South Convoy Compact: route dane" = 1',
    '"B2 South Convoy Compact: route reeve" = 1',
    '"B2 South Convoy Compact: route pledge" = 1',
]
required_settlements = [
    '"B2 South Convoy Compact: settlement standing rescue compact" = 1',
    '"B2 South Convoy Compact: settlement public rescue registry" = 1',
]

for token in required_missions + required_characters + required_routes + required_settlements:
    assert token in text, f"missing required token: {token}"

assert text.count('mission "B2 South Convoy Compact:') == 3
assert text.count('"B2 South Convoy Compact: settlement standing rescue compact" = 1') == 1
assert text.count('"B2 South Convoy Compact: settlement public rescue registry" = 1') == 1
assert '"B2 South Convoy Compact: reviewed" = 1' in text
assert '"B2 South Convoy Compact: aftermath seen" = 1' in text
assert '"B2 South Convoy Compact: declined" = 1' in text

# The slice must stay scoped to southern non-station worlds.
for block in re.split(r'(?=mission "B2 South Convoy Compact:)', text)[1:]:
    assert 'attributes "south"' in block
    assert 'not attributes "station"' in block

# This is character/institutional content, not a direct material reward slice.
for forbidden in ["payment", "credits", "reputation", "cargo", "outfit", "combat"]:
    assert not re.search(rf'^\s*{re.escape(forbidden)}\b', text, re.MULTILINE), forbidden

# Every explicit goto target in each conversation must have a matching label.
for mission in re.split(r'(?=mission "B2 South Convoy Compact:)', text)[1:]:
    gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', mission, re.MULTILINE))
    labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', mission, re.MULTILINE))
    missing = gotos - labels
    assert not missing, f"missing labels for goto targets: {sorted(missing)}"

# Review consumes Dane and Reeve routes explicitly; the pledge route is intentional fallthrough.
review = text.split('mission "B2 South Convoy Compact: Review"', 1)[1]
review = review.split('mission "B2 South Convoy Compact: Reeve Remembers"', 1)[0]
assert 'branch dane' in review and 'has "B2 South Convoy Compact: route dane"' in review
assert 'branch reeve' in review and 'has "B2 South Convoy Compact: route reeve"' in review
review_preamble = review.split('on offer', 1)[1].split('label dane', 1)[0]
assert 'route pledge' not in review_preamble, "pledge route should remain intentional review fallthrough"

# Later reader consumes both mutually exclusive terminal outcomes.
after = text.split('mission "B2 South Convoy Compact: Reeve Remembers"', 1)[1]
assert 'has "B2 South Convoy Compact: settlement standing rescue compact"' in after
assert 'has "B2 South Convoy Compact: settlement public rescue registry"' in after

# Terminal settlement variables are only written in the Review mission.
offer = text.split('mission "B2 South Convoy Compact: Offer"', 1)[1].split('mission "B2 South Convoy Compact: Review"', 1)[0]
assert 'settlement standing rescue compact' not in offer
assert 'settlement public rescue registry' not in offer

print("PASS: B2 South Convoy Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: review_routing=pledge fallthrough + explicit Dane/Reeve branches")
print("PASS: terminal_settlements=2")
print("PASS: later_reader=Reeve Remembers")
print("PASS: persistence_model=stock mission/global conditions")
