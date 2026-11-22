"""Refresh the data of the slide "Context Performance Benchmark" (genai_intro, bck_llm_context_benchmark).

Reads the public API of Context Arena (MRCR v2, 8 needles, full mode) and rewrites
modules/shared-blocks/static/_SHARED/csv/mrcr-line-chart-8-nee.csv. Run it before each edition:

    uv run python scripts/update_context_arena.py

One row per model and context bin. For each provider, only its best variant is kept (highest area under the
curve up to 1M tokens, then up to 128k). The slide shows the `featured` rows; the others stay in the legend,
one click away. Featured: Anthropic, OpenAI, Google, Mistral, plus the best open-weights provider in
OPEN_WEIGHTS (NG, 2026-11-22: "le meilleur par fournisseur").
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import sys
import urllib.request
from pathlib import Path

API = "https://contextarena.ai/api/needle-summary?needles=8"
OUT = (Path(__file__).resolve().parent.parent / "modules" / "shared-blocks" / "static" / "_SHARED" / "csv"
       / "mrcr-line-chart-8-nee.csv")
BINS = {8192: "8k", 16384: "16k", 32768: "32k", 65536: "64k",
        131072: "128k", 262144: "256k", 524288: "512k", 1048576: "1M"}
FEATURED = ["anthropic", "openai", "google", "mistralai"]
OPEN_WEIGHTS = ["qwen", "deepseek", "moonshotai", "z-ai", "meta"]   # best one of these is featured too
MAX_PROVIDERS = 12   # providers kept in the CSV (legend), best first


def _rank(m: dict) -> tuple[float, float]:
    o = m.get("overall_metrics") or {}
    return (o.get("auc_1m") or 0.0, o.get("auc_128k") or 0.0)


def main() -> int:
    req = urllib.request.Request(API, headers={"User-Agent": "ai4se6d-slides/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)

    best: dict[str, dict] = {}
    for m in data["models"]:
        provider = m["model_slug"].split("/", 1)[0]
        if provider not in best or _rank(m) > _rank(best[provider]):
            best[provider] = m
    providers = sorted(best, key=lambda p: _rank(best[p]), reverse=True)
    open_best = next((p for p in providers if p in OPEN_WEIGHTS), None)
    featured = set(FEATURED) | ({open_best} if open_best else set())
    kept = [p for p in providers if p in featured] + [p for p in providers if p not in featured]
    kept = kept[:max(MAX_PROVIDERS, len(featured))]

    today = dt.date.today().strftime("%B %Y")
    rows = []
    for p in kept:
        m = best[p]
        slug = m["model_slug"] + (f":{m['reasoning_mode']}" if m.get("reasoning_mode") else "")
        for b, label in BINS.items():
            bm = (m.get("bin_metrics") or {}).get(str(b))
            if not bm or bm.get("avg_score") is None or bm.get("is_incomplete"):
                continue
            rows.append({"model_slug": slug, "context_bin": label, "avg_score": f"{100 * bm['avg_score']:.2f}",
                         "featured": int(p in featured), "snapshot": today})

    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["model_slug", "context_bin", "avg_score", "featured", "snapshot"],
                           quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    print(f"{OUT}: {len(rows)} rows, {len(kept)} models, snapshot {today}")
    for p in kept:
        print(("  * " if p in featured else "    ") + best[p]["model_slug"], best[p].get("reasoning_mode") or "")
    return 0


if __name__ == "__main__":
    sys.exit(main())
