#!/usr/bin/env python3
"""Focused structural validator for A2 Southern Rim Traffic Coordination."""
from pathlib import Path
import sys

A1_CONGESTION = "world: southern rim transit congestion"
A1_RESCUE = "world: merchant rescue load"


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 southern rim traffic coordination.txt")
    text = path.read_text(encoding="utf-8")
    errors = []
    required = [
        'mission "A2 Southern Rim Traffic Coordination: Briefing"',
        'mission "A2 Southern Rim Traffic Coordination: After Action"',
        'Rhea Solano',
        f'"{A1_CONGESTION}" >= 4', f'"{A1_CONGESTION}" >= 6', f'"{A1_CONGESTION}" < 4',
        f'"{A1_RESCUE}" >= 3', f'"{A1_RESCUE}" < 3',
        '"A2 Southern Rim Traffic Coordination: policy emergency corridors" = 1',
        '"A2 Southern Rim Traffic Coordination: policy staggered clearance" = 1',
        '"A2 Southern Rim Traffic Coordination: policy distributed routing" = 1',
        '"A2 Southern Rim Traffic Coordination: refused" = 1',
        '"A2 Southern Rim Traffic Coordination: followup pending" = 1',
        '"A2 Southern Rim Traffic Coordination: followup pending" = 0',
        '"A2 Southern Rim Traffic Coordination: refusal respected" = 1',
    ]
    for needle in required:
        if needle not in text:
            errors.append(f"missing: {needle}")

    for label in (
        "label emergency", "label staggered", "label distributed", "label refuse",
        "label emergency_rescue_high", "label emergency_rescue_low",
        "label staggered_rescue_high", "label staggered_rescue_low",
        "label distributed_rescue_high", "label distributed_rescue_low",
    ):
        if label not in text:
            errors.append(f"missing route: {label}")

    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if A1_CONGESTION in stripped or A1_RESCUE in stripped:
            if any(op in stripped for op in (" += ", " -= ", " = ", "<?= ", ">?= ")):
                errors.append(f"A1-state write at line {lineno}: {stripped}")
            if stripped.startswith("set ") or stripped.startswith("clear "):
                errors.append(f"A1-state set/clear at line {lineno}: {stripped}")

    for flag in (
        "Solano remembers emergency high rescue", "Solano remembers emergency low rescue",
        "Solano remembers staggered high rescue", "Solano remembers staggered low rescue",
        "Solano remembers distributed high rescue", "Solano remembers distributed low rescue",
    ):
        if flag not in text:
            errors.append(f"missing outcome memory: {flag}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print("missions=2")
    print("named_character=Rhea Solano")
    print("authoritative_inputs=southern rim transit congestion, merchant rescue load")
    print("initial_routes=emergency, staggered, distributed, refusal")
    print("briefing_context_variants=combined, gridlock, rescue, baseline")
    print("after_action_variants=6 + refusal")
    print("authoritative_A1_writes=none")
    print("persistent_A2_memory=yes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
