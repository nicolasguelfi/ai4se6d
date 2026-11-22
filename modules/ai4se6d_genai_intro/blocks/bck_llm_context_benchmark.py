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
        # the "i" on the title line: two-column header grid (NG, 2026-11-22)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                st_write(bs.heading, "Context Performance Benchmark", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(
                    title="MRCR 8 Needles — What this test measures",
                    entries=[
                        (
                            "MRCR v2",
                            "Multi-Round Co-reference Resolution, version 2 (Google DeepMind), "
                            "run by Context Arena with the same harness for every model. A long "
                            "conversation contains several near-identical requests, "
                            "e.g. 'write a poem about tapirs'. The model is then asked: "
                            "'return the 3rd poem about tapirs'.",
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
                            "(0-100%), not a right/wrong accuracy. A perfect model scores 100% "
                            "at all context sizes; picking one of the 8 answers at random "
                            "gives about 15%.",
                        ),
                    ],
                    position="left",
                    width="50vw",
                )

        st_image(uri=_IMAGE, width="100%", max_vh=56, align="center")   # the title takes two lines

        with st_block(s.center_txt):
            st_write(
                bs.source,
                cite("uzar2026contextarena"), " · ", cite("gdm2025mrcrv2"),   # GDM-MRCR v2, as in the data (NG, 2026-11-22)
                f" — data snapshot {snapshot}",
            )
