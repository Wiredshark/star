#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data" / "coalition" / "b2 coalition shared table compact.txt"
TEXT = PATH.read_text(encoding="utf-8")
PREFIX = "B2 Coalition Shared Table Compact:"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def mission_block(name: str, next_name: str | None = None) -> str:
    marker = f'mission "{name}"'
    start = TEXT.find(marker)
    require(start >= 0, f"missing mission {name}")
    if next_name:
        end = TEXT.find(f'mission "{next_name}"', start + len(marker))
        require(end >= 0, f"missing next mission {next_name}")
        return TEXT[start:end]
    return TEXT[start:]


def label_block(text: str, label: str, next_labels: list[str]) -> str:
    marker = f"\t\t\tlabel {label}\n"
    start = text.find(marker)
    require(start >= 0, f"missing label {label}")
    ends = []
    for nxt in next_labels:
        pos = text.find(f"\t\t\tlabel {nxt}\n", start + len(marker))
        if pos >= 0:
            ends.append(pos)
    return text[start:min(ends) if ends else len(text)]


require(TEXT.endswith("\n"), "file must end with newline")
require(TEXT.startswith("# Copyright (c) 2026 by the Endless Sky contributors"), "missing canonical GPL header")
require(TEXT.count('mission "B2 Coalition Shared Table Compact:') == 3, "expected exactly three missions")
require(TEXT.count('event "B2 Coalition Shared Table Compact: Review Ready"') == 4, "expected one event declaration plus three schedules")
require('attributes "saryd"' in TEXT, "slice must stay in Saryd local scope")
require('has "known to the heliarchs"' in TEXT, "Offer must consume Coalition access state")
require("centralized Coalition food law" in TEXT, "must disclaim centralized Coalition food law")
require("family recipes" in TEXT and "shared version" in TEXT, "must preserve source recipe and shared adaptation distinction")
require("universal authenticity" in TEXT, "must reject repetition as universal authenticity")

missions = [
    "B2 Coalition Shared Table Compact: Offer",
    "B2 Coalition Shared Table Compact: Review",
    "B2 Coalition Shared Table Compact: Mato Remembers",
]
offer = mission_block(missions[0], missions[1])
review = mission_block(missions[1], missions[2])
after = mission_block(missions[2])

for who in ("Leri Vann", "Mato Kesh"):
    require(who in offer, f"Offer missing recurring character {who}")

routes = {
    "lineage": '"B2 Coalition Shared Table Compact: route attributable lineage" = 1',
    "living": '"B2 Coalition Shared Table Compact: route living version" = 1',
    "paired": '"B2 Coalition Shared Table Compact: route paired records" = 1',
}
for label, state in routes.items():
    block = label_block(offer, label, ["lineage", "living", "paired", "decline"])
    require(block.count('"B2 Coalition Shared Table Compact: introduced" = 1') == 1, f"{label} must introduce exactly once")
    require(block.count(state) == 1, f"{label} must write its route exactly once")
    for other_label, other_state in routes.items():
        if other_label != label:
            require(other_state not in block, f"{label} must not write {other_label} route")
    require(block.count('event "B2 Coalition Shared Table Compact: Review Ready" 7 11') == 1, f"{label} must schedule Review exactly once")
    require(block.count("\n\t\t\t\tdecline\n") == 1, f"{label} must terminate exactly once")

decline = label_block(offer, "decline", [])
require('"B2 Coalition Shared Table Compact: declined" = 1' in decline, "refusal must persist declined state")
require('"B2 Coalition Shared Table Compact: introduced" = 1' not in decline, "refusal must not introduce arc")
require('event "B2 Coalition Shared Table Compact: Review Ready" 7 11' not in decline, "refusal must not arm Review")
require(decline.count("\n\t\t\t\tdecline\n") == 1, "refusal must terminate once")

for gate in (
    'has "B2 Coalition Shared Table Compact: introduced"',
    'has "B2 Coalition Shared Table Compact: review ready"',
    'not "B2 Coalition Shared Table Compact: reviewed"',
):
    require(gate in review, f"Review missing lifecycle gate: {gate}")

settlements = {
    "packet": '"B2 Coalition Shared Table Compact: settlement portable lineage" = 1',
    "coexist": '"B2 Coalition Shared Table Compact: settlement versioned coexistence" = 1',
}
for label, state in settlements.items():
    block = label_block(review, label, ["packet", "coexist"])
    require(block.count('"B2 Coalition Shared Table Compact: reviewed" = 1') == 1, f"{label} must close Review exactly once")
    require(block.count(state) == 1, f"{label} must write its settlement exactly once")
    for other_label, other_state in settlements.items():
        if other_label != label:
            require(other_state not in block, f"{label} must not write {other_label} settlement")
    require(block.count("\n\t\t\t\tdecline\n") == 1, f"{label} must terminate once")

require('not "B2 Coalition Shared Table Compact: aftermath seen"' in after, "aftermath must be one-shot")
for state in settlements.values():
    condition = state.replace(" = 1", "").replace('"', '')
    require(condition in after, "aftermath must accept either settlement")
require(after.count('"B2 Coalition Shared Table Compact: aftermath seen" = 1') == 1, "aftermath must write seen exactly once")
require(after.count("\n\t\t\t\tdecline\n") == 1, "aftermath must terminate once")

writes = re.findall(r'^\s*"([^\"]+)"\s*=\s*1\s*$', TEXT, flags=re.MULTILINE)
require(writes, "expected persistent writes")
require(all(name.startswith(PREFIX) for name in writes), "all persistent writes must stay in B2 namespace")

for forbidden in (
    "credits ", "reputation ", "cargo ", "outfit ", "ship ", "fleet ",
    "combat rating", "government ", "destination ", "stopover ", "waypoint ",
    "npc ", "passenger ", "deadline ", "timer ",
):
    require(not re.search(rf'^\t+{re.escape(forbidden)}', TEXT, flags=re.MULTILINE), f"unexpected gameplay mutation/objective directive: {forbidden.strip()}")

require(TEXT.count("\n\t\t\t\tdecline\n") == 7, "expected exactly seven state-only decline terminals")
require("\n\t\t\t\taccept\n" not in TEXT, "state-only slice must not accept objective-less missions")

print("PASS: B2 Coalition Shared Table Compact")
