"""draw_context_chart — the ai4se6d chart "Performance vs Context Size (MRCR — 8 Needles)", one image per language.

Method of streamtex-all-trainings (NG, 2026-11-22): the figures live in a JSON with their sources
(modules/shared-blocks/data/context_length_scores.json, written by scripts/fetch_context_arena.py) and this tool
draws the image from it. The chart itself is the ai4se6d one (same title, axes, value labels and colours as the
former interactive chart of bck_llm_context_benchmark), not the all-trainings one. Updating = refresh the JSON, then:

    uv run python scripts/draw_context_chart.py
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "modules/shared-blocks/data/context_length_scores.json"
OUT_DIR = ROOT / "modules/shared-blocks/static/_SHARED/images/diagrams/context-length"
LANGS = ("en", "fr")

BG, TEXT, GRID = "#0E1117", "#FAFAFA", "#2A3242"        # the former chart's dark template
COLORS = ["#00D4AA", "#FF6B6B", "#FFE66D", "#7AB8F5", "#F39C12", "#B8A9C9", "#A8E6CF", "#FF8B94"]


def tick(tokens: int) -> str:
    return f"{tokens // 1048576}M" if tokens >= 1048576 else f"{tokens // 1024}k"


def draw(d: dict, chart: dict, lang: str, out: Path) -> None:
    lab = {k: v[lang] for k, v in d["labels"].items()}
    bins = d["bins"]
    x = list(range(len(bins)))
    plt.rcParams.update({"font.size": 22, "text.color": TEXT, "axes.labelcolor": TEXT,
                         "xtick.color": TEXT, "ytick.color": TEXT})
    fig, ax = plt.subplots(figsize=(19.2, 9.0), dpi=100, facecolor=BG)
    ax.set_facecolor(BG)
    for i, s in enumerate(chart["series"]):
        color = COLORS[i % len(COLORS)]
        pts = [(xi, v) for xi, v in zip(x, s["scores"]) if v is not None]
        ax.plot(*zip(*pts), "-o", color=color, lw=6, ms=20, label=f'{s["provider"]} — {s["model"]}')
        for xi, v in pts:
            ax.annotate(f"{v:.0f}", (xi, v), textcoords="offset points", xytext=(0, 16), ha="center",
                        fontsize=20, color=color)
    ax.set_title(lab["title"], fontsize=36, color=TEXT, pad=24)
    ax.set_xticks(x)
    ax.set_xticklabels([tick(b) for b in bins], fontsize=26)
    ax.set_xlim(-0.4, len(bins) - 0.6)
    ax.set_ylim(0, 105)
    ax.set_yticks(range(0, 101, 10))
    ax.tick_params(axis="y", labelsize=24)
    ax.set_xlabel(lab["x"], fontsize=30)
    ax.set_ylabel(lab["y"], fontsize=30)
    ax.grid(color=GRID, lw=1.2)
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=22, labelcolor=TEXT,
              facecolor="#1A1A2E", edgecolor="#333333", framealpha=0.8)
    fig.tight_layout()
    fig.savefig(out, facecolor=BG)
    plt.close(fig)


def main() -> int:
    d = json.loads(DATA.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for chart in d["charts"].values():
        for lang in LANGS:
            out = OUT_DIR / f'{chart["file"]}-{lang}.png'
            draw(d, chart, lang, out)
            print(f"drawn: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
