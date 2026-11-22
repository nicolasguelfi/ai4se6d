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
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_IMAGES = "_SHARED/images/diagrams/ai-index"
# Title + chart + source fill the screen: each slide top-aligned, without the st_slide top margin.
_slide_top = Style("justify-content:flex-start;margin-top:0;", "aiidx_slide_top")


class BlockStyles:
    """Benchmark slides styles."""
    heading = s.project.titles.slide_title + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


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

# (title, image, tooltip entries)
_VIEWS = [
    ("AI Index: Results", "ai-index-score", None),
    ("AI Index: Token Usage", "ai-index-tokens", _TOKEN_ENTRIES),
    ("AI Index: Cost per Task", "ai-index-cost", None),
    ("AI Index: Score vs. Cost", "ai-index-score-vs-cost", None),
    ("AI Index: Coding Benchmarks", "ai-index-coding", _CODING_ENTRIES),   # NG, 2026-11-22
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
            with st_zoom(120):   # NG, 2026-11-22
                st_image(uri=f"{_IMAGES}/{image}-en.png", width="100%", max_vh=70, align="center")
            with st_block(s.center_txt):
                st_write(bs.source, cite("artificialanalysis2026"))
