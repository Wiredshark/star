#!/usr/bin/env python3
"""Focused structural validation for the A2 Broken Compact production candidate."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "a2 broken compact.txt"

REQUIRED_MISSIONS = (
    'mission "A2 Broken Compact: First Hearing"',
    'mission "A2 Broken Compact: Evidence Hearing"',
    'mission "A2 Broken Compact: Later Reader"',
    'mission "A2 Broken Compact: Refusal Reader"',
)

REQUIRED_CHARACTERS = (
    "Nadia Kelm",
    "Elias Dorne",
    "Mara Senn",
    "Morrow Line",
)

REQUIRED_PERSISTENT_STATES = (
    '"A2 Broken Compact: found private message" = 1',
    '"A2 Broken Compact: found senn annotation" = 1',
    '"A2 Broken Compact: settlement arbitration" = 1',
    '"A2 Broken Compact: settlement operating partnership" = 1',
    '"A2 Broken Compact: settlement estate sale" = 1',
    '"A2 Broken Compact: kelm trusts player" = 1',
    '"A2 Broken Compact: dorne trusts player" = 1',
    '"A2 Broken Compact: later reader pending" = 1',
)

LATER_READS = (
    'has "A2 Broken Compact: settlement arbitration"',
    'has "A2 Broken Compact: settlement operating partnership"',
    'has "A2 Broken Compact: declined"',
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    if not DATA.is_file():
        fail(f"missing {DATA.relative_to(ROOT)}")

    text = DATA.read_text(encoding="utf-8")

    for needle in REQUIRED_MISSIONS:
        if needle not in text:
            fail(f"missing mission block: {needle}")

    for name in REQUIRED_CHARACTERS:
        if name not in text:
            fail(f"missing production character/reference: {name}")

    for state in REQUIRED_PERSISTENT_STATES:
        if state not in text:
            fail(f"missing persistent consequence: {state}")

    for read in LATER_READS:
        if read not in text:
            fail(f"missing later reader: {read}")

    if '"reputation: Republic" > 0' not in text:
        fail("missing real Republic reputation input")

    if "[Republic standing: preserve the claim before sale]" not in text:
        fail("missing player-visible special response label")

    # Require multiple materially distinct first-hearing routes.
    for label in ("label evidence", "label procedure", "label estate", "label refuse"):
        if label not in text:
            fail(f"missing first-hearing route: {label}")

    # Require three mutually exclusive evidence-hearing settlement writes.
    settlement_writes = re.findall(
        r'"A2 Broken Compact: settlement (?:arbitration|operating partnership|estate sale)" = 1',
        text,
    )
    if len(settlement_writes) < 3:
        fail("expected all three evidence-hearing settlement outcomes")

    # The proof slice intentionally uses the engine's ordinary condition store.
    # Reject obvious attempts to create a generic A2-owned shadow world-state blob.
    forbidden = (
        "dialogue world state",
        "a2 relationship database",
        "a2 character memory database",
    )
    lowered = text.lower()
    for token in forbidden:
        if token in lowered:
            fail(f"forbidden duplicate state authority: {token}")

    print("PASS: A2 Broken Compact structural acceptance checks")
    print(f"missions={len(REQUIRED_MISSIONS)}")
    print("first_hearing_routes=4")
    print("evidence_hearing_settlements=3")
    print("later_readers=3+refusal")
    print("persistence=ordinary mission/global conditions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
