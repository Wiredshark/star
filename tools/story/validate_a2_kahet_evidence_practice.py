#!/usr/bin/env python3
"""Validate the A2 Ka'het Evidence Practice current-main restage."""

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
    require(text.count('"offer precedence" 9') == 2,
            "both state-only missions must use offer precedence 9")
    require(text.count('has "B2 Ka\'het Signal Interpretation: aftermath seen"') == 2,
            "both missions must require resolved B2 aftermath")
    require('has "B2 Ka\'het Signal Interpretation: settlement contradiction register"' in text,
            "offer must recognize contradiction-register settlement")

    routes = (
        "route bounded hypothesis",
        "route contradiction preserved",
        "route local only",
    )
    for route in routes:
        require(f'"A2 Ka\'het Evidence Practice: {route}" = 1' in text,
                f"persistent route missing: {route}")
        require(f'has "A2 Ka\'het Evidence Practice: {route}"' in text,
                f"reflection missing explicit route gate: {route}")

    require('"A2 Ka\'het Evidence Practice: declined" = 1' in text,
            "decline route missing")
    require('"A2 Ka\'het Evidence Practice: reflection seen" = 1' in text,
            "reflection persistence missing")
    require(text.count('event "A2 Ka\'het Evidence Practice: Reflection Ready" 9 14') == 3,
            "each positive route must schedule the reflection exactly once")

    # These are dialogue/state-only missions: no objective-less accepted mission may remain.
    require(re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE) is None,
            "state-only A2 missions must not use accept")
    require(len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE)) == 5,
            "expected four Offer terminals plus one Reflection terminal to decline")
    objective_directives = re.findall(
        r'^\s*(destination|waypoint|stopover|cargo|passengers|npc|ship|fleet|deadline)\b',
        text,
        flags=re.MULTILINE,
    )
    require(not objective_directives,
            f"state-only slice must not add gameplay objectives: {objective_directives}")

    assignment_lines = [
        line.strip() for line in text.splitlines()
        if line.strip().startswith('"') and re.search(r'\s(?:=|\+=|-=)\s', line)
    ]
    forbidden_writes = [
        line for line in assignment_lines
        if line.startswith('"B2 Ka\'het Signal Interpretation:') or line.startswith('"world:')
    ]
    require(not forbidden_writes,
            f"A2 must not write B2/world state: {forbidden_writes}")

    a2_writes = [line for line in assignment_lines if line.startswith('"A2 Ka\'het Evidence Practice:')]
    require(len(a2_writes) >= 8, "expected persistent A2 route/reflection state")

    # Refusal must not arm the later reader.
    decline_block = text.split('\t\t\tlabel decline', 1)[1].split('\n\n\nmission ', 1)[0]
    require('Reflection Ready' not in decline_block,
            "refusal must not schedule reflection")

    authority_terms = re.findall(
        r"(?i)\b(Ka'het office|Ka'het authority|Remnant office|Remnant authority)\b",
        text,
    )
    require(not authority_terms, "text must not grant formal Ka'het/Remnant authority")
    require('private shorthand' in text,
            "Interpreter/Scout private-shorthand boundary must remain explicit")

    print("PASS: A2 Ka'het Evidence Practice current-main restage")
    print("missions=2 routes=3 refusal=1 reflection=1 precedence=9 accepts=0 declines=5 b2_world_writes=0")


if __name__ == "__main__":
    main()
