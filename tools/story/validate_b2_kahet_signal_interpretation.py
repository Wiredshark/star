#!/usr/bin/env python3
"""Focused structural validator for B2 Ka'het Signal Interpretation."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/kahet/b2 kahet signal interpretation.txt")
PREFIX = "B2 Ka'het Signal Interpretation:"


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
        f"{PREFIX} Scout Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if 'event "B2 Ka\'het Signal Interpretation: Review Ready"' not in text:
        fail("missing delayed review event")
    if text.count('event "B2 Ka\'het Signal Interpretation: Review Ready" 7 11') != 3:
        fail("exactly three substantive initial routes must schedule delayed review")

    for phrase in (
        "First Contact: Ka'het: Remnant 1B: offered",
        "Ka'het History: Lost Network Register: offered",
        "Ka'het History: Builder-Ka'het Distinction Ledger: offered",
        "Interpreter",
        "Scout",
    ):
        if phrase not in text:
            fail(f"missing B1/character continuity phrase: {phrase}")

    if text.count('government "Remnant"') != 3:
        fail("all three missions must remain scoped to Remnant sources")

    for route in ("route translation", "route field", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent initial route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["confidence atlas", "contradiction register"]
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
        "first contact: ka'het",
        "ka'het history:",
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
        "original signal",
        "alternate readings",
        "current observations",
        "translation confidence",
        "observation date",
        "unresolved contradictions",
        "what the ka'het had transmitted",
        "historical reconstruction and current navigation",
    ):
        if phrase not in lower:
            fail(f"missing signal-interpretation/accountability concept: {phrase}")

    # Preserve B1's epistemic boundary. Old automated traffic can establish that
    # a connection or task was expected, not current site existence, Builder
    # motive, exact collapse chronology, or omniscient Ka'het historical knowledge.
    forbidden_certainty_patterns = (
        r"the ka'het know exactly",
        r"the ka'het remember exactly",
        r"the builders intended",
        r"the builders created the ka'het so that",
        r"the station still exists because",
        r"the signal proves the station still exists",
    )
    for pattern in forbidden_certainty_patterns:
        if re.search(pattern, lower):
            fail(f"asserts unsupported Ka'het/Builder certainty: {pattern}")

    for phrase in (
        "confidence-tagged route atlas",
        "source type",
        "explicit expiry",
        "contradiction register",
        "distinct linked entries",
        "research target instead of an invisible editing choice",
    ):
        if phrase not in lower:
            fail(f"missing terminal accountability invariant: {phrase}")

    if "private shorthand" not in lower or "not formal offices" not in lower:
        fail("Interpreter/Scout must remain player-private shorthand, not canonical offices")

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("decline path must not set introduced")
    if 'event "B2 Ka\'het Signal Interpretation: Review Ready" 7 11' in decline_block:
        fail("decline path must not schedule review")

    print("PASS: B2 Ka'het Signal Interpretation structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Interpreter + Scout (player-private shorthand)")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Scout Remembers")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: b1_inputs=Lost Network Register + Builder-Ka'het Distinction Ledger")
    print("PASS: continuity=historical signal evidence remains distinct from current field truth")


if __name__ == "__main__":
    main()
