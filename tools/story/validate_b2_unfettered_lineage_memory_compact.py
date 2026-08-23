#!/usr/bin/env python3
"""Focused structural validator for B2 Unfettered Lineage Memory Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/hai/b2 unfettered lineage memory compact.txt")
PREFIX = "B2 Unfettered Lineage Memory Compact:"
B1_ARCHIVE = "Unfettered Lineage Recitation Archive: offered"
FIRST_CONTACT = "First Contact: Unfettered: offered"
INVASION = "event: wanderers: unfettered invasion starts"


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
        f"{PREFIX} Descendant Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if f'event "{PREFIX} Review Ready"' not in text:
        fail("missing delayed Review-ready event")
    if text.count(f'event "{PREFIX} Review Ready" 7 11') != 3:
        fail("each substantive Offer route must schedule Review Ready at 7-11 days")

    if text.count('attributes "unfettered"') != 3:
        fail("all three missions must be scoped to Unfettered locations")
    if text.count('"offer precedence" 8') != 3:
        fail("all three missions must use offer precedence 8")

    if f'has "{FIRST_CONTACT}"' not in text:
        fail("Offer must require Unfettered first contact")
    if f'has "{B1_ARCHIVE}"' not in text:
        fail("Offer must consume the B1 Lineage Recitation Archive")
    if f'not "{INVASION}"' not in text:
        fail("Offer must remain pre-invasion")
    if f'has "{INVASION}"' not in text:
        fail("Review must react to later invasion-state context")

    for route in (
        "route living inheritance",
        "route contradiction preserved",
        "route lineage consent",
    ):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing persistent refusal state")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["consent citation", "layered recitation"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("Descendant Remembers must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("Descendant Remembers must persist completion")

    # Every explicit persistent write belongs to this B2 namespace.
    direct_writes = re.findall(r'^\s*"([^"]+)"\s*=\s*[01]\s*$', text, flags=re.MULTILINE)
    for key in direct_writes:
        if not key.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {key}")

    # The B1 and campaign-state inputs are read-only.
    for line in text.splitlines():
        stripped = line.strip()
        if B1_ARCHIVE in stripped or FIRST_CONTACT in stripped or INVASION in stripped:
            if re.search(r'(?:\+=|-=|\+\+|--|<\?=|>\?=|\?=|(?<![<>])=(?!=))', stripped):
                fail(f"B2 must not mutate upstream/campaign state: {stripped}")

    # Dialogue/state-only lifecycle: no objective-less accepted missions.
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

    # No direct material, reputation, combat, or world-state mutation.
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

    # Every conversation goto target must resolve inside its mission block.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    # Cultural/family continuity: living inheritance and evidence are not identical;
    # contradiction remains source-linked; preservation does not imply publication.
    continuity_terms = (
        "living inheritance",
        "family",
        "lineage",
        "speaker",
        "source chain",
        "contradiction",
        "evidence class",
        "permission",
        "private",
        "public",
        "repetition",
    )
    for term in continuity_terms:
        if term not in lowered:
            fail(f"missing lineage-memory continuity concept: {term}")

    if "private shorthand" not in lowered:
        fail("Reciter/Descendant must be explicitly framed as player-private shorthand")
    if "not canonical unfettered offices" not in lowered:
        fail("must reject interpreting private shorthand as canonical Unfettered offices")

    # Avoid turning one lineage's practice into centralized Unfettered authority.
    forbidden_authority_claims = (
        "centralized unfettered archive authority",
        "universal unfettered archive law",
        "official unfettered memory ministry",
    )
    for claim in forbidden_authority_claims:
        if claim in lowered:
            fail(f"unexpected centralized authority claim: {claim}")

    print("PASS: B2 Unfettered Lineage Memory Compact structure validated")
    print("PASS: missions=3")
    print("PASS: character_pair=Reciter + Descendant private shorthand")
    print("PASS: b1_lineage_archive_dependency=present")
    print("PASS: campaign_context=first contact + invasion reaction read-only")
    print("PASS: delayed_review=7-11 days")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Descendant Remembers")
    print("PASS: lifecycle=7 declines / 0 accepts")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: domain=cultural/family memory")


if __name__ == "__main__":
    main()
