"""Slide — Debrief: what I would have done by hand / what the AI did (one example each)."""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Debrief comparison styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    example = Style.create(s.project.titles.table_cell + s.italic + s.project.colors.muted, "setup_debrief_example")
    empty = Style.create(s.project.titles.table_cell + s.project.colors.muted, "setup_debrief_empty")
    body = Style.create(s.project.titles.body + s.center_txt, "setup_debrief_body")
    keyword = s.bold + s.project.colors.highlight
bs = BlockStyles

_COLS = "1fr 1fr"  # fixed: a two-column table


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "By Hand vs. AI", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        with st_grid(cols=_COLS, gap="12px", cell_styles=s.project.containers.table_header_cell) as g:
            with g.cell():
                st_write(bs.header_text, "What I would have done by hand")
            with g.cell():
                st_write(bs.header_text, "What the AI did")
        with st_grid(cols=_COLS, gap="12px", cell_styles=s.project.containers.table_normal_cell) as g:
            with g.cell():
                st_write(bs.example, "e.g. search how to save data in the browser")
            with g.cell():
                st_write(bs.example, "e.g. used localStorage — I never checked how")
            with g.cell():
                st_write(bs.empty, "…")
            with g.cell():
                st_write(bs.empty, "…")
        st_space("v", 1)
        st_write(bs.body, (bs.keyword, "Each of you: one example"), " — 30 seconds.", tag=t.div)
