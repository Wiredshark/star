#!/usr/bin/env python3
from pathlib import Path
import re
import sys

PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/human/a2 syndicate maintenance triage.txt")
text = PATH.read_text(encoding="utf-8")
lines = text.splitlines()
stripped_lines = [line.strip() for line in lines]
errors = []

HEADER = """# Copyright (c) 2026 by the Endless Sky contributors
#
# Endless Sky is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
"""


def need(token, count=None):
    actual = text.count(token)
    if actual == 0:
        errors.append(f"missing: {token}")
    elif count is not None and actual != count:
        errors.append(f"wrong count for {token!r}: expected {count}, got {actual}")


def need_line(token, count=1):
    actual = stripped_lines.count(token)
    if actual != count:
        errors.append(f"wrong exact-line count for {token!r}: expected {count}, got {actual}")


def direct_assignment(line):
    stripped = line.strip()
    match = re.match(r'^"([^"]+)"\s*(\+=|-=|(?<![<>!])=(?!=))\s*', stripped)
    return match.group(1) if match else None


if not text.startswith(HEADER + "\n"):
    errors.append("missing canonical GPL content header")
if not text.endswith("\n"):
    errors.append("missing trailing newline")

need('mission "A2 Syndicate Maintenance Triage: Surge Briefing"', 1)
need('mission "A2 Syndicate Maintenance Triage: After Action"', 1)
if text.count('\nmission "') != 2:
    errors.append(f"expected exactly 2 missions, got {text.count(chr(10) + 'mission ')}")
need_line('"offer precedence" 9', 2)
need('Tessa Marr')

# Authoritative A1 inputs and thresholds remain read-only.
need('has "world: syndicate maintenance surge"', 1)
need('not "world: syndicate maintenance surge"', 1)
need_line('"world: syndicate maintenance backlog" >= 3', 4)
need_line('"world: syndicate maintenance backlog" < 3', 3)

# Save-compatible initial routes.
for state in (
    "priority safety",
    "priority contracts",
    "priority resilience",
    "refused",
):
    need_line(f'"A2 Syndicate Maintenance Triage: {state}" = 1', 1)
need_line('"A2 Syndicate Maintenance Triage: briefing seen" = 1', 4)
need_line('"A2 Syndicate Maintenance Triage: followup pending" = 1', 4)
need_line('"A2 Syndicate Maintenance Triage: followup pending" = 0', 1)
need_line('"A2 Syndicate Maintenance Triage: followup seen" = 1', 1)

# Explicit refusal handling and all six positive after-action outcomes.
need_line('branch refused', 1)
need_line('label refused', 1)
need_line('has "A2 Syndicate Maintenance Triage: refused"', 1)
need_line('"A2 Syndicate Maintenance Triage: refusal respected" = 1', 1)
for state in (
    "Marr remembers safety under pressure",
    "Marr remembers safety stabilized",
    "Marr remembers contracts under pressure",
    "Marr remembers contracts stabilized",
    "Marr remembers resilience under pressure",
    "Marr remembers resilience stabilized",
):
    need_line(f'"A2 Syndicate Maintenance Triage: {state}" = 1', 1)

for label in (
    "severe", "triage", "safety", "contracts", "resilience", "refuse",
    "refused", "safety_high", "safety_low", "contracts_high", "contracts_low",
    "resilience_high", "resilience_low", "finish",
):
    need_line(f"label {label}", 1)
need_line('goto finish', 7)

# State-only lifecycle: four Briefing terminals plus one converged After Action terminal.
decline_count = stripped_lines.count("decline")
accept_count = stripped_lines.count("accept")
if decline_count != 5:
    errors.append(f"expected exactly 5 decline terminals, got {decline_count}")
if accept_count:
    errors.append(f"state-only missions contain {accept_count} accept terminal(s)")

# All direct writes must remain within this A2 namespace. Comparisons such as >= and <= are reads.
for line in lines:
    state = direct_assignment(line)
    if state and not state.startswith("A2 Syndicate Maintenance Triage:"):
        errors.append(f"write outside A2 Syndicate Maintenance Triage namespace: {line.strip()}")

# Reject directive-shaped gameplay objectives/material mutations while allowing ordinary dialogue prose.
for line in lines:
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or stripped.startswith("`"):
        continue
    if re.match(r'^(destination|waypoint|stopover|cargo|passenger|passengers|npc|deadline|payment|outfit|ship|fleet|combat|reputation)\b', stripped):
        errors.append(f"unexpected gameplay/material directive: {stripped}")

# Every local goto target must be declared as a conversation label.
labels = {m.group(1) for m in re.finditer(r'^\s*label\s+(\S+)\s*$', text, re.MULTILINE)}
gotos = [m.group(1) for m in re.finditer(r'^\s*goto\s+(\S+)\s*$', text, re.MULTILINE)]
for target in gotos:
    if target not in labels:
        errors.append(f"goto target lacks local label: {target}")

if errors:
    print("FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("PASS")
print("missions=2")
print("named_character=Tessa Marr")
print("authoritative_inputs=world: syndicate maintenance surge + backlog")
print("initial_routes=safety, contracts, resilience, refusal")
print("after_action_variants=6 + explicit refusal")
print("state_only_terminals=5 decline, 0 accept")
print("authoritative_A1_writes=none")
print("persistent_A2_memory=yes")
