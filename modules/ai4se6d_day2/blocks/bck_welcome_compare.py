"""Slide — Day 1 vs Day 2 comparison table."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Comparison table styles."""
    heading = s.project.titles.heading
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
bs = BlockStyles

_HEADER = ("", "Day 1 — yesterday", "Day 2 — today")
_ROWS = [
    ("Mindset", "Explore, move fast", "Plan, then build"),
    ("Output", "FreeSelfApp, a prototype", "CalcApp v0.1, tested"),
    ("Approach", "“Let the AI figure it out”", "“Guide the AI with intent”"),
    ("Tests", "None, or very few", "Test first, every task"),
    ("Safety net", "None", "Git: commit, branch"),
    ("Plan", "In your head", "docs/plan.md, committed"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Day 1 vs Day 2", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(cols="20% 40% 40%", gap="4px") as g:
            for h in _HEADER:
                with g.cell():
                    if h:
                        with st_block(s.project.containers.table_header_cell):
                            st_write(bs.th, h)
            for label, day1, day2 in _ROWS:
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(bs.tl, label)
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(bs.td, day1)
                with g.cell():
                    with st_block(s.project.containers.table_active_cell):
                        st_write(bs.td, day2)
