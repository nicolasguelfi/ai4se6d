"""Slide — Quality attribute scenarios: six parts (Bass, Clements, Kazman) (CCSET11, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Quality scenario styles."""
    heading = s.project.titles.heading
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "scenario_tl")
    txt = s.project.titles.table_cell
    source = s.project.citation + s.large + s.center_txt
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "scenario_foot")
bs = BlockStyles

ROWS = [
    ("Source", "a user"),
    ("Stimulus", "closes the browser in the middle of adding an expense"),
    ("Artefact", "the stored list of expenses"),
    ("Environment", "normal use, no network"),
    ("Response", "on reopening, every confirmed expense is there"),
    ("Measure", "0 confirmed expense lost over 100 trials"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(65):
            st_write(bs.heading, "A Quality Scenario", tag=t.div, toc_lvl="+1", label="Quality attribute scenario")
            for name, value in ROWS:
                with st_grid(cols="22% 74%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, value)
            st_write(bs.source, cite("bass-sap2021"), tag=t.div)
            st_write(bs.foot, "Qualities shape the architecture: decide them before the design.", tag=t.div)
