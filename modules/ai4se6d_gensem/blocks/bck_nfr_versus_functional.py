"""Slide — Functional versus non-functional requirements (CCSET11, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """FR versus NFR styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "nfr_vs_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "nfr_vs_tl")
    txt = Style.create(s.project.titles.table_cell + s.center_txt, "nfr_vs_td")
    source = s.project.citation + s.large + s.center_txt
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "nfr_vs_foot")
bs = BlockStyles

ROWS = [
    ("Question", "What does it do?", "How well must it do it?"),
    ("CalcApp", "Add an expense", "Saved even if the browser closes"),
    ("CalcApp", "Show the monthly total", "Shown in under 200 ms for 1,000 expenses"),
    ("If missing", "A feature is absent", "Every feature is slow, unsafe or unusable"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Functional vs Non-Functional", tag=t.div, toc_lvl="+1", label="FR versus NFR")
            with st_grid(cols="20% 38% 38%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "")
                with g.cell(): st_write(bs.hdr, "Functional")
                with g.cell(): st_write(bs.hdr, "Non-functional (quality)")
            for name, fr, nfr in ROWS:
                with st_grid(cols="20% 38% 38%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, fr)
                    with g.cell(): st_write(bs.txt, nfr)
            st_write(bs.source, "The line is not always sharp — ", cite("glinz-nfr2007"), tag=t.div)
            st_write(bs.foot, "Users rarely state qualities: you have to ask for them.", tag=t.div)
