#!/usr/bin/env python3
"""Focused structural validator for B2 Syndicate Charter Obligations."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "b2 syndicate charter obligations.txt"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> None:
    text = DATA.read_text(encoding="utf-8")

    missions = re.findall(r'^mission "([^"]+)"$', text, flags=re.MULTILINE)
    require(len(missions) == 3, f"expected 3 missions, found {len(missions)}")
    require(missions == [
        "B2 Syndicate Charter Obligations: Offer",
        "B2 Syndicate Charter Obligations: Review",
        "B2 Syndicate Charter Obligations: Solis Remembers",
    ], "mission names/order changed")

    for name in ("Rhea Solis", "Ilan Merrow"):
        require(name in text, f"missing named character {name}")

    for route in ("solis", "compromise", "merrow"):
        require(
            f'"B2 Syndicate Charter Obligations: route {route}" = 1' in text,
            f"missing persistent route {route}",
        )

    settlements = (
        "settlement public covenant",
        "settlement consortium reserve",
    )
    for settlement in settlements:
        require(
            f'"B2 Syndicate Charter Obligations: {settlement}" = 1' in text,
            f"missing terminal settlement {settlement}",
        )

    require(text.count('"B2 Syndicate Charter Obligations: reviewed" = 1') == 2,
            "each terminal settlement must mark the review complete")
    require('has "B2 Syndicate Charter Obligations: introduced"' in text,
            "review does not consume persistent introduction state")
    require('not "B2 Syndicate Charter Obligations: reviewed"' in text,
            "review lacks one-shot persistence gate")
    require('not "B2 Syndicate Charter Obligations: aftermath seen"' in text,
            "later reader lacks one-shot persistence gate")
    require('"B2 Syndicate Charter Obligations: aftermath seen" = 1' in text,
            "later reader does not persist completion")

    # Both terminal outcomes must be readable by the later named-character mission.
    later = text.split('mission "B2 Syndicate Charter Obligations: Solis Remembers"', 1)[1]
    for settlement in settlements:
        require(f'has "B2 Syndicate Charter Obligations: {settlement}"' in later,
                f"later reader does not consume {settlement}")

    # The slice is specifically anchored to Syndicate institutional history.
    require(text.count('government "Syndicate"') == 3,
            "all three missions must remain Syndicate-scoped")
    require("charter" in text.lower() and "emergency" in text.lower(),
            "institutional-history anchor disappeared")

    # These three missions are dialogue/state-only. A terminal `accept` would move
    # an objective-less offered mission into the active mission list after the
    # conversation closes. All seven terminal paths must persist the same state and
    # terminate with `decline` instead.
    require(not re.search(r'^\s*accept\s*$', text, flags=re.MULTILINE),
            "state-only Syndicate Charter missions must not leave accepted missions active")
    decline_count = len(re.findall(r'^\s*decline\s*$', text, flags=re.MULTILINE))
    require(decline_count == 7,
            f"expected exactly seven state-only dialogue terminals to decline, found {decline_count}")

    # If a real gameplay objective is added later, the lifecycle assumption above
    # must be revisited rather than silently keeping this validator stale.
    for objective in (
        '\tdestination ',
        '\tstopover ',
        '\twaypoint ',
        '\tnpc ',
        '\tdeadline ',
        '\tpassengers ',
        '\tcargo ',
    ):
        require(objective not in text,
                f"unexpected mission objective in state-only lifecycle slice: {objective.strip()}")

    # Guard against accidentally turning this into economy rewards/reputation mutation.
    forbidden = ("payment ", "credits", "reputation", "combat rating", "cargo ")
    lower = text.lower()
    for token in forbidden:
        require(token not in lower, f"unexpected gameplay-reward/state token: {token.strip()}")

    # Labels referenced by goto must exist inside this file.
    labels = set(re.findall(r'^\s*label ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE))
    gotos = re.findall(r'^\s*goto ([A-Za-z0-9_-]+)\s*$', text, flags=re.MULTILINE)
    missing = sorted(set(gotos) - labels)
    require(not missing, f"goto target(s) missing label: {missing}")

    print("PASS: B2 Syndicate Charter Obligations structure validated")
    print("PASS: missions=3")
    print("PASS: named_characters=2")
    print("PASS: initial_routes=3 + refusal")
    print("PASS: terminal_settlements=2")
    print("PASS: later_reader=Solis Remembers")
    print("PASS: persistence_model=stock mission/global conditions")
    print("PASS: lifecycle=state-only dialogue terminals decline cleanly")


if __name__ == "__main__":
    main()
