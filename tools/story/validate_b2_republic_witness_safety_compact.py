#!/usr/bin/env python3
"""Focused structural validator for B2 Republic Witness Safety Compact."""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATH = Path("data/human/b2 republic witness safety compact.txt")
PREFIX = "B2 Republic Witness Safety Compact:"
A1_SIGNAL = "world: republic border pressure"
PRIOR = "B2 Republic Border Testimony Compact: aftermath seen"


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
        f"{PREFIX} Verran Remembers",
    ]
    if missions != expected:
        fail(f"expected missions {expected!r}, found {missions!r}")

    for name in ("Talia Rook", "Jace Verran"):
        if name not in text:
            fail(f"missing returning named character {name}")

    if text.count('government "Republic"') != 3:
        fail("all three missions must be scoped to Republic government")

    if f'has "{PRIOR}"' not in text:
        fail("Offer must require integrated Border Testimony aftermath")

    if f'"{A1_SIGNAL}" >= 3' not in text:
        fail("Offer must react to renewed/elevated A1 border pressure")
    if f'"{A1_SIGNAL}" <= 2' not in text:
        fail("Review must wait for A1 border pressure to ease")

    for line in text.splitlines():
        stripped = line.strip()
        if A1_SIGNAL in stripped and any(op in stripped for op in (" += ", " -= ", " = ")):
            fail(f"B2 must not mutate A1-owned border pressure: {stripped}")

    if 'event "B2 Republic Witness Safety Compact: Review Ready"' not in text:
        fail("missing delayed Review Ready event")
    if text.count('event "B2 Republic Witness Safety Compact: Review Ready" 7 11') != 3:
        fail("all three substantive routes must schedule Review Ready at 7-11 days")

    for route in ("route identity escrow", "route purpose bounded", "route paired records"):
        if f'"{PREFIX} {route}" = 1' not in text:
            fail(f"missing persistent route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    settlements = re.findall(rf'"{re.escape(PREFIX)} settlement ([^"]+)" = 1', text)
    expected_settlements = ["expiry plus fresh cause", "portable access packet"]
    if sorted(set(settlements)) != expected_settlements:
        fail(f"unexpected settlements: {sorted(set(settlements))}")
    if len(settlements) != 2:
        fail("each terminal settlement must be written exactly once")

    if f'not "{PREFIX} aftermath seen"' not in text:
        fail("aftermath reader must be one-shot")
    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("aftermath reader must persist completion")

    # Every direct persistent write must remain inside this B2 namespace.
    for raw in re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, flags=re.MULTILINE):
        if not raw.startswith(PREFIX):
            fail(f"out-of-scope persistent write: {raw}")

    # Dialogue/state-only lifecycle: no objective-less accepted missions.
    accepts = re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE)
    declines = re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)
    if accepts:
        fail(f"state-only slice must not use terminal accept; found {len(accepts)}")
    if len(declines) != 7:
        fail(f"expected exactly 7 terminal declines, found {len(declines)}")

    objective_directives = (
        "destination ",
        "stopover ",
        "waypoint ",
        "npc ",
        "cargo ",
        "passenger ",
        "deadline ",
        "timer ",
    )
    for line in text.splitlines():
        stripped = line.lstrip("\t").lower()
        leading_tabs = len(line) - len(line.lstrip("\t"))
        if leading_tabs > 0 and any(stripped.startswith(token) for token in objective_directives):
            fail(f"unexpected gameplay-objective directive: {line.strip()}")

    # No direct material/reputation/world mutation.
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

    # Validate local conversation goto/label targets.
    blocks = re.split(r'(?=^mission ")', text, flags=re.MULTILINE)
    for block in blocks:
        if not block.startswith("mission "):
            continue
        labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', block, flags=re.MULTILINE))
        missing = gotos - labels
        if missing:
            fail(f"unresolved local goto labels: {sorted(missing)}")

    continuity_terms = (
        "identity escrow",
        "purpose",
        "stable witness reference",
        "protected fields",
        "current berth",
        "emergency contact",
        "expiry",
        "fresh cause",
        "authorship",
        "safety control",
    )
    for term in continuity_terms:
        if term not in lowered:
            fail(f"missing witness-safety continuity concept: {term}")

    if "protection" not in lowered or "evidence" not in lowered:
        fail("must distinguish witness protection from evidentiary weight")
    if "not" not in lowered or "fresh evidence" not in lowered:
        fail("must explicitly reject historical protection as automatic fresh evidence")

    print("PASS: B2 Republic Witness Safety Compact structure validated")
    print("PASS: missions=3")
    print("PASS: returning_characters=Talia Rook,Jace Verran")
    print("PASS: prior_border_testimony_aftermath=required")
    print("PASS: a1_border_pressure=read_only")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: delayed_review=7-11 days")
    print("PASS: terminal_settlements=2")
    print("PASS: state_only_terminals=7 decline / 0 accept")
    print("PASS: mutation_surface=B2 conditions only")


if __name__ == "__main__":
    main()
