#!/usr/bin/env python3
from pathlib import Path
import re
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 syndicate parts practice.txt")
text = path.read_text(encoding="utf-8")
errors: list[str] = []


def need(token: str) -> None:
    if token not in text:
        errors.append(f"missing: {token}")


required = [
    'mission "A2 Syndicate Parts Practice: Scarcity Briefing"',
    'mission "A2 Syndicate Parts Practice: Recovery Review"',
    'Elara Dane',
    '"world: syndicate parts scarcity" >= 3',
    '"world: syndicate parts scarcity" >= 5',
    '"world: syndicate parts scarcity" <= 1',
    '"world: syndicate maintenance backlog" >= 3',
    '"world: syndicate maintenance backlog" < 3',
    '"A2 Syndicate Parts Practice: provenance first" = 1',
    '"A2 Syndicate Parts Practice: critical reserve" = 1',
    '"A2 Syndicate Parts Practice: reversible substitution" = 1',
    '"A2 Syndicate Parts Practice: refused" = 1',
    '"A2 Syndicate Parts Practice: refusal respected" = 1',
    '"A2 Syndicate Parts Practice: followup pending" = 1',
    '"A2 Syndicate Parts Practice: followup pending" = 0',
    '"A2 Syndicate Parts Practice: followup seen" = 1',
    '"A2 Syndicate Parts Practice: Dane remembers provenance under backlog" = 1',
    '"A2 Syndicate Parts Practice: Dane remembers provenance stabilized" = 1',
    '"A2 Syndicate Parts Practice: Dane remembers reserve under backlog" = 1',
    '"A2 Syndicate Parts Practice: Dane remembers reserve stabilized" = 1',
    '"A2 Syndicate Parts Practice: Dane remembers reversible under backlog" = 1',
    '"A2 Syndicate Parts Practice: Dane remembers reversible stabilized" = 1',
    'label provenance',
    'label reserve',
    'label reversible',
    'label refuse',
    'label provenance_high',
    'label provenance_low',
    'label reserve_high',
    'label reserve_low',
    'label reversible_high',
    'label reversible_low',
    'label finish',
]
for token in required:
    need(token)

if text.count('mission "A2 Syndicate Parts Practice:') != 2:
    errors.append("expected exactly two A2 Syndicate Parts Practice missions")
if text.count('"offer precedence" 9') != 2:
    errors.append("expected offer precedence 9 on both missions")
if len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)) != 5:
    errors.append("expected exactly five state-only decline terminals")
if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
    errors.append("state-only A2 slice must not accept objective-less missions")

# A1 owns these world variables. Comparisons are allowed; assignments are not.
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith(('"world: syndicate parts scarcity"', '"world: syndicate maintenance backlog"')):
        if re.search(r'\s(?:\+=|-=|=)\s', stripped):
            errors.append(f"forbidden A1 world-state write: {stripped}")
    if stripped.startswith(('set "world:', 'clear "world:')):
        errors.append(f"forbidden world-state mutation: {stripped}")

# Every assignment must remain in the A2 namespace unless it is a read-only world comparison.
for match in re.finditer(r'^\s*"([^"]+)"\s(?:\+=|-=|=)\s', text, flags=re.MULTILINE):
    condition = match.group(1)
    if not condition.startswith('A2 Syndicate Parts Practice:'):
        errors.append(f"write outside A2 namespace: {condition}")

# This is a dialogue/state slice; gameplay objectives would invalidate the decline lifecycle assumption.
objective_prefixes = (
    'cargo ', 'passengers ', 'destination ', 'waypoint ', 'stopover ',
    'npc ', 'deadline ', 'distance ', 'clearance ', 'outfit ', 'ship ',
)
for line in text.splitlines():
    stripped = line.strip()
    if line.startswith('\t') and stripped.startswith(objective_prefixes):
        errors.append(f"unexpected gameplay objective directive: {stripped}")

# Refusal records the boundary but must not create a positive policy outcome.
refusal_block = text.split('label refuse', 1)[1].split('mission "A2 Syndicate Parts Practice: Recovery Review"', 1)[0]
for forbidden in ('provenance first" = 1', 'critical reserve" = 1', 'reversible substitution" = 1'):
    if forbidden in refusal_block:
        errors.append(f"refusal leaks into positive policy: {forbidden}")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("PASS")
print("missions=2")
print("named_character=Elara Dane")
print("authoritative_inputs=world: syndicate parts scarcity + maintenance backlog")
print("initial_routes=provenance,reserve,reversible,refusal")
print("recovery_variants=6+refusal")
print("state_only_declines=5")
print("state_only_accepts=0")
print("authoritative_world_writes=none")
print("persistent_A2_memory=yes")
