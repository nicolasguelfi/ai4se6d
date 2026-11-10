"""Print exercise sheets as syllabus Markdown — the same source as the slides.

The sheets live in modules/shared-blocks/exercise_sheets.py. The slides render them through
modules/shared-blocks/exercise_sheet.py; this script renders them for the course kit syllabus
(ai4se-kit/syllabus/hdNN-*.md), so a sheet is written once.

Usage: uv run python scripts/sheets_markdown.py discover plan requirements
       uv run python scripts/sheets_markdown.py --all
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "modules" / "shared-blocks"))

from exercise_sheets import SHEETS  # noqa: E402


def to_markdown(key: str) -> str:
    sh = SHEETS[key]
    lines = [
        f"### Exercise — {sh['title']} ({sh['time']})",
        "",
        f"*{sh['cycle']}*",
        "",
        f"**Goal:** {sh['goal']}",
        "",
        "**Steps:**",
        "",
    ]
    lines += [f"{i}. {step}" for i, step in enumerate(sh["steps"], 1)]
    lines += ["", f"**Done when:** {sh['done_when']}", ""]
    if sh.get("midpoint"):
        lines += [f"**Mid-point:** {sh['midpoint']}", ""]
    lines += [f"**If stuck:** {sh['if_stuck']}", "", f"**Debrief:** {sh['debrief']}", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("keys", nargs="*")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    keys = list(SHEETS) if args.all else args.keys
    unknown = [k for k in keys if k not in SHEETS]
    if unknown or not keys:
        sys.stderr.write(f"unknown or missing keys: {unknown}; known: {', '.join(SHEETS)}\n")
        return 2
    sys.stdout.write("\n".join(to_markdown(k) for k in keys))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
