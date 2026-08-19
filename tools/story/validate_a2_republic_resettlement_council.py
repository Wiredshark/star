#!/usr/bin/env python3
"""Focused structural validation for the A2 Republic Resettlement Council slice.

This validates the candidate's source contract. It does not replace the normal
Endless Sky parser/build/runtime/save-load gates.
"""
from pathlib import Path
import re
import sys

A1_STATES = (
    "world: republic displacement pressure",
    "world: republic border pressure",
    "world: republic resettlement surge",
)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/human/a2 republic resettlement council.txt"
    )
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    required = (
        'mission "A2 Republic Resettlement Council: Emergency Session"',
        'mission "A2 Republic Resettlement Council: After Action"',
        "Lena Orr",
        '"world: republic displacement pressure" >= 2',
        '"world: republic displacement pressure" >= 4',
        '"world: republic displacement pressure" < 2',
        'has "world: republic resettlement surge"',
        '"world: republic border pressure" >= 4',
        '"world: republic border pressure" < 4',
        '"A2 Republic Resettlement Council: priority family unity" = 1',
        '"A2 Republic Resettlement Council: priority work continuity" = 1',
        '"A2 Republic Resettlement Council: priority distributed placement" = 1',
        '"A2 Republic Resettlement Council: refused" = 1',
        '"A2 Republic Resettlement Council: followup pending" = 1',
        '"A2 Republic Resettlement Council: followup pending" = 0',
        '"A2 Republic Resettlement Council: refusal respected" = 1',
        'label family_border_high',
        'label family_border_low',
        'label work_border_high',
        'label work_border_low',
        'label distributed_border_high',
        'label distributed_border_low',
    )
    for token in required:
        if token not in text:
            errors.append(f"missing: {token}")

    for state in A1_STATES:
        escaped = re.escape(state)
        illegal = re.compile(
            rf'^\s*(?:set|clear)\s+"{escaped}"|"{escaped}"\s*(?:\+=|-=|=\s*\d)',
            re.MULTILINE,
        )
        if illegal.search(text):
            errors.append(f"A2 illegally writes authoritative A1 state: {state}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print("missions=2")
    print("named_character=Lena Orr")
    print("authoritative_inputs=republic displacement pressure, republic border pressure, republic resettlement surge")
    print("initial_routes=family unity, work continuity, distributed placement, refusal")
    print("after_action_variants=6 + refusal")
    print("authoritative_A1_writes=none")
    print("persistent_A2_memory=yes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
