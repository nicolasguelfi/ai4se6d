"""Slide — Making a quality requirement measurable: scale, meter, goal (Gilb) (CCSET11, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Measurable NFR styles."""
    heading = s.project.titles.heading
    bad = Style.create(s.project.titles.body + s.project.colors.critical + s.center_txt, "measurable_bad")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "measurable_tl")
    txt = s.project.titles.table_cell
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

ROWS = [
    ("Scale", "seconds from a click on \"Summary\" to the totals shown"),
    ("Meter", "an automated test with 1,000 stored expenses, on the course laptop"),
    ("Goal", "under 0.2 s"),
    ("Tolerable", "under 1 s — beyond that, it is a defect"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Make It Measurable", tag=t.div, toc_lvl="+1", label="Measurable NFR")
            st_write(bs.bad, "✗ \"The summary is fast.\"", tag=t.div)
            for name, value in ROWS:
                with st_grid(cols="22% 74%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, value)
            st_write(bs.source, "Quantified qualities — ", cite("gilb-competitive2005"), tag=t.div)
