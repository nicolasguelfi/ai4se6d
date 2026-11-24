"""Slides — Artificial Analysis Intelligence Index: five charts drawn from data (score, output tokens, cost per task, score vs cost, coding benchmarks).

Method of streamtex-all-trainings (NG, 2026-11-22): the figures live in a JSON with their sources and the
selection rules (modules/shared-blocks/data/ai_index_scores.json) and the images are drawn from it:

    uv run python scripts/fetch_ai_index.py          # refresh the JSON (same generation, complete results)
    uv run python scripts/draw_ai_index_charts.py    # redraw _SHARED/images/diagrams/ai-index/*.png

Fair comparison: only models of the same generation (released within three months) and with a result on each
of the nine evaluations of the index. The fourth view is score vs. cost per task: with a single generation, the
former "score vs. release date" view no longer says anything.
"""
# @guideline: maximize-viewport
import json
from pathlib import Path

from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_IMAGES = "_SHARED/images/diagrams/ai-index"
# Bar charts drawn natively from the JSON (NG, 2026-11-24: readable in dark mode and in a large room); the
# score-vs-cost scatter stays an image (scripts/draw_ai_index_charts.py).
_DATA = json.loads((Path(__file__).resolve().parents[2] / "shared-blocks/data/ai_index_scores.json")
                   .read_text(encoding="utf-8"))
_PROVIDER = {"Anthropic": "#F39C12", "OpenAI": "#2EC4B6", "Google": "#7AB8F5"}   # same colours as the images
_OTHER = "#B8A9C9"
_CHART_ZOOM = 52    # 16 rows; tuned by measure (content bottom <= 1000 px at 1920x1080)
_BAR_MAX = 78       # % of the bar cell taken by the longest bar (room left for the value)

# Title + chart + source fill the screen: each slide top-aligned, without the st_slide top margin.
_slide_top = Style("justify-content:flex-start;margin-top:0;", "aiidx_slide_top")


class BlockStyles:
    """Benchmark slides styles."""
    heading = s.project.titles.slide_title + s.center_txt
    source = s.project.citation + s.large + s.center_txt
    model = Style.create(s.project.titles.body + Style("text-align: right; white-space: nowrap;", "aiidx_right"),
                         "aiidx_model")
    value = Style.create(s.project.titles.body + Style("white-space: nowrap; width: 100%;", "aiidx_nowrap"), "aiidx_value")
    axis = Style.create(s.project.titles.caption + s.center_txt, "aiidx_axis")
    course = Style.create(s.bold + s.project.colors.highlight, "aiidx_course")
    cell = Style("display: flex; align-items: center; gap: 0.6vw; width: 100%;", "aiidx_bar_cell")
bs = BlockStyles


def _colour(m):
    return _PROVIDER.get(m["provider"], _OTHER)


def _bar(m, key, top, tag):
    """One bar: width proportional to the value; the course model is outlined in the text colour."""
    width = _BAR_MAX * m[key] / top
    outline = " outline: 4px solid currentColor;" if m["course_model"] else ""
    return Style(f"display: inline-block; width: {width:.1f}%; height: 1.1em; border-radius: 4px; "
                 f"background-color: {_colour(m)};{outline}", f"aiidx_bar_{tag}_{m['slug']}")


def _name(m):
    return m["model"] + (" ◆" if m["open_weights"] else "")


def _legend():
    parts = []
    for name, colour in [*_PROVIDER.items(), ("other", _OTHER)]:
        parts += [(Style(f"color: {colour};", f"aiidx_lg_{name}"), "■ "), name, "   "]
    parts += ["◆ open weights   ", (bs.course, "outlined"), " = course model"]
    st_write(bs.axis, *parts, tag=t.div)


def _bars(key, fmt, label_key):
    """Horizontal bar chart of one JSON field, models sorted by value (as the old image)."""
    models = sorted(_DATA["models"], key=lambda m: m[key], reverse=True)
    top = max(m[key] for m in models)
    with st_zoom(_CHART_ZOOM):
        with st_grid(cols="30% 70%", gap="0.5vh 1vw",
                     cell_styles=[s.project.containers.grid_cell_centered, bs.cell] * len(models)) as g:
            for m in models:
                with g.cell():
                    st_write(bs.model, _name(m), tag=t.div)
                with g.cell():
                    extra = [(bs.course, "  ← course model")] if m["course_model"] else []
                    st_write(bs.value, (_bar(m, key, top, key), "\u00a0"), "  " + fmt.format(m[key]), *extra,
                             tag=t.div)
        st_space("v", "1vh")
        st_write(bs.axis, _DATA["labels"][label_key]["en"], tag=t.div)
        _legend()


def _coding():
    """The two coding evaluations side by side, same model order (mean of the two), as the old image."""
    keys = ["terminal_bench_4", "frontiercode_2"]
    models = sorted(_DATA["models"], key=lambda m: -(m[keys[0]] + m[keys[1]]))
    with st_zoom(_CHART_ZOOM):
        cells = [s.project.containers.grid_cell_centered, bs.cell, bs.cell]
        with st_grid(cols="26% 37% 37%", gap="0.5vh 1vw", cell_styles=cells * (len(models) + 1)) as g:
            with g.cell():
                pass
            for k in keys:
                with g.cell():
                    st_write(bs.axis, _DATA["labels"][k]["en"], tag=t.div)
            for m in models:
                with g.cell():
                    st_write(bs.model, _name(m), tag=t.div)
                for k in keys:
                    with g.cell():
                        st_write(bs.value, (_bar(m, k, 80, k), "\u00a0"), f"  {m[k]:.0f}%", tag=t.div)
        st_space("v", "1vh")
        _legend()


_TOKEN_ENTRIES = [
    ("Output tokens (chart)", "Tokens the model generated to run the whole index: its visible answers, tool calls "
                              "and, for reasoning models, its internal thinking."),
    ("Input tokens", "Tokens sent to the model at each turn of the agent loop — prompt, conversation history and "
                     "tool results, re-sent every turn. Often 100x the output: this is what you pay for."),
    ("Reading it", "A verbose model costs more and takes longer per task, even at the same price per token."),
]

_CODING_ENTRIES = [
    ("What the chart shows",
     "The two coding evaluations inside the index, for the same 16 models (same generation, released Sep–Nov 2026), "
     "measured by Artificial Analysis itself with the same harness for every model. Models are ordered by the mean "
     "of the two scores."),
    ("Terminal-Bench 4.0 — what it measures",
     "Can an agent finish real work in a terminal? 66 hard tasks across software, machine learning, science, "
     "operations, security, hardware and media — e.g. migrate a live API from MySQL to PostgreSQL with zero downtime. "
     "Each task has its own tests and passes only if every test passes. Score: % of tasks passed (pass@1, mean of "
     "three runs, mini-swe-agent harness). By the Laude Institute, Stanford and open-source contributors "
     "(arXiv 2601.11868)."),
    ("FrontierCode-AA 2.0 — what it measures",
     "Would a maintainer merge the agent's change? 132 private tasks (kept private to avoid contamination), each a "
     "change to a real open-source repository, built by Cognition with the maintainers. Graded with the task's tests "
     "and a rubric of blocking and non-blocking checks: a failed blocking check, or a solution looked up instead of "
     "written, scores 0; otherwise a weighted partial score. Mean over three attempts, up to 500 turns, "
     "LLM judge GPT-6 Luna (medium)."),
    ("Reading it",
     "Terminal-Bench says whether the agent can drive tools and environments end to end (our git, npm and test "
     "work); FrontierCode says whether the change is good enough for a reviewer (our /gse-review). A model can be "
     "strong on one and weak on the other: Kimi K3.1 Pro passes 67% of the terminal tasks but scores 26% on "
     "FrontierCode."),
    ("Our course model",
     "DeepSeek V4.1 Flash: 34% and 28%, mid-table; GPT-6.2 Sol does better (60% and 44%). But each key is capped at "
     "$30: about 15 million tokens sent with Sol ($2 per million) against about 600 million with DeepSeek, and an "
     "agent session re-sends ~2 million. Our bench of 21 Nov 2026 on the real workshops: DeepSeek followed GSE-One "
     "most faithfully (sub-agent reviews) for the lowest sprint cost. No public benchmark measures fidelity to a "
     "method."),
]

# (title, how to draw it, tooltip entries): a callable draws natively, a string is an image name
_VIEWS = [
    ("AI Index: Results", lambda: _bars("score", "{:.0f}", "score"), None),
    ("AI Index: Token Usage", lambda: _bars("output_tokens_m", "{:.0f}M", "output_tokens_m"), _TOKEN_ENTRIES),
    ("AI Index: Cost per Task", lambda: _bars("cost_per_task", "${:.2f}", "cost_per_task"), None),
    ("AI Index: Score vs. Cost", "ai-index-score-vs-cost", None),
    ("AI Index: Coding Benchmarks", _coding, _CODING_ENTRIES),   # NG, 2026-11-22
]


def build():
    for idx, (title, image, notes) in enumerate(_VIEWS):
        with st_slide(cut=idx > 0, marker=(title if idx > 0 else None), style=_slide_top):
            lvl = "1" if idx == 0 else "2"
            if notes:   # the "i" on the title line: two-column header grid (NG, 2026-11-22)
                with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                    with h.cell():
                        st_write(bs.heading+"zoom:0.75;", title, tag=t.div, toc_lvl=lvl)
                    with h.cell():
                        st_hover_tooltip(title=f"Trainer notes — {title}" if notes is not _TOKEN_ENTRIES
                                         else "Token Types", entries=notes, position="left", width="50vw")
            else:
                with st_block(s.center_txt):
                    st_write(bs.heading+"zoom:0.75;", title, tag=t.div, toc_lvl=lvl)
            if callable(image):
                image()
            else:
                with st_zoom(120):   # NG, 2026-11-22
                    st_image(uri=f"{_IMAGES}/{image}-en.png", width="100%", max_vh=70, align="center")
            with st_block(s.center_txt):
                st_write(bs.source, cite("artificialanalysis2026"))
