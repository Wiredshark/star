#!/usr/bin/env python3
"""Focused validation for the integrated A2 Republic Resettlement Council."""
from pathlib import Path
import re
import sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
    "data/human/a2 republic resettlement council.txt"
)
text = path.read_text(encoding="utf-8")
errors: list[str] = []

A1_STATES = (
    "world: republic displacement pressure",
    "world: republic border pressure",
    "world: republic resettlement surge",
)


def need(token: str) -> None:
    if token not in text:
        errors.append(f"missing: {token}")


required = (
    'mission "A2 Republic Resettlement Council: Emergency Session"',
    'mission "A2 Republic Resettlement Council: After Action"',
    "Lena Orr",
    '"offer precedence" 9',
    '"world: republic displacement pressure" >= 2',
    '"world: republic displacement pressure" >= 4',
    '"world: republic displacement pressure" < 2',
    'has "world: republic resettlement surge"',
    '"world: republic border pressure" >= 4',
    '"world: republic border pressure" < 4',
    '"A2 Republic Resettlement Council: priority family unity" = 1',
    '"A2 Republic Resettlement Council: priority work continuity" = 1',
    '"A2 Republic Resettlement Council: priority distributed placement" = 1',
    '"A2 Republic Resettlement Council: refused" = 1',
    '"A2 Republic Resettlement Council: followup pending" = 1',
    '"A2 Republic Resettlement Council: followup pending" = 0',
    '"A2 Republic Resettlement Council: followup seen" = 1',
    '"A2 Republic Resettlement Council: refusal respected" = 1',
    'branch refused',
    'has "A2 Republic Resettlement Council: refused"',
    'label refused',
    'label family_border_high',
    'label family_border_low',
    'label work_border_high',
    'label work_border_low',
    'label distributed_border_high',
    'label distributed_border_low',
    'label finish',
)
for token in required:
    need(token)

if text.count('mission "A2 Republic Resettlement Council:') != 2:
    errors.append("expected exactly 2 A2 Republic Resettlement Council missions")
if text.count('"offer precedence" 9') != 2:
    errors.append("both state-only missions must use offer precedence 9")
if re.search(r"^\s*accept\s*$", text, re.MULTILINE):
    errors.append("state-only dialogue must not use objective-less accept")
if len(re.findall(r"^\s*decline\s*$", text, re.MULTILINE)) != 5:
    errors.append("expected exactly 5 state-only decline terminals")

for state in A1_STATES:
    escaped = re.escape(state)
    illegal = re.compile(
        rf'^\s*(?:set|clear)\s+"{escaped}"|"{escaped}"\s*(?:\+=|-=|=\s*\d)',
        re.MULTILINE,
    )
    if illegal.search(text):
        errors.append(f"A2 illegally writes authoritative A1 state: {state}")

# These missions are pure dialogue/state machines, not gameplay-objective missions.
objective_directives = re.compile(
    r'^\t(?:destination|waypoint|stopover|cargo|passengers?|npc|timer|deadline|clearance)\b',
    re.MULTILINE,
)
if objective_directives.search(text):
    errors.append("unexpected gameplay objective directive in state-only A2 slice")

# Each positive policy has a distinct high/low-border consequence.
outcomes = (
    "Orr remembers family under pressure",
    "Orr remembers family stabilized",
    "Orr remembers work under pressure",
    "Orr remembers work stabilized",
    "Orr remembers distribution under pressure",
    "Orr remembers distribution stabilized",
)
for outcome in outcomes:
    need(f'"A2 Republic Resettlement Council: {outcome}" = 1')

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("PASS")
print("missions=2")
print("named_character=Lena Orr")
print("authoritative_A1_inputs=3 read-only")
print("initial_routes=family, work, distributed, refusal")
print("after_action_variants=6 + explicit refusal")
print("offer_precedence=9 on both missions")
print("state_only_terminals=5 decline, 0 accept")
print("persistent_A2_memory=yes")
