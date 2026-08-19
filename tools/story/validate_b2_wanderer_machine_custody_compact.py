#!/usr/bin/env python3
"""Focused structural validator for B2 Wanderer Machine Custody Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/wanderer/b2 wanderer machine custody compact.txt")
PREFIX = "B2 Wanderer Machine Custody Compact:"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    if not path.is_file():
        fail(f"missing content file: {path}")

    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    expected = [
        f"{PREFIX} Offer",
        f"{PREFIX} Review",
        f"{PREFIX} Engineer Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if f'event "{PREFIX} Review Ready"' not in text:
        fail("missing delayed review event")
    if text.count(f'event "{PREFIX} Review Ready" 7 11') != 3:
        fail("exactly three substantive initial routes must schedule delayed review")

    for phrase in (
        "wanderers sestor done",
        "Wanderer History: Factory Deactivation Provenance Ledger: offered",
        "Wanderer History: Autonomous Weapon Custody Record: offered",
        "Curator",
        "Engineer",
    ):
        if phrase not in text:
            fail(f"missing B1/character continuity phrase: {phrase}")

    if text.count('government "Wanderer"') != 3:
        fail("all three missions must remain scoped to Wanderer sources")

    for route in ("route custody", "route sandbox", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = [
        "transferable custody packet",
        "two-key derivative review",
    ]
    if sorted(set(settlements)) != sorted(expected_settlements):
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("aftermath reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("aftermath reader must persist completion")

    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE)
    for raw in writes:
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    forbidden_write_tokens = (
        "world:",
        "credits",
        "reputation:",
        "combat rating",
        "cargo ",
        "outfit ",
        "ship ",
        "fleet ",
        "wanderers sestor done",
        "wanderer history:",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if " = " in stripped and any(token in stripped for token in forbidden_write_tokens):
            fail(f"forbidden direct state mutation: {line.strip()}")

    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    for phrase in (
        "sealed core",
        "chain of custody",
        "working image",
        "derived research image",
        "recovery location",
        "transformation",
        "unreadable",
        "uncertain",
        "transferable custody packet",
        "two-key derivative review",
        "independent reexamination",
        "sealed original",
    ):
        if phrase not in lower:
            fail(f"missing custody/provenance concept: {phrase}")

    # Preserve B1's epistemic/canon boundary: the machine war archives distinguish
    # observed behavior and recovered technology from unsupported claims about
    # original directives or universal machine motives.
    forbidden_certainty_patterns = (
        r"the kor sestor were created to",
        r"the kor mereti were created to",
        r"the machines wanted to exterminate",
        r"the machines wanted peace",
        r"the core proves why the machines",
        r"the builders intended the machines",
    )
    for pattern in forbidden_certainty_patterns:
        if re.search(pattern, lower):
            fail(f"asserts unsupported machine-war certainty: {pattern}")

    for phrase in (
        "private shorthand",
        "not formal titles",
        "battlefield evidence",
        "research utility",
        "derivative",
        "chain of responsibility",
    ):
        if phrase not in lower:
            fail(f"missing authority/accountability invariant: {phrase}")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")
    if f'event "{PREFIX} Review Ready" 7 11' in decline_block:
        fail("decline path must not schedule review")

    print("PASS: B2 Wanderer Machine Custody Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Curator + Engineer (player-private shorthand)")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Engineer Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=Factory Deactivation Provenance Ledger + Autonomous Weapon Custody Record")
    print("PASS: continuity=machine evidence/provenance remains distinct from derived research claims")


if __name__ == "__main__":
    main()
