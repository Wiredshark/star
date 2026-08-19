#!/usr/bin/env python3
from pathlib import Path
import sys

GROUPS = [
    "portable pilot",
    "portable registrar",
    "tiered pilot",
    "tiered registrar",
]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/incipias/a2 incipias license practice news.txt")
    text = path.read_text(encoding="utf-8")
    errors = []

    if text.count('news "A2 Incipias license practice ') != 4:
        errors.append("expected exactly 4 Incipias license-practice news groups")

    for group in GROUPS:
        if f'news "A2 Incipias license practice {group}"' not in text:
            errors.append(f"missing news group: {group}")

    if text.count('has "B2 Incipias License Compact: aftermath seen"') != 4:
        errors.append("every news group must require B2 aftermath seen")
    if text.count('has "B2 Incipias License Compact: settlement portable endorsement"') != 2:
        errors.append("portable settlement must gate exactly two news groups")
    if text.count('has "B2 Incipias License Compact: settlement tiered renewal"') != 2:
        errors.append("tiered settlement must gate exactly two news groups")
    if text.count('government "Conlatio"') != 4:
        errors.append("every news group must remain scoped to Conlatio ports")

    forbidden = [
        '\taction\n',
        '"B2 Incipias License Compact: aftermath seen" =',
        '"B2 Incipias License Compact: settlement portable endorsement" =',
        '"B2 Incipias License Compact: settlement tiered renewal" =',
        '"B2 Incipias License Compact: introduced" =',
        '"B2 Incipias License Compact: reviewed" =',
        '"world:',
    ]
    for token in forbidden:
        if token in text:
            errors.append(f"forbidden mutation/world-state token: {token}")

    if "declined" in text.lower() or "refusal" in text.lower():
        errors.append("declined/refusal route must not be publicized by this News consumer")

    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("PASS")
    print("news_groups=4")
    print("portable_groups=2")
    print("tiered_groups=2")
    print("state_writes=none")
    print("declined_route_publicized=no")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
