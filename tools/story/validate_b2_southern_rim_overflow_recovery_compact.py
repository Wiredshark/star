#!/usr/bin/env python3
"""Focused structural validation for B2 Southern Rim Overflow Recovery Compact."""

from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/human/b2 southern rim overflow recovery compact.txt")
PREFIX = "B2 Southern Rim Overflow Recovery Compact:"
EXPECTED_MISSIONS = {
    f"{PREFIX} Offer",
    f"{PREFIX} Review",
    f"{PREFIX} Kessler Remembers",
}
EXPECTED_CHARACTERS = {"Rhea Solano", "Jo Kessler"}
EXPECTED_ROUTES = {
    f"{PREFIX} route obligation",
    f"{PREFIX} route restoration",
    f"{PREFIX} route paired",
}
EXPECTED_SETTLEMENTS = {
    f"{PREFIX} settlement portable capacity packet",
    f"{PREFIX} settlement reconciliation cycle",
}
A1_INPUT = "world: southern rim transit congestion"
B1_GATE = "Southern Rim Overflow Berth Compact Archive: offered"
A2_GATE = "A2 Southern Rim Traffic Coordination: followup seen"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def mission_names(text: str) -> set[str]:
    return set(re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE))


def labels_and_gotos(text: str) -> tuple[set[str], set[str]]:
    labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)$', text, flags=re.MULTILINE))
    gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)$', text, flags=re.MULTILINE))
    return labels, gotos


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")

    names = mission_names(text)
    if names != EXPECTED_MISSIONS:
        fail(f"expected missions {sorted(EXPECTED_MISSIONS)}, got {sorted(names)}")

    for name in EXPECTED_CHARACTERS:
        if name not in text:
            fail(f"missing named character {name}")

    if text.count('government "Free Worlds"') != 3:
        fail("all three missions must remain scoped to Free Worlds government")
    if text.count('not attributes "station"') != 3:
        fail("all three missions must exclude station-only sources")

    # Upstream dependencies must be consumed, never owned.
    if f'has "{B1_GATE}"' not in text:
        fail("Offer must require the B1 overflow-berth history gate")
    if f'has "{A2_GATE}"' not in text:
        fail("Offer must require the completed A2 traffic-coordination aftermath")

    if text.count(A1_INPUT) < 2:
        fail("expected authoritative A1 transit-congestion input in Offer and Review")
    if f'"{A1_INPUT}" >= 4' not in text:
        fail("Offer must require renewed severe congestion >= 4")
    if f'"{A1_INPUT}" <= 1' not in text:
        fail("Review must wait for congestion recovery <= 1")

    for line in text.splitlines():
        if A1_INPUT in line and any(op in line for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"B2 may not mutate authoritative A1 congestion state: {line.strip()}")
        if B1_GATE in line and any(op in line for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"B2 may not mutate B1 history state: {line.strip()}")
        if A2_GATE in line and any(op in line for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"B2 may not mutate A2 traffic-coordination state: {line.strip()}")

    for route in EXPECTED_ROUTES:
        if f'"{route}" = 1' not in text:
            fail(f"missing persistent initial route {route}")

    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    for settlement in EXPECTED_SETTLEMENTS:
        if f'"{settlement}" = 1' not in text:
            fail(f"missing terminal settlement write {settlement}")
        if text.count(f'has "{settlement}"') < 1:
            fail(f"later reader does not consume {settlement}")

    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("missing one-shot aftermath state")

    # Dialogue-only lifecycle contract: these missions only persist conditions and
    # create no gameplay objective. Every terminal path must close with decline so
    # no objective-less accepted mission can remain active in the mission list.
    terminal_accepts = len(re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE))
    terminal_declines = len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE))
    if terminal_accepts != 0:
        fail(f"state-only slice must contain zero terminal accept commands, found {terminal_accepts}")
    if terminal_declines != 7:
        fail(f"expected exactly seven state-only decline terminals, found {terminal_declines}")

    objective_directives = re.compile(
        r'^\s*(destination|stopover|waypoint|npc|cargo|passenger|deadline|timer)\b',
        flags=re.MULTILINE,
    )
    match = objective_directives.search(text)
    if match:
        fail(f"state-only lifecycle assumption invalidated by objective directive: {match.group(1)}")

    # Every condition write must remain inside the B2 namespace.
    condition_write = re.compile(r'^\s*"([^"]+)"\s*(?:=|\+=|-=)\s*\d+', re.MULTILINE)
    for cond in condition_write.findall(text):
        if not cond.startswith(PREFIX):
            fail(f"unexpected condition write outside B2 namespace: {cond}")

    # Guard direct gameplay/material mutations while allowing those words in prose.
    forbidden_commands = (
        "credits ", "reputation ", "combat rating ", "cargo ", "outfit ",
        "ship ", "fleet ",
    )
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(forbidden_commands):
            fail(f"unexpected direct gameplay mutation command: {stripped}")

    # Core continuity concepts from B1/A2 must remain explicit and distinct.
    required_phrases = (
        "overflow routing",
        "borrowed capacity",
        "berth",
        "tug",
        "repair",
        "fuel",
        "crew",
        "maintenance",
        "closure evidence",
        "local authority",
    )
    lowered = text.lower()
    for phrase in required_phrases:
        if phrase.lower() not in lowered:
            fail(f"missing overflow-recovery continuity concept: {phrase}")

    if "queue can be clear" not in lowered and "queue is clear" not in lowered:
        fail("must preserve the distinction between queue clearance and capacity restoration")

    labels, gotos = labels_and_gotos(text)
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    print("PASS: B2 Southern Rim Overflow Recovery Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: upstream_gates=B1 overflow history + A2 traffic aftermath")
    print("PASS: authoritative_a1_input=world: southern rim transit congestion (read-only)")
    print("PASS: severe-congestion offer + recovered-congestion review")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Kessler Remembers")
    print("PASS: persistence_model=stock mission/global conditions")
    print("PASS: lifecycle=state-only, terminal_accepts=0, terminal_declines=7")
    print("PASS: write_ownership=B2 namespace only")


if __name__ == "__main__":
    main()
