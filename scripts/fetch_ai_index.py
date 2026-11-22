"""fetch_ai_index — the figures of the four "AI Index" charts, written to modules/shared-blocks/data/.

Aligned on streamtex-all-trainings (NG, 2026-11-22): the figures live in a JSON that carries their source and the
selection rules (modules/shared-blocks/data/ai_index_scores.json), and scripts/draw_ai_index_charts.py draws the
images from it, as draw_context_chart.py does for the context chart.

Source: the public model pages of Artificial Analysis (https://artificialanalysis.ai/models/<slug>), read in
headless Chrome. Artificial Analysis runs the same nine evaluations on every model itself, so its scores are
comparable. Selection rules (NG, 2026-11-22):
- same generation: models released within WINDOW_MONTHS months, counted back from the most recent release;
- complete results: each model appears on the page of each of the nine evaluations of the index.

    uv run python scripts/fetch_ai_index.py      # then: uv run python scripts/draw_ai_index_charts.py

To change the models: edit MODELS (slugs = last part of the model page URLs), rerun, read what is printed, check the
JSON (git diff), then draw. COURSE_MODEL is outlined on the charts.
"""
from __future__ import annotations

import json
import datetime as dt
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent.parent / "modules/shared-blocks/data/ai_index_scores.json"
INDEX = "Artificial Analysis Intelligence Index v5.0.1"
EVALS = {   # the nine evaluations of the index: page slug -> name
    "aa-briefcase": "AA-Briefcase v1.1", "automationbench-aa": "AutomationBench-AA",
    "terminalbench-4-0": "Terminal-Bench 4.0", "frontiercode-2-0": "FrontierCode-AA 2.0",
    "omniscience": "AA-Omniscience v1.1", "gdp-pdf": "GDP.pdf", "hle-diamond": "HLE-Diamond",
    "critpt-v2": "CritPt v2 (Hard Subset)", "terminal-bench-science": "Terminal-Bench-Science 0.1",
}

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
        # rule "complete results": the model is listed on the page of each of the nine evaluations
        missing: dict[str, list[str]] = {}
        for ev, ev_name in EVALS.items():
            page.goto(f"https://artificialanalysis.ai/evaluations/{ev}?model-filters=frontier-model",
                      wait_until="domcontentloaded", timeout=90000)
            page.wait_for_timeout(6000)
            text = page.inner_text("body")
            for r in rows:
                if r["model"].split(" (")[0] not in text:
                    missing.setdefault(r["model"], []).append(ev_name)
        browser.close()
    if not rows:
        return 1
    left_out = [f"{m} left out: no result on {', '.join(evs)}." for m, evs in missing.items()]
    rows = [r for r in rows if r["model"] not in missing]
    # rule "same generation"
    newest = max(r["released"] for r in rows)
    y, m = map(int, newest.split("-"))
    m -= WINDOW_MONTHS - 1
    while m < 1:
        y, m = y - 1, m + 12
    start = f"{y:04d}-{m:02d}"
    left_out += [f"{r['model']} left out: released {r['released']}, outside the generation window "
                 f"({start} .. {newest})." for r in rows if r["released"] < start]
    rows = sorted((r for r in rows if r["released"] >= start), key=lambda r: -r["score"])

    out = {
        "title": {"en": f"{INDEX} — models of the same generation",
                  "fr": f"{INDEX} — modèles de la même génération"},
        "updated": dt.date.today().isoformat(),
        "decision": "NG 2026-11-22: charts drawn from data (no screenshots), aligned on streamtex-all-trainings; "
                    "same generation (3 months) and complete results (nine evaluations)",
        "benchmark": {
            "name": INDEX,
            "method": "Composite of nine evaluations run by Artificial Analysis on every model: "
                      + ", ".join(EVALS.values()) + ".",
            "metric": "index score (0-100); cost per task = weighted average USD cost of one index task; output "
                      "tokens = tokens generated to run the whole index (answers, tool calls, reasoning); input "
                      "tokens = tokens sent, re-sent at every turn of the agent loop",
            "measures": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index",
            "measured_by": "Artificial Analysis, third party, same harness for every model",
            "notes": [
                f"Same generation: models released {start} .. {newest}.",
                "Complete results: each model is listed on the page of each of the nine evaluations.",
                *left_out,
                f"Course model: {next((r['model'] for r in rows if r['course_model']), 'none')} (outlined).",
                "◆ = open weights.",
            ],
        },
        "models": rows,
        "labels": {
            "score": {"en": "Artificial Analysis Intelligence Index (9 evaluations)",
                      "fr": "Indice d'intelligence Artificial Analysis (9 évaluations)"},
            "output_tokens_m": {"en": "Output tokens to run the index (millions)",
                                "fr": "Tokens générés pour passer l'indice (millions)"},
            "cost_per_task": {"en": "Average cost of one index task (USD)",
                              "fr": "Coût moyen d'une tâche de l'indice (USD)"},
            "score_vs_cost": {"en": "Cost per task (USD, log scale)", "fr": "Coût par tâche (USD, échelle log)"},
            "course": {"en": "course model", "fr": "modèle du cours"},
            "source": {"en": "Source: Artificial Analysis, Intelligence Index v5.0.1 — models released {window}, "
                             "read on {updated} · ◆ open weights",
                       "fr": "Source : Artificial Analysis, Intelligence Index v5.0.1 — modèles sortis {window}, "
                             "relevé du {updated} · ◆ poids ouverts"},
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{OUT}: {len(rows)} models")
    for note in left_out:
        print("  " + note)
    if failed:
        print(f"  FAILED (page layout changed?): {', '.join(failed)}")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
