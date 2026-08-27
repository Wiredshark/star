#!/usr/bin/env python3
"""Focused structural validation for the A2 reactive-news production slice."""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "a2 reactive news.txt"

NEWS_ITEMS = (
    'news "A2 Deep convoy veteran"',
    'news "A2 Deep convoy command veteran"',
    'news "A2 experienced Republic captain"',
)

GPL_HEADER = """# Copyright (c) 2026 by the Endless Sky contributors
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


def require(ok: bool, failures: list[str], message: str) -> None:
    if not ok:
        failures.append(message)


def blocks(text: str) -> list[str]:
    starts = [match.start() for match in re.finditer(r'^news "A2 ', text, re.MULTILINE)]
    return [text[start:(starts[i + 1] if i + 1 < len(starts) else len(text))]
            for i, start in enumerate(starts)]


def main() -> int:
    failures: list[str] = []
    if not DATA.is_file():
        print(f"FAIL: missing {DATA.relative_to(ROOT)}")
        return 1

    text = DATA.read_text(encoding="utf-8")
    require(text.startswith(GPL_HEADER + "\n"), failures, "missing canonical GPL content header")
    require(text.endswith("\n"), failures, "missing trailing newline")

    found_blocks = blocks(text)
    require(len(found_blocks) == 3, failures, f"expected exactly 3 A2 News groups, found {len(found_blocks)}")
    for item in NEWS_ITEMS:
        require(text.count(item) == 1, failures, f"expected exactly one production news item: {item}")

    by_name = {block.splitlines()[0]: block for block in found_blocks}
    convoy = by_name.get(NEWS_ITEMS[0], "")
    combined = by_name.get(NEWS_ITEMS[1], "")
    experienced = by_name.get(NEWS_ITEMS[2], "")

    require('\tgovernment "Republic"' in convoy and '\tattributes "deep"' in convoy,
            failures, "Deep convoy veteran scope changed")
    require('has "Deep: Syndicate Convoy: done"' in convoy,
            failures, "Deep convoy veteran missing persistent mission-history gate")
    require('"combat rating" >= 5' not in convoy,
            failures, "Deep convoy veteran must not require combat rating")

    require('\tgovernment "Republic"' in combined and '\tattributes "deep"' in combined,
            failures, "Deep command veteran scope changed")
    require('has "Deep: Syndicate Convoy: done"' in combined,
            failures, "Deep command veteran missing mission-history gate")
    require('"combat rating" >= 5' in combined,
            failures, "Deep command veteran missing combat-rating gate")

    require('\tgovernment "Republic"' in experienced and '\tnot attributes "station"' in experienced,
            failures, "experienced Republic captain scope changed")
    require('"combat rating" >= 5' in experienced,
            failures, "experienced Republic captain missing combat-rating gate")
    require('has "Deep: Syndicate Convoy: done"' not in experienced,
            failures, "experienced Republic captain must remain independent of Deep convoy history")

    for index, block in enumerate(found_blocks, 1):
        require(block.count("\tto show\n") == 1, failures, f"news group {index} must have exactly one to-show gate")
        require("\tname\n" in block and "\tmessage\n" in block,
                failures, f"news group {index} missing name/message payload")

    # This is an ambient read-only consumer. Reject directive-shaped state or gameplay mutations,
    # while ignoring ordinary prose inside backtick-quoted News text.
    directive_patterns = (
        r'^\s*action(?:\s|$)', r'^\s*on show(?:\s|$)', r'^\s*set\s', r'^\s*clear\s',
        r'^\s*payment(?:\s|$)', r'^\s*give\s', r'^\s*take\s', r'^\s*destination(?:\s|$)',
        r'^\s*waypoint(?:\s|$)', r'^\s*objective(?:\s|$)', r'^\s*ship(?:\s|$)',
    )
    non_prose = "\n".join(line for line in text.splitlines() if "`" not in line)
    for pattern in directive_patterns:
        require(re.search(pattern, non_prose, re.MULTILINE) is None,
                failures, f"forbidden mutation/gameplay directive matched: {pattern}")

    require("world:" not in non_prose.lower(), failures, "reactive News must not consume or mutate world:* state")
    require("A2 Reactive News:" not in text, failures, "reactive News must not create shadow persistent state")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: A2 reactive-news structure validated")
    print("PASS: news_groups=3")
    print("PASS: inputs=Deep convoy completion, combat rating")
    print("PASS: scopes=Deep Republic history, Deep command veteran, non-station Republic veteran")
    print("PASS: persistence_model=read-only stock News conditions")
    print("PASS: mutations=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
