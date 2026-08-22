#!/usr/bin/env python3
"""Focused structural validation for B2 Republic Border Testimony Compact."""

from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/human/b2 republic border testimony compact.txt")
EXPECTED_MISSIONS = {
    "B2 Republic Border Testimony Compact: Offer",
    "B2 Republic Border Testimony Compact: Review",
    "B2 Republic Border Testimony Compact: Rook Remembers",
}
EXPECTED_ROUTES = {
    "B2 Republic Border Testimony Compact: route lineage",
    "B2 Republic Border Testimony Compact: route independent",
    "B2 Republic Border Testimony Compact: route paired",
}
EXPECTED_SETTLEMENTS = {
    "B2 Republic Border Testimony Compact: settlement portable provenance packet",
    "B2 Republic Border Testimony Compact: settlement expiry and renewal",
}
A1_INPUT = "world: republic border pressure"
PREFIX = "B2 Republic Border Testimony Compact:"


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

    if text.count('government "Republic"') != 3:
        fail("all three missions must be scoped to Republic government")

    for character in ("Talia Rook", "Jace Verran"):
        if character not in text:
            fail(f"missing recurring named character: {character}")

    # A1 owns live border pressure. B2 may only read it for Offer/Review gating.
    if text.count(A1_INPUT) < 2:
        fail("expected authoritative border-pressure input in Offer and Review")
    if f'"{A1_INPUT}" >= 4' not in text:
        fail("Offer must require Republic border pressure >= 4")
    if f'"{A1_INPUT}" <= 2' not in text:
        fail("Review must wait until Republic border pressure <= 2")
    for line in text.splitlines():
        if A1_INPUT in line and any(op in line for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"B2 may not mutate authoritative A1 input: {line.strip()}")

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

    # Every direct condition write must remain inside this B2 namespace.
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

    # Lifecycle contract: these are dialogue/state-only missions. Accepting a
    # mission with no gameplay objective can leave an objective-less mission active.
    # Every terminal path should persist state and close with `decline` instead.
    accept_count = len(re.findall(r'^\s*accept\s*$', text, flags=re.MULTILINE))
    decline_count = len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE))
    if accept_count != 0:
        fail(f"state-only dialogue must not use terminal accept; found {accept_count}")
    if decline_count != 7:
        fail(f"expected exactly 7 terminal decline paths, got {decline_count}")

    objective_prefixes = (
        "destination ", "stopover ", "waypoint ", "npc ", "cargo ",
        "passenger ", "deadline ", "timer ",
    )
    for line in text.splitlines():
        stripped = line.strip().lower()
        if stripped.startswith(objective_prefixes):
            fail(f"state-only lifecycle assumption invalidated by objective directive: {line.strip()}")

    # Evidence-boundary contract: repeated copies are not independent evidence,
    # and closed reports must carry disposition rather than remain perpetual warnings.
    required_fragments = (
        "one observation look like a pattern",
        "direct patrol observation",
        "independent observations",
        "duplication cannot manufacture independent corroboration",
        "source type",
        "observation date",
        "corrections",
        "contradictions",
        "current disposition",
        "stop circulating as active warnings",
        "genuinely new observation",
    )
    for fragment in required_fragments:
        if fragment.lower() not in lowered:
            fail(f"missing border-testimony continuity concept: {fragment}")

    # Do not turn source history into unsupported guilt/motive claims.
    forbidden_claims = (
        "proof of criminal intent",
        "proves criminal intent",
        "pirate traffic proves",
        "old suspicion is guilt",
    )
    for phrase in forbidden_claims:
        if phrase in lowered:
            fail(f"unsupported motive/guilt claim: {phrase}")

    labels, gotos = labels_and_gotos(text)
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    print("PASS: B2 Republic Border Testimony Compact structure validated")
    print("PASS: missions=3")
    print("PASS: recurring_characters=Talia Rook + Jace Verran")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: authoritative_a1_input=world: republic border pressure (read-only)")
    print("PASS: elevated-pressure offer + recovered-pressure review")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Rook Remembers")
    print("PASS: persistence_model=stock mission/global conditions")
    print("PASS: write_ownership=B2 namespace only")
    print("PASS: lifecycle=7 state-only terminals use decline")
    print("PASS: objective_surface=none")
    print("PASS: evidence_boundary=copies do not manufacture independent corroboration")


if __name__ == "__main__":
    main()
