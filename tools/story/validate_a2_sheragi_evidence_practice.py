#!/usr/bin/env python3
from pathlib import Path

PATH = Path("data/sheragi/a2 sheragi evidence practice.txt")
TEXT = PATH.read_text(encoding="utf-8")


def require(fragment: str) -> None:
    if fragment not in TEXT:
        raise SystemExit(f"missing required fragment: {fragment!r}")


missions = [
    'mission "A2 Sheragi Evidence Practice: Reflection"',
    'mission "A2 Sheragi Evidence Practice: Later Reflection"',
]
for mission in missions:
    require(mission)

require('has "Sheragi Archaeology: Epilogue: done"')
require('"A2 Sheragi Evidence Practice: resolved" = 1')
require('"A2 Sheragi Evidence Practice: provenance" = 1')
require('"A2 Sheragi Evidence Practice: context" = 1')
require('"A2 Sheragi Evidence Practice: revision" = 1')
require('"A2 Sheragi Evidence Practice: local" = 1')
require('"A2 Sheragi Evidence Practice: reflection seen" = 1')

for branch in ("provenance", "context", "revision"):
    require(f"branch {branch}")
    require(f'has "A2 Sheragi Evidence Practice: {branch}"')

for forbidden in (
    '"Sheragi Archaeology: Epilogue: done" =',
    '"Sheragi Archaeology: Epilogue: done" +=',
    '"Sheragi Archaeology: Epilogue: done" -=',
    'world:',
):
    if forbidden in TEXT:
        raise SystemExit(f"forbidden authority write/reference: {forbidden!r}")

if TEXT.count('mission "A2 Sheragi Evidence Practice:') != 2:
    raise SystemExit("expected exactly two A2 Sheragi Evidence Practice missions")

if TEXT.count("\t\tchoice\n") != 1:
    raise SystemExit("expected exactly one primary player choice")

for phrase in (
    "does not present these habits as Sheragi doctrine",
    "modern human and Hai responses",
    "Nothing in the exchange makes you an archaeologist, curator, Hai official, or representative",
):
    require(phrase)

print("PASS: A2 Sheragi Evidence Practice")
print("missions=2 routes=4 later_reflections=4 b1_epilogue_read_only=true world_state_writes=0")
