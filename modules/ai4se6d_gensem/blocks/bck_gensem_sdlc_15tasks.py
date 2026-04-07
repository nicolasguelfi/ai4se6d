"""Slide — 15 Core Tasks of the Generative Software Engineer."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """15 tasks table styles."""
    heading = s.project.titles.heading
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    td_label = s.project.titles.table_label

bs = BlockStyles


# (task_id, name, change_level, cell_bg)
_TASKS = [
    ("T1", "Intent Specification", "NEW", s.project.containers.cell_active_bg),
    ("T2", "Context Engineering", "NEW", s.project.containers.cell_active_bg),
    ("T3", "Architecture & Design", "ELEVATED", s.project.containers.cell_accent_bg),
    ("T4", "Code Gen Orchestration", "TRANSFORMED", s.project.containers.cell_primary_bg),
    ("T5", "Code Review & Validation", "ELEVATED", s.project.containers.cell_accent_bg),
    ("T6", "Test Strategy", "ELEVATED", s.project.containers.cell_accent_bg),
    ("T7", "Debugging", "TRANSFORMED", s.project.containers.cell_primary_bg),
    ("T8", "Refactoring", "TRANSFORMED", s.project.containers.cell_primary_bg),
    ("T9", "Documentation", "AUTOMATED", s.project.containers.cell_primary_bg),
    ("T10", "Dependency & Security", "ELEVATED", s.project.containers.cell_accent_bg),
    ("T11", "CI/CD", "ELEVATED", s.project.containers.cell_accent_bg),
    ("T12", "Version Control", "EVOLVED", s.project.containers.cell_primary_bg),
    ("T13", "Agent Supervision", "NEW", s.project.containers.cell_active_bg),
    ("T14", "Knowledge Curation", "NEW", s.project.containers.cell_active_bg),
    ("T15", "Requirements Elicitation", "ELEVATED", s.project.containers.cell_accent_bg),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "15 Core Tasks of the GenSE", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="0.5fr 2fr 1fr",
            gap="4px",
            cell_styles=s.project.containers.cell_pad_sm,
        ) as g:
            # Header
            with g.cell():
                with st_block(s.project.containers.table_header_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.th, "#")
            with g.cell():
                with st_block(s.project.containers.table_header_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.th, "Task")
            with g.cell():
                with st_block(s.project.containers.table_header_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.th, "Change Level")

            # Rows
            for tid, name, level, bg in _TASKS:
                cell = bg + s.project.containers.cell_pad_sm
                with g.cell():
                    with st_block(cell):
                        st_write(bs.td, tid)
                with g.cell():
                    with st_block(cell):
                        st_write(bs.td_label, name)
                with g.cell():
                    with st_block(cell):
                        st_write(bs.td, level)
