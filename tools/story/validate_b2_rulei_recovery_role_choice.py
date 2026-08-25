#!/usr/bin/env python3
"""Focused validation for B2 Rulei Recovery Role Choice."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data" / "rulei" / "b2 rulei recovery role choice.txt"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def need(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


text = PATH.read_text(encoding="utf-8")
flat = " ".join(text.split())

missions = [
    "B2 Rulei Recovery Role Choice: Offer",
    "B2 Rulei Recovery Role Choice: Review",
    "B2 Rulei Recovery Role Choice: Renn Remembers",
]
for mission in missions:
    need(text.count(f'mission "{mission}"') == 1, f"expected exactly one {mission} mission")
need(len(re.findall(r'^event "B2 Rulei Recovery Role Choice: Review Ready"$', text, flags=re.MULTILINE)) == 1,
     "expected exactly one Review Ready event declaration")
need('has "B2 Rulei Exposure Accountability: aftermath seen"' in text,
     "Offer must consume integrated Rulei Exposure Accountability aftermath read-only")

# Three substantive routes introduce the arc and schedule exactly one delayed Review.
need(text.count('"B2 Rulei Recovery Role Choice: introduced" = 1') == 3,
     "exactly three substantive Offer routes must introduce the arc")
need(text.count('event "B2 Rulei Recovery Role Choice: Review Ready" 7 11') == 3,
     "exactly three substantive routes must schedule Review for 7-11 days")
for route in (
    "route current function",
    "route worker directed support",
    "route paired",
):
    need(text.count(f'"B2 Rulei Recovery Role Choice: {route}" = 1') == 1,
         f"{route} must be written exactly once")
need(text.count('"B2 Rulei Recovery Role Choice: declined" = 1') == 1,
     "refusal must write declined exactly once")

# Review and aftermath persistence must be cardinality-safe.
need(text.count('"B2 Rulei Recovery Role Choice: reviewed" = 1') == 2,
     "both Review settlements must close Review exactly once")
for settlement in (
    "settlement portable current role",
    "settlement fresh need renewal",
):
    need(text.count(f'"B2 Rulei Recovery Role Choice: {settlement}" = 1') == 1,
         f"{settlement} must be written exactly once")
need(text.count('"B2 Rulei Recovery Role Choice: aftermath seen" = 1') == 1,
     "aftermath must be written exactly once")
need('not "B2 Rulei Recovery Role Choice: aftermath seen"' in text,
     "aftermath must be one-shot")

# This slice is state-only: every terminal path closes with decline and none accepts.
need(len(re.findall(r"^\s*decline\s*$", text, flags=re.MULTILINE)) == 7,
     "expected exactly seven state-only decline terminals")
need(not re.search(r"^\s*accept\s*$", text, flags=re.MULTILINE),
     "state-only slice must not contain terminal accept")
for directive in ("destination", "stopover", "waypoint", "npc", "cargo", "passengers", "deadline", "timer"):
    need(not re.search(rf"^\s+{directive}\b", text, flags=re.MULTILINE | re.IGNORECASE),
         f"state-only slice must not add gameplay objective directive {directive}")

# Persistent writes must stay inside the new B2 namespace.
assignments = re.findall(r'^\s*"([^"]+)"\s*(?:=|\+=|-=|\+\+|--)', text, flags=re.MULTILINE)
for name in assignments:
    need(name.startswith("B2 Rulei Recovery Role Choice:"),
         f"unexpected persistent write outside B2 namespace: {name}")

# Core continuity/canon boundaries: history is useful, but it is not present authority.
for fragment in (
    "history without letting history assign the present",
    "historical recovery note can remain true without deciding today's assignment",
    "support should describe a present request",
    "Neither record silently overwrites the other",
    "The history is true. The inference is not",
    "Old supports remain in the recovery history",
    "History should remember me. It should not schedule me",
    "does not diagnose a lasting Rulei effect",
):
    need(fragment in flat, f"missing continuity/canon fragment: {fragment}")

# The new content must not claim broad law or Rulei causation.
need("create universal employment law" in flat,
     "production must explicitly disclaim universal employment law")
need("Rulei effect" in flat,
     "production must preserve uncertainty around lasting Rulei effects")

print("PASS: B2 Rulei Recovery Role Choice focused validation")
