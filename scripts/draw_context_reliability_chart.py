"""draw_context_reliability_chart — the two all-trainings charts "reliability vs context length", per language.

Copy of streamtex-all-trainings/_project/tools/draw_context_chart.py (planche contexte1), added to ai4se6d by NG on
2026-11-22: these two charts follow the ai4se6d "Context Performance Benchmark" slide (block
bck_llm_context_reliability). Changes: the dark palette is written here (trainings_pack.palette.DARK), the data
and images live in the ai4se6d shared folders, and there is no media manifest. Updating = change
modules/shared-blocks/data/context_reliability_scores.json, then:

    uv run python scripts/draw_context_reliability_chart.py
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "modules/shared-blocks/data/context_reliability_scores.json"
OUT_DIR = ROOT / "modules/shared-blocks/static/_SHARED/images/diagrams/context-reliability"
LANGS = ("en", "fr")
#: streamtex-all-trainings trainings_pack.palette.DARK (the keys used here)
DARK = {"bg": "#14171F", "body": "#F2EEE6", "muted": "#9AA5AD", "row_2": "#2A3242"}

#: Une teinte par fournisseur, lisible sur le fond de projection, et un marqueur chacun.
PROVIDER = {"OpenAI": ("#4FD8C9", "o"), "Anthropic": ("#EE9187", "s"), "Google": ("#8FC3F7", "D"),
            "xAI": ("#B9C2CC", "^"), "DeepSeek": ("#C792EA", "v"), "Alibaba": ("#F7B23B", "P"),
            "Mistral": ("#9BE36B", "X")}


def pages(tokens: int, d: dict) -> str:
    """Un équivalent en pages, arrondi à deux chiffres significatifs (≈ 12, 25, 50 … 1 600)."""
    p = tokens * d["pages"]["words_per_token"] / d["pages"]["words_per_page"]
    r = float(f"{p:.2g}")
    return f"{int(r):,}".replace(",", " ")


def tick(tokens: int) -> str:
    return f"{tokens // 1048576}M" if tokens >= 1048576 else f"{tokens // 1024}K"


def draw(d: dict, chart: dict, lang: str, out: Path) -> None:
    lab = {k: v[lang] for k, v in d["labels"].items()}
    # l'axe s'arrête à la dernière tranche mesurée du graphique
    last = max(i for s in chart["series"] for i, v in enumerate(s["scores"]) if v is not None)
    bins = d["bins"][:last + 1]
    plt.rcParams.update({"font.size": 20, "text.color": DARK["body"], "axes.labelcolor": DARK["body"],
                         "xtick.color": DARK["body"], "ytick.color": DARK["body"]})
    fig, ax = plt.subplots(figsize=(16, 8.4), dpi=120, facecolor=DARK["bg"])
    ax.set_facecolor(DARK["bg"])
    used = {}
    for s in chart["series"]:
        color, marker = PROVIDER[s["provider"]]
        dashed = s["reasoning"] == "none"
        n = used.setdefault(s["provider"], 0)
        used[s["provider"]] += 1
        if n:                                    # deuxième courbe d'un même fournisseur : autre marqueur
            marker = "s"
        pts = [(b, v) for b, v in zip(bins, s["scores"][:len(bins)]) if v is not None]
        name = s["label"][lang] if "label" in s else f'{s["model"]} ({s["provider"]})'
        ax.plot(*zip(*pts), "--" if dashed else "-", color=color, marker=marker, ms=13, lw=4, label=name)
    ax.axhline(d["benchmark"]["chance_level"], color=DARK["muted"], lw=2, ls=":")
    ax.text(bins[0] * 0.93, d["benchmark"]["chance_level"] + 2.5, lab["chance"], color=DARK["muted"], fontsize=18)
    ax.set_xscale("log", base=2)
    ax.set_xticks(bins)
    ax.set_xticklabels([f"{tick(b)}\n{pages(b, d)} {lab['pages']}" for b in bins], fontsize=17)
    ax.minorticks_off()
    ax.set_xlim(bins[0] * 0.8, bins[-1] * 1.25)
    ax.set_ylim(0, 103)
    ax.set_ylabel(lab["y"], fontsize=22)
    ax.set_xlabel(lab["x"], fontsize=22)
    ax.grid(color=DARK["row_2"], lw=1.2)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(DARK["muted"])
    # la légende : à droite (beaucoup de courbes) ou au-dessus (deux courbes aux noms longs) — `legend` du JSON
    where = {"right": dict(loc="center left", bbox_to_anchor=(1.01, 0.5), ncol=1),
             "top": dict(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2)}[chart.get("legend", "right")]
    ax.legend(frameon=False, fontsize=19, labelcolor=DARK["body"], handlelength=2.6, **where)
    run = max(s["latest_run"] for s in chart["series"])
    fig.text(0.01, 0.012, lab["source"].format(run=run), fontsize=14, color=DARK["muted"])
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out, facecolor=DARK["bg"])
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
