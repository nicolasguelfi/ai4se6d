"""Slide — Four quality signals you can check (CCSET13, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Quality signals styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "signals_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "signals_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "signals_foot")
bs = BlockStyles

ROWS = [
    ("Lint", "rule breaks, suspicious code — without running it", "npm run lint"),
    ("Tests", "the behaviour you specified still holds", "npm run test:run"),
    ("Coverage", "which lines the tests executed", "npm run test:coverage"),
    ("Build", "the app compiles and packages", "npm run build"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "Signals, Not Opinions", tag=t.div, toc_lvl="+1", label="Quality signals")
            with st_grid(cols="18% 50% 28%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Signal")
                with g.cell(): st_write(bs.hdr, "It tells you")
                with g.cell(): st_write(bs.hdr, "CalcApp")
            for name, tells, cmd in ROWS:
                with st_grid(cols="18% 50% 28%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, tells)
                    with g.cell(): st_write(bs.txt, (s.text.fonts.font_monospace, cmd))
            st_write(bs.foot, "\"All done, tests pass\" from the agent is a claim. A green signal is a fact.", tag=t.div)
