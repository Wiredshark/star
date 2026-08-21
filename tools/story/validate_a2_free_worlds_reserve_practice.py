#!/usr/bin/env python3
"""Focused structural validation for A2 Free Worlds Reserve Practice."""

from pathlib import Path
import re
import sys

DEFAULT_PATH = Path("data/human/a2 free worlds reserve practice.txt")
EXPECTED_MISSIONS = {
    "A2 Free Worlds Reserve Practice: Briefing",
    "A2 Free Worlds Reserve Practice: Recurrence",
}
A1_INPUT = "world: free worlds relief reserve strain"
B2_PREFIX = "B2 Free Worlds Reserve Recovery Compact:"
A2_PREFIX = "A2 Free Worlds Reserve Practice:"
EXPECTED_ROUTES = {
    "A2 Free Worlds Reserve Practice: closure evidence",
    "A2 Free Worlds Reserve Practice: current capacity",
    "A2 Free Worlds Reserve Practice: local only",
}
EXPECTED_SETTLEMENTS = {
    "B2 Free Worlds Reserve Recovery Compact: settlement portable reserve packet",
    "B2 Free Worlds Reserve Recovery Compact: settlement reconciliation cycle",
}


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

    for name in ("Rina Sol", "Cal Brenner"):
        if name not in text:
            fail(f"missing returning B2 character {name}")

    if text.count('government "Free Worlds"') != 2:
        fail("both missions must be scoped to Free Worlds government")

    if 'has "B2 Free Worlds Reserve Recovery Compact: aftermath seen"' not in text:
        fail("Briefing must consume completed B2 aftermath")

    for settlement in EXPECTED_SETTLEMENTS:
        if f'has "{settlement}"' not in text:
            fail(f"Recurrence must preserve B2 settlement context: {settlement}")

    if f'"{A1_INPUT}" <= 1' not in text:
        fail("Briefing must occur during recovered reserve strain <= 1")
    if f'"{A1_INPUT}" >= 3' not in text:
        fail("Recurrence must require a later reserve-strain episode >= 3")

    for route in EXPECTED_ROUTES:
        if f'"{route}" = 1' not in text:
            fail(f"missing persistent A2 route {route}")
        if f'has "{route}"' not in text:
            fail(f"Recurrence does not consume A2 route {route}")

    if '"A2 Free Worlds Reserve Practice: declined" = 1' not in text:
        fail("missing explicit refusal persistence")
    if 'has "A2 Free Worlds Reserve Practice: declined"' in text:
        fail("refusal must not arm the recurrence mission")

    if '"A2 Free Worlds Reserve Practice: recurrence seen" = 1' not in text:
        fail("missing one-shot recurrence state")

    # Both missions are state-only conversations. Their terminal paths must close
    # the offer instead of moving an objective-less mission into the accepted list.
    if re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE):
        fail("dialogue-only A2 missions must terminate with decline, not accept")
    if len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)) < 5:
        fail("expected all four briefing terminals and recurrence terminal to decline")

    condition_write = re.compile(r'^\s*"([^"]+)"\s*(?:=|\+=|-=)\s*\d+', re.MULTILINE)
    for cond in condition_write.findall(text):
        if not cond.startswith(A2_PREFIX):
            fail(f"unexpected condition write outside A2 namespace: {cond}")

    for line in text.splitlines():
        stripped = line.strip()
        if A1_INPUT in stripped and any(op in stripped for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"A2 may not mutate authoritative A1 state: {stripped}")
        if B2_PREFIX in stripped and any(op in stripped for op in (" = ", " += ", " -= ", "set ", "clear ")):
            fail(f"A2 may not mutate B2 settlement state: {stripped}")

    forbidden_commands = (
        "credits ", "reputation ", "combat rating ", "cargo ", "outfit ",
        "ship ", "fleet ",
    )
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(forbidden_commands):
            fail(f"unexpected direct gameplay mutation command: {stripped}")

    required_concepts = (
        "closure evidence",
        "current capacity",
        "context, not authority",
        "borrowed",
        "maintenance",
        "old packet is evidence about what was true then",
    )
    lowered = text.lower()
    for phrase in required_concepts:
        if phrase.lower() not in lowered:
            fail(f"missing continuity concept: {phrase}")

    labels, gotos = labels_and_gotos(text)
    missing = sorted(gotos - labels)
    if missing:
        fail(f"goto target(s) missing labels: {missing}")

    # Three positive practices crossed with the two integrated B2 settlements
    # must remain visibly distinct in the future recurrence reader.
    expected_branch_labels = {
        "closureReconcile",
        "currentPacket",
        "currentReconcile",
        "localPacket",
        "localReconcile",
    }
    if not expected_branch_labels.issubset(labels):
        fail("missing settlement-sensitive recurrence branches")
    if "record" not in labels:
        fail("missing common one-shot recurrence record label")

    print("PASS: A2 Free Worlds Reserve Practice structure validated")
    print("PASS: missions=2")
    print("PASS: returning_characters=Rina Sol, Cal Brenner")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: authoritative_a1_input=world: free worlds relief reserve strain (read-only)")
    print("PASS: b2_aftermath_and_settlements=read-only")
    print("PASS: calm-period briefing + future high-strain recurrence")
    print("PASS: dialogue_lifecycle=state-only terminals decline")
    print("PASS: persistence_model=stock mission/global conditions")
    print("PASS: write_ownership=A2 namespace only")


if __name__ == "__main__":
    main()
