#!/usr/bin/env python3
"""Focused structural validator for A2 Free Worlds Relief Coordination."""
from pathlib import Path
import re
import sys


def require(text: str, needle: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"missing: {needle}")


def assignment_names(text: str) -> list[str]:
    names: list[str] = []
    pattern = re.compile(r'^\s*"([^"]+)"\s*(?:\+=|-=|=(?!=))\s*')
    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            names.append(match.group(1))
    return names


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/human/a2 free worlds relief coordination.txt"
    )
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    header = (
        "# Copyright (c) 2026 by the Endless Sky contributors\n"
        "#\n"
        "# Endless Sky is free software: you can redistribute it and/or modify it under the\n"
        "# terms of the GNU General Public License as published by the Free Software\n"
    )
    if not text.startswith(header):
        errors.append("canonical GPL header missing")
    if not text.endswith("\n"):
        errors.append("missing trailing newline")

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    expected_missions = [
        "A2 Free Worlds Relief Coordination: Surge Briefing",
        "A2 Free Worlds Relief Coordination: After Action",
    ]
    if missions != expected_missions:
        errors.append(f"mission order mismatch: {missions!r}")

    for needle in (
        "Imani Vale",
        '"world: free worlds relief demand" >= 3',
        '"world: free worlds relief demand" >= 5',
        '"world: free worlds relief demand" < 3',
        '"world: free worlds relief demand" == 0',
        '"world: free worlds relief demand" > 0',
        '"A2 Free Worlds Relief Coordination: priority medical" = 1',
        '"A2 Free Worlds Relief Coordination: priority throughput" = 1',
        '"A2 Free Worlds Relief Coordination: priority distribution" = 1',
        '"A2 Free Worlds Relief Coordination: refused" = 1',
        '"A2 Free Worlds Relief Coordination: followup pending" = 1',
        '"A2 Free Worlds Relief Coordination: followup pending" = 0',
        '"A2 Free Worlds Relief Coordination: followup seen" = 1',
        '"A2 Free Worlds Relief Coordination: refusal respected" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers medical clear" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers medical residual" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers throughput clear" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers throughput residual" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers distribution clear" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers distribution residual" = 1',
        'branch refused\n\t\t\t\thas "A2 Free Worlds Relief Coordination: refused"',
        'label refused',
        'label finish',
        'no recorded allocation route',
    ):
        require(text, needle, errors)

    for label in (
        "severe",
        "triage",
        "medical",
        "throughput",
        "distribution",
        "refuse",
        "medical_clear",
        "medical_residual",
        "throughput_clear",
        "throughput_residual",
        "distribution_clear",
        "distribution_residual",
        "refused",
        "finish",
    ):
        require(text, f"label {label}", errors)

    if text.count('"offer precedence" 9') != 2:
        errors.append("both state-only missions must use offer precedence 9")
    if len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)) != 5:
        errors.append("expected exactly five state-only decline terminals")
    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        errors.append("state-only mission must not use accept")

    # All six positive after-action outcomes and explicit refusal must converge.
    for route in (
        "medical_clear",
        "medical_residual",
        "throughput_clear",
        "throughput_residual",
        "distribution_clear",
        "distribution_residual",
        "refused",
    ):
        marker = f"label {route}"
        start = text.find(marker)
        if start < 0:
            continue
        next_label = text.find("\n\t\t\tlabel ", start + len(marker))
        block = text[start: next_label if next_label >= 0 else len(text)]
        if "goto finish" not in block:
            errors.append(f"after-action route does not converge through finish: {route}")

    # A1 relief-demand state and every non-A2 namespace are read-only.
    writes = assignment_names(text)
    for name in writes:
        if not name.startswith("A2 Free Worlds Relief Coordination:"):
            errors.append(f"write outside A2 relief namespace: {name}")
    if any(name.startswith("world:") for name in writes):
        errors.append("world state must remain read-only")

    forbidden_directives = (
        "destination ",
        "waypoint ",
        "stopover ",
        "cargo ",
        "outfit ",
        "ship ",
        "fleet ",
        "npc ",
        "payment ",
        "fine ",
        "reputation ",
        "timer ",
    )
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("`"):
            continue
        if any(stripped.startswith(prefix) for prefix in forbidden_directives):
            errors.append(f"unexpected gameplay/material directive: {stripped}")

    labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_]+)\s*$', text, flags=re.MULTILINE))
    gotos = re.findall(r'\bgoto\s+([A-Za-z0-9_]+)\b', text)
    missing_targets = sorted(set(gotos) - labels)
    if missing_targets:
        errors.append(f"undeclared local goto targets: {missing_targets}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print("missions=2")
    print("named_character=Imani Vale")
    print("authoritative_input=world: free worlds relief demand")
    print("initial_routes=medical,throughput,distribution,refusal")
    print("after_action_variants=6+explicit_refusal+defensive_fallback")
    print("state_only_terminals=5_decline,0_accept")
    print("authoritative_A1_writes=none")
    print("persistent_A2_memory=yes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
