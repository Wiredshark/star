#!/usr/bin/env python3
from pathlib import Path
import sys

EXPECTED = [
    "safeguards routine",
    "safeguards elevated",
    "circles routine",
    "circles elevated",
]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 republic review practice news.txt")
    text = path.read_text(encoding="utf-8")
    errors = []

    if text.count('news "A2 Republic review practice ') != 4:
        errors.append("expected exactly 4 Republic review-practice news groups")

    for outcome in EXPECTED:
        if f'news "A2 Republic review practice {outcome}"' not in text:
            errors.append(f"missing news group: {outcome}")

    if text.count('has "B2 Republic Review Mentorship: aftermath seen"') != 4:
        errors.append("every group must require the resolved B2 aftermath")
    if text.count('has "A2 Republic Customs Review: precedent use bounded"') != 4:
        errors.append("every group must require bounded public precedent consent")
    if text.count('not "A2 Republic Customs Review: precedent kept private"') != 4:
        errors.append("every group must explicitly exclude private precedent")

    if text.count('has "B2 Republic Review Mentorship: settlement safeguards record"') != 2:
        errors.append("safeguards settlement must drive exactly two groups")
    if text.count('has "B2 Republic Review Mentorship: settlement supervised review circle"') != 2:
        errors.append("review-circle settlement must drive exactly two groups")
    if text.count('"world: republic customs scrutiny" < 3') != 2:
        errors.append("expected two routine-scrutiny variants")
    if text.count('"world: republic customs scrutiny" >= 3') != 2:
        errors.append("expected two elevated-scrutiny variants")

    forbidden = [
        '"world: republic customs scrutiny" =',
        '"world: republic customs scrutiny" +=',
        '"world: republic customs scrutiny" -=',
        '"B2 Republic Review Mentorship: settlement safeguards record" =',
        '"B2 Republic Review Mentorship: settlement supervised review circle" =',
        '"A2 Republic Customs Review: precedent use bounded" =',
        '"A2 Republic Customs Review: precedent kept private" =',
        "\taction\n",
    ]
    for token in forbidden:
        if token in text:
            errors.append(f"forbidden write/action: {token}")

    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("PASS")
    print("news_groups=4")
    print("b2_settlements=safeguards_record,supervised_review_circle")
    print("a1_scrutiny_variants=routine,elevated")
    print("public_consent=bounded_only")
    print("private_precedent_publicized=no")
    print("state_writes=none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
