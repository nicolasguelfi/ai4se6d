"""Slide — Mapping CE Phases to Today's Activities."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """CE mapping slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header = s.project.titles.table_header
    label = s.project.titles.table_label
    cell = s.project.titles.table_cell
    arrow = s.bold + s.project.colors.highlight + s.Large
bs = BlockStyles

_ROWS = [
    ("CE Brainstorm", "Requirements Elicitation", "NG 45min"),
    ("CE Plan", "Functional Requirements Workshop", "TS 45min"),
    ("CE Work", "TDD Implementation", "TS 45min \u00d72"),
    ("CE Review", "Verification & Validation", "NG 30min + TS 45min"),
    ("CE Compound", "Debrief", "implicit"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading,
                "Mapping CE Phases to Today\u2019s Activities",
                tag=t.div,
                toc_lvl="1",
                )
            st_space("v", 1)

        # Header row
        with st_grid(
            cols="20% 5% 45% 30%",
            gap="8px",
            cell_styles=s.project.containers.table_header_cell,
        ) as g:
            with g.cell():
                st_write(bs.header, "CE Phase")
            with g.cell():
                st_write(bs.header, "\u2192")
            with g.cell():
                st_write(bs.header, "Today\u2019s Activity")
            with g.cell():
                st_write(bs.header, "Duration")

        st_space("v", 0.3)

        # Data rows
        for phase, activity, duration in _ROWS:
            with st_grid(
                cols="20% 5% 45% 30%",
                gap="8px",
                cell_styles=s.project.containers.table_normal_cell,
            ) as g:
                with g.cell():
                    st_write(bs.label, phase)
                with g.cell():
                    st_write(bs.arrow, "\u2192")
                with g.cell():
                    st_write(bs.cell, activity)
                with g.cell():
                    st_write(bs.cell, duration)

            st_space("v", 0.2)
