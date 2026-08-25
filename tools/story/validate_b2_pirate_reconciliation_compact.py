#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/b2 pirate reconciliation compact.txt"
TEXT = PATH.read_text(encoding="utf-8")
PREFIX = "B2 Pirate Reconciliation Compact:"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def block_between(start_marker: str, end_marker: str | None = None) -> str:
    start = TEXT.find(start_marker)
    require(start >= 0, f"missing marker: {start_marker}")
    if end_marker is None:
        return TEXT[start:]
    end = TEXT.find(end_marker, start + len(start_marker))
    require(end >= 0, f"missing end marker: {end_marker}")
    return TEXT[start:end]


require(TEXT.endswith("\n"), "production file must end with newline")
for name in ["Offer", "Review", "Ressa Remembers"]:
    require(f'mission "{PREFIX} {name}"' in TEXT, f"missing mission {name}")
require(TEXT.count(f'mission "{PREFIX}') == 3, "expected exactly three compact missions")
require(TEXT.count('government "Pirate"') == 3, "all missions must remain Pirate-scoped")
require('"pirate jobs" > 2' in TEXT, "Offer must consume existing pirate RPG history")

# Lifecycle and persistence cardinality.
require(TEXT.count('event "B2 Pirate Reconciliation Compact: Review Ready" 7 11') == 3, "exactly three substantive routes must schedule Review")
require(TEXT.count('\n\t\t\t\tdecline\n') == 7, "all seven state-only terminal paths must decline")
require('\n\t\t\t\taccept\n' not in TEXT, "no objective-less accept terminal is allowed")
require(TEXT.count(f'"{PREFIX} introduced" = 1') == 3, "each substantive route must introduce once")
require(TEXT.count(f'"{PREFIX} declined" = 1') == 1, "refusal must be written once")
require(TEXT.count(f'"{PREFIX} reviewed" = 1') == 2, "each Review settlement must close once")
require(TEXT.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must be one-shot")

routes = [
    ("apology", "route apology stands"),
    ("repair", "route repair by action"),
    ("separate", "route forgiveness separate"),
]
for index, (label, route) in enumerate(routes):
    next_label = routes[index + 1][0] if index + 1 < len(routes) else "decline"
    block = block_between(f"\n\t\t\tlabel {label}\n", f"\n\t\t\tlabel {next_label}\n")
    require(block.count(f'"{PREFIX} introduced" = 1') == 1, f"{label} must introduce exactly once")
    require(block.count(f'"{PREFIX} {route}" = 1') == 1, f"{label} must write its own route exactly once")
    require(block.count('Review Ready" 7 11') == 1, f"{label} must schedule one Review")
    require(block.count("\n\t\t\t\tdecline\n") == 1, f"{label} must terminate exactly once")
    for _, other_route in routes:
        if other_route != route:
            require(f'"{PREFIX} {other_route}" = 1' not in block, f"{label} must not write {other_route}")

refusal = block_between("\n\t\t\tlabel decline\n", '\n\nmission "B2 Pirate Reconciliation Compact: Review"')
require(f'"{PREFIX} declined" = 1' in refusal, "refusal must write declined")
require(f'"{PREFIX} introduced" = 1' not in refusal, "refusal must not introduce")
require("Review Ready\" 7 11" not in refusal, "refusal must not schedule Review")
for _, route in routes:
    require(f'"{PREFIX} {route}" = 1' not in refusal, f"refusal must not write {route}")

review = block_between('mission "B2 Pirate Reconciliation Compact: Review"', '\n\nmission "B2 Pirate Reconciliation Compact: Ressa Remembers"')
require(f'has "{PREFIX} introduced"' in review, "Review requires introduction")
require(f'has "{PREFIX} review ready"' in review, "Review requires delayed readiness")
require(f'not "{PREFIX} reviewed"' in review, "Review must be one-shot")
settlements = [
    ("fresh", "settlement fresh trust"),
    ("gradual", "settlement gradual trust"),
]
for index, (label, settlement) in enumerate(settlements):
    end_marker = f"\n\t\t\tlabel {settlements[index + 1][0]}\n" if index + 1 < len(settlements) else '\n\nmission "B2 Pirate Reconciliation Compact: Ressa Remembers"'
    block = block_between(f"\n\t\t\tlabel {label}\n", end_marker)
    require(block.count(f'"{PREFIX} reviewed" = 1') == 1, f"{label} must close Review exactly once")
    require(block.count(f'"{PREFIX} {settlement}" = 1') == 1, f"{label} must write its own settlement")
    require(block.count("\n\t\t\t\tdecline\n") == 1, f"{label} must terminate exactly once")
    for _, other in settlements:
        if other != settlement:
            require(f'"{PREFIX} {other}" = 1' not in block, f"{label} must not write {other}")

after = block_between('mission "B2 Pirate Reconciliation Compact: Ressa Remembers"')
require(f'not "{PREFIX} aftermath seen"' in after, "aftermath must be one-shot")
for _, settlement in settlements:
    require(f'has "{PREFIX} {settlement}"' in after, f"aftermath must accept {settlement}")
require(after.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath write must occur once")
require(after.count("\n\t\t\t\tdecline\n") == 1, "aftermath must terminate once")

# Every assignment must remain B2-owned. The vanilla pirate-jobs counter is read-only.
for line in TEXT.splitlines():
    stripped = line.strip()
    if stripped.startswith('"') and '" =' in stripped:
        key = stripped.split('"', 2)[1]
        require(key.startswith(PREFIX), f"out-of-namespace write: {key}")
require('"pirate jobs" =' not in TEXT, "pirate jobs history must remain read-only")
require('"world:' not in TEXT, "slice must not read or write world state")

# Dialogue-only slice: no gameplay objectives, material rewards, or reputation mutation.
for directive in [
    "\n\tdestination ", "\n\tstopover ", "\n\twaypoint ", "\n\tnpc ", "\n\tcargo ",
    "\n\tpassengers ", "\n\tdeadline ", "\n\ttimer ", "\n\t\tpayment ", "\n\t\toutfit ",
    "reputation:",
]:
    require(directive not in TEXT, f"unexpected gameplay/material directive: {directive.strip()}")

# Character and canon boundaries.
for phrase in [
    "Ressa Vale", "Kade Orin", "apology", "forgive", "friendship", "operational trust",
    "specific job", "changed behavior",
]:
    require(phrase.lower() in TEXT.lower(), f"missing character/theme phrase: {phrase}")
for forbidden in [
    "Pirate law", "Pirate court", "Pirate office", "binding Pirate rule", "universal Pirate code",
    "forgiveness restores trust", "apology purchases forgiveness",
]:
    require(forbidden.lower() not in TEXT.lower(), f"must not invent coercive or centralized rule: {forbidden}")

print("PASS: B2 Pirate Reconciliation Compact")
