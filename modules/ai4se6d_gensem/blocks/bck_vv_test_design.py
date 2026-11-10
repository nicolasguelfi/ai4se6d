"""Slide — Designing test cases: equivalence classes and boundaries (Myers) (CCSET12, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Test design styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "test_design_body")
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "test_design_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "test_design_tl")
    txt = Style.create(s.project.titles.table_cell + s.center_txt, "test_design_td")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

ROWS = [
    ("Invalid: ≤ 0", "−5 · 0", "error shown"),
    ("Boundary", "0.01", "accepted"),
    ("Valid", "25.50", "accepted, shown as €25.50"),
    ("Invalid: text", "\"abc\"", "error shown"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Which Cases to Test?", tag=t.div, toc_lvl="+1", label="Test case design")
            st_write(bs.body, "Requirement: \"the amount of an expense is a positive number\".", tag=t.div)
            with st_grid(cols="32% 30% 34%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Class")
                with g.cell(): st_write(bs.hdr, "Input")
                with g.cell(): st_write(bs.hdr, "Expected")
            for cls, value, expected in ROWS:
                with st_grid(cols="32% 30% 34%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, cls)
                    with g.cell(): st_write(bs.txt, value)
                    with g.cell(): st_write(bs.txt, expected)
            st_write(bs.source, "One test per class, plus the boundaries — ", cite("myers-testing2011"), tag=t.div)
