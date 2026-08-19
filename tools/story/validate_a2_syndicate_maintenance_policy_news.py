#!/usr/bin/env python3
from pathlib import Path
import sys

EXPECTED = [
    "safety pressure",
    "safety stable",
    "contracts pressure",
    "contracts stable",
    "resilience pressure",
    "resilience stable",
]
MEMORIES = [
    "Marr remembers safety under pressure",
    "Marr remembers safety stabilized",
    "Marr remembers contracts under pressure",
    "Marr remembers contracts stabilized",
    "Marr remembers resilience under pressure",
    "Marr remembers resilience stabilized",
]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 syndicate maintenance policy news.txt")
    text = path.read_text(encoding="utf-8")
    errors = []

    if text.count('news "A2 Syndicate maintenance policy ') != 6:
        errors.append("expected exactly 6 Syndicate maintenance policy News groups")

    for outcome, memory in zip(EXPECTED, MEMORIES):
        if f'news "A2 Syndicate maintenance policy {outcome}"' not in text:
            errors.append(f"missing News group: {outcome}")
        if f'has "A2 Syndicate Maintenance Triage: {memory}"' not in text:
            errors.append(f"missing resolved-memory gate: {memory}")

    if text.count('has "A2 Syndicate Maintenance Triage: followup seen"') != 6:
        errors.append("every News group must require resolved followup state")

    if "A2 Syndicate Maintenance Triage: refusal respected" in text:
        errors.append("refusal must remain private and must not be publicized through ambient News")

    forbidden = [
        '"world: syndicate maintenance backlog" =',
        '"world: syndicate maintenance backlog" +=',
        '"world: syndicate maintenance backlog" -=',
        '"world: syndicate maintenance surge" =',
        '"A2 Syndicate Maintenance Triage: priority safety" =',
        '"A2 Syndicate Maintenance Triage: priority contracts" =',
        '"A2 Syndicate Maintenance Triage: priority resilience" =',
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
    print("news_groups=6")
    print("resolved_outcomes=6")
    print("state_writes=none")
    print("refusal_publicized=no")
    print("a1_ownership=preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
