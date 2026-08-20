#!/usr/bin/env python3
"""Focused structural validator for B2 Republic Manifest Appeal Compact."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 republic manifest appeal compact.txt")
PREFIX = "B2 Republic Manifest Appeal Compact:"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")

    missions = re.findall(r'^mission "([^"]+)"', text, re.M)
    expected = [
        "B2 Republic Manifest Appeal Compact: Offer",
        "B2 Republic Manifest Appeal Compact: Review",
        "B2 Republic Manifest Appeal Compact: Varo Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected}, got {missions}")

    for name in ("Lena Varo", "Orren Pike"):
        if name not in text:
            fail(f"missing named character {name}")

    for phrase in (
        "Republic customs-history archives",
        "inherited suspicion",
        "current declaration",
        "unresolved challenges",
        "portable disposition packet",
        "new evidence",
    ):
        if phrase not in text:
            fail(f"missing continuity phrase: {phrase}")

    routes = [
        "route correction chain",
        "route current record",
        "route linked records",
    ]
    for route in routes:
        if text.count(f'"{PREFIX} {route}" = 1') != 1:
            fail(f"route write count wrong for {route}")

    if text.count(f'"{PREFIX} declined" = 1') != 1:
        fail("expected exactly one refusal write")

    settlements = [
        "settlement disposition packet",
        "settlement expiry renewal",
    ]
    for settlement in settlements:
        if text.count(f'"{PREFIX} {settlement}" = 1') != 1:
            fail(f"settlement write count wrong for {settlement}")

    if text.count(f'"{PREFIX} aftermath seen" = 1') != 1:
        fail("aftermath must be one-shot")

    # All explicit condition writes in this file must remain B2-owned.
    for match in re.finditer(r'^\s*"([^"]+)"\s*=\s*[-0-9]+\s*$', text, re.M):
        condition = match.group(1)
        if not condition.startswith(PREFIX):
            fail(f"non-B2 condition write: {condition}")

    lowered = text.lower()
    forbidden_commands = (
        "credits +",
        "credits -",
        "reputation ",
        "combat rating",
        "cargo ",
        "outfit ",
        "ship ",
        "fleet ",
    )
    for command in forbidden_commands:
        # Check command-like lines rather than ordinary dialogue words.
        if re.search(rf'^\s*{re.escape(command)}', lowered, re.M):
            fail(f"forbidden material/state mutation command: {command.strip()}")

    # Local goto/label integrity.
    labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', text, re.M))
    gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', text, re.M)
    missing = sorted(set(gotos) - labels)
    if missing:
        fail(f"goto targets missing labels: {missing}")

    # Ensure the core continuity boundary is explicit: review history is not evidence.
    if "decision to investigate as today's new fact" not in text:
        fail("missing explicit repeat-review / evidence boundary")

    print("PASS: B2 Republic Manifest Appeal Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Varo Remembers")
    print("PASS: writes=B2-prefixed only")


if __name__ == "__main__":
    main()
