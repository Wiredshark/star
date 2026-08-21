#!/usr/bin/env python3
"""Focused structural validator for B2 Coalition Translation Appeal Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/coalition/b2 coalition translation appeal compact.txt")
PREFIX = "B2 Coalition Translation Appeal Compact:"


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
        f"{PREFIX} Interpreter Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for phrase in (
        "privately you think of that person as the Interpreter",
        "in your own head you call that person the Arbiter",
        "Neither word is a title or office they have given you",
    ):
        if phrase not in text:
            fail(f"missing recurring-character continuity phrase: {phrase}")

    if text.count('government "Coalition"') != 3:
        fail("all three missions must use existing Coalition government")
    if text.count('has "license: Coalition"') != 3:
        fail("all three missions must require existing Coalition license")

    for route in ("route source first", "route local rendering", "route paired records"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["disposition ledger", "provenance packet"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("later reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("later reader must persist completion")

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
        "source wording",
        "literal translation",
        "working interpretation",
        "review status",
        "alternative",
        "port-arbitration",
    ):
        if phrase not in lower:
            fail(f"missing Coalition interpretation/arbitration continuity concept: {phrase}")

    for phrase in (
        "portable translation-provenance packet",
        "source wording, translator, literal rendering, assumptions, alternatives, revisions, confidence, and disposition",
        "dual-language disposition ledger",
        "source evidence stays fixed",
    ):
        if phrase not in text:
            fail(f"missing translation-provenance invariant: {phrase}")

    if "repeated copies of one translation must never become independent corroboration" not in lower:
        fail("missing translation-provenance invariant: repeated copies remain one evidence lineage")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")

    review_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Review"'))
    if review_block.count(f'"{PREFIX} reviewed" = 1') != 2:
        fail("each terminal Review path must persist reviewed exactly once")

    if "new central authority has appeared" not in text:
        fail("missing explicit continuity boundary against centralized Coalition authority")

    print("PASS: B2 Coalition Translation Appeal Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Interpreter + Arbiter private shorthands")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Interpreter Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=interpretation register + port arbitration ledger")
    print("PASS: provenance_rule=repeated translation copies are one evidence lineage")


if __name__ == "__main__":
    main()
