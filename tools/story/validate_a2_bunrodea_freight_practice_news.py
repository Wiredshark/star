#!/usr/bin/env python3
from pathlib import Path
import sys

EXPECTED = [
    "portable Megasa",
    "portable Erabu",
    "dual Megasa",
    "dual Erabu",
]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/bunrodea/a2 bunrodea freight practice news.txt")
    text = path.read_text(encoding="utf-8")
    errors = []

    if text.count('news "A2 Bunrodea freight practice ') != 4:
        errors.append("expected exactly 4 Bunrodea freight practice news groups")
    for outcome in EXPECTED:
        if f'news "A2 Bunrodea freight practice {outcome}"' not in text:
            errors.append(f"missing news group: {outcome}")

    if text.count('has "B2 Bunrodea Freight Petition Compact: aftermath seen"') != 4:
        errors.append("every group must require B2 aftermath seen")
    if text.count('has "B2 Bunrodea Freight Petition Compact: settlement portable docket"') != 2:
        errors.append("portable-docket settlement must gate exactly 2 groups")
    if text.count('has "B2 Bunrodea Freight Petition Compact: settlement dual ledger"') != 2:
        errors.append("dual-ledger settlement must gate exactly 2 groups")
    if text.count('government "Bunrodea (Megasa)"') != 2:
        errors.append("expected exactly 2 Megasa-scoped groups")
    if text.count('government "Bunrodea"') != 2:
        errors.append("expected exactly 2 Erabu/general Bunrodea-scoped groups")

    forbidden = [
        '"B2 Bunrodea Freight Petition Compact: settlement portable docket" =',
        '"B2 Bunrodea Freight Petition Compact: settlement dual ledger" =',
        '"B2 Bunrodea Freight Petition Compact: aftermath seen" =',
        '"B2 Bunrodea Freight Petition Compact: declined"',
        '"world:',
        "\taction\n",
    ]
    for token in forbidden:
        if token in text:
            errors.append(f"forbidden state write/publicization token: {token}")

    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("PASS")
    print("news_groups=4")
    print("settlements=portable_docket,dual_ledger")
    print("state_writes=none")
    print("declined_publicized=no")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
