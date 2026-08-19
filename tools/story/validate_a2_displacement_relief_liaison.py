#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/a2 displacement relief liaison.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Displacement Relief Liaison: Cross-Border Briefing"',
    'mission "A2 Displacement Relief Liaison: Review"',
    'has "world: republic displacement relief spillover active"',
    'not "world: republic displacement relief spillover active"',
    '"world: republic displacement pressure" >= 4',
    '"world: republic displacement pressure" < 4',
    '"A2 Displacement Relief Liaison: bounded provenance" = 1',
    '"A2 Displacement Relief Liaison: aggregate only" = 1',
    '"A2 Displacement Relief Liaison: consent led" = 1',
    '"A2 Displacement Relief Liaison: refused" = 1',
    '"A2 Displacement Relief Liaison: followup seen" = 1',
]
missing = [token for token in required if token not in text]
if missing:
    raise SystemExit("missing required tokens: " + repr(missing))

outcomes = re.findall(r'"A2 Displacement Relief Liaison: (?:bounded|aggregate|consent) pressure (?:persists|eased)" = 1', text)
if len(outcomes) != 6 or len(set(outcomes)) != 6:
    raise SystemExit(f"expected six distinct simulation-sensitive outcomes, got {len(set(outcomes))}")

# A2 may read these A1-owned states but must never mutate them.
for state in (
    "world: republic displacement relief spillover active",
    "world: republic displacement pressure",
    "world: free worlds relief demand",
):
    mutation = re.compile(rf'^\s*"{re.escape(state)}"\s*(?:=|\+=|-=|\?=|<\?=|>\?=)', re.MULTILINE)
    if mutation.search(text):
        raise SystemExit(f"illegal A1-state write: {state}")

if text.count('mission "A2 Displacement Relief Liaison:') != 2:
    raise SystemExit("expected exactly two A2 liaison missions")

print("PASS: A2 displacement relief liaison; 2 missions, 3 policy routes + refusal, 6 pressure-sensitive outcomes, A1 state read-only")
