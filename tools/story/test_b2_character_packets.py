#!/usr/bin/env python3
"""Focused validation for B2 character/dynamic-content packets."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
PACKETS = ROOT / "story" / "B2_CHARACTER_PACKETS.md"

REQUIRED_PHRASES = (
    "ES-STORY-0002",
    "Broken Compact",
    "Nadia Kelm",
    "Elias Dorne",
    "Mara Senn",
    "Persistent consequence states",
    "Later readers",
    "Save/persistence assumptions",
    "A2 dependencies",
    "A3 integration notes",
    "B3 continuity notes",
    "Diversity check",
)

REQUIRED_OUTCOMES = (
    "settlement operating partnership",
    "settlement estate sale",
    "settlement arbitration",
    "unresolved at departure",
)


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main() -> int:
    if not PACKETS.is_file():
        return fail("story/B2_CHARACTER_PACKETS.md is missing")

    text = PACKETS.read_text(encoding="utf-8")

    missing = [phrase for phrase in REQUIRED_PHRASES if phrase.lower() not in text.lower()]
    if missing:
        return fail("missing required B2 packet fields: " + ", ".join(missing))

    for outcome in REQUIRED_OUTCOMES:
        if f"ES-STORY-0002: {outcome}" not in text:
            return fail(f"missing persistent terminal outcome: {outcome}")

    approaches = re.findall(r"^\d+\. \*\*(.+?)\*\*$", text, flags=re.MULTILINE)
    if len(approaches) < 3:
        return fail(f"expected at least 3 player approaches, found {len(approaches)}")

    if "[Engineering: deferred refit records]" not in text:
        return fail("missing player-visible engineering requirement label target")
    if "[Republic procedure: preserve the claim before sale]" not in text:
        return fail("missing player-visible institutional requirement label target")

    if "no branch that invents a hidden legal/relationship stat solely for this conversation" not in text.lower():
        return fail("missing no-shadow-state requirement")

    if "no shortage, convoy, cargo-loss, route-security, or market-stabilization loop" not in text.lower():
        return fail("missing narrative diversity structural distinction")

    print("PASS: B2 Broken Compact packet contract validated")
    print(f"PASS: player approaches={len(approaches)}")
    print("PASS: persistent terminal outcomes=4")
    print("PASS: named characters=3")
    print("PASS: special-response label targets=2")
    return 0


if __name__ == "__main__":
    sys.exit(main())
