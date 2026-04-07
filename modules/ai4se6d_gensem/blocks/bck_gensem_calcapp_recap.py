"""Slide — Where We Are: CalcApp Journey timeline."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """CalcApp recap timeline styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header = s.project.titles.table_header
    label = s.project.titles.table_label
    label_active = s.project.titles.table_label_active
    cell = s.project.titles.table_cell
bs = BlockStyles

_VERSIONS = [
    # (version, status, when, description, ce_phase, active)
    ("v0.0", "\u2714", "Day 2", "Planning docs, no code", "Plan", False),
    ("v0.1", "\u2714", "Day 2", "CRUD + TDD + routing", "Work", False),
    ("v0.2", "\u2714", "Day 2", "AI-assisted review", "Review", False),
    (
        "v0.3", "\U0001f51c", "TODAY",
        "Full requirements engineering",
        "Brainstorm + Plan + Work + Review",
        True,
    ),
    ("v0.4\u2013v0.5", "", "Tomorrow", "Architecture + Features + Production", "", False),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Where We Are: CalcApp Journey", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        # Header row
        with st_grid(
            cols="10% 20% 40% 30%",
            gap="8px",
            cell_styles=s.project.containers.table_header_cell,
        ) as g:
            with g.cell():
                st_write(bs.header, "Version")
            with g.cell():
                st_write(bs.header, "When")
            with g.cell():
                st_write(bs.header, "Description")
            with g.cell():
                st_write(bs.header, "CE Phase")

        st_space("v", 0.3)

        # Data rows
        for version, status, when, description, ce_phase, active in _VERSIONS:
            cell_style = (
                s.project.containers.table_active_cell if active
                else s.project.containers.table_normal_cell
            )
            lbl = bs.label_active if active else bs.label
            txt = bs.cell

            with st_grid(cols="10% 20% 40% 30%", gap="8px", cell_styles=cell_style) as g:
                with g.cell():
                    st_write(lbl, (lbl, version), " ", status)
                with g.cell():
                    st_write(txt, when)
                with g.cell():
                    st_write(txt, description)
                with g.cell():
                    st_write(txt, ce_phase)

            st_space("v", 0.2)
