"""Slide — Your 3-Parts Journey: session roadmap grid."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Session map table styles."""
    heading = s.project.titles.heading
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    td_label = s.project.titles.table_label
    td_active = s.project.titles.table_label_active

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Your 3-Parts Journey", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="1fr 2fr",
            gap="4px",
            cell_styles=s.project.containers.cell_pad_sm,
        ) as g:
            # Header row
            with g.cell():
                with st_block(s.project.containers.table_header_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.th, "When")
            with g.cell():
                with st_block(s.project.containers.table_header_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.th, "Content")

            # Row 1 — Part 1
            with g.cell():
                with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.td_label, "1")
            with g.cell():
                with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.td, "SOTA, Evidence, Frameworks, CE Theory, CalcApp v0.3")

            # Row 2 — Part 2
            with g.cell():
                with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.td_active, "2")
            with g.cell():
                with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.td, "Mini-project with GenSEMOne")

            # Row 3 — Part 3
            with g.cell():
                with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.td_active, "3")
            with g.cell():
                with st_block(s.project.containers.table_normal_cell + s.project.containers.cell_pad_sm):
                    st_write(bs.td, "Mini-project with GenSEMOne ctnd + Advanced GenSEM demo")
