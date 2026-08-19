#!/usr/bin/env python3
from pathlib import Path
import sys

EXPECTED = [
    "medical clear", "medical residual",
    "throughput clear", "throughput residual",
    "distribution clear", "distribution residual",
]

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 free worlds relief policy news.txt")
    text = path.read_text(encoding="utf-8")
    errors = []
    if text.count('news "A2 Free Worlds relief policy ') != 6:
        errors.append("expected exactly 6 relief policy news groups")
    for outcome in EXPECTED:
        if f'news "A2 Free Worlds relief policy {outcome}"' not in text:
            errors.append(f"missing news group: {outcome}")
        if f'has "A2 Free Worlds Relief Coordination: Vale remembers {outcome}"' not in text:
            errors.append(f"missing memory gate: {outcome}")
    if text.count('has "A2 Free Worlds Relief Coordination: followup seen"') != 6:
        errors.append("every group must require followup seen")
    forbidden = [
        '"world: free worlds relief demand" =',
        '"world: free worlds relief demand" +=',
        '"world: free worlds relief demand" -=',
        '"A2 Free Worlds Relief Coordination: priority medical" =',
        '"A2 Free Worlds Relief Coordination: priority throughput" =',
        '"A2 Free Worlds Relief Coordination: priority distribution" =',
        "\taction\n",
    ]
    for token in forbidden:
        if token in text:
            errors.append(f"forbidden write/action: {token}")
    if errors:
        print("FAIL")
        for e in errors:
            print("-", e)
        return 1
    print("PASS")
    print("news_groups=6")
    print("state_writes=none")
    print("refusal_publicized=no")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
