#!/usr/bin/env python3
from pathlib import Path
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "data/human/a2 republic border testimony practice.txt")
text = path.read_text(encoding="utf-8")
required = [
    'mission "A2 Republic Border Testimony Practice: Briefing"',
    'mission "A2 Republic Border Testimony Practice: Recurrence"',
    'has "B2 Republic Border Testimony Compact: aftermath seen"',
    '"world: republic border pressure" <= 2',
    '"world: republic border pressure" >= 4',
    '[Evidence: Portable provenance packet]',
    'has "B2 Republic Border Testimony Compact: settlement portable provenance packet"',
    '[Verran trusts your evidence judgment]',
    'has "B2 Republic Border Testimony Compact: verran trusts player"',
    '[Settlement: Expiry and renewal]',
    'has "B2 Republic Border Testimony Compact: settlement expiry and renewal"',
    '"A2 Republic Border Testimony Practice: lineage" = 1',
    '"A2 Republic Border Testimony Practice: independence" = 1',
    '"A2 Republic Border Testimony Practice: closure" = 1',
    '"A2 Republic Border Testimony Practice: local" = 1',
    '"A2 Republic Border Testimony Practice: refused" = 1',
    '"A2 Republic Border Testimony Practice: recurrence seen" = 1',
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("missing required contracts: " + ", ".join(missing))

for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') and (' = ' in stripped or ' += ' in stripped or ' -= ' in stripped):
        raise SystemExit("A2 must not write world state: " + stripped)
    if stripped.startswith('"B2 Republic Border Testimony Compact:') and (' = ' in stripped or ' += ' in stripped or ' -= ' in stripped):
        raise SystemExit("A2 must not write B2 state: " + stripped)

if text.count('mission "A2 Republic Border Testimony Practice:') != 2:
    raise SystemExit("expected exactly two A2 missions")
if text.count('\t"offer precedence" 8') != 2:
    raise SystemExit("both production missions must outrank ambient history with offer precedence 8")
if text.count('\t\t\t\t\tto display') < 3:
    raise SystemExit("expected at least three persistent-state-dependent player responses")
if text.count('[') < 3:
    raise SystemExit("expected player-visible metadata labels on special responses")
if '\n\t\t\taccept\n' in text:
    raise SystemExit("dialogue-only A2 missions must decline after recording state, not remain active via accept")
if text.count('\n\t\t\tdecline\n') < 6:
    raise SystemExit("expected four positive routes, refusal, and recurrence to close as dialogue-only missions")

print("PASS: Republic border testimony practice contracts")
