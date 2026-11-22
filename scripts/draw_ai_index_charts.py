"""draw_ai_index_charts — the four "AI Index" charts of genai_intro (bck_llm_benchmarks), one image per language.

Method of streamtex-all-trainings (NG, 2026-11-22): the figures live in a JSON with their sources and the
selection rules (modules/shared-blocks/data/ai_index_scores.json, written by scripts/fetch_ai_index.py) and this
tool draws the images from it. Updating = refresh the JSON, then:

    uv run python scripts/draw_ai_index_charts.py

Charts: score, output tokens, cost per task (horizontal bars, one colour per main provider, the course model
outlined, ◆ = open weights) and score vs cost per task (log scale).
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "modules/shared-blocks/data/ai_index_scores.json"
OUT_DIR = ROOT / "modules/shared-blocks/static/_SHARED/images/diagrams/ai-index"
LANGS = ("en", "fr")

BG, TEXT, GRID, COURSE = "#0E1117", "#FAFAFA", "#2A3242", "#FFFFFF"
PROVIDER = {"Anthropic": "#F39C12", "OpenAI": "#2EC4B6", "Google": "#7AB8F5"}
OTHER = "#B8A9C9"
FONT = 22
#: Score vs cost: label position (dx, dy in points, horizontal alignment) for points too close to the others;
#: every other label goes above its point. Revisit after a data refresh if two labels overlap.
NUDGE = {
    "Gemini 4 Carbon": (-14, -16, "right"), "GPT-6.2 Astra": (-16, 6, "right"), "Claude Opus 5.5": (16, 4, "left"),
    "Claude Sonnet 5.5": (16, -10, "left"), "Kimi K3.1 Pro": (-16, 4, "right"),
    "Qwen4 Max": (0, -26, "center"), "DeepSeek V4.1 Flash 1017": (0, -28, "center"),
}


def _label(m: dict) -> str:
    return m["model"] + (" ◆" if m["open_weights"] else "")


def _color(m: dict) -> str:
    return PROVIDER.get(m["provider"], OTHER)


def _figure():
    plt.rcParams.update({"font.size": FONT, "text.color": TEXT, "axes.labelcolor": TEXT,
                         "xtick.color": TEXT, "ytick.color": TEXT})
    fig, ax = plt.subplots(figsize=(19.2, 8.6), dpi=100, facecolor=BG)
    ax.set_facecolor(BG)
    ax.grid(color=GRID, lw=1.2)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(False)
    return fig, ax


def _source(fig, d: dict, lang: str) -> None:
    months = sorted(m["released"] for m in d["models"])
    first, last = (dt.date.fromisoformat(x + "-01") for x in (months[0], months[-1]))
    window = f"{first:%b}–{last:%b %Y}"
    fig.text(0.01, 0.012, d["labels"]["source"][lang].format(window=window, updated=d["updated"]),
             fontsize=15, color="#9AA5AD")


def bars(d: dict, key: str, fmt: str, lang: str, out: Path) -> None:
    models = sorted(d["models"], key=lambda m: m[key], reverse=True)
    fig, ax = _figure()
    y = range(len(models))
    vals = [m[key] for m in models]
    ax.barh(y, vals, color=[_color(m) for m in models], height=0.75,
            edgecolor=[COURSE if m["course_model"] else "none" for m in models], linewidth=4)
    top = max(vals)
    for yi, (m, v) in enumerate(zip(models, vals)):
        text = fmt.format(v) + (f"   ← {d['labels']['course'][lang]}" if m["course_model"] else "")
        ax.text(v + top * 0.01, yi, text, va="center", fontsize=FONT, color=TEXT)
    ax.set_yticks(list(y))
    ax.set_yticklabels([_label(m) for m in models], fontsize=FONT)
    ax.invert_yaxis()
    ax.set_xlim(0, top * 1.35)
    ax.set_xlabel(d["labels"][key][lang], fontsize=FONT + 2)
    ax.grid(axis="y", visible=False)
    _source(fig, d, lang)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out, facecolor=BG)
    plt.close(fig)


def score_vs_cost(d: dict, lang: str, out: Path) -> None:
    models = d["models"]
    fig, ax = _figure()
    for m in models:
        ax.scatter(m["cost_per_task"], m["score"], s=420, color=_color(m), zorder=3,
                   edgecolors=COURSE if m["course_model"] else _color(m), linewidths=4)
        dx, dy, ha = NUDGE.get(m["model"], (0, 18, "center"))
        ax.annotate(_label(m), (m["cost_per_task"], m["score"]), textcoords="offset points",
                    xytext=(dx, dy), ha=ha, va="center" if dx else "bottom" if dy > 0 else "top",
                    fontsize=FONT - 4, color=TEXT)
    ax.set_xscale("log")
    ticks = [t for t in (0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50)
             if min(m["cost_per_task"] for m in models) / 1.5 <= t <= max(m["cost_per_task"] for m in models) * 1.5]
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"${t:g}" for t in ticks])
    ax.minorticks_off()
    ax.set_xlabel(d["labels"]["score_vs_cost"][lang] + "  — ← cheaper", fontsize=FONT + 2)
    ax.set_ylabel("Intelligence Index", fontsize=FONT + 2)
    scores = [m["score"] for m in models]
    ax.set_ylim(min(scores) - 6, max(scores) + 6)
    _source(fig, d, lang)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out, facecolor=BG)
    plt.close(fig)


def main() -> int:
    d = json.loads(DATA.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        jobs = [("ai-index-score", lambda o: bars(d, "score", "{:.0f}", lang, o)),
                ("ai-index-tokens", lambda o: bars(d, "output_tokens_m", "{:.0f}M", lang, o)),
                ("ai-index-cost", lambda o: bars(d, "cost_per_task", "${:.2f}", lang, o)),
                ("ai-index-score-vs-cost", lambda o: score_vs_cost(d, lang, o))]
        for name, job in jobs:
            out = OUT_DIR / f"{name}-{lang}.png"
            job(out)
            print(f"drawn: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
