#!/usr/bin/env python3
"""Focused structural validator for A2 Free Worlds Relief Coordination.

This checks the specialist content contract only. It does not replace the normal
Endless Sky content parser, build, runtime, or save/load validation gates.
"""
from pathlib import Path
import sys


def require(text: str, needle: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"missing: {needle}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/human/a2 free worlds relief coordination.txt"
    )
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for needle in (
        'mission "A2 Free Worlds Relief Coordination: Surge Briefing"',
        'mission "A2 Free Worlds Relief Coordination: After Action"',
        'Imani Vale',
        '"world: free worlds relief demand" >= 3',
        '"world: free worlds relief demand" >= 5',
        '"world: free worlds relief demand" < 3',
        '"A2 Free Worlds Relief Coordination: priority medical" = 1',
        '"A2 Free Worlds Relief Coordination: priority throughput" = 1',
        '"A2 Free Worlds Relief Coordination: priority distribution" = 1',
        '"A2 Free Worlds Relief Coordination: refused" = 1',
        '"A2 Free Worlds Relief Coordination: followup pending" = 1',
        '"A2 Free Worlds Relief Coordination: followup pending" = 0',
        '"A2 Free Worlds Relief Coordination: refusal respected" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers medical clear" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers medical residual" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers throughput clear" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers throughput residual" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers distribution clear" = 1',
        '"A2 Free Worlds Relief Coordination: Vale remembers distribution residual" = 1',
    ):
        require(text, needle, errors)

    for label in (
        'label medical',
        'label throughput',
        'label distribution',
        'label refuse',
        'label medical_clear',
        'label medical_residual',
        'label throughput_clear',
        'label throughput_residual',
        'label distribution_clear',
        'label distribution_residual',
    ):
        require(text, label, errors)

    # A2 is a read-only consumer of the authoritative A1 relief-demand state.
    forbidden_world_writes = (
        '"world: free worlds relief demand" +=',
        '"world: free worlds relief demand" -=',
        '"world: free worlds relief demand" = ',
        'set "world: free worlds relief demand"',
        'clear "world: free worlds relief demand"',
    )
    for needle in forbidden_world_writes:
        if needle in text:
            errors.append(f"forbidden A1 state write: {needle}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print("missions=2")
    print("named_character=Imani Vale")
    print("authoritative_input=world: free worlds relief demand")
    print("initial_routes=medical,throughput,distribution,refusal")
    print("after_action_variants=6+refusal")
    print("authoritative_A1_writes=none")
    print("persistent_A2_memory=yes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
