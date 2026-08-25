#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/a2 displacement relief liaison restage.txt"
text = PATH.read_text(encoding="utf-8")

MISSION_PREFIX = "A2 Displacement Relief Liaison:"
A1_STATES = (
    "world: republic displacement relief spillover active",
    "world: republic displacement pressure",
    "world: free worlds relief demand",
)

required = [
    'mission "A2 Displacement Relief Liaison: Cross-Border Briefing"',
    'mission "A2 Displacement Relief Liaison: Review"',
    'has "world: republic displacement relief spillover active"',
    'not "world: republic displacement relief spillover active"',
    '"world: republic displacement pressure" >= 4',
    '"world: republic displacement pressure" < 4',
    '"A2 Displacement Relief Liaison: bounded provenance" = 1',
    '"A2 Displacement Relief Liaison: aggregate only" = 1',
    '"A2 Displacement Relief Liaison: consent led" = 1',
    '"A2 Displacement Relief Liaison: refused" = 1',
    'branch refused',
    'has "A2 Displacement Relief Liaison: refused"',
    'label refused',
    '"A2 Displacement Relief Liaison: refusal respected" = 1',
    '"A2 Displacement Relief Liaison: followup pending" = 0',
    '"A2 Displacement Relief Liaison: followup seen" = 1',
]
missing = [token for token in required if token not in text]
if missing:
    raise SystemExit("missing required tokens: " + repr(missing))

if text.count(f'mission "{MISSION_PREFIX}') != 2:
    raise SystemExit("expected exactly two A2 liaison missions")

if text.count('"offer precedence" 9') != 2:
    raise SystemExit("both state-only missions must use offer precedence 9")

# Four Briefing choices converge to four explicit labels.
for route in ("bounded", "aggregate", "consent", "refuse"):
    if text.count(f"goto {route}") != 1:
        raise SystemExit(f"expected exactly one briefing goto for {route}")
    if text.count(f"label {route}") < 1:
        raise SystemExit(f"missing briefing label for {route}")

# Every Review route is explicit. No refusal or positive outcome may depend on fallthrough.
review_labels = (
    "bounded_high",
    "bounded_low",
    "aggregate_high",
    "aggregate_low",
    "consent_high",
    "consent_low",
    "refused",
)
for label in review_labels:
    if f"branch {label}" not in text:
        raise SystemExit(f"missing explicit review branch: {label}")
    if f"label {label}" not in text:
        raise SystemExit(f"missing explicit review label: {label}")

# Seven Review routes must all converge through the declared finish label.
if text.count("goto finish") != 7:
    raise SystemExit(f"expected seven explicit review goto finish paths, got {text.count('goto finish')}")
if text.count("label finish") != 1:
    raise SystemExit("expected one declared finish label")

outcomes = re.findall(
    r'"A2 Displacement Relief Liaison: (?:bounded|aggregate|consent) pressure (?:persists|eased)" = 1',
    text,
)
if len(outcomes) != 6 or len(set(outcomes)) != 6:
    raise SystemExit(f"expected six distinct simulation-sensitive positive outcomes, got {len(set(outcomes))}")

# State-only lifecycle: four briefing terminals + one review terminal, all decline.
if len(re.findall(r"^\s*decline\s*$", text, re.MULTILINE)) != 5:
    raise SystemExit("expected exactly five state-only decline terminals")
if re.search(r"^\s*accept\s*$", text, re.MULTILINE):
    raise SystemExit("state-only liaison missions must not use accept")

# No objective-bearing or material/gameplay mutation directives belong in this state-only slice.
for directive in (
    "destination ",
    "waypoint ",
    "stopover ",
    "cargo ",
    "passengers ",
    "outfit ",
    "ship ",
    "fleet ",
    "credits ",
    "payment ",
    "reputation ",
):
    if re.search(rf"^\s*{re.escape(directive)}", text, re.MULTILINE):
        raise SystemExit(f"unexpected gameplay directive: {directive.strip()}")

# A2 may read these A1-owned states but must never mutate them.
for state in A1_STATES:
    mutation = re.compile(
        rf'^\s*"{re.escape(state)}"\s*(?:=|\+=|-=|\?=|<\?=|>\?=)',
        re.MULTILINE,
    )
    if mutation.search(text):
        raise SystemExit(f"illegal A1-state write: {state}")

# Every assignment must remain inside the A2 liaison namespace.
for match in re.finditer(r'^\s*"([^"]+)"\s*(?:=|\+=|-=|\?=|<\?=|>\?=)', text, re.MULTILINE):
    state = match.group(1)
    if not state.startswith(MISSION_PREFIX):
        raise SystemExit(f"write outside A2 liaison namespace: {state}")

# Preserve the core consent/privacy boundary in player-facing text.
for phrase in (
    "keep individual arrivals anonymous",
    "do not attach a political origin to individual cases",
    "unless an arrival asks for the connection to be recorded",
    "declined rather than treating silence as permission",
    "Nobody converted it into a documentation policy",
):
    if phrase not in text:
        raise SystemExit(f"missing consent/privacy continuity phrase: {phrase}")

if not text.endswith("\n"):
    raise SystemExit("production file must end with newline")

print(
    "PASS: A2 displacement relief liaison current-main restage; "
    "2 missions, 3 positive policies + refusal, 6 pressure-sensitive outcomes, "
    "explicit refusal gating, A1 read-only, state-only decline lifecycle"
)
