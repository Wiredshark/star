#!/usr/bin/env python3
"""Focused structural validator for B2 Pug Uncertainty Protocol."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/pug/b2 pug uncertainty protocol.txt")
PREFIX = "B2 Pug Uncertainty Protocol:"


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
        f"{PREFIX} Archivist Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if 'event "B2 Pug Uncertainty Protocol: Review Ready"' not in text:
        fail("missing delayed review event")
    if 'event "B2 Pug Uncertainty Protocol: Review Ready" 7 11' not in text:
        fail("all substantive initial routes must schedule delayed review")

    for phrase in (
        "privately you have begun thinking of that one as the Archivist",
        "in your own head you call that one the Interpreter",
        "Neither is a title they have introduced themselves with",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('government "Neutral"') != 3:
        fail("all three missions must use existing Neutral government")
    if text.count('system "Deneb"') != 3:
        fail("all three missions must remain scoped to Deneb")
    if 'has "main plot completed"' not in text:
        fail("offer must remain post-main-plot")
    if 'has "Pug Contact Testimony Archive: offered"' not in text:
        fail("offer must consume B1 Pug Contact Testimony Archive")

    for route in ("route observation", "route interpretation", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["provenance ladder", "uncertainty envelope"]
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
        "main plot",
        "pug contact testimony archive",
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
        "observed",
        "motive",
        "witness",
        "sensor",
        "translation",
        "confidence",
        "competing explanation",
    ):
        if phrase not in lower:
            fail(f"missing B1 contact-uncertainty continuity concept: {phrase}")

    for forbidden_certainty in (
        "the pug intended",
        "the pug wanted",
        "the pug invaded because",
        "the pug withdrew because",
    ):
        if forbidden_certainty in lower:
            fail(f"asserts unsupported Pug motive: {forbidden_certainty}")

    for phrase in (
        "immutable observation record",
        "separately labeled interpretation",
        "provenance ladder",
        "machine-readable link to the observation, interpretation step, confidence, and later revisions",
        "uncertainty envelope",
        "observed behavior does not establish motive",
    ):
        if phrase not in lower:
            fail(f"missing uncertainty-protocol invariant: {phrase}")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")
    if 'event "B2 Pug Uncertainty Protocol: Review Ready" 7 11' in decline_block:
        fail("decline path must not schedule review")

    if text.count('event "B2 Pug Uncertainty Protocol: Review Ready" 7 11') != 3:
        fail("exactly three substantive initial routes must schedule review")

    print("PASS: B2 Pug Uncertainty Protocol structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Archivist + Interpreter private shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Archivist Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_input=Pug Contact Testimony Archive")
    print("PASS: continuity=observed behavior remains distinct from inferred motive")


if __name__ == "__main__":
    main()
