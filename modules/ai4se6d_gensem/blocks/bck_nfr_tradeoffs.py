"""Slide — Qualities conflict: trade-offs to decide explicitly (CCSET11, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Trade-off styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "tradeoffs_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "tradeoffs_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tradeoffs_foot")
bs = BlockStyles

ROWS = [
    ("Security ↔ usability", "one more login step protects the data, and annoys the user"),
    ("Performance ↔ maintainability", "a clever cache is fast, and hard to change"),
    ("Flexibility ↔ simplicity", "\"any currency\" today costs a week; \"euros only\" costs nothing"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Qualities Conflict", tag=t.div, toc_lvl="+1", label="Quality trade-offs")
            with st_grid(cols="36% 60%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Tension")
                with g.cell(): st_write(bs.hdr, "Example")
            for tension, example in ROWS:
                with st_grid(cols="36% 60%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, tension)
                    with g.cell(): st_write(bs.txt, example)
            st_write(bs.foot, "A trade-off is a decision: write it down, with its reason.", tag=t.div)
