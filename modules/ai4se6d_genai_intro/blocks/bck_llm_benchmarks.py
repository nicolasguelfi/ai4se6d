"""Slides — Artificial Analysis Intelligence Index: four charts drawn from data.

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

# (title, image, tooltip entries)
_VIEWS = [
    ("AI Index: Results", "ai-index-score", None),
    ("AI Index: Token Usage", "ai-index-tokens", _TOKEN_ENTRIES),
    ("AI Index: Cost per Task", "ai-index-cost", None),
    ("AI Index: Score vs. Cost", "ai-index-score-vs-cost", None),
]


def build():
    for idx, (title, image, notes) in enumerate(_VIEWS):
        with st_slide(cut=idx > 0, marker=(title if idx > 0 else None), style=_slide_top):
            with st_block(s.center_txt):
                st_write(bs.heading, title, tag=t.div, toc_lvl="1" if idx == 0 else "2")
                if notes:
                    st_hover_tooltip(title="Token Types", entries=notes, scale="2vw", width="65vw",
                                     position="center")
            with st_zoom(110):   # NG, 2026-11-22
                st_image(uri=f"{_IMAGES}/{image}-en.png", width="100%", max_vh=70, align="center")
            with st_block(s.center_txt):
                st_write(bs.source, cite("artificialanalysis2026"))
