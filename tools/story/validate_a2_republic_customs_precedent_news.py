#!/usr/bin/env python3
from pathlib import Path
import sys

OUTCOMES = [
    "bounded audit",
    "written uncertainty",
    "contextualized routing",
    "formal process",
]
MEMORY = {
    "bounded audit": "A2 Republic Customs Review: outcome bounded audit",
    "written uncertainty": "A2 Republic Customs Review: outcome written uncertainty",
    "contextualized routing": "A2 Republic Customs Review: outcome contextualized routing",
    "formal process": "A2 Republic Customs Review: outcome refusal preserved",
}


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 republic customs precedent news.txt")
    text = path.read_text(encoding="utf-8")
    errors = []

    if text.count('news "A2 Republic customs precedent ') != 4:
        errors.append("expected exactly 4 Republic customs precedent news groups")

    for outcome in OUTCOMES:
        if f'news "A2 Republic customs precedent {outcome}"' not in text:
            errors.append(f"missing news group: {outcome}")
        if f'has "{MEMORY[outcome]}"' not in text:
            errors.append(f"missing outcome memory gate: {outcome}")

    if text.count('has "A2 Republic Customs Review: later reader seen"') != 4:
        errors.append("every group must require the resolved later reader")
    if text.count('has "A2 Republic Customs Review: precedent use bounded"') != 4:
        errors.append("every public group must require bounded precedent consent")
    if 'has "A2 Republic Customs Review: precedent kept private"' in text:
        errors.append("private-precedent state must never authorize public news")

    forbidden = [
        '\taction\n',
        '"world: republic customs scrutiny" =',
        '"world: republic customs scrutiny" +=',
        '"world: republic customs scrutiny" -=',
        '"world: republic border pressure" =',
        '"world: republic border pressure" +=',
        '"world: republic border pressure" -=',
        '"A2 Republic Customs Review: precedent use bounded" =',
        '"A2 Republic Customs Review: precedent kept private" =',
    ]
    for token in forbidden:
        if token in text:
            errors.append(f"forbidden state write/action: {token}")

    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("PASS")
    print("news_groups=4")
    print("public_consent_gate=precedent use bounded")
    print("private_precedent_publicized=no")
    print("state_writes=none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())