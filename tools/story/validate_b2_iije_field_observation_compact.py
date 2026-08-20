#!/usr/bin/env python3
"""Focused structural validator for B2 Iije Field Observation Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/rulei/b2 iije field observation compact.txt")
PREFIX = "B2 Iije Field Observation Compact:"


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
        f"{PREFIX} Pilot Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if 'event "B2 Iije Field Observation Compact: Review Ready"' not in text:
        fail("missing delayed review event")
    if text.count('event "B2 Iije Field Observation Compact: Review Ready" 7 11') != 3:
        fail("exactly three substantive initial routes must schedule delayed review")

    for phrase in (
        "you have private shorthand for them",
        "you think of the careful field biologist as the Observer",
        "the expedition pilot as the Pilot",
        "Neither has introduced those words as a title",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('source "Midgard"') != 2:
        fail("Offer and Review must remain on Midgard")
    if text.count('source "Mirrorlake"') != 1:
        fail("aftermath reader must remain on Mirrorlake")
    if 'has "Rulei: Umbral Reach: offered"' not in text:
        fail("Offer must require Umbral Reach discovery")
    if 'has "Iije History: Stellar Feeding Survey: offered"' not in text:
        fail("Offer must consume B1 Iije Stellar Feeding Survey")

    for route in ("route passive", "route stimulus", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = [
        "reversible field model",
        "stimulus provenance packet",
    ]
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
        "rulei: umbral reach",
        "iije history:",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if " = " in stripped and any(token in stripped for token in forbidden_write_tokens):
            fail(f"forbidden direct state mutation: {line.strip()}")

    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(
            re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE)
        )
        gotos = set(
            re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE)
        )
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    for phrase in (
        "unprovoked behavior",
        "controlled light",
        "stimulus",
        "baseline",
        "ambient",
        "sensor limits",
        "uncertainty",
        "does not establish intent",
    ):
        if phrase not in lower:
            fail(f"missing Iije observation-provenance concept: {phrase}")

    for forbidden_claim in (
        "the iije intended",
        "the jje intended",
        "the jje wanted",
        "the ayym intended",
        "the ayym wanted",
        "the ayym carry jje because",
        "the jje approach humans because",
    ):
        if forbidden_claim in lower:
            fail(f"asserts unsupported Iije motive: {forbidden_claim}")

    for phrase in (
        "stimulus provenance packet",
        "ambient brightness",
        "the exact human stimulus",
        "reversible field models",
        "separable baseline observations and stimulus trials",
        "change a prediction about iije movement without changing what the expedition actually observed",
    ):
        if phrase not in lower:
            fail(f"missing field-observation compact invariant: {phrase}")

    offer_block = next(
        b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"')
    )
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")
    if 'event "B2 Iije Field Observation Compact: Review Ready" 7 11' in decline_block:
        fail("decline path must not schedule review")

    print("PASS: B2 Iije Field Observation Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Observer + Pilot private shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Pilot Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_input=Iije History: Stellar Feeding Survey")
    print("PASS: continuity=spontaneous behavior remains distinct from human-elicited response")


if __name__ == "__main__":
    main()
