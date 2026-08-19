#!/usr/bin/env python3
"""Focused structural validator for B2 Rulei Exposure Accountability."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/rulei/b2 rulei exposure accountability.txt")
PREFIX = "B2 Rulei Exposure Accountability:"


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
        f"{PREFIX} Orlov Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if 'event "B2 Rulei Exposure Accountability: Review Ready"' not in text:
        fail("missing delayed review event")
    if text.count('event "B2 Rulei Exposure Accountability: Review Ready" 7 11') != 3:
        fail("exactly three substantive initial routes must schedule delayed review")

    for phrase in (
        "Dr. Sena Orlov",
        "Eli Verran",
        "Rulei History: Exposure Register: offered",
        "Rulei History: Testimony Protocol: offered",
        "First Contact: Rulei: offered",
    ):
        if phrase not in text:
            fail(f"missing B1/character continuity phrase: {phrase}")

    if text.count('source "Earth"') != 3:
        fail("all three missions must remain scoped to Earth")

    for route in ("route clinical", "route witness", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["bounded certificate", "consent escrow"]
    if sorted(set(settlements)) != expected_settlements:
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
        "first contact: rulei",
        "rulei history:",
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
        "directly observed symptoms",
        "testimony",
        "interpretation",
        "current fitness",
        "expiry",
        "consent",
        "nobody can prove what caused the symptoms",
    ):
        if phrase not in lower:
            fail(f"missing Rulei contact-uncertainty/accountability concept: {phrase}")

    # Reject affirmative unsupported causal/motive claims, while allowing the
    # production text to explicitly negate those claims (e.g. "not a claim that
    # the Rulei caused lasting damage").
    forbidden_certainty_patterns = (
        r"(?<!not a claim that )the rulei caused lasting damage",
        r"rulei psionics permanently damaged",
        r"the rulei intended to harm",
        r"the rulei wanted to harm",
    )
    for pattern in forbidden_certainty_patterns:
        if re.search(pattern, lower):
            fail(f"asserts unsupported Rulei causation or motive: {pattern}")

    for phrase in (
        "bounded exposure certificate",
        "observed exposure history",
        "raw testimony stays sealed",
        "consent escrow",
        "purpose, audience, and expiry",
        "interpretive claims require renewed consent or a fresh clinical finding",
    ):
        if phrase not in lower:
            fail(f"missing accountability invariant: {phrase}")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")
    if 'event "B2 Rulei Exposure Accountability: Review Ready" 7 11' in decline_block:
        fail("decline path must not schedule review")

    print("PASS: B2 Rulei Exposure Accountability structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=Dr. Sena Orlov + Eli Verran")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Orlov Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=Exposure Register + Testimony Protocol")
    print("PASS: continuity=observed exposure effects remain distinct from unsupported causation")


if __name__ == "__main__":
    main()
