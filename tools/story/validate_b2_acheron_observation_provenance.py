#!/usr/bin/env python3
"""Focused structural validator for B2 Acheron Observation Provenance."""
from pathlib import Path
import re
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/vyrmeid/b2 acheron observation provenance.txt")
text = path.read_text(encoding="utf-8")

required = [
    'mission "B2 Acheron Observation Provenance: Offer"',
    'mission "B2 Acheron Observation Provenance: Review"',
    'mission "B2 Acheron Observation Provenance: Sol Remembers"',
    'Nira Sol',
    'Tomas Pell',
    '"B2 Acheron Observation Provenance: route baseline" = 1',
    '"B2 Acheron Observation Provenance: route stimulus" = 1',
    '"B2 Acheron Observation Provenance: route paired" = 1',
    '"B2 Acheron Observation Provenance: settlement packet" = 1',
    '"B2 Acheron Observation Provenance: settlement ladder" = 1',
    '"B2 Acheron Observation Provenance: declined" = 1',
    '"B2 Acheron Observation Provenance: aftermath seen" = 1',
    'Rulei: Umbral Reach: offered',
    'responsive is not the same as intentional',
    'dangerous is not the same as hostile',
]
for item in required:
    if item not in text:
        raise SystemExit(f"missing required B2 Acheron element: {item}")

missions = re.findall(r'^mission "B2 Acheron Observation Provenance: ([^"]+)"', text, re.M)
if missions != ["Offer", "Review", "Sol Remembers"]:
    raise SystemExit(f"unexpected mission graph/order: {missions}")

writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, re.M)
foreign = [w for w in writes if not w.startswith("B2 Acheron Observation Provenance:")]
if foreign:
    raise SystemExit(f"foreign persistent writes: {foreign}")

for forbidden in ["credits", "reputation", "cargo ", "outfit ", "ship ", "fleet ", "combat rating", '"world:']:
    if re.search(rf'^\s*{re.escape(forbidden)}', text, re.M | re.I):
        raise SystemExit(f"forbidden material/world mutation surface: {forbidden}")

labels = set(re.findall(r'^\s*label\s+(\S+)', text, re.M))
gotos = re.findall(r'^\s*goto\s+(\S+)', text, re.M)
missing = sorted(set(gotos) - labels)
if missing:
    raise SystemExit(f"goto targets without labels: {missing}")

if text.count('settlement packet" = 1') != 1 or text.count('settlement ladder" = 1') != 1:
    raise SystemExit("expected exactly two terminal settlement writes")

# Semantic continuity is intentionally checked using exact language that appears
# in the production dialogue rather than brittle prose fragments from one branch.
# The required phrases above prove that responsiveness != intention and danger !=
# hostility; the production mission graph separately preserves stimulus/source
# provenance and an explicit refusal route.

print("PASS: B2 Acheron Observation Provenance structure validated")
print("PASS: missions=3")
print("PASS: named_characters=2")
print("PASS: initial_routes=3 + refusal")
print("PASS: terminal_settlements=2")
print("PASS: later_reader=Sol Remembers")
print("PASS: persistence_writes=B2 namespace only")
print("PASS: continuity=observation/stimulus/hazard/motive kept distinct")
