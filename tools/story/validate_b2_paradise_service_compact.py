#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/human/b2 paradise service compact.txt"
text = DATA.read_text(encoding="utf-8")

required_missions = [
    'mission "B2 Paradise Service Compact: Offer"',
    'mission "B2 Paradise Service Compact: Review"',
    'mission "B2 Paradise Service Compact: Mercer Remembers"',
]
required_characters = ["Iona Mercer", "Celia Voss"]
required_routes = [
    '"B2 Paradise Service Compact: route mercer" = 1',
    '"B2 Paradise Service Compact: route voss" = 1',
    '"B2 Paradise Service Compact: route compact" = 1',
]
required_settlements = [
    '"B2 Paradise Service Compact: settlement municipal corridor" = 1',
    '"B2 Paradise Service Compact: settlement shared service compact" = 1',
]

for token in required_missions + required_characters + required_routes + required_settlements:
    assert token in text, f"missing required token: {token}"

assert text.count('mission "B2 Paradise Service Compact:') == 3
assert text.count('"B2 Paradise Service Compact: settlement municipal corridor" = 1') == 1
assert text.count('"B2 Paradise Service Compact: settlement shared service compact" = 1') == 1
assert '"B2 Paradise Service Compact: reviewed" = 1' in text
assert '"B2 Paradise Service Compact: aftermath seen" = 1' in text
assert '"B2 Paradise Service Compact: declined" = 1' in text

# The slice must stay scoped to Paradise Republic worlds and avoid stations.
for block in re.split(r'(?=mission "B2 Paradise Service Compact:)', text)[1:]:
    assert 'government "Republic"' in block
    assert 'attributes "paradise"' in block
    assert 'not attributes "station"' in block

# No direct material/gameplay reward mutation belongs in this character slice.
for forbidden in ["payment", "credits", "reputation", "cargo", "outfit", "combat"]:
    assert not re.search(rf'^\s*{re.escape(forbidden)}\b', text, re.MULTILINE), forbidden

# Every explicit goto target in each conversation must have a matching label.
for mission in re.split(r'(?=mission "B2 Paradise Service Compact:)', text)[1:]:
    gotos = set(re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', mission, re.MULTILINE))
    labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', mission, re.MULTILINE))
    missing = gotos - labels
    assert not missing, f"missing labels for goto targets: {sorted(missing)}"

# Review must consume all three initial routes, with compact as intentional fallthrough.
review = text.split('mission "B2 Paradise Service Compact: Review"', 1)[1]
review = review.split('mission "B2 Paradise Service Compact: Mercer Remembers"', 1)[0]
assert 'branch mercer' in review and 'has "B2 Paradise Service Compact: route mercer"' in review
assert 'branch voss' in review and 'has "B2 Paradise Service Compact: route voss"' in review
assert 'route compact' not in review.split('on offer', 1)[1].split('label mercer', 1)[0], (
    "compact route is intentionally the review fallthrough and should not be double-gated"
)

# Later reader must consume both mutually exclusive settlement conditions.
after = text.split('mission "B2 Paradise Service Compact: Mercer Remembers"', 1)[1]
assert 'has "B2 Paradise Service Compact: settlement municipal corridor"' in after
assert 'has "B2 Paradise Service Compact: settlement shared service compact"' in after

print("PASS: B2 Paradise Service Compact structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: later_reader=Mercer Remembers")
print("PASS: persistence_model=stock mission/global conditions")
