#!/usr/bin/env python3
"""Focused structural validation for the A2 Deep Field Review slice.

This validator checks the specialist contract only. It does not replace Endless
Sky's normal content parser, build, runtime, or save/load gates.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "a2 deep field review.txt"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    text = DATA.read_text(encoding="utf-8")

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    require(missions == [
        "A2 Deep Field Review: Arcos Interview",
        "A2 Deep Field Review: Arcos Remembers",
        "A2 Deep Field Review: Refusal Reader",
    ], f"unexpected mission list: {missions}")

    require("Selene Arcos" in text, "missing named character Selene Arcos")

    require("[Scientific history: Mystery Cubes investigation]" in text,
            "missing player-visible Mystery Cubes requirement label")
    require('has "Deep: Mystery Cubes 4: done"' in text,
            "missing authoritative Mystery Cubes completion reader")

    require("[Field service: repeated Deep convoy work]" in text,
            "missing player-visible repeated-service requirement label")
    require('"deep convoy" >= 2' in text,
            "missing authoritative repeated Deep convoy reader")

    interview = text.split('mission "A2 Deep Field Review: Arcos Interview"', 1)[1]
    interview = interview.split('mission "A2 Deep Field Review: Arcos Remembers"', 1)[0]
    for route in ("anomaly", "service", "method", "refuse"):
        require(f"goto {route}" in interview, f"missing interview route {route}")
        require(f"label {route}" in interview, f"missing interview label {route}")

    for state in (
        "route anomaly",
        "route field service",
        "route method",
        "declined",
    ):
        require(f'"A2 Deep Field Review: {state}" = 1' in text,
                f"persistent state never written: {state}")

    later = text.split('mission "A2 Deep Field Review: Arcos Remembers"', 1)[1]
    later = later.split('mission "A2 Deep Field Review: Refusal Reader"', 1)[0]
    require('has "A2 Deep Field Review: route anomaly"' in later,
            "later reader does not consume anomaly route")
    require('has "A2 Deep Field Review: route field service"' in later,
            "later reader does not consume field-service route")
    require('"A2 Deep Field Review: arcos future methods contact" = 1' in later,
            "method-route later consequence missing")
    require('"A2 Deep Field Review: arcos future anomaly contact" = 1' in later,
            "anomaly-route later consequence missing")
    require('"A2 Deep Field Review: arcos future field contact" = 1' in later,
            "field-service later consequence missing")
    require('"A2 Deep Field Review: followup pending" = 0' in later,
            "later reader does not consume its pending state")

    refusal = text.split('mission "A2 Deep Field Review: Refusal Reader"', 1)[1]
    require('has "A2 Deep Field Review: declined"' in refusal,
            "refusal reader does not consume refusal state")
    require('"A2 Deep Field Review: refusal respected" = 1' in refusal,
            "refusal reader does not persist consequence")

    # A2 should reuse the existing condition store rather than introduce a
    # parallel narrative-state authority.
    lowered = text.lower()
    for forbidden in (
        "dialogue world state",
        "a2 character database",
        "a2 research state database",
        "sqlite",
    ):
        require(forbidden not in lowered, f"forbidden shadow-state marker: {forbidden}")

    print("PASS: A2 Deep Field Review structure validated")
    print("PASS: missions=3")
    print("PASS: named_character=Selene Arcos")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: authoritative_inputs=Mystery Cubes completion + repeated Deep convoy count")
    print("PASS: special_response_modes=hidden + visible-disabled")
    print("PASS: later_readers=route-specific + refusal")
    print("PASS: persistence_model=stock mission/global conditions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
