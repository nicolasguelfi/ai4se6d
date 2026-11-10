"""Slide — After delivery: the four kinds of maintenance (ISO/IEC/IEEE 14764) (CCSET14, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Maintenance styles."""
    heading = s.project.titles.heading
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "maintenance_tl")
    txt = s.project.titles.table_cell
    source = s.project.citation + s.large + s.center_txt
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "maintenance_foot")
bs = BlockStyles

ROWS = [
    ("Corrective", "fix a defect found in use"),
    ("Adaptive", "follow a change of environment: a new browser, a new library"),
    ("Perfective", "improve: speed, readability, a better feature"),
    ("Preventive", "fix a weakness before it hurts"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Delivered Is Not Finished", tag=t.div, toc_lvl="+1", label="Kinds of maintenance")
            for name, what in ROWS:
                with st_grid(cols="24% 72%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, what)
            st_write(bs.source, cite("iso14764-2022"), tag=t.div)
            st_write(bs.foot, "Most of a program's life is maintenance: write it for the next reader.", tag=t.div)
