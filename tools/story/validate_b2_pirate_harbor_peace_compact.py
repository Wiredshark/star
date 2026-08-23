#!/usr/bin/env python3
"""Focused structural validator for B2 Pirate Harbor Peace Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 pirate harbor peace compact.txt")
PREFIX = "B2 Pirate Harbor Peace Compact:"


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
    expected = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Sima Remembers"]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    if text.count('event "B2 Pirate Harbor Peace Compact: Review Ready" 7 11') != 3:
        fail("exactly three substantive routes must schedule delayed review")

    for phrase in ("Rhea Corbin", "Captain Jory Kade", "Sima Voss"):
        if phrase not in text:
            fail(f"missing character continuity: {phrase}")

    if text.count('government "Pirate"') != 3:
        fail("all three missions must remain Pirate-government scoped")
    if 'has "Pirate Safe Harbor Register: offered"' not in text:
        fail("missing B1 Pirate Safe Harbor Register dependency")

    for route in ("route exit", "route delay", "route paired"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing route state: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["expiry and fresh cause", "status packet"]
    if sorted(set(settlements)) != expected_settlements or len(settlements) != 2:
        fail(f"unexpected settlement set: {settlements!r}")

    if text.count("\t\t\t\tdecline") != 7:
        fail("all seven dialogue/state-only terminal paths must decline cleanly")
    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        fail("state-only slice must not use terminal accept")

    objective_directives = (
        "destination ", "stopover ", "waypoint ", "npc ", "cargo ",
        "passenger ", "deadline ", "timer ",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if line.startswith("\t") and any(stripped.startswith(token) for token in objective_directives):
            fail(f"unexpected gameplay-objective directive: {line.strip()}")

    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE)
    for raw in writes:
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    forbidden_write_tokens = (
        "world:", "credits", "reputation:", "combat rating", "cargo ",
        "outfit ", "ship ", "fleet ", "pirate safe harbor register:",
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

    offer_block = next(b for b in blocks if b.startswith(f'mission "{PREFIX} Offer"'))
    decline_block = offer_block.split("label decline", 1)[1]
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("refusal must not enter the review chain")
    if 'event "B2 Pirate Harbor Peace Compact: Review Ready" 7 11' in decline_block:
        fail("refusal must not schedule review")

    required_concepts = (
        "neutral harbor", "temporary", "cannot become custody", "expiry",
        "fresh evidence", "protected departure", "automatically prove",
        "movement", "information",
    )
    for phrase in required_concepts:
        if phrase not in lower:
            fail(f"missing harbor-peace continuity concept: {phrase}")

    forbidden_claims = (
        "universal pirate law", "central pirate government", "sima belongs to kade",
        "protected departure proves innocence", "safety delay proves guilt",
    )
    for phrase in forbidden_claims:
        if phrase in lower:
            fail(f"asserts forbidden authority or evidentiary certainty: {phrase}")

    print("PASS: B2 Pirate Harbor Peace Compact structure validated")
    print("PASS: missions=3")
    print("PASS: characters=Rhea Corbin + Jory Kade + Sima Voss")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Sima Remembers")
    print("PASS: lifecycle=7 state-only terminals decline")
    print("PASS: mutation_surface=B2 conditions only")
    print("PASS: dependency=Pirate Safe Harbor Register read-only")
    print("PASS: primary_domain=law / personal autonomy / feud boundaries")


if __name__ == "__main__":
    main()
