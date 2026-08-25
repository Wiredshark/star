#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/b2 deep keepsake friendship.txt"
TEXT = PATH.read_text(encoding="utf-8")
PREFIX = "B2 Deep Keepsake Friendship:"


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
for name in ["Offer", "Review", "Sana Remembers"]:
    require(f'mission "{PREFIX} {name}"' in TEXT, f"missing mission {name}")
require(TEXT.count(f'mission "{PREFIX}') == 3, "expected exactly three compact missions")
require(TEXT.count('attributes "deep"') == 3, "each mission must remain Deep-scoped")
require('has "Gift Store Interaction: declined"' in TEXT, "must consume the established gift-store encounter")

# Lifecycle and persistence cardinality.
require(TEXT.count('event "B2 Deep Keepsake Friendship: Review Ready" 7 11') == 3, "exactly three positive routes must schedule Review")
require(TEXT.count('\n\t\t\t\tdecline\n') == 7, "all seven state-only terminal paths must decline")
require('\n\t\t\t\taccept\n' not in TEXT, "no objective-less accept terminal is allowed")
require(TEXT.count(f'"{PREFIX} introduced" = 1') == 3, "each positive route must introduce once")
require(TEXT.count(f'"{PREFIX} declined" = 1') == 1, "refusal must be written once")
require(TEXT.count(f'"{PREFIX} reviewed" = 1') == 2, "each settlement must close Review once")
require(TEXT.count(f'"{PREFIX} aftermath seen" = 1') == 1, "aftermath must be one-shot")

for route in ["route shared ritual", "route no debt", "route gifts separate"]:
    require(TEXT.count(f'"{PREFIX} {route}" = 1') == 1, f"route write must occur once: {route}")
for settlement in ["settlement broad reciprocity", "settlement explicit promises"]:
    require(TEXT.count(f'"{PREFIX} {settlement}" = 1') == 1, f"settlement write must occur once: {settlement}")
    require(f'has "{PREFIX} {settlement}"' in TEXT, f"aftermath must read settlement: {settlement}")

# Refusal must not arm the later Review.
refusal = block_between("\n\t\t\tlabel decline\n", '\n\nmission "B2 Deep Keepsake Friendship: Review"')
require(f'"{PREFIX} declined" = 1' in refusal, "refusal must write declined")
require(f'"{PREFIX} introduced" = 1' not in refusal, "refusal must not introduce the arc")
require("Review Ready\" 7 11" not in refusal, "refusal must not schedule Review")

review = block_between('mission "B2 Deep Keepsake Friendship: Review"', '\n\nmission "B2 Deep Keepsake Friendship: Sana Remembers"')
require(f'has "{PREFIX} introduced"' in review, "Review requires introduction")
require(f'has "{PREFIX} review ready"' in review, "Review requires delayed readiness")
require(f'not "{PREFIX} reviewed"' in review, "Review must be one-shot")

after = block_between('mission "B2 Deep Keepsake Friendship: Sana Remembers"')
require(f'not "{PREFIX} aftermath seen"' in after, "aftermath must be one-shot")
for settlement in ["settlement broad reciprocity", "settlement explicit promises"]:
    require(f'has "{PREFIX} {settlement}"' in after, f"aftermath must accept {settlement}")

# Every assignment in this file must remain B2-owned.
for line in TEXT.splitlines():
    stripped = line.strip()
    if stripped.startswith('"') and '" =' in stripped:
        key = stripped.split('"', 2)[1]
        require(key.startswith(PREFIX), f"out-of-namespace write: {key}")
require('"world:' not in TEXT, "slice must not depend on or write world state")

# Dialogue-only slice: no gameplay objectives or material rewards.
for directive in ["\n\tdestination ", "\n\tstopover ", "\n\twaypoint ", "\n\tnpc ", "\n\tcargo ", "\n\tpassengers ", "\n\tdeadline ", "\n\ttimer ", "\n\t\tpayment ", "\n\t\toutfit "]:
    require(directive not in TEXT, f"unexpected gameplay/material directive: {directive.strip()}")

# Character continuity and deliberately local scope.
for phrase in ["Niko Rell", "Sana Vey", "souvenir", "friendship", "gift", "favor", "promise"]:
    require(phrase.lower() in TEXT.lower(), f"missing character/theme phrase: {phrase}")
require("institution" not in TEXT.lower(), "this friendship arc must not invent a new institution")
require("universal" not in TEXT.lower(), "this friendship arc must not claim universal authority")

print("PASS: B2 Deep Keepsake Friendship")
