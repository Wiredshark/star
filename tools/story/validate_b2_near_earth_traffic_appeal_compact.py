#!/usr/bin/env python3
"""Focused structural validator for B2 Near Earth Traffic Appeal Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 near earth traffic appeal compact.txt")
PREFIX = "B2 Near Earth Traffic Appeal Compact:"
B1_GATE = "Near Earth Traffic Archive: offered"
REVIEW_EVENT = "B2 Near Earth Traffic Appeal Compact: Review Ready"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    if not path.is_file():
        fail(f"missing content file: {path}")

    text = path.read_text(encoding="utf-8")
    lowered = text.lower()

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    expected = [
        f"{PREFIX} Offer",
        f"{PREFIX} Review",
        f"{PREFIX} Sera Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if text.count(f'event "{REVIEW_EVENT}"\n') != 1:
        fail("review-ready event definition must appear exactly once")
    if text.count(f'event "{REVIEW_EVENT}" 7 11') != 3:
        fail("each substantive initial route must schedule the 7-11 day Review")
    if f'has "{PREFIX} review ready"' not in text:
        fail("Review must require delayed review-ready state")

    for name in ("Sera Venn", "Oren Mall"):
        if name not in text:
            fail(f"missing named character {name}")

    if text.count('government "Republic"') != 3:
        fail("all three missions must be Republic-scoped")
    if text.count('attributes "near earth"') != 3:
        fail("all three missions must be Near Earth-scoped")
    if text.count('not attributes "station"') != 3:
        fail("all three missions must exclude stations")
    if f'has "{B1_GATE}"' not in text:
        fail("Offer must consume the integrated B1 Near Earth Traffic Archive")

    routes = (
        "route change provenance",
        "route current schedule link",
        "route paired schedule ledger",
    )
    for route in routes:
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["expiry and renewal", "portable slot change packet"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("terminal settlements must each be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("Sera reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("Sera reader must persist completion")

    # Dialogue-only state missions must not remain accepted after their conversation.
    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        fail("dialogue-only B2 missions must terminate with decline, not accept")

    # All direct persistent writes must remain inside the B2 namespace.
    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    forbidden_write_tokens = (
        "credits",
        "reputation:",
        "combat rating",
        "cargo ",
        "outfit ",
        "ship ",
        "fleet ",
        "world:",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if " = " in stripped and any(token in stripped for token in forbidden_write_tokens):
            fail(f"forbidden direct state mutation: {line.strip()}")

    # Validate local goto/label integrity within each mission block.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    # Continuity: copied traffic schedules must preserve the difference between
    # a historical emergency exception and a current operational restriction.
    required_terms = (
        "original slot",
        "reassigned slot",
        "emergency",
        "affected ship",
        "review point",
        "closure evidence",
        "expiry-and-renewal",
        "historical",
        "current restriction",
    )
    for term in required_terms:
        if term not in lowered:
            fail(f"missing traffic-record continuity concept: {term}")

    # Practical inter-port procedure must not become invented centralized authority.
    forbidden_authority = (
        "centralized near earth traffic authority",
        "near earth traffic government",
        "universal near earth traffic code",
    )
    if any(term in lowered for term in forbidden_authority):
        fail("unexpected centralized Near Earth traffic authority claim")

    print("PASS: B2 Near Earth Traffic Appeal Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: b1_traffic_archive_dependency=present")
    print("PASS: delayed_review=7-11 days")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Sera Remembers")
    print("PASS: lifecycle=dialogue-only decline")
    print("PASS: mutation_surface=B2 conditions only")


if __name__ == "__main__":
    main()
