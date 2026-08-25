#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/b2 deep veteran shadow compact.txt"
TEXT = PATH.read_text(encoding="utf-8")
PREFIX = "B2 Deep Veteran Shadow Compact:"


def require(fragment: str, message: str) -> None:
    if fragment not in TEXT:
        raise SystemExit(f"FAIL: {message}")


def section(start: str, end: str | None = None) -> str:
    i = TEXT.index(start)
    j = TEXT.index(end, i + len(start)) if end else len(TEXT)
    return TEXT[i:j]


def label_block(container: str, label: str, next_label: str | None = None) -> str:
    start = f"\t\t\tlabel {label}\n"
    i = container.index(start)
    if next_label:
        j = container.index(f"\t\t\tlabel {next_label}\n", i + len(start))
    else:
        j = len(container)
    return container[i:j]


for mission in ("Offer", "Review", "Lio Remembers"):
    require(f'mission "{PREFIX} {mission}"', f"{mission} mission missing")
require(f'event "{PREFIX} Review Ready"', "Review Ready event missing")
require('"combat rating" >= 80', "Offer must react to veteran combat progression")
require('"combat rating" >= 160', "Review must react to increased veteran reputation")

OFFER = section(f'mission "{PREFIX} Offer"', f'mission "{PREFIX} Review"')
REVIEW = section(f'mission "{PREFIX} Review"', f'mission "{PREFIX} Lio Remembers"')
AFTERMATH = section(f'mission "{PREFIX} Lio Remembers"')

routes = [
    ("reasoning", "judgment", "route decision reasoning"),
    ("judgment", "paired", "route independent judgment"),
    ("paired", "decline", "route paired example assessment"),
]
route_states = [state for _, _, state in routes]
for label, next_label, state in routes:
    seg = label_block(OFFER, label, next_label)
    if seg.count(f'"{PREFIX} introduced" = 1') != 1:
        raise SystemExit(f"FAIL: {label} must introduce exactly once")
    if seg.count(f'"{PREFIX} {state}" = 1') != 1:
        raise SystemExit(f"FAIL: {label} must write its route state exactly once")
    for other in route_states:
        if other != state and f'"{PREFIX} {other}" = 1' in seg:
            raise SystemExit(f"FAIL: {label} writes another route state")
    if seg.count(f'event "{PREFIX} Review Ready" 7 11') != 1:
        raise SystemExit(f"FAIL: {label} must schedule one 7-11 day Review")
    if seg.count("\t\t\t\tdecline") != 1:
        raise SystemExit(f"FAIL: {label} must terminate once with decline")

refusal = label_block(OFFER, "decline")
for forbidden in ("introduced", *route_states, "Review Ready"):
    if forbidden in refusal:
        raise SystemExit("FAIL: refusal must not introduce or arm Review")
if refusal.count(f'"{PREFIX} declined" = 1') != 1 or refusal.count("\t\t\t\tdecline") != 1:
    raise SystemExit("FAIL: refusal persistence/lifecycle mismatch")

if TEXT.count(f'event "{PREFIX} Review Ready" 7 11') != 3:
    raise SystemExit("FAIL: exactly three substantive routes must schedule Review")
if TEXT.count("\t\t\t\tdecline") != 7:
    raise SystemExit("FAIL: exactly seven state-only terminal declines required")
if "\t\t\t\taccept" in TEXT:
    raise SystemExit("FAIL: state-only compact must not accept objective-less missions")

require(f'has "{PREFIX} introduced"', "Review must require introduction")
require(f'has "{PREFIX} review ready"', "Review must require delayed readiness")
require(f'not "{PREFIX} reviewed"', "Review must be one-shot")
for route in ("route independent judgment", "route paired example assessment"):
    require(f'has "{PREFIX} {route}"', f"Review branch missing {route}")

settlements = [
    ("practice", "attribution", "settlement independent practice"),
    ("attribution", None, "settlement explicit mentor attribution"),
]
for label, next_label, state in settlements:
    seg = label_block(REVIEW, label, next_label)
    if seg.count(f'"{PREFIX} reviewed" = 1') != 1:
        raise SystemExit(f"FAIL: {label} must close Review exactly once")
    if seg.count(f'"{PREFIX} {state}" = 1') != 1:
        raise SystemExit(f"FAIL: {label} settlement write missing")
    if seg.count("\t\t\t\tdecline") != 1:
        raise SystemExit(f"FAIL: {label} must terminate once")

for state in ("settlement independent practice", "settlement explicit mentor attribution"):
    require(f'has "{PREFIX} {state}"', f"aftermath gate missing {state}")
if AFTERMATH.count(f'"{PREFIX} aftermath seen" = 1') != 1:
    raise SystemExit("FAIL: aftermath must write one-shot state exactly once")
if AFTERMATH.count("\t\t\t\tdecline") != 1:
    raise SystemExit("FAIL: aftermath must terminate once")

# State ownership: condition assignments must stay inside the B2 namespace.
for line in TEXT.splitlines():
    stripped = line.strip()
    if " = " in stripped and stripped.startswith('"'):
        name = stripped.split('"', 2)[1]
        if not name.startswith(PREFIX):
            raise SystemExit(f"FAIL: non-B2 persistent write: {name}")

# This arc is dialogue/state-only; reject objective-bearing mission directives.
for line in TEXT.splitlines():
    stripped = line.strip()
    if stripped.startswith(("destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passengers ", "deadline ", "timer ")):
        raise SystemExit(f"FAIL: unexpected gameplay objective directive: {stripped}")

for fragment, message in (
    ("Study the decision, not the signature move", "decision-reasoning route missing"),
    ("disagreement is part of learning", "independent-judgment route missing"),
    ("paired notes", "paired-example structure missing"),
    ("The observed examples are unchanged", "history-versus-assessment distinction missing"),
    ("only the advice actually given travels", "mentor-attribution boundary missing"),
    ("not a Deep command doctrine or Pilot Guild rule", "local-not-centralized canon boundary missing"),
):
    require(fragment, message)

print("PASS: B2 Deep Veteran Shadow Compact")
