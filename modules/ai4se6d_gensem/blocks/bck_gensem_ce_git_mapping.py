"""Slide — GSE-One Phase-to-Git Mapping."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Git mapping table slide styles."""
    heading = s.project.titles.heading
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label

bs = BlockStyles

_HEADER = ("Phase", "Git Operation", "Profile A", "Profile C")

_ROWS = [
    ("Brainstorm", "stash / notes", "direct", "branch discussion"),
    ("Plan", "branch create", "direct", "feature/ branch"),
    ("Work", "commits", "frequent commits", "PR commits"),
    ("Review", "diff", "git log", "PR review"),
    ("Compound", "tag + docs", "commit rules", "merge + release notes"),
]


def build():
    st_marker("Phase → Git Mapping")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                with st_zoom(90):
                    st_write(bs.heading, "GSE-One Phase-to-Git Mapping", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="GSE-One Phase-to-Git Mapping",
                    entries=[
                        ("Brainstorm", "CE Brainstorm = /gse:assess. Maps to stash/notes or branch discussion."),
                        ("Plan + Work", "CE Plan = /gse:plan, CE Work = /gse:produce. Maps to branch create and commits."),
                        ("Review + Compound", "CE Review = /gse:review, CE Compound = /gse:compound. Maps to diff/tag/docs."),
                        ("Profiles", "Profile A (solo) uses direct commits; Profile C (team) uses PRs and release notes."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )
        st_space("v", 1)

        with st_zoom(120):
            with st_grid(
                cols="20% 30% 25% 25%",
                gap="4px",
                cell_styles=s.project.containers.cell_pad_sm,
            ) as g:
                # Header row
                for h in _HEADER:
                    with g.cell():
                        with st_block(s.project.containers.table_header_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.th, h)

                # Data rows
                for phase, git_op, prof_a, prof_c in _ROWS:
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.tl, phase)
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.td, git_op)
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.td, prof_a)
                    with g.cell():
                        with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                            st_write(bs.td, prof_c)
