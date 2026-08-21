#!/usr/bin/env python3
"""Focused structural validation for B2 Free Worlds Relief Bargain."""

from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/human/b2 free worlds relief bargain.txt")
EXPECTED_MISSIONS = {
    "B2 Free Worlds Relief Bargain: Offer",
    "B2 Free Worlds Relief Bargain: Review",
    "B2 Free Worlds Relief Bargain: Vale Remembers",
}
EXPECTED_CHARACTERS = {"Lysa Kern", "Oren Vale"}
EXPECTED_ROUTES = {
    "B2 Free Worlds Relief Bargain: route reserve",
    "B2 Free Worlds Relief Bargain: route floor",
    "B2 Free Worlds Relief Bargain: route ledger",
}
EXPECTED_SETTLEMENTS = {
    "B2 Free Worlds Relief Bargain: settlement shared recovery ledger",
    "B2 Free Worlds Relief Bargain: settlement mutual relief reserve",
}
A1_INPUT = "world: free worlds relief demand"


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

    # B2 must read the A1 simulation truth but never own or mutate it.
    if text.count(A1_INPUT) < 2:
        fail("expected A1 relief-demand input in Offer and Review")
    for line in text.splitlines():
        if A1_INPUT in line and any(op in line for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"B2 may not mutate authoritative A1 input: {line.strip()}")

    for route in EXPECTED_ROUTES:
        if f'"{route}" = 1' not in text:
            fail(f"missing persistent initial route {route}")

    if '"B2 Free Worlds Relief Bargain: declined" = 1' not in text:
        fail("missing refusal persistence")

    settlement_writes = [
        settlement
        for settlement in EXPECTED_SETTLEMENTS
        if f'"{settlement}" = 1' in text
    ]
    if set(settlement_writes) != EXPECTED_SETTLEMENTS:
        fail("expected exactly both terminal settlement writes")

    # Later reader must consume both settlement outcomes and record one-shot aftermath.
    for settlement in EXPECTED_SETTLEMENTS:
        if text.count(f'has "{settlement}"') < 1:
            fail(f"later reader does not consume {settlement}")
    if '"B2 Free Worlds Relief Bargain: aftermath seen" = 1' not in text:
        fail("missing one-shot aftermath state")

    # Guard against direct material/combat/reputation mutation commands while
    # allowing those words to appear naturally in dialogue prose.
    forbidden_commands = ("credits ", "reputation ", "combat rating ", "cargo ")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(forbidden_commands):
            fail(f"unexpected direct gameplay mutation command: {stripped}")

    # This slice consists entirely of conversations that persist global state.
    # It creates no destination, cargo, NPC, timer, or other gameplay objective,
    # so accepting these missions would leave objective-less active missions.
    accepts = re.findall(r'^\s*accept$', text, flags=re.MULTILINE)
    declines = re.findall(r'^\s*decline$', text, flags=re.MULTILINE)
    if accepts:
        fail(f"state-only dialogue slice must have zero accept terminals, got {len(accepts)}")
    if len(declines) != 7:
        fail(f"expected exactly seven decline terminals, got {len(declines)}")

    objective_prefixes = (
        "destination ",
        "waypoint ",
        "stopover ",
        "npc ",
        "deadline ",
        "passengers ",
        "cargo ",
    )
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(objective_prefixes):
            fail(f"unexpected gameplay objective in state-only dialogue slice: {stripped}")

    labels, gotos = labels_and_gotos(text)
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    print("PASS: B2 Free Worlds Relief Bargain structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: authoritative_a1_input=world: free worlds relief demand (read-only)")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Vale Remembers")
    print("PASS: lifecycle=state-only dialogue; accept=0 decline=7")
    print("PASS: persistence_model=stock mission/global conditions")


if __name__ == "__main__":
    main()
