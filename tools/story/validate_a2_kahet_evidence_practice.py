#!/usr/bin/env python3
"""Validate the A2 Ka'het Evidence Practice specialist slice."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "kahet" / "a2 kahet evidence practice.txt"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    text = DATA.read_text(encoding="utf-8")

    require(text.count('mission "A2 Ka\'het Evidence Practice:') == 2,
            "expected exactly two A2 Ka'het Evidence Practice missions")
    require('has "B2 Ka\'het Signal Interpretation: aftermath seen"' in text,
            "offer must require resolved B2 aftermath")
    require('has "B2 Ka\'het Signal Interpretation: settlement contradiction register"' in text,
            "offer must recognize contradiction-register settlement")
    require('"A2 Ka\'het Evidence Practice: route bounded hypothesis" = 1' in text,
            "bounded-hypothesis route missing")
    require('"A2 Ka\'het Evidence Practice: route contradiction preserved" = 1' in text,
            "contradiction-preserving route missing")
    require('"A2 Ka\'het Evidence Practice: route local only" = 1' in text,
            "local-only route missing")
    require('"A2 Ka\'het Evidence Practice: declined" = 1' in text,
            "decline route missing")
    require('"A2 Ka\'het Evidence Practice: reflection seen" = 1' in text,
            "reflection persistence missing")
    require(text.count('event "A2 Ka\'het Evidence Practice: Reflection Ready"') >= 4,
            "reflection event must exist and be scheduled by each positive route")

    action_lines = [line.strip() for line in text.splitlines() if line.strip().startswith('"') and '= 1' in line]
    forbidden_writes = [
        line for line in action_lines
        if line.startswith('"B2 Ka\'het Signal Interpretation:') or line.startswith('"world:')
    ]
    require(not forbidden_writes,
            f"A2 must not write B2/world state: {forbidden_writes}")

    a2_writes = [line for line in action_lines if line.startswith('"A2 Ka\'het Evidence Practice:')]
    require(len(a2_writes) >= 8, "expected persistent A2 route/reflection state")

    authority_terms = re.findall(r'(?i)\b(Ka\'het office|Ka\'het authority|Remnant office|Remnant authority)\b', text)
    require(not authority_terms, "text must not grant formal Ka'het/Remnant authority")
    require('private shorthand' in text,
            "Interpreter/Scout private-shorthand boundary must remain explicit")

    print("PASS: A2 Ka'het Evidence Practice")
    print("missions=2 routes=3 refusal=1 reflection=1 b2_world_writes=0")


if __name__ == "__main__":
    main()
