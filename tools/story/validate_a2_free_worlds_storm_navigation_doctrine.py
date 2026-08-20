#!/usr/bin/env python3
"""Focused structural validator for A2 Free Worlds Storm Navigation Doctrine."""
from pathlib import Path
import sys


def require(text: str, needle: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"missing: {needle}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/human/a2 free worlds storm navigation doctrine.txt"
    )
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for needle in (
        'mission "A2 Free Worlds Storm Navigation Doctrine: Briefing"',
        'mission "A2 Free Worlds Storm Navigation Doctrine: Recovery Boundary"',
        'mission "A2 Free Worlds Storm Navigation Doctrine: Recurrence Review"',
        'Rhea Solano',
        'has "world: free worlds geomagnetic storm active"',
        '"world: free worlds geomagnetic navigation strain" >= 3',
        '"world: free worlds geomagnetic navigation strain" >= 5',
        'not "world: free worlds geomagnetic storm active"',
        '"world: free worlds geomagnetic navigation strain" <= 1',
        '"A2 Free Worlds Storm Navigation Doctrine: doctrine verified corridors" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: doctrine independent crosscheck" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: doctrine local autonomy" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: refused" = 1',
        'set "A2 Free Worlds Storm Navigation Doctrine: recurrence armed"',
        '"A2 Free Worlds Storm Navigation Doctrine: refusal respected" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: Solano remembers corridors severe" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: Solano remembers corridors moderate" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: Solano remembers crosscheck severe" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: Solano remembers crosscheck moderate" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: Solano remembers autonomy severe" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: Solano remembers autonomy moderate" = 1',
        '"A2 Free Worlds Storm Navigation Doctrine: recurrence seen" = 1',
    ):
        require(text, needle, errors)

    for label in (
        'label corridors',
        'label crosscheck',
        'label autonomy',
        'label refuse',
        'label corridors_severe',
        'label corridors_moderate',
        'label crosscheck_severe',
        'label crosscheck_moderate',
        'label autonomy_severe',
        'label autonomy_moderate',
    ):
        require(text, label, errors)

    # The recurrence review must be impossible until the first storm has fully
    # recovered, preventing it from firing again during the same disturbance.
    recovery_start = text.find('mission "A2 Free Worlds Storm Navigation Doctrine: Recovery Boundary"')
    recurrence_start = text.find('mission "A2 Free Worlds Storm Navigation Doctrine: Recurrence Review"')
    if recovery_start < 0 or recurrence_start < 0 or recovery_start >= recurrence_start:
        errors.append("recovery boundary must precede recurrence review")

    # A2 may read but never mutate A1-owned storm/navigation state.
    a1_states = (
        "world: free worlds geomagnetic storm active",
        "world: free worlds geomagnetic storm cooldown",
        "world: free worlds geomagnetic storm advisory seen",
        "world: free worlds geomagnetic strain advisory seen",
        "world: free worlds geomagnetic navigation strain",
    )
    for state in a1_states:
        for operator in (
            f'set "{state}"',
            f'clear "{state}"',
            f'"{state}" +=',
            f'"{state}" -=',
            f'"{state}" = ',
            f'"{state}" <?=',
            f'"{state}" >?=',
        ):
            if operator in text:
                errors.append(f"forbidden A1 state write: {operator}")

    # Refusal should not arm a future doctrine test.
    refuse_block = text[text.find('label refuse'):text.find('mission "A2 Free Worlds Storm Navigation Doctrine: Recovery Boundary"')]
    if 'recovery pending' in refuse_block or 'recurrence armed' in refuse_block:
        errors.append("refusal must not arm recurrence evaluation")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print("missions=3")
    print("named_character=Rhea Solano")
    print("authoritative_inputs=storm_active,navigation_strain")
    print("initial_routes=verified_corridors,independent_crosscheck,local_autonomy,refusal")
    print("recovery_boundary=storm_inactive+strain<=1")
    print("recurrence_variants=6+refusal")
    print("authoritative_A1_writes=none")
    print("persistent_A2_memory=yes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
