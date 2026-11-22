"""fetch_context_arena — the figures of the "context length" chart, written to modules/shared-blocks/data/.

Method of streamtex-all-trainings (NG, 2026-11-22): the figures live in a JSON with their sources and the
selection rules (as content/llm/context_length_scores.json there, rule m1: for each model, the highest reasoning
effort measured), and scripts/draw_context_chart.py draws the ai4se6d chart from it. Added for ai4se6d (NG, 2026-11-22): the models compared are of the same
generation (put online within WINDOW_DAYS of each other) and each has a result at every length up to
COMPLETE_UP_TO tokens; the script leaves out, with the reason, those that do not meet both rules.

    uv run python scripts/fetch_context_arena.py      # then: uv run python scripts/draw_context_chart.py

To change the models: edit SELECTION (one recent model per provider), rerun, read what is printed, check the
JSON (git diff), then draw. The script also lists, per provider, models newer than the one selected.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "modules/shared-blocks/data/context_length_scores.json"
API = "https://contextarena.ai/api/needle-summary?needles=8"
EFFORT = ["max", "xhigh", "high", "medium", "low", "enabled"]   # rule m1: the first one measured
BINS = [8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
WINDOW_DAYS = 92               # same generation: about three months between the first and the last model
COMPLETE_UP_TO = 524288        # every model must have a score at each length up to this one (1M: Gemini only)

#: (slug, name, provider) — one recent model per provider; the rules below may still leave one out.
SELECTION = [
    ("openai/gpt-5.6-sol", "GPT-5.6 Sol", "OpenAI"),
    ("anthropic/claude-opus-5", "Claude Opus 5", "Anthropic"),
    ("google/gemini-3.7-flash", "Gemini 3.7 Flash", "Google"),
    ("x-ai/grok-4.6", "Grok 4.6", "xAI"),
    ("deepseek/deepseek-v4-pro-0813", "DeepSeek V4 Pro", "DeepSeek"),
    ("qwen/qwen3.8-max", "Qwen 3.8 Max", "Alibaba"),
    ("mistralai/mistral-medium-3.5", "Mistral Medium 3.5", "Mistral"),
]


def _fetch() -> dict:
    req = urllib.request.Request(API, headers={"User-Agent": "ai4se6d-slides/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def _best_effort(rows: list[dict]) -> dict:
    measured = [r for r in rows if (r.get("reasoning_mode") or "") in EFFORT]
    return sorted(measured, key=lambda r: EFFORT.index(r["reasoning_mode"]))[0] if measured else rows[0]


def main() -> int:
    data = _fetch()
    by_slug: dict[str, list[dict]] = {}
    for m in data["models"]:
        by_slug.setdefault(m["model_slug"], []).append(m)

    candidates = []
    for slug, name, provider in SELECTION:
        r = _best_effort(by_slug[slug])
        bins = r.get("bin_metrics") or {}
        scores = [round(100 * bins[str(b)]["avg_score"], 1) if str(b) in bins and bins[str(b)].get("avg_score")
                  is not None and not bins[str(b)].get("is_incomplete") else None for b in BINS]
        tests = [bins[str(b)].get("n_tests") if str(b) in bins else None for b in BINS]
        candidates.append({
            "model": name, "provider": provider, "slug": slug, "reasoning": r.get("reasoning_mode") or "none",
            "online": (r.get("api_created_at") or "")[:10], "latest_run": (r.get("latest_run_timestamp") or "")[:10],
            "scores": scores, "tests": tests,
        })

    # rule "same generation": a window ending at the most recent model
    newest = max(dt.date.fromisoformat(c["online"]) for c in candidates)
    start = newest - dt.timedelta(days=WINDOW_DAYS)
    left_out, series = [], []
    for c in candidates:
        online = dt.date.fromisoformat(c["online"])
        missing = [b for b, v in zip(BINS, c["scores"]) if b <= COMPLETE_UP_TO and v is None]
        if online < start:
            left_out.append(f"{c['model']} left out: online {c['online']}, outside the generation window "
                            f"({start} .. {newest}).")
        elif missing:
            left_out.append(f"{c['model']} left out: no score at {', '.join(f'{b // 1024}K' for b in missing)} "
                            f"(every model must be measured at each length up to {COMPLETE_UP_TO // 1024}K).")
        else:
            series.append(c)

    out = {
        "title": {"en": "LLM reliability as the context grows — GDM-MRCR v2, 8 needles (Context Arena)",
                  "fr": "Fiabilité des LLM quand le contexte s'allonge — GDM-MRCR v2, 8 aiguilles (Context Arena)"},
        "updated": dt.date.today().isoformat(),
        "decision": "method of streamtex-all-trainings (data JSON with sources + drawing tool, rule m1); "
                    "ai4se6d chart design kept; same-generation and complete-results rules (NG 2026-11-22)",
        "benchmark": {
            "name": "GDM-MRCR v2, 8 needles",
            "method": "Multi-round co-reference resolution: a long fictional conversation in which the user made "
                      "exactly the same request 8 times (« write a poem about tapirs ») and received a different "
                      "answer each time, among dozens of similar requests with other formats, topics or styles; at "
                      "the end the model must reproduce the n-th of the 8 answers (e.g. the 3rd poem about tapirs), "
                      "preceded by a random string. Same task at every length: only the surrounding conversation grows.",
            "metric": "mean similarity to the reference answer (0-100), not a right/wrong accuracy",
            "chance_level": 15,
            "chance_source": "Google DeepMind, eval_hub mrcr_v2 README: guessing among the needles scores about 15 % "
                             "with 8 needles",
            "dataset": "https://github.com/google-deepmind/eval_hub/tree/master/eval_hub/mrcr_v2",
            "measures": "https://contextarena.ai",
            "api": API,
            "measured_by": "Dillon Uzar (Context Arena), third party, same harness for every model",
            "bins_note": "a bin is named by its upper bound: 8K = (4K, 8K] tokens … 1M = (512K, 1M]",
            "notes": [
                "Rule m1: for each model, the highest reasoning effort measured.",
                f"Same generation: models put online between {start} and {newest} (about three months).",
                f"Complete results: a score at every length up to {COMPLETE_UP_TO // 1024}K tokens.",
                *left_out,
                "Above 512K only Gemini has a point (the 1M prompts do not fit the other models' windows).",
            ],
        },
        "bins": BINS,
        "charts": {"providers": {"file": "context-length", "series": series}},
        "labels": {
            "title": {"en": "Performance vs Context Size (MRCR — 8 Needles)",
                      "fr": "Performance selon la taille du contexte (MRCR — 8 aiguilles)"},
            "x": {"en": "Context Size", "fr": "Taille du contexte"},
            "y": {"en": "MRCR Score (%)", "fr": "Score MRCR (%)"},
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"{OUT}")
    for s in series:
        print(f"  {s['model']:20s} {s['reasoning']:6s} online {s['online']}  {s['scores']}")
    for note in left_out:
        print("  " + note)
    # what is newer than the selection, per provider (to review SELECTION next time)
    chosen = {slug: dt.date.fromisoformat(_best_effort(by_slug[slug]).get("api_created_at", "")[:10] or "1970-01-01")
              for slug, _, _ in SELECTION}
    for slug, rows in by_slug.items():
        prov = slug.split("/")[0]
        mine = [d for s, d in chosen.items() if s.startswith(prov + "/")]
        created = (rows[0].get("api_created_at") or "")[:10]
        if mine and created and dt.date.fromisoformat(created) > max(mine):
            print(f"  newer on Context Arena: {slug} (online {created})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
