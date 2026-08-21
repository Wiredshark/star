#!/usr/bin/env python3
"""Focused structural validator for B2 Merchant Salvage Claim Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 merchant salvage claim compact.txt")
PREFIX = "B2 Merchant Salvage Claim Compact:"
B1_GATE = "Merchant Salvage Provenance Ledger: offered"
WORLD_INPUT = "world: merchant salvage demand"
REVIEW_EVENT = "B2 Merchant Salvage Claim Compact: Review Ready"


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
        f"{PREFIX} Tessa Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if text.count(f'event "{REVIEW_EVENT}"\n') != 1:
        fail("review-ready event definition must appear exactly once")
    if text.count(f'event "{REVIEW_EVENT}" 7 11') != 3:
        fail("each substantive initial route must schedule the 7-11 day Review")
    if f'has "{PREFIX} review ready"' not in text:
        fail("Review must require delayed review-ready state")

    for name in ("Tessa Arlen", "Bram Voss"):
        if name not in text:
            fail(f"missing named character {name}")

    if text.count('government "Merchant"') != 3:
        fail("all three missions must be Merchant-scoped")
    if text.count('not attributes "automaton"') != 3:
        fail("all three missions must exclude automaton sources")
    if f'has "{B1_GATE}"' not in text:
        fail("Offer must consume integrated B1 Merchant Salvage Provenance Ledger")
    if text.count(f'"{WORLD_INPUT}" >= 3') != 1:
        fail("Offer must react to high authoritative A1 salvage demand")
    if text.count(f'"{WORLD_INPUT}" <= 1') != 1:
        fail("Review must wait for authoritative A1 salvage demand recovery")

    routes = (
        "route provenance first",
        "route emergency reuse",
        "route paired records",
    )
    for route in routes:
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(
        rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text
    )
    expected_settlements = ["custody reconciliation", "portable claim packet"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected terminal settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("terminal settlements must each be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("Tessa reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("Tessa reader must persist completion")

    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        fail("dialogue-only B2 missions must terminate with decline, not accept")

    # All direct persistent writes must stay in the B2 namespace.
    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    # A1 signal and all material/reputation state are read-only.
    for line in text.splitlines():
        stripped = line.strip().lower()
        if not re.search(r'\s(?:=|\+=|-=|\?=|<\?=|>\?=)\s', stripped):
            continue
        if stripped.startswith(f'"{WORLD_INPUT}"'):
            fail("B2 must not write authoritative A1 merchant salvage demand")
        if any(token in stripped for token in (
            "credits", "reputation:", "combat rating", "cargo ", "outfit ",
            "ship ", "fleet ", "world:",
        )) and not stripped.startswith(f'"{PREFIX.lower()}'):
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

    required_terms = (
        "recovery source",
        "claimant",
        "custody",
        "repair history",
        "technical",
        "compatibility",
        "unresolved claim",
        "closure evidence",
        "temporary",
        "ownership",
    )
    for term in required_terms:
        if term not in lowered:
            fail(f"missing salvage continuity concept: {term}")

    # Salvage scarcity must not collapse technical fitness into ownership.
    semantic_pairs = (
        ("safe to use", "ownership"),
        ("successful use", "ownership"),
        ("possession", "judgment"),
    )
    for first, second in semantic_pairs:
        if first not in lowered or second not in lowered:
            fail(f"missing ownership/custody distinction: {first!r} / {second!r}")

    forbidden_authority = (
        "centralized merchant salvage court",
        "merchant salvage government",
        "universal merchant salvage law",
    )
    if any(term in lowered for term in forbidden_authority):
        fail("unexpected centralized Merchant salvage authority claim")

    print("PASS: B2 Merchant Salvage Claim Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: b1_salvage_provenance_dependency=present")
    print("PASS: a1_salvage_demand=read-only high/recovery gating")
    print("PASS: delayed_review=7-11 days")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Tessa Remembers")
    print("PASS: lifecycle=dialogue-only decline")
    print("PASS: mutation_surface=B2 conditions only")


if __name__ == "__main__":
    main()
