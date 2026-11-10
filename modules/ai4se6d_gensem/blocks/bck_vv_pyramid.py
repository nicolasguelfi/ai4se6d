"""Slide — The test pyramid and how to adapt it (Cohn) (CCSET12, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Test pyramid styles."""
    heading = s.project.titles.heading
    level = Style.create(s.project.titles.table_label + s.center_txt, "pyramid_level")
    note = Style.create(s.project.titles.table_cell + s.center_txt, "pyramid_note")
    source = s.project.citation + s.large + s.center_txt
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "pyramid_foot")
bs = BlockStyles

LEVELS = [
    ("30%", "End-to-end / UI", "few: slow, fragile, close to the user"),
    ("55%", "Integration / service", "some: parts and storage together"),
    ("80%", "Unit", "many: fast, precise, cheap"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "The Test Pyramid", tag=t.div, toc_lvl="+1", label="Test pyramid")
            for width, name, note in LEVELS:
                with st_grid(cols=f"{(100 - int(width[:-1])) // 2}% {width} 1fr", gap="0px") as g:
                    with g.cell(): None
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell):
                            st_write(bs.level, name, tag=t.div)
                            st_write(bs.note, note, tag=t.div)
                    with g.cell(): None
            st_write(bs.source, cite("cohn-succeeding2009"), tag=t.div)
            st_write(bs.foot, "A shape to adapt, not a law: a web front-end needs some end-to-end tests.", tag=t.div)
