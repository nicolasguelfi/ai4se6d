"""Slide — GenSEMOne Timeline: 1.5 Days."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Timeline slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    callout_text = s.project.titles.body + s.project.colors.highlight
bs = BlockStyles

_BLOCKS = [
    (
        "Day 5 AM (9:15\u201312:30)",
        "Seed (15m) + Requirements (30m) + Plan (15m) + Iterate FR1\u20133 (2h)",
    ),
    (
        "Day 5 PM (1:30\u20135:00)",
        "Iterate FR4\u20136 (2.5h) + Quick review (30m)",
    ),
    (
        "Day 6 AM (9:15\u201312:30)",
        "FR7\u20138 + fixes (2h) + Compound (15m) + Demo prep (45m)",
    ),
    (
        "Day 6 PM (1:30\u20133:15)",
        "Polish + final presentation",
    ),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "GenSEMOne Timeline \u2014 1.5 Days", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="25% 75%",
            gap="8px",
            cell_styles=s.project.containers.cell_pad_sm,
        ) as g:
            # Header row
            with g.cell():
                with st_block(s.project.containers.table_header_cell):
                    st_write(s.project.titles.table_header, "Time Block")
            with g.cell():
                with st_block(s.project.containers.table_header_cell):
                    st_write(s.project.titles.table_header, "Activities")

            for label, activities in _BLOCKS:
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(s.project.titles.table_label, label)
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(s.project.titles.table_cell, activities)

        st_space("v", 2)
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_text,
                "Key rhythm: ~30 min per FR. 8 FRs \u00d7 30 min = 4h focused iteration.",
            )
