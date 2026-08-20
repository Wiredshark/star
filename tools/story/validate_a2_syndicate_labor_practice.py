#!/usr/bin/env python3
from pathlib import Path
import sys

PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 syndicate labor practice.txt")
text = PATH.read_text(encoding="utf-8")
errors = []


def need(token):
    if token not in text:
        errors.append(f"missing: {token}")


for token in (
    'mission "A2 Syndicate Labor Practice: Rotation Briefing"',
    'mission "A2 Syndicate Labor Practice: Rotation Review"',
    'Nera Voss',
    'has "world: syndicate labor rotation active"',
    'not "world: syndicate labor rotation active"',
    '"world: syndicate labor strain" >= 2',
    '"world: syndicate labor strain" < 2',
    '"A2 Syndicate Labor Practice: qualifications first" = 1',
    '"A2 Syndicate Labor Practice: rest protected" = 1',
    '"A2 Syndicate Labor Practice: reassignment bounded" = 1',
    '"A2 Syndicate Labor Practice: refused" = 1',
    '"A2 Syndicate Labor Practice: followup pending" = 1',
    '"A2 Syndicate Labor Practice: followup pending" = 0',
    '"A2 Syndicate Labor Practice: followup seen" = 1',
    'label qualifications_high',
    'label qualifications_low',
    'label rest_high',
    'label rest_low',
    'label reassignment_high',
    'label reassignment_low',
):
    need(token)

for label in ('label qualifications', 'label rest', 'label reassignment', 'label refuse'):
    need(label)

for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world: syndicate labor strain"') and any(op in stripped for op in (' += ', ' -= ', ' = ', '>?=', '<?=')):
        errors.append(f"A2 mutates authoritative labor strain: {stripped}")
    if stripped.startswith('set "world: syndicate labor rotation active"') or stripped.startswith('clear "world: syndicate labor rotation active"'):
        errors.append(f"A2 mutates authoritative labor rotation: {stripped}")
    if stripped.startswith('"world: syndicate maintenance backlog"') and any(op in stripped for op in (' += ', ' -= ', ' = ', '>?=', '<?=')):
        errors.append(f"A2 mutates maintenance backlog: {stripped}")
    if stripped.startswith('"world: syndicate parts scarcity"') and any(op in stripped for op in (' += ', ' -= ', ' = ', '>?=', '<?=')):
        errors.append(f"A2 mutates parts scarcity: {stripped}")

if text.count('mission "A2 Syndicate Labor Practice:') != 2:
    errors.append("expected exactly two A2 Syndicate Labor Practice missions")

if errors:
    print("FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("PASS")
print("missions=2")
print("named_character=Nera Voss")
print("authoritative_inputs=world: syndicate labor rotation active + labor strain")
print("initial_routes=qualifications, rest, reassignment, refusal")
print("review_variants=6 + refusal")
print("authoritative_A1_writes=none")
print("persistent_A2_memory=yes")
