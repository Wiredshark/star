#!/usr/bin/env python3
from pathlib import Path
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "data/bunrodea/a2 bunrodea review queue practice.txt")
text = path.read_text(encoding="utf-8")

required = [
    'mission "A2 Bunrodea Review Queue Practice: Briefing"',
    'mission "A2 Bunrodea Review Queue Practice: Recurrence"',
    'has "B2 Bunrodea Review Queue Compact: aftermath seen"',
    '"world: bunrodea freight review backlog" <= 1',
    '"world: bunrodea freight review backlog" >= 4',
    '[Settlement: Portable delay history]',
    'has "B2 Bunrodea Review Queue Compact: settlement portable delay history"',
    '[Settlement: Reconciliation cycle]',
    'has "B2 Bunrodea Review Queue Compact: settlement reconciliation cycle"',
    '"A2 Bunrodea Review Queue Practice: lineage" = 1',
    '"A2 Bunrodea Review Queue Practice: reconcile" = 1',
    '"A2 Bunrodea Review Queue Practice: closure" = 1',
    '"A2 Bunrodea Review Queue Practice: refused" = 1',
    '"A2 Bunrodea Review Queue Practice: recurrence seen" = 1',
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("missing required contracts: " + ", ".join(missing))

for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world:') and (' = ' in stripped or ' += ' in stripped or ' -= ' in stripped):
        raise SystemExit("A2 must not write world state: " + stripped)
    if stripped.startswith('"B2 Bunrodea Review Queue Compact:') and (' = ' in stripped or ' += ' in stripped or ' -= ' in stripped):
        raise SystemExit("A2 must not write B2 state: " + stripped)

if text.count('mission "A2 Bunrodea Review Queue Practice:') != 2:
    raise SystemExit("expected exactly two A2 missions")
if text.count('\t"offer precedence" 8') != 2:
    raise SystemExit("both missions must use offer precedence 8")
if text.count('\t\t\t\t\tto display') != 2:
    raise SystemExit("expected two settlement-aware hidden response labels")
if '\n\t\t\taccept\n' in text:
    raise SystemExit("dialogue-only A2 missions must decline after recording state")
if text.count('\n\t\t\tdecline\n') < 5:
    raise SystemExit("expected three positive routes, refusal, and recurrence to close with decline")

pairs = [
    ("lineage", "portable delay history", "lineage_history"),
    ("lineage", "reconciliation cycle", "lineage_reconcile"),
    ("reconcile", "portable delay history", "reconcile_history"),
    ("reconcile", "reconciliation cycle", "reconcile_cycle"),
    ("closure", "portable delay history", "closure_history"),
    ("closure", "reconciliation cycle", "closure_cycle"),
]
for route, settlement, label in pairs:
    block = (
        f"branch {label}\n"
        f"\t\t\t\thas \"A2 Bunrodea Review Queue Practice: {route}\"\n"
        f"\t\t\t\thas \"B2 Bunrodea Review Queue Compact: settlement {settlement}\""
    )
    if block not in text:
        raise SystemExit(f"missing recurrence branch {label}")
    if f"label {label}" not in text:
        raise SystemExit(f"missing recurrence outcome {label}")

if "aggregate backlog recovery" not in text and "visible review queue is quiet again" not in text:
    raise SystemExit("expected recovery-vs-individual-history invariant to remain visible")

print("PASS: Bunrodea review queue practice contracts")
print("PASS: routes=3 refusal=1 recurrence_outcomes=6")
print("PASS: A1/B2 inputs read-only; dialogue-only lifecycle closes with decline")
