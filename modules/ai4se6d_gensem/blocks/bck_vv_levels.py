"""Slide — Test levels mirror the specification levels (V model) (CCSET12, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Test levels styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "vv_levels_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "vv_levels_tl")
    txt = Style.create(s.project.titles.table_cell + s.center_txt, "vv_levels_td")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "vv_levels_foot")
bs = BlockStyles

ROWS = [
    ("Requirements", "Acceptance tests", "the user's examples pass"),
    ("Design", "Integration tests", "the parts work together"),
    ("Code", "Unit tests", "each function does what it says"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(72):
            st_write(bs.heading, "Each Level Has Its Tests", tag=t.div, toc_lvl="+1", label="Test levels")
            with st_grid(cols="30% 32% 34%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "What you wrote")
                with g.cell(): st_write(bs.hdr, "What checks it")
                with g.cell(): st_write(bs.hdr, "It shows that…")
            for spec, test, shows in ROWS:
                with st_grid(cols="30% 32% 34%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, spec)
                    with g.cell(): st_write(bs.txt, test)
                    with g.cell(): st_write(bs.txt, shows)
            st_write(bs.foot, "Design the test when you write the specification, not after the code.", tag=t.div)
