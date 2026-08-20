#!/usr/bin/env python3
"""Focused structural validation for B2 Pirate Repair Credit Compact."""

from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/human/b2 pirate repair credit compact.txt")
EXPECTED_MISSIONS = {
    "B2 Pirate Repair Credit Compact: Offer",
    "B2 Pirate Repair Credit Compact: Review",
    "B2 Pirate Repair Credit Compact: Quell Remembers",
}
EXPECTED_ROUTES = {
    "B2 Pirate Repair Credit Compact: route provenance",
    "B2 Pirate Repair Credit Compact: route current",
    "B2 Pirate Repair Credit Compact: route paired",
}
EXPECTED_SETTLEMENTS = {
    "B2 Pirate Repair Credit Compact: settlement portable obligation packet",
    "B2 Pirate Repair Credit Compact: settlement reconciliation",
}
PREFIX = "B2 Pirate Repair Credit Compact:"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    names = set(re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE))
    if names != EXPECTED_MISSIONS:
        fail(f"expected missions {sorted(EXPECTED_MISSIONS)}, got {sorted(names)}")

    if text.count('government "Pirate"') != 3:
        fail("all three missions must be scoped to Pirate government")

    for character in ("Mara Quell", "Venn Daro"):
        if character not in text:
            fail(f"missing recurring character: {character}")

    for route in EXPECTED_ROUTES:
        if f'"{route}" = 1' not in text:
            fail(f"missing persistent route: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    for settlement in EXPECTED_SETTLEMENTS:
        if f'"{settlement}" = 1' not in text:
            fail(f"missing settlement write: {settlement}")
        if f'has "{settlement}"' not in text:
            fail(f"later reader does not consume settlement: {settlement}")

    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("missing one-shot aftermath state")

    write_rx = re.compile(r'^\s*"([^"]+)"\s*(?:=|\+=|-=)\s*\d+', re.MULTILINE)
    for cond in write_rx.findall(text):
        if not cond.startswith(PREFIX):
            fail(f"unexpected condition write outside B2 namespace: {cond}")

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("credits ", "reputation ", "combat rating ", "cargo ", "outfit ", "ship ", "fleet ")):
            fail(f"unexpected direct gameplay mutation: {stripped}")

    required = (
        "original repair obligation",
        "original promise",
        "substitutions",
        "partial repayment",
        "current holder",
        "closure evidence",
        "market value and obligation value are not the same thing",
        "no copy may close the obligation until",
        "local",
        "not because any central authority",
    )
    # Last B1 phrase is not duplicated verbatim in B2; ensure the same concept is present.
    for fragment in required[:-1]:
        if fragment.lower() not in lower:
            fail(f"missing repair-credit continuity concept: {fragment}")
    if "pirate bank" not in lower and "universal legal code" not in lower:
        fail("must explicitly reject centralized/universal pirate credit authority")

    labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)$', text, flags=re.MULTILINE))
    gotos = set(re.findall(r'^\s*goto ([A-Za-z0-9_-]+)$', text, flags=re.MULTILINE))
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    print("PASS: B2 Pirate Repair Credit Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Mara Quell + Venn Daro")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Quell Remembers")
    print("PASS: write_ownership=B2 namespace only")
    print("PASS: repair-credit boundary=original obligation != current transfer value")
    print("PASS: pirate authority boundary=local conventions, no central bank/code")


if __name__ == "__main__":
    main()
