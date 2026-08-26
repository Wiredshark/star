#!/usr/bin/env python3
from pathlib import Path
import re
import sys

PREFIX = "B2 Remnant Successor Judgment Compact:"
EXPECTED = Path("data/remnant/b2 remnant successor judgment compact.txt")


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EXPECTED
    text = path.read_text(encoding="utf-8")

    if not text.endswith("\n"):
        fail("missing trailing newline")
    if "GNU General Public License" not in text:
        fail("missing GPL header")

    for name in ("Corin Taal", "Aven Sile"):
        if name not in text:
            fail(f"missing named recurring character {name}")

    missions = re.findall(r'^mission "([^"]+)"$', text, re.M)
    expected_missions = {
        PREFIX + " Offer",
        PREFIX + " Review",
        PREFIX + " Aven Remembers",
    }
    if set(missions) != expected_missions:
        fail(f"mission set mismatch: {missions}")

    if text.count('event "B2 Remnant Successor Judgment Compact: Review Ready"') != 4:
        fail("Review Ready declaration plus exactly three schedules required")
    if "\tdate +7 +11\n" not in text:
        fail("review delay must be 7-11 days")

    for route in ("reasoning chain", "bounded precedent", "paired decisions"):
        if f'"{PREFIX} route {route}" = 1' not in text:
            fail(f"missing route-local write: {route}")
    if f'"{PREFIX} declined" = 1' not in text:
        fail("missing refusal persistence")

    offer = text.split(f'mission "{PREFIX} Offer"', 1)[1].split(f'mission "{PREFIX} Review"', 1)[0]
    decline_block = offer.split("\t\t\tlabel decline", 1)[1]
    if 'event "B2 Remnant Successor Judgment Compact: Review Ready"' in decline_block:
        fail("refusal must not schedule Review")
    if f'"{PREFIX} introduced" = 1' in decline_block:
        fail("refusal must not introduce arc")

    review = text.split(f'mission "{PREFIX} Review"', 1)[1].split(f'mission "{PREFIX} Aven Remembers"', 1)[0]
    if f'has "{PREFIX} review ready"' not in review:
        fail("Review must require delayed readiness")
    for settlement in ("independent decision", "explicit attribution"):
        if f'"{PREFIX} settlement {settlement}" = 1' not in review:
            fail(f"missing settlement {settlement}")
    if review.count(f'"{PREFIX} reviewed" = 1') != 2:
        fail("each settlement must close Review exactly once")

    aftermath = text.split(f'mission "{PREFIX} Aven Remembers"', 1)[1]
    for settlement in ("independent decision", "explicit attribution"):
        if f'has "{PREFIX} settlement {settlement}"' not in aftermath:
            fail(f"aftermath missing settlement gate {settlement}")
    if aftermath.count(f'"{PREFIX} aftermath seen" = 1') != 1:
        fail("aftermath must close exactly once")

    if text.count("\n\t\t\tdecline\n") != 7:
        fail("expected exactly seven state-only decline terminals")
    if re.search(r"\n\t\t\taccept\n", text):
        fail("state-only content must not use accept terminals")

    assignments = re.findall(r'^\s*"([^"]+)"\s*=\s*[-+]?\d+\s*$', text, re.M)
    bad = [name for name in assignments if not name.startswith(PREFIX)]
    if bad:
        fail(f"writes outside B2 namespace: {bad}")

    forbidden_directives = re.compile(r'^\s*(payment|reputation|cargo|outfit|ship|fleet|combat|destination|waypoint)\b', re.M)
    if forbidden_directives.search(text):
        fail("gameplay/material directive detected")
    if re.search(r'^\s*"world:[^"]+"\s*=', text, re.M):
        fail("world state mutation detected")

    if 'has "B2 Remnant Continuity Compact: aftermath seen"' not in offer:
        fail("Offer must consume integrated prior B2 aftermath read-only")

    phrases = (
        "present decision",
        "old decisions",
        "current evidence",
        "responsibility",
        "mentor",
        "successor",
    )
    for phrase in phrases:
        if phrase not in text.lower():
            fail(f"continuity boundary phrase missing: {phrase}")

    print("PASS: B2 Remnant Successor Judgment Compact validated")
    print("PASS: missions=3 routes=3+refusal settlements=2 aftermath=1")
    print("PASS: delayed_review=7-11_days terminals=7_decline_0_accept")
    print("PASS: ownership=B2-only prior_continuity=read-only material_mutation=none")


if __name__ == "__main__":
    main()
