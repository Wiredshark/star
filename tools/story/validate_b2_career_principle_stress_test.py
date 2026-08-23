#!/usr/bin/env python3
"""Focused structural validator for B2 Career Principle Stress Test."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 career principle stress test.txt")
PREFIX = "B2 Career Principle Stress Test:"
BORDER = "world: republic border pressure"
A2_PREFIX = "A2 Career Review:"


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
    expected = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Sorn Remembers"]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if 'event "B2 Career Principle Stress Test: Review Ready"' not in text:
        fail("missing delayed Review-ready event")
    if text.count('event "B2 Career Principle Stress Test: Review Ready" 7 11') != 3:
        fail("each substantive route must schedule Review Ready at 7-11 days")

    for name in ("Nia Calder", "Rafi Sorn"):
        if name not in text:
            fail(f"missing named character: {name}")

    if text.count('government "Republic"') != 3:
        fail("all three missions must be Republic scoped")
    if text.count('not attributes "station"') != 3:
        fail("all three missions must exclude stations")

    # Consume A2 Career Review memory without writing it.
    required_a2_reads = (
        f'has "{A2_PREFIX} later reader seen"',
        f'has "{A2_PREFIX} principle margin"',
        f'has "{A2_PREFIX} principle force"',
        f'has "{A2_PREFIX} principle options"',
    )
    for token in required_a2_reads:
        if token not in text:
            fail(f"missing A2 dependency/read: {token}")

    for line in text.splitlines():
        stripped = line.strip()
        if A2_PREFIX in stripped and re.search(r'(?:\+=|-=|\+\+|--|<\?=|>\?=|\?=|(?<![<>])=(?!=))', stripped):
            fail(f"B2 must not mutate A2-owned state: {stripped}")

    # A1 owns the live border pressure signal; B2 reads high and recovered states only.
    for token in (f'"{BORDER}" >= 4', f'"{BORDER}" <= 2'):
        if token not in text:
            fail(f"missing A1 border-pressure gate: {token}")
    for line in text.splitlines():
        stripped = line.strip()
        if BORDER in stripped and re.search(r'(?:\+=|-=|\+\+|--|<\?=|>\?=|\?=|(?<![<>])=(?!=))', stripped):
            fail(f"B2 must not mutate A1-owned state: {stripped}")

    for route in ("route default", "route explicit exception", "route hypothesis"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["portable rationale", "revalidation cycle"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("Sorn Remembers must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("Sorn Remembers must persist completion")

    direct_writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE)
    for key in direct_writes:
        if not key.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {key}")

    # State-only conversation lifecycle: no accepted objective-less missions.
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

    # Every conversation goto must resolve locally.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    # Continuity contract: the A2 principle is remembered evidence, not inherited
    # authority. Current conditions, exceptions/revisions, outcomes, uncertainty,
    # source lineage, and review status remain distinguishable.
    continuity_terms = (
        "not an order",
        "evidence about how one experienced captain thinks",
        "default, not command",
        "exception",
        "hypothesis",
        "portable command-rationale packet",
        "revalidation cycle",
        "uncertainty",
        "source",
        "repetition of one old note never counts as independent corroboration",
    )
    for term in continuity_terms:
        if term not in lowered:
            fail(f"missing career-principle continuity concept: {term}")

    # Do not turn the Pilot Guild teaching practice into binding Republic doctrine.
    if re.search(r'(?:pilot guild|republic)\s+(?:command|career)\s+(?:authority|law|doctrine)', lowered):
        fail("unexpected centralized/binding career-doctrine claim")

    print("PASS: B2 Career Principle Stress Test structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: a2_career_review=read_only")
    print("PASS: a1_republic_border_pressure=read_only")
    print("PASS: delayed_review=7-11 days")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Sorn Remembers")
    print("PASS: lifecycle=7 declines / 0 accepts")
    print("PASS: mutation_surface=B2 conditions only")


if __name__ == "__main__":
    main()
