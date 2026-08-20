#!/usr/bin/env python3
from pathlib import Path
import sys

PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 syndicate parts practice.txt")
text = PATH.read_text(encoding="utf-8")
errors = []


def need(token):
    if token not in text:
        errors.append(f"missing: {token}")


for token in (
    'mission "A2 Syndicate Parts Practice: Scarcity Briefing"',
    'mission "A2 Syndicate Parts Practice: Recovery Review"',
    'Elara Dane',
    '"world: syndicate parts scarcity" >= 3',
    '"world: syndicate parts scarcity" <= 1',
    '"world: syndicate maintenance backlog" >= 3',
    '"world: syndicate maintenance backlog" < 3',
    '"A2 Syndicate Parts Practice: provenance first" = 1',
    '"A2 Syndicate Parts Practice: critical reserve" = 1',
    '"A2 Syndicate Parts Practice: reversible substitution" = 1',
    '"A2 Syndicate Parts Practice: refused" = 1',
    '"A2 Syndicate Parts Practice: followup pending" = 1',
    '"A2 Syndicate Parts Practice: followup pending" = 0',
    '"A2 Syndicate Parts Practice: followup seen" = 1',
    'label provenance_high', 'label provenance_low',
    'label reserve_high', 'label reserve_low',
    'label reversible_high', 'label reversible_low',
):
    need(token)

for label in ('label provenance', 'label reserve', 'label reversible', 'label refuse'):
    need(label)

for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world: syndicate parts scarcity"') and any(op in stripped for op in (' += ', ' -= ', ' = ', '>?=', '<?=')):
        errors.append(f"A2 mutates authoritative parts scarcity: {stripped}")
    if stripped.startswith('"world: syndicate maintenance backlog"') and any(op in stripped for op in (' += ', ' -= ', ' = ', '>?=', '<?=')):
        errors.append(f"A2 mutates authoritative maintenance backlog: {stripped}")
    if stripped.startswith('set "world:') or stripped.startswith('clear "world:'):
        errors.append(f"A2 mutates authoritative world state: {stripped}")

if text.count('mission "A2 Syndicate Parts Practice:') != 2:
    errors.append("expected exactly two A2 Syndicate Parts Practice missions")

if errors:
    print("FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("PASS")
print("missions=2")
print("named_character=Elara Dane")
print("authoritative_inputs=world: syndicate parts scarcity + maintenance backlog")
print("initial_routes=provenance, reserve, reversible, refusal")
print("recovery_variants=6 + refusal")
print("authoritative_world_writes=none")
print("persistent_A2_memory=yes")
