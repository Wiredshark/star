#!/usr/bin/env python3
"""Focused structural validator for A2 Southern Rim Traffic Coordination."""
from pathlib import Path
import re
import sys

A2_PREFIX = "A2 Southern Rim Traffic Coordination:"
A1_CONGESTION = "world: southern rim transit congestion"
A1_RESCUE = "world: merchant rescue load"
GPL_PREFIX = "# Copyright (c) 2026 by the Endless Sky contributors\n#\n# Endless Sky is free software:"

POSITIVE_POLICIES = (
    "policy emergency corridors",
    "policy staggered clearance",
    "policy distributed routing",
)
OUTCOMES = (
    "Solano remembers emergency high rescue",
    "Solano remembers emergency low rescue",
    "Solano remembers staggered high rescue",
    "Solano remembers staggered low rescue",
    "Solano remembers distributed high rescue",
    "Solano remembers distributed low rescue",
)
FOLLOWUP_LABELS = (
    "refused",
    "emergency_rescue_high",
    "emergency_rescue_low",
    "staggered_rescue_high",
    "staggered_rescue_low",
    "distributed_rescue_high",
    "distributed_rescue_low",
    "finish",
)
OBJECTIVE_DIRECTIVES = (
    "cargo ", "passenger ", "destination ", "waypoint ", "stopover ",
    "npc ", "deadline ", "payment ", "outfit ", "ship ", "fleet ",
)


def assignment_name(line: str) -> str | None:
    match = re.match(r'^\s*"([^"]+)"\s*(?:\+=|-=|=|<\?=|>\?=)\s*-?\d+\s*$', line)
    return match.group(1) if match else None


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 southern rim traffic coordination.txt")
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []

    if not text.startswith(GPL_PREFIX):
        errors.append("missing canonical GPL content header")
    if not text.endswith("\n"):
        errors.append("missing trailing newline")

    if text.count('mission "A2 Southern Rim Traffic Coordination:') != 2:
        errors.append("expected exactly two A2 Southern Rim Traffic Coordination missions")
    if text.count('"offer precedence" 9') != 2:
        errors.append("expected offer precedence 9 on both missions")
    if text.count("\n\t\t\t\tdecline\n") != 5:
        errors.append("expected exactly five state-only decline terminals")
    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        errors.append("state-only slice must not contain terminal accept")

    required = [
        'mission "A2 Southern Rim Traffic Coordination: Briefing"',
        'mission "A2 Southern Rim Traffic Coordination: After Action"',
        'Rhea Solano',
        f'"{A1_CONGESTION}" >= 4',
        f'"{A1_CONGESTION}" >= 6',
        f'"{A1_CONGESTION}" < 4',
        f'"{A1_RESCUE}" >= 3',
        f'"{A1_RESCUE}" < 3',
        f'"{A2_PREFIX} refused" = 1',
        f'has "{A2_PREFIX} refused"',
        'branch refused',
        'label refused',
        'label finish',
        f'"{A2_PREFIX} followup pending" = 1',
        f'"{A2_PREFIX} followup pending" = 0',
        f'"{A2_PREFIX} followup seen" = 1',
        f'"{A2_PREFIX} refusal respected" = 1',
    ]
    for policy in POSITIVE_POLICIES:
        required.append(f'"{A2_PREFIX} {policy}" = 1')
        required.append(f'has "{A2_PREFIX} {policy}"')
    for outcome in OUTCOMES:
        required.append(f'"{A2_PREFIX} {outcome}" = 1')
    for label in FOLLOWUP_LABELS:
        required.append(f"label {label}")

    for needle in required:
        if needle not in text:
            errors.append(f"missing: {needle}")

    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        assigned = assignment_name(line)
        if assigned and not assigned.startswith(A2_PREFIX):
            errors.append(f"write outside A2 namespace at line {lineno}: {assigned}")
        if stripped.startswith("set ") or stripped.startswith("clear "):
            errors.append(f"set/clear mutation forbidden at line {lineno}: {stripped}")
        if line.startswith("\t") and any(stripped.startswith(token) for token in OBJECTIVE_DIRECTIVES):
            errors.append(f"gameplay/material directive forbidden at line {lineno}: {stripped}")

    for state in (A1_CONGESTION, A1_RESCUE):
        for lineno, line in enumerate(lines, 1):
            if state in line and assignment_name(line) == state:
                errors.append(f"authoritative A1-state write at line {lineno}: {state}")

    # Each positive route must write exactly one policy and arm the follow-up once.
    for policy in POSITIVE_POLICIES:
        if text.count(f'"{A2_PREFIX} {policy}" = 1') != 1:
            errors.append(f"policy write cardinality must be one: {policy}")
    if text.count(f'"{A2_PREFIX} refused" = 1') != 1:
        errors.append("refusal write cardinality must be one")
    if text.count(f'"{A2_PREFIX} followup pending" = 1') != 4:
        errors.append("all four Briefing routes must arm exactly one follow-up")

    # Six positive outcomes plus one explicit refusal result must converge on finish.
    if text.count("goto finish") != 7:
        errors.append("expected seven explicit After Action routes to converge on finish")
    if text.count(f'"{A2_PREFIX} refusal respected" = 1') != 1:
        errors.append("refusal-respected outcome must write exactly once")
    for outcome in OUTCOMES:
        if text.count(f'"{A2_PREFIX} {outcome}" = 1') != 1:
            errors.append(f"outcome write cardinality must be one: {outcome}")

    # Refusal must be a first-class persistent branch, not accidental fallthrough.
    after_action = text.split('mission "A2 Southern Rim Traffic Coordination: After Action"', 1)[1]
    if 'branch refused\n\t\t\t\thas "A2 Southern Rim Traffic Coordination: refused"' not in after_action:
        errors.append("After Action refusal must be explicitly gated by refused state")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print("missions=2")
    print("named_character=Rhea Solano")
    print("authoritative_inputs=southern rim transit congestion, merchant rescue load")
    print("initial_routes=emergency, staggered, distributed, refusal")
    print("briefing_context_variants=combined, gridlock, rescue, baseline")
    print("after_action_variants=6 + explicit refusal")
    print("authoritative_A1_writes=none")
    print("persistent_A2_memory=yes")
    print("state_only_terminal_declines=5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
