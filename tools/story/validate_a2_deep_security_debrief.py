#!/usr/bin/env python3
"""Focused structural validator for A2 Deep Security Debrief."""
from pathlib import Path
import re
import sys


def require(text: str, needle: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"missing: {needle}")


def assignment_names(text: str) -> list[str]:
    pattern = re.compile(r'^\s*"([^"]+)"\s*(?:\+=|-=|=(?!=))\s*')
    return [
        match.group(1)
        for line in text.splitlines()
        if (match := pattern.match(line))
    ]


def directive_lines(text: str) -> list[str]:
    blocked = re.compile(
        r"^(?:destination|waypoint|stopover|cargo|passenger|outfit|ship|fleet|npc|timer|payment|fine|reputation)\b",
        re.IGNORECASE,
    )
    return [line.strip() for line in text.splitlines() if blocked.match(line.strip())]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/human/a2 deep security debrief.txt"
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
        errors.append("missing canonical GPL header")
    if not text.endswith("\n"):
        errors.append("missing trailing newline")

    required = [
        'mission "A2 Deep Debrief: First Meeting"',
        'mission "A2 Deep Debrief: Later Reader"',
        "Mara Venn",
        '[Convoy record: Deep Syndicate escort]',
        '[Combat record: veteran escort]',
        'has "Deep: Syndicate Convoy: done"',
        '"combat rating" >= 80',
        '"A2 Deep Debrief: approach convoy precedent" = 1',
        '"A2 Deep Debrief: approach threat judgment" = 1',
        '"A2 Deep Debrief: approach procedure" = 1',
        '"A2 Deep Debrief: refused" = 1',
        '"A2 Deep Debrief: refusal respected" = 1',
        '"A2 Deep Debrief: venn future field contact" = 1',
        '"A2 Deep Debrief: venn future security contact" = 1',
        '"A2 Deep Debrief: venn future review contact" = 1',
        '"A2 Deep Debrief: later reader pending" = 0',
        "label convoy",
        "label veteran",
        "label procedure",
        "label refuse",
        "label finish",
        "branch convoy",
        "branch veteran",
        "branch procedure",
        "branch refuse",
    ]
    for needle in required:
        require(text, needle, errors)

    if text.count('mission "A2 Deep Debrief:') != 2:
        errors.append("expected exactly two A2 Deep Debrief missions")
    if text.count("\toffer precedence 9\n") != 2:
        errors.append("both missions must use offer precedence 9")
    if text.count("\t\t\tdecline\n") != 5:
        errors.append("expected exactly five state-only decline terminals")
    if re.search(r"^\s*accept\s*$", text, flags=re.MULTILINE):
        errors.append("state-only Deep Debrief missions must not accept")

    assignments = assignment_names(text)
    illegal = [name for name in assignments if not name.startswith("A2 Deep Debrief:")]
    if illegal:
        errors.append("writes outside A2 Deep Debrief namespace: " + ", ".join(illegal))
    if "Deep: Syndicate Convoy: done" in assignments or "combat rating" in assignments:
        errors.append("upstream history/capability inputs must remain read-only")

    if text.count('"A2 Deep Debrief: later reader pending" = 1') != 4:
        errors.append("all four First Meeting routes must arm the later reader exactly once")
    if text.count('"A2 Deep Debrief: later reader pending" = 0') != 1:
        errors.append("Later Reader must close pending state exactly once")

    for route in ("convoy", "veteran", "procedure", "refuse"):
        if f"branch {route}" not in text:
            errors.append(f"Later Reader missing explicit {route} branch")
    if "The review record says you were involved, but the route marker is incomplete." not in text:
        errors.append("missing defensive incomplete-record reader fallback")

    labels = set(re.findall(r"^\s*label\s+([A-Za-z0-9_-]+)\s*$", text, flags=re.MULTILINE))
    gotos = re.findall(r"^\s*goto\s+([A-Za-z0-9_-]+)\s*$", text, flags=re.MULTILINE)
    missing_labels = sorted(set(gotos) - labels)
    if missing_labels:
        errors.append("goto target(s) missing label: " + ", ".join(missing_labels))

    blocked_directives = directive_lines(text)
    if blocked_directives:
        errors.append("unexpected gameplay/material directive(s): " + "; ".join(blocked_directives))

    lowered = text.lower()
    for shadow in ("dialogue world state", "dialogue_state", "dialogue memory database"):
        if shadow in lowered:
            errors.append(f"shadow state reference forbidden: {shadow}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print("missions=2")
    print("named_character=Mara Venn")
    print("first_meeting_routes=4")
    print("later_reader_routes=4+defensive_fallback")
    print("persistent_state_sources=Deep: Syndicate Convoy: done, combat rating")
    print("read_only_upstream_inputs=2")
    print("state_only_declines=5; accepts=0")
    print("offer_precedence=9,9")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
