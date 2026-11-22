"""Slide — Context Performance Benchmark: MRCR 8 needles, score per context size.

Method of streamtex-all-trainings (NG, 2026-11-22): the figures live in a JSON with their sources and the
selection rules (modules/shared-blocks/data/context_length_scores.json); the chart is an image drawn from it, in
the ai4se6d design (same title, axes and labels as the former interactive chart). Updating:

    uv run python scripts/fetch_context_arena.py    # refresh the JSON (rule m1, same generation, complete results)
    uv run python scripts/draw_context_chart.py     # redraw _SHARED/images/diagrams/context-length/*.png
"""
# @guideline: maximize-viewport
import datetime as dt
import json
from pathlib import Path

from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_page_fill = s.project.containers.page_fill_top
_DATA = Path(__file__).parent.parent.parent / "shared-blocks" / "data" / "context_length_scores.json"
_IMAGE = "_SHARED/images/diagrams/context-length/context-length-en.png"


class BlockStyles:
    """Slide: Context Performance Benchmark — maximize-viewport: full-width chart."""
    heading = s.project.titles.slide_title + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    updated = json.loads(_DATA.read_text(encoding="utf-8"))["updated"]
    snapshot = dt.date.fromisoformat(updated).strftime("%B %Y")
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Context Performance Benchmark", tag=t.div, toc_lvl="1")
            st_hover_tooltip(
                title="MRCR 8 Needles — What this test measures",
                entries=[
                    (
                        "MRCR",
                        "Multi-Round Co-reference Resolution (OpenAI). A long "
                        "conversation contains several near-identical requests, "
                        "e.g. 'write a poem about tapirs'. The model is then asked: "
                        "'return the 2nd poem about tapirs'.",
                    ),
                    (
                        "8 Needles",
                        "8 identical requests ('needles') are hidden in the "
                        "conversation ('haystack'). The model must pick the right "
                        "one by its order. More needles = harder.",
                    ),
                    (
                        "Context sizes",
                        "Each model is tested at 8k, 16k, 32k, 64k, 128k, 256k, 512k, "
                        "and 1M tokens. A score drop at larger sizes means the model "
                        "'forgets' information buried deep in its context window.",
                    ),
                    (
                        "Score",
                        "Text similarity between the answer and the expected one "
                        "(0-100%). A perfect model scores 100% at all context sizes.",
                    ),
                ],
                scale="1.5vw",
                width="50vw",
            )

        st_image(uri=_IMAGE, width="100%", max_vh=56, align="center")   # the title takes two lines

        with st_block(s.center_txt):
            st_write(
                bs.source,
                cite("contextarena2026"), " · ", cite("openai-mrcr2025"),
                f" — data snapshot {snapshot}",
            )
