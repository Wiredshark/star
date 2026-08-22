#!/usr/bin/env python3
"""Focused structural validation for B2 Successor Interface Provenance Compact."""

from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/successors/b2 successor interface provenance compact.txt")
EXPECTED_MISSIONS = {
    "B2 Successor Interface Provenance Compact: Offer",
    "B2 Successor Interface Provenance Compact: Review",
    "B2 Successor Interface Provenance Compact: Fitter Remembers",
}
EXPECTED_ROUTES = {
    "B2 Successor Interface Provenance Compact: route provenance",
    "B2 Successor Interface Provenance Compact: route field",
    "B2 Successor Interface Provenance Compact: route paired",
}
EXPECTED_SETTLEMENTS = {
    "B2 Successor Interface Provenance Compact: settlement portable qualification packet",
    "B2 Successor Interface Provenance Compact: settlement expiry and revalidation",
}
PREFIX = "B2 Successor Interface Provenance Compact:"


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
    lowered = text.lower()

    names = mission_names(text)
    if names != EXPECTED_MISSIONS:
        fail(f"expected missions {sorted(EXPECTED_MISSIONS)}, got {sorted(names)}")

    if text.count('has "language: Successor"') != 3:
        fail("all three missions must require Successor language access")

    if text.count('attributes "successor"') != 3:
        fail("all three missions must be scoped to Successor worlds")

    for private_name in ("Archivist", "Fitter"):
        if private_name not in text:
            fail(f"missing recurring player-private character shorthand: {private_name}")

    if 'event "B2 Successor Interface Provenance Compact: Review Ready"' not in text:
        fail("missing delayed Review Ready event")
    if text.count('event "B2 Successor Interface Provenance Compact: Review Ready" 7 11') != 3:
        fail("all three substantive routes must schedule Review Ready in 7-11 days")

    for route in EXPECTED_ROUTES:
        if f'"{route}" = 1' not in text:
            fail(f"missing persistent initial route {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    for settlement in EXPECTED_SETTLEMENTS:
        if f'"{settlement}" = 1' not in text:
            fail(f"missing terminal settlement write {settlement}")
        if f'has "{settlement}"' not in text:
            fail(f"later reader does not consume {settlement}")

    if f'"{PREFIX} aftermath seen" = 1' not in text:
        fail("missing one-shot aftermath state")

    # These missions are dialogue/state-only. A terminal `accept` would move an
    # objective-less mission into the accepted mission list instead of closing it.
    accept_count = len(re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE))
    decline_count = len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE))
    if accept_count:
        fail(f"state-only dialogue lifecycle must contain zero accept terminals, got {accept_count}")
    if decline_count != 7:
        fail(f"expected exactly 7 state-only decline terminals, got {decline_count}")

    # Keep this check anchored to real tab-indented mission directives so ordinary
    # dialogue prose containing words such as 'destination' cannot become a false
    # positive. If an actual gameplay objective is added later, the lifecycle must
    # be reconsidered rather than silently retaining the state-only contract.
    objective_directive = re.compile(
        r'^(?:\t)+(?:destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b',
        flags=re.MULTILINE | re.IGNORECASE,
    )
    objective_match = objective_directive.search(text)
    if objective_match:
        fail(f"state-only lifecycle invalidated by gameplay objective directive: {objective_match.group(0).strip()}")

    condition_write = re.compile(r'^\s*"([^"]+)"\s*(?:=|\+=|-=)\s*\d+', re.MULTILINE)
    for cond in condition_write.findall(text):
        if not cond.startswith(PREFIX):
            fail(f"unexpected condition write outside B2 namespace: {cond}")

    forbidden_commands = (
        "credits ", "reputation ", "combat rating ", "cargo ", "outfit ",
        "ship ", "fleet ",
    )
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(forbidden_commands):
            fail(f"unexpected direct gameplay mutation command: {stripped}")

    required_fragments = (
        "morphic",
        "interface registry",
        "geometry",
        "pressure",
        "electrical behavior",
        "control convention",
        "temperature",
        "material limits",
        "repairs",
        "tested-interface record",
        "installation record",
        "portable qualification packet",
        "expiry and revalidation",
        "old approval is permanent proof",
        "shape traveled",
        "reasons we trusted it",
    )
    for fragment in required_fragments:
        if fragment.lower() not in lowered:
            fail(f"missing interface-provenance continuity concept: {fragment}")

    forbidden_claims = (
        "all successor ports use one authority",
        "central successor engineering office",
        "universal successor engineering law",
        "shape proves compatibility",
        "geometry proves compatibility",
    )
    for phrase in forbidden_claims:
        if phrase in lowered:
            fail(f"unsupported Successor authority/compatibility claim: {phrase}")

    labels, gotos = labels_and_gotos(text)
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    print("PASS: B2 Successor Interface Provenance Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Archivist + Fitter (player-private shorthand)")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: delayed_review=7-11 days")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Fitter Remembers")
    print("PASS: persistence_model=stock mission/global conditions")
    print("PASS: write_ownership=B2 namespace only")
    print("PASS: dialogue_lifecycle=0 accept + 7 decline")
    print("PASS: objective_surface=state-only dialogue")
    print("PASS: compatibility_boundary=geometry does not prove operating-context compatibility")


if __name__ == "__main__":
    main()
