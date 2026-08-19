#!/usr/bin/env python3
"""Focused structural validation for A2 Avgi Allocation Practice News."""

from pathlib import Path
import sys

TARGET = Path("data/avgi/a2 avgi allocation practice news.txt")


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else TARGET
    text = path.read_text(encoding="utf-8")

    expected_groups = {
        'news "a2 avgi allocation practice public ledger"': (
            '"B2 Avgi Allocation Compact: settlement public emergency ledger"',
            "public-ledger civilian consequence",
        ),
        'news "a2 avgi allocation practice public ledger guard"': (
            '"B2 Avgi Allocation Compact: settlement public emergency ledger"',
            "public-ledger Guard consequence",
        ),
        'news "a2 avgi allocation practice dual threshold"': (
            '"B2 Avgi Allocation Compact: settlement dual threshold"',
            "dual-threshold civilian consequence",
        ),
        'news "a2 avgi allocation practice dual threshold guard"': (
            '"B2 Avgi Allocation Compact: settlement dual threshold"',
            "dual-threshold Guard consequence",
        ),
    }

    if text.count('\nnews "') + int(text.startswith('news "')) != 4:
        fail("expected exactly four News groups")

    for marker, (settlement, label) in expected_groups.items():
        start = text.find(marker)
        if start < 0:
            fail(f"missing {label}")
        next_group = text.find('\nnews "', start + len(marker))
        block = text[start:] if next_group < 0 else text[start:next_group]
        if 'has "B2 Avgi Allocation Compact: aftermath seen"' not in block:
            fail(f"{label} must require resolved B2 aftermath")
        if f"has {settlement}" not in block:
            fail(f"{label} must require its exact B2 settlement")
        if 'has "language: Avgi"' not in block:
            fail(f"{label} must preserve Avgi-language gating")
        if 'government "Avgi (Consonance)"' not in block:
            fail(f"{label} must remain scoped to Consonance ports")

    forbidden = (
        "\taction\n",
        '"B2 Avgi Allocation Compact: aftermath seen" =',
        '"B2 Avgi Allocation Compact: settlement public emergency ledger" =',
        '"B2 Avgi Allocation Compact: settlement dual threshold" =',
        '"world:',
    )
    for token in forbidden:
        if token in text:
            fail(f"read-only consumer contains forbidden write/authority token: {token}")

    if "declined" in text.lower() or "refusal" in text.lower():
        fail("declined/refusal path must not be publicized by this News layer")

    print(
        "PASS A2 Avgi Allocation Practice News: "
        "4 groups; aftermath-gated; 2 public-ledger + 2 dual-threshold; "
        "read-only; declined path remains private"
    )


if __name__ == "__main__":
    main()
