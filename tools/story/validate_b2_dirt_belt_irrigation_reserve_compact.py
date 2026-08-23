#!/usr/bin/env python3
"""Focused structural validator for B2 Dirt Belt Irrigation Reserve Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 dirt belt irrigation reserve compact.txt")
PREFIX = "B2 Dirt Belt Irrigation Reserve Compact:"
DROUGHT = "world: dirt belt drought pressure"
IRRIGATION = "world: dirt belt irrigation reserve strain"


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
    expected_missions = [
        f"{PREFIX} Offer",
        f"{PREFIX} Review",
        f"{PREFIX} Calder Remembers",
    ]
    if missions != expected_missions:
        fail(f"expected missions {expected_missions!r}, found {missions!r}")

    if 'event "B2 Dirt Belt Irrigation Reserve Compact: Review Ready"' not in text:
        fail("missing delayed Review-ready event")
    if text.count('event "B2 Dirt Belt Irrigation Reserve Compact: Review Ready" 7 11') != 3:
        fail("each positive initial route must schedule Review Ready at 7-11 days")

    for name in ("Mae Calder", "Tobin Shaw"):
        if name not in text:
            fail(f"missing named character: {name}")

    if text.count('government "Republic"') != 3:
        fail("all three missions must use Republic source government")
    if text.count('attributes "dirt belt"') != 3:
        fail("all three missions must be Dirt Belt scoped")
    if text.count('attributes "farming"') != 2:
        fail("Offer and Review must be farming-world scoped")
    if text.count('not attributes "station"') != 3:
        fail("all three missions must exclude stations")

    if 'has "Dirt Belt Water Share Archive: offered"' not in text:
        fail("Offer must consume the integrated B1 Water Share Archive")

    # A1 owns both live resource signals. B2 only reads them.
    required_a1_reads = (
        f'"{DROUGHT}" >= 3',
        f'"{IRRIGATION}" >= 3',
        f'"{DROUGHT}" <= 1',
        f'"{IRRIGATION}" <= 1',
    )
    for token in required_a1_reads:
        if token not in text:
            fail(f"missing A1 state gate: {token}")

    for line in text.splitlines():
        stripped = line.strip()
        if any(signal in stripped for signal in (DROUGHT, IRRIGATION)):
            if re.search(r'(?:\+=|-=|\+\+|--|<\?=|>\?=|\?=|(?<![<>])=(?!=))', stripped):
                fail(f"B2 must not mutate A1-owned state: {stripped}")

    for route in ("route emergency floor", "route capacity repair", "route paired records"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing persistent refusal")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["dual closure", "portable water share"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("Calder Remembers must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("Calder Remembers must persist completion")

    # All persistent direct writes stay in this B2 namespace.
    direct_writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE)
    for key in direct_writes:
        if not key.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {key}")

    # State-only conversation missions close cleanly and create no objective-bearing
    # accepted mission lifecycle.
    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        fail("state-only B2 missions must not use terminal accept")
    declines = re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)
    if len(declines) != 7:
        fail(f"expected exactly 7 terminal declines, found {len(declines)}")

    objective_directives = re.compile(
        r'^\t(?:destination|stopover|waypoint|npc|cargo|passenger|deadline|timer)(?:\s|$)',
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if objective_directives.search(text):
        fail("unexpected gameplay-objective directive in state-only B2 slice")

    # No material/reputation/combat/world mutation.
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
            fail(f"forbidden direct mutation: {line.strip()}")

    # Conversation goto targets must be local and resolvable.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    # Continuity contract: claims and infrastructure capacity are linked but not
    # interchangeable. Recovery of aggregate A1 strain does not itself close every
    # transfer, delivery, borrowed-equipment, or maintenance obligation.
    continuity_terms = (
        "emergency minimum",
        "temporary transfer",
        "physical capacity",
        "maintenance",
        "claim",
        "actually deliver",
        "closure evidence",
        "reconciliation",
        "reserve strain recovered",
    )
    for term in continuity_terms:
        if term not in lowered:
            fail(f"missing irrigation-continuity concept: {term}")

    # Do not manufacture centralized Dirt Belt water authority from the B1 archive.
    if re.search(r'central(?:ized|ised)\s+(?:water|irrigation|dirt belt)\s+(?:authority|government|office)', lowered):
        fail("unexpected centralized Dirt Belt water-authority claim")

    print("PASS: B2 Dirt Belt Irrigation Reserve Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: b1_water_share_dependency=present")
    print("PASS: a1_drought_and_irrigation_state=read_only")
    print("PASS: delayed_review=7-11 days")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Calder Remembers")
    print("PASS: lifecycle=7 declines / 0 accepts")
    print("PASS: mutation_surface=B2 conditions only")


if __name__ == "__main__":
    main()
