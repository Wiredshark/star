#!/usr/bin/env python3
from pathlib import Path
import sys
PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 syndicate maintenance triage.txt")
text = PATH.read_text(encoding="utf-8")
errors=[]
def need(token):
    if token not in text: errors.append(f"missing: {token}")
for token in (
    'mission "A2 Syndicate Maintenance Triage: Surge Briefing"',
    'mission "A2 Syndicate Maintenance Triage: After Action"',
    'Tessa Marr',
    'has "world: syndicate maintenance surge"',
    'not "world: syndicate maintenance surge"',
    '"world: syndicate maintenance backlog" >= 3',
    '"world: syndicate maintenance backlog" < 3',
    '"A2 Syndicate Maintenance Triage: priority safety" = 1',
    '"A2 Syndicate Maintenance Triage: priority contracts" = 1',
    '"A2 Syndicate Maintenance Triage: priority resilience" = 1',
    '"A2 Syndicate Maintenance Triage: refused" = 1',
    '"A2 Syndicate Maintenance Triage: followup pending" = 1',
    '"A2 Syndicate Maintenance Triage: followup pending" = 0',
    'label safety_high','label safety_low','label contracts_high','label contracts_low','label resilience_high','label resilience_low',
): need(token)
for line in text.splitlines():
    stripped=line.strip()
    if stripped.startswith('"world: syndicate maintenance backlog"') and any(op in stripped for op in (' += ', ' -= ', ' = ', '>?=', '<?=')):
        errors.append(f"A2 mutates authoritative backlog state: {stripped}")
    if stripped.startswith('set "world: syndicate maintenance surge"') or stripped.startswith('clear "world: syndicate maintenance surge"'):
        errors.append(f"A2 mutates authoritative surge state: {stripped}")
for label in ('label safety','label contracts','label resilience','label refuse'): need(label)
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('PASS')
print('missions=2')
print('named_character=Tessa Marr')
print('authoritative_inputs=world: syndicate maintenance surge + backlog')
print('initial_routes=safety, contracts, resilience, refusal')
print('after_action_variants=6 + refusal')
print('authoritative_A1_writes=none')
print('persistent_A2_memory=yes')
