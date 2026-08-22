#!/usr/bin/env python3
"""Focused structural validation for B2 Free Worlds Reserve Recovery Compact."""

from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/human/b2 free worlds reserve recovery compact.txt")
EXPECTED_MISSIONS = {
    "B2 Free Worlds Reserve Recovery Compact: Offer",
    "B2 Free Worlds Reserve Recovery Compact: Review",
    "B2 Free Worlds Reserve Recovery Compact: Brenner Remembers",
}
EXPECTED_CHARACTERS = {"Rina Sol", "Cal Brenner"}
EXPECTED_ROUTES = {
    "B2 Free Worlds Reserve Recovery Compact: route target",
    "B2 Free Worlds Reserve Recovery Compact: route support",
    "B2 Free Worlds Reserve Recovery Compact: route paired",
}
EXPECTED_SETTLEMENTS = {
    "B2 Free Worlds Reserve Recovery Compact: settlement portable reserve packet",
    "B2 Free Worlds Reserve Recovery Compact: settlement reconciliation cycle",
}
A1_INPUT = "world: free worlds relief reserve strain"


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
        fail("all three missions must be scoped to Free Worlds government")

    # A1 owns reserve strain. B2 may gate on it but may never mutate it.
    if text.count(A1_INPUT) < 2:
        fail("expected A1 reserve-strain input in Offer and Review")
    for line in text.splitlines():
        if A1_INPUT in line and any(op in line for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"B2 may not mutate authoritative A1 input: {line.strip()}")

    # High strain introduces the dispute; recovery enables the later review.
    if f'"{A1_INPUT}" >= 3' not in text:
        fail("Offer must require reserve strain >= 3")
    if f'"{A1_INPUT}" <= 1' not in text:
        fail("Review must wait until reserve strain <= 1")

    for route in EXPECTED_ROUTES:
        if f'"{route}" = 1' not in text:
            fail(f"missing persistent initial route {route}")

    if '"B2 Free Worlds Reserve Recovery Compact: declined" = 1' not in text:
        fail("missing refusal persistence")

    for settlement in EXPECTED_SETTLEMENTS:
        if f'"{settlement}" = 1' not in text:
            fail(f"missing terminal settlement write {settlement}")
        if text.count(f'has "{settlement}"') < 1:
            fail(f"later reader does not consume {settlement}")

    if '"B2 Free Worlds Reserve Recovery Compact: aftermath seen" = 1' not in text:
        fail("missing one-shot aftermath state")

    # These missions are dialogue/state-only. They create no objective that should
    # remain active after the conversation, so every terminal path must decline.
    terminal_accepts = len(re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE))
    terminal_declines = len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE))
    if terminal_accepts:
        fail(f"state-only lifecycle must not use accept terminals; found {terminal_accepts}")
    if terminal_declines != 7:
        fail(f"expected exactly 7 state-only decline terminals, got {terminal_declines}")

    objective_directives = re.compile(
        r'^\s*(destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b',
        flags=re.MULTILINE | re.IGNORECASE,
    )
    objective_hits = objective_directives.findall(text)
    if objective_hits:
        fail(f"unexpected objective-bearing directive(s) in state-only slice: {objective_hits}")

    # Guard ownership: every condition write must be B2-owned.
    condition_write = re.compile(r'^\s*"([^"]+)"\s*(?:=|\+=|-=)\s*\d+', re.MULTILINE)
    for cond in condition_write.findall(text):
        if not cond.startswith("B2 Free Worlds Reserve Recovery Compact:"):
            fail(f"unexpected condition write outside B2 namespace: {cond}")

    # Guard against direct material/combat/reputation mutation commands while
    # allowing those words in dialogue prose.
    forbidden_commands = (
        "credits ", "reputation ", "combat rating ", "cargo ", "outfit ",
        "ship ", "fleet ",
    )
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(forbidden_commands):
            fail(f"unexpected direct gameplay mutation command: {stripped}")

    # Core continuity concepts inherited from B1 must remain explicit.
    required_phrases = (
        "stock-rotation",
        "shelter",
        "maintenance",
        "borrowed",
        "restored capacity",
    )
    lowered = text.lower()
    for phrase in required_phrases:
        if phrase.lower() not in lowered:
            fail(f"missing reserve-recovery continuity concept: {phrase}")

    labels, gotos = labels_and_gotos(text)
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    print("PASS: B2 Free Worlds Reserve Recovery Compact structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: authoritative_a1_input=world: free worlds relief reserve strain (read-only)")
    print("PASS: high-strain offer + recovered-strain review")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Brenner Remembers")
    print("PASS: persistence_model=stock mission/global conditions")
    print("PASS: write_ownership=B2 namespace only")
    print("PASS: dialogue_lifecycle=7 decline terminals, 0 accept terminals")


if __name__ == "__main__":
    main()
