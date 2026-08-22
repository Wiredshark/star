#!/usr/bin/env python3
"""Focused structural validation for B2 Wanderer Evacuation Recovery Compact."""

from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/wanderer/b2 wanderer evacuation recovery compact.txt")
EXPECTED_MISSIONS = {
    "B2 Wanderer Evacuation Recovery Compact: Offer",
    "B2 Wanderer Evacuation Recovery Compact: Review",
    "B2 Wanderer Evacuation Recovery Compact: Keeper Remembers",
}
EXPECTED_ROUTES = {
    "B2 Wanderer Evacuation Recovery Compact: route obligations",
    "B2 Wanderer Evacuation Recovery Compact: route current",
    "B2 Wanderer Evacuation Recovery Compact: route paired",
}
EXPECTED_SETTLEMENTS = {
    "B2 Wanderer Evacuation Recovery Compact: settlement portable recovery packet",
    "B2 Wanderer Evacuation Recovery Compact: settlement reconciliation cycle",
}
A1_INPUT = "world: wanderer evacuation logistics strain"


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

    if text.count('government "Wanderer"') != 3:
        fail("all three missions must be scoped to Wanderer government")

    for phrase in ("Harbor Keeper", "Route Tender"):
        if phrase not in text:
            fail(f"missing recurring character shorthand: {phrase}")

    # Avoid inventing formal offices from the descriptive shorthand.
    lowered = text.lower()
    if "not offices" not in lowered and "not office" not in lowered:
        fail("production comment must state private shorthand does not create offices")

    # A1 owns the live strain signal. B2 may gate on it but must not mutate it.
    if text.count(A1_INPUT) < 2:
        fail("expected A1 evacuation strain input in Offer and Review")
    for line in text.splitlines():
        if A1_INPUT in line and any(op in line for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"B2 may not mutate authoritative A1 input: {line.strip()}")

    if f'"{A1_INPUT}" >= 3' not in text:
        fail("Offer must require evacuation strain >= 3")
    if f'"{A1_INPUT}" <= 1' not in text:
        fail("Review must wait until evacuation strain <= 1")

    # Ground the slice in the existing Wanderer invasion without mutating campaign state.
    if 'has "event: wanderers: unfettered invasion starts"' not in text:
        fail("Offer must be grounded in the existing Wanderer invasion event")

    for route in EXPECTED_ROUTES:
        if f'"{route}" = 1' not in text:
            fail(f"missing persistent initial route {route}")
    if '"B2 Wanderer Evacuation Recovery Compact: declined" = 1' not in text:
        fail("missing refusal persistence")

    for settlement in EXPECTED_SETTLEMENTS:
        if f'"{settlement}" = 1' not in text:
            fail(f"missing terminal settlement write {settlement}")
        if f'has "{settlement}"' not in text:
            fail(f"later reader does not consume {settlement}")

    if '"B2 Wanderer Evacuation Recovery Compact: aftermath seen" = 1' not in text:
        fail("missing one-shot aftermath state")

    # Every direct condition write must remain inside the B2 namespace.
    condition_write = re.compile(r'^\s*"([^"]+)"\s*(?:=|\+=|-=)\s*\d+', re.MULTILINE)
    for cond in condition_write.findall(text):
        if not cond.startswith("B2 Wanderer Evacuation Recovery Compact:"):
            fail(f"unexpected condition write outside B2 namespace: {cond}")

    forbidden_commands = (
        "credits ", "reputation ", "combat rating ", "cargo ", "outfit ",
        "ship ", "fleet ",
    )
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(forbidden_commands):
            fail(f"unexpected direct gameplay mutation command: {stripped}")

    # These three missions are dialogue/state-only. Accepting them would leave an
    # objective-less mission active, so every terminal path must persist state and
    # then decline. If a real objective is ever added, this lifecycle assertion
    # must be deliberately revised rather than silently weakened.
    accept_terminals = len(re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE))
    decline_terminals = len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE))
    if accept_terminals != 0:
        fail(f"state-only dialogue missions must not accept; found {accept_terminals} terminal accept(s)")
    if decline_terminals != 7:
        fail(f"expected exactly 7 state-only decline terminals, got {decline_terminals}")

    objective_directives = re.compile(
        r'^\s*(?:destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b',
        flags=re.MULTILINE | re.IGNORECASE,
    )
    objective_hits = objective_directives.findall(text)
    if objective_hits:
        fail(f"state-only lifecycle assumption invalidated by objective directive(s): {objective_hits}")

    # The continuity contract must keep successful arrival separate from restored capacity.
    required_fragments = (
        "successful arrival is an event",
        "restored capacity is a condition",
        "borrowed capacity",
        "closure evidence",
        "resolved items stop propagating as active warnings",
    )
    for fragment in required_fragments:
        if fragment.lower() not in lowered:
            fail(f"missing evacuation-recovery continuity concept: {fragment}")

    labels, gotos = labels_and_gotos(text)
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    print("PASS: B2 Wanderer Evacuation Recovery Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Harbor Keeper + Route Tender (player-private shorthand)")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: authoritative_a1_input=world: wanderer evacuation logistics strain (read-only)")
    print("PASS: high-strain offer + recovered-strain review")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Keeper Remembers")
    print("PASS: persistence_model=stock mission/global conditions")
    print("PASS: write_ownership=B2 namespace only")
    print("PASS: dialogue_lifecycle=7 decline terminals / 0 accept terminals / no objectives")


if __name__ == "__main__":
    main()
