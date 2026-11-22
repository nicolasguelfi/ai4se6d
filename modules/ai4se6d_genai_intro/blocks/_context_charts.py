"""Shared layout of the two context-length chart slides (bck_llm_context_reliability, bck_llm_context_reasoning).

Not a block (no bck_ prefix): a helper, like ai4se6d_various/blocks/_diagram_export.py. One slide per block, so that
each chart is on its own page (NG, 2026-11-22: "vraiment sur des slides séparés"); images +20 % (max_vh 64 → 77).
The charts come from streamtex-all-trainings; redraw with

    uv run python scripts/draw_context_reliability_chart.py
"""
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


_IMAGES = "_SHARED/images/diagrams/context-reliability"
_slide_top = Style("justify-content:flex-start;margin-top:0;", "ctxrel_slide_top")
_heading = s.project.titles.slide_title + s.center_txt
_source = s.project.citation + s.large + s.center_txt


def chart_slide(title, image, notes, refs, toc_lvl):
    """Title (one line) with the « i » at the top right, the chart, then the citations."""
    with st_slide(style=_slide_top):
        with st_grid(cols="92% 8%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(46):   # long titles kept on one line
                st_write(_heading, title, tag=t.div, toc_lvl=toc_lvl)
            with h.cell():
                st_hover_tooltip(title=f"Trainer notes — {title}", entries=notes, position="left", width="50vw")
        st_image(uri=f"{_IMAGES}/{image}-en.png", width="100%", max_vh=77, align="center")   # +20 % (NG, 2026-11-22)
        with st_block(s.center_txt):
            parts = []
            for i, key in enumerate(refs):
                parts += ([" · "] if i else []) + [cite(key)]
            st_write(_source, *parts)
