#!/usr/bin/env python3
"""Focused structural validation for A2 Bunrodea Freight Practice News."""

from pathlib import Path
import re
import sys

TARGET = Path("data/bunrodea/a2 bunrodea freight practice news.txt")

CANONICAL_HEADER = """# Copyright (c) 2026 by Wiredshark
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


def fail(message: str) -> None:
    raise AssertionError(message)


def news_blocks(text: str) -> dict[str, str]:
    starts = list(re.finditer(r'^news "([^"]+)"$', text, flags=re.MULTILINE))
    blocks: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        blocks[match.group(1)] = text[match.start():end]
    return blocks


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else TARGET
    text = path.read_text(encoding="utf-8")

    if not text.startswith(CANONICAL_HEADER):
        fail("production file must use the canonical 2026 Wiredshark GPL header")
    if not text.endswith("\n"):
        fail("production file must end with a trailing newline")

    expected = {
        "A2 Bunrodea freight practice portable Megasa": (
            "B2 Bunrodea Freight Petition Compact: settlement portable docket",
            'government "Bunrodea (Megasa)"',
        ),
        "A2 Bunrodea freight practice portable Erabu": (
            "B2 Bunrodea Freight Petition Compact: settlement portable docket",
            'government "Bunrodea"',
        ),
        "A2 Bunrodea freight practice dual Megasa": (
            "B2 Bunrodea Freight Petition Compact: settlement dual ledger",
            'government "Bunrodea (Megasa)"',
        ),
        "A2 Bunrodea freight practice dual Erabu": (
            "B2 Bunrodea Freight Petition Compact: settlement dual ledger",
            'government "Bunrodea"',
        ),
    }

    blocks = news_blocks(text)
    if set(blocks) != set(expected):
        fail(f"expected exactly four named Bunrodea freight-practice News groups, got: {sorted(blocks)}")

    portable = 0
    dual = 0
    megasa = 0
    erabu = 0
    for name, (settlement, government) in expected.items():
        block = blocks[name]
        required = (
            'has "B2 Bunrodea Freight Petition Compact: aftermath seen"',
            f'has "{settlement}"',
            government,
            "\n\tname\n",
            "\n\tmessage\n",
        )
        for token in required:
            if token not in block:
                fail(f"{name}: missing required gate/payload {token!r}")

        if block.count('has "B2 Bunrodea Freight Petition Compact: aftermath seen"') != 1:
            fail(f"{name}: aftermath gate must appear exactly once")
        settlement_gates = [
            line.strip()
            for line in block.splitlines()
            if "B2 Bunrodea Freight Petition Compact: settlement" in line
        ]
        if settlement_gates != [f'has "{settlement}"']:
            fail(f"{name}: must consume exactly one matching B2 settlement gate")

        if "portable docket" in settlement:
            portable += 1
        else:
            dual += 1
        if government == 'government "Bunrodea (Megasa)"':
            megasa += 1
        else:
            erabu += 1

        lowered = block.lower()
        if "declined" in lowered or "refusal" in lowered:
            fail(f"{name}: declined/refusal route must not be publicized")

    if (portable, dual) != (2, 2):
        fail("expected two portable-docket and two dual-ledger News consumers")
    if (megasa, erabu) != (2, 2):
        fail("expected two Megasa and two general/Erabu Bunrodea News consumers")

    content_without_comments = "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )
    forbidden_patterns = (
        r'^mission\s',
        r'^conversation\s',
        r'^event\s',
        r'^\s*action\s*$',
        r'^\s*(set|clear|add|subtract|multiply)\b',
        r'"world:',
        r'^\s*(credits|reputation|cargo|outfit|ship|fleet|combat|destination|waypoint|objective)\b',
    )
    for pattern in forbidden_patterns:
        if re.search(pattern, content_without_comments, flags=re.MULTILINE | re.IGNORECASE):
            fail(f"read-only News consumer contains forbidden mutation/objective pattern: {pattern}")

    assignment_lines = [
        line
        for line in content_without_comments.splitlines()
        if re.search(r'"(?:A1|A2|B1|B2|world:)[^"]+"\s*(?:=|\+=|-=)', line)
    ]
    if assignment_lines:
        fail(f"read-only News consumer contains persistent assignments: {assignment_lines}")

    if "declined/refusal route remains private" not in text:
        fail("production comments must explicitly preserve declined/refusal privacy")

    print(
        "PASS A2 Bunrodea Freight Practice News: 4 groups; exact aftermath + settlement mapping; "
        "2 portable + 2 dual; 2 Megasa + 2 general Bunrodea; read-only; refusal private"
    )


if __name__ == "__main__":
    main()
