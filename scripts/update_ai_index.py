"""Refresh the data of the "AI Index" slides (genai_intro, bck_llm_benchmarks).

Reads the public model pages of Artificial Analysis (https://artificialanalysis.ai/models/<slug>) in headless
Chrome and rewrites modules/shared-blocks/static/_SHARED/csv/ai-index.csv. Run it before each edition:

    uv run python scripts/update_ai_index.py

Artificial Analysis runs the same nine evaluations on every model itself, so its scores are comparable — the
reason it stays the source of the slides (NG, 2026-11-22). Edit MODELS to change the models shown: the slugs are
the last part of the model page URLs. COURSE_MODEL is highlighted on the charts.

Fair comparison (NG, 2026-11-22): only models of the same generation — released within WINDOW_MONTHS months,
counted back from the most recent release — and every model has a result on each of the nine evaluations of
the index (Artificial Analysis computes the index only then; checked test by test on 2026-11-22).
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = (Path(__file__).resolve().parent.parent / "modules" / "shared-blocks" / "static" / "_SHARED" / "csv"
       / "ai-index.csv")

# Frontier models of the main providers, plus the open-weights leaders and the course model.
MODELS = [
    "claude-fable-5-2", "gpt-6-2-astra", "gemini-4-neon", "gemini-4-carbon", "claude-opus-5-5",
    "gpt-6-2-sol", "claude-sonnet-5-5", "gemini-4-hydrogen", "kimi-k3-1-pro", "qwen4-max",
    "claude-haiku-5-5", "grok-4-7", "deepseek-v4-1-flash-1017", "glm-5-3", "gpt-6-luna", "mistral-large-4",
    "muse-wonder",
]
WINDOW_MONTHS = 3
COURSE_MODEL = "deepseek-v4-1-flash-1017"   # the model of the course (ai4se-kit opencode.base.json)

_NUM = r"([\d.,]+)"
_UNIT = {"K": 1e-3, "M": 1.0, "B": 1e3, "T": 1e6}   # → millions


def _millions(text: str) -> float:
    m = re.fullmatch(r"([\d.,]+)\s*([KMBT])?", text.strip())
    if not m:
        raise ValueError(text)
    return float(m.group(1).replace(",", "")) * _UNIT.get(m.group(2) or "M", 1.0)


def _after(lines: list[str], label: str, offset: int = -1) -> str:
    """The line at *offset* from the first line equal to *label*."""
    i = lines.index(label)
    return lines[i + offset]


def parse(slug: str, text: str) -> dict:
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    name = re.search(r"^(.+?): Intelligence, Performance & Price Analysis", text, re.M).group(1).strip()
    creator = lines[lines.index("All Releases") + 2]
    released = re.search(r"Released (\w+ \d{4})", text).group(1)
    return {
        "model": name,
        "slug": slug,
        "provider": creator,
        "score": int(_after(lines, "Artificial Analysis Intelligence Index")),
        "cost_per_task": float(_after(lines, "Cost per Intelligence Index task").lstrip("$").replace(",", "")),
        "output_tokens_m": round(_millions(_after(lines, "Output tokens from Intelligence Index")), 2),
        "input_tokens_m": round(_millions(re.search(r"Input tokens ([\d.,]+\s*[KMBT]?)", text).group(1)), 1),
        "minutes_per_task": float(_after(lines, "Time per Intelligence Index task (minutes)")),
        "price_in": float(re.search(r"^In \$" + _NUM, text, re.M).group(1)),
        "price_out": float(re.search(r"^Out \$" + _NUM, text, re.M).group(1)),
        "released": dt.datetime.strptime(released, "%B %Y").strftime("%Y-%m"),
        "open_weights": int("Open weights" in text[:2000] or "Open Weights" in text[:2000]),
        "course_model": int(slug == COURSE_MODEL),
    }


def main() -> int:
    rows, failed = [], []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        for slug in MODELS:
            page.goto(f"https://artificialanalysis.ai/models/{slug}", wait_until="domcontentloaded", timeout=90000)
            page.wait_for_timeout(6000)
            try:
                rows.append(parse(slug, page.inner_text("body")))
                r = rows[-1]
                print(f"  {r['model'][:40]:40s} {r['score']:3d}  ${r['cost_per_task']:<7} {r['output_tokens_m']}M out  {r['released']}")
            except Exception as e:   # page layout changed: report, keep going
                failed.append(slug)
                print(f"  FAILED {slug}: {e!r}")
        browser.close()
    if not rows:
        return 1
    newest = max(r["released"] for r in rows)
    y, m = map(int, newest.split("-"))
    m -= WINDOW_MONTHS - 1
    while m < 1:
        y, m = y - 1, m + 12
    start = f"{y:04d}-{m:02d}"
    dropped = [r["model"] for r in rows if r["released"] < start]
    rows = [r for r in rows if r["released"] >= start]
    print(f"Same generation: released {start} .. {newest}" + (f" — left out: {', '.join(dropped)}" if dropped else ""))
    snapshot = dt.date.today().strftime("%B %Y")
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[*rows[0].keys(), "snapshot"], quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in sorted(rows, key=lambda r: -r["score"]):
            w.writerow({**r, "snapshot": snapshot})
    print(f"{OUT}: {len(rows)} models, snapshot {snapshot}" + (f" — FAILED: {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
