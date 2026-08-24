#!/usr/bin/env python3
"""Focused contract checks for B2 Quarg Cross-Generation Promise."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/quarg/b2 quarg cross generation promise.txt"
PREFIX = "B2 Quarg Cross-Generation Promise:"


def fail(message: str) -> None:
    raise AssertionError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def segment(text: str, start: str, end: str | None = None) -> str:
    require(start in text, f"missing segment start: {start}")
    part = text.split(start, 1)[1]
    if end is not None:
        require(end in part, f"missing segment end after {start}: {end}")
        part = part.split(end, 1)[0]
    return part


def main() -> int:
    require(DATA.exists(), f"missing production file: {DATA}")
    text = DATA.read_text(encoding="utf-8")

    missions = [
        "B2 Quarg Cross-Generation Promise: Offer",
        "B2 Quarg Cross-Generation Promise: Review",
        "B2 Quarg Cross-Generation Promise: Jules Remembers",
    ]
    for name in missions:
        require(text.count(f'mission "{name}"') == 1, f"mission must appear exactly once: {name}")
    require(text.count('mission "B2 Quarg Cross-Generation Promise:') == 3,
            "slice must contain exactly three B2 missions")
    require(text.count('event "B2 Quarg Cross-Generation Promise: Review Ready"') == 4,
            "review-ready event must have one declaration and exactly three schedules")

    # Canon / access grounding.
    require('has "First Contact: Quarg: offered"' in text,
            "Offer must remain gated behind established Quarg first contact")
    require(text.count('\t\tgovernment "Quarg"') == 3,
            "all three missions must be scoped to Quarg government sources")
    require("many human\n# lifetimes" in text,
            "header must preserve the established Quarg longevity premise")
    require("not a Quarg title or\n# office" in text,
            "Old Friend must remain player-private shorthand, not an office")
    require("This local relationship is not Quarg law." in text,
            "local relationship must not be generalized into Quarg law")

    # Offer routes and refusal semantics.
    route_states = [
        "route living renewal",
        "route bounded family continuity",
        "route paired promise records",
    ]
    for state in route_states:
        require(text.count(f'"{PREFIX} {state}" = 1') == 1,
                f"missing or duplicated route write: {state}")
    require(text.count(f'"{PREFIX} introduced" = 1') == 3,
            "exactly the three substantive routes must write introduced")
    require(text.count(f'event "{PREFIX} Review Ready" 7 11') == 3,
            "exactly the three substantive routes must schedule Review for 7-11 days")

    offer = segment(
        text,
        'mission "B2 Quarg Cross-Generation Promise: Offer"',
        'mission "B2 Quarg Cross-Generation Promise: Review"',
    )
    decline = segment(offer, "\t\t\tlabel decline")
    require(f'"{PREFIX} declined" = 1' in decline,
            "refusal must persist the declined state")
    require(f'"{PREFIX} introduced"' not in decline,
            "refusal must not arm the Review")
    require(f'event "{PREFIX} Review Ready" 7 11' not in decline,
            "refusal must not schedule the Review")

    # Review lifecycle and terminal settlements.
    review = segment(
        text,
        'mission "B2 Quarg Cross-Generation Promise: Review"',
        'mission "B2 Quarg Cross-Generation Promise: Jules Remembers"',
    )
    for gate in (
        f'has "{PREFIX} introduced"',
        f'has "{PREFIX} review ready"',
        f'not "{PREFIX} reviewed"',
    ):
        require(gate in review, f"Review missing lifecycle gate: {gate}")

    settlements = [
        "settlement portable promise history",
        "settlement renewal by living parties",
    ]
    for state in settlements:
        require(text.count(f'"{PREFIX} {state}" = 1') == 1,
                f"missing or duplicated settlement write: {state}")
    require(text.count(f'"{PREFIX} reviewed" = 1') == 2,
            "each terminal settlement must close Review exactly once")

    # One-shot aftermath must consume either settlement and write once.
    aftermath = segment(text, 'mission "B2 Quarg Cross-Generation Promise: Jules Remembers"')
    require(f'not "{PREFIX} aftermath seen"' in aftermath,
            "aftermath must be explicitly one-shot")
    for state in settlements:
        require(f'has "{PREFIX} {state}"' in aftermath,
                f"aftermath must read settlement: {state}")
    require(text.count(f'"{PREFIX} aftermath seen" = 1') == 1,
            "aftermath must write its seen flag exactly once")

    # State ownership: all direct condition assignments belong to this B2 namespace.
    assignments = re.findall(r'^\s*"([^"]+)"\s*=\s*-?\d+\s*$', text, flags=re.MULTILINE)
    require(assignments, "expected persistent condition assignments")
    foreign = [name for name in assignments if not name.startswith(PREFIX)]
    require(not foreign, f"foreign condition writes detected: {foreign}")
    require("world:" not in text, "slice must not read or write A1 world state")

    # Dialogue-only lifecycle: no accepted objective-less missions and no objective directives.
    lines = [line.strip() for line in text.splitlines()]
    require(lines.count("accept") == 0, "state-only slice must not contain terminal accept")
    require(lines.count("decline") == 7, "expected exactly seven state-only decline terminals")
    forbidden_directives = (
        "destination ", "stopover ", "waypoint ", "npc ", "cargo ",
        "passenger ", "deadline ", "timer ", "payment ", "reputation ",
        "outfit ", "ship ", "fleet ",
    )
    bad = [line for line in lines if any(line.lower().startswith(token) for token in forbidden_directives)]
    require(not bad, f"unexpected gameplay-objective/material directive(s): {bad}")

    # Every local goto must resolve to a declared local label.
    labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
    gotos = re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE)
    missing = sorted(set(gotos) - labels)
    require(not missing, f"goto target(s) missing local labels: {missing}")

    # Core relationship boundary: historical promise is not automatic present authority.
    required_fragments = [
        "historical relationship evidence",
        "current agreements carry their own scope, consent, duration, and closure",
        "Unknown intent stays unknown rather than being filled in by repetition",
        "inherited promises remain history",
        "the copy itself cannot answer on behalf of either side",
    ]
    for fragment in required_fragments:
        require(fragment in text, f"missing continuity statement: {fragment}")

    print("B2 Quarg Cross-Generation Promise validator: PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as exc:
        print(f"B2 Quarg Cross-Generation Promise validator: FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
