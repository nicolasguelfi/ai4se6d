"""Slide — Day 3 agenda: four concepts this morning, GSE-One this afternoon (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Day 3 agenda styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "today_concepts_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "today_concepts_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "today_concepts_foot")
bs = BlockStyles

ROWS = [
    ("09:15", "CCSET09", "Software engineering concepts — defining your GenSEM"),
    ("10:15", "CCSET10", "Requirements elicitation"),
    ("11:15", "CCSET11", "Non-functional requirements"),
    ("12:00", "CCSET12", "Verification and validation"),
    ("13:30", "Exercises", "With GSE-One on your CalcApp: discover, plan, requirements and design"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Day 3 — From Concepts to Method", tag=t.div, toc_lvl="1", label="Day 3 agenda")
            with st_grid(cols="14% 20% 62%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Time")
                with g.cell(): st_write(bs.hdr, "Cycle")
                with g.cell(): st_write(bs.hdr, "Topic")
            for time, cycle, topic in ROWS:
                with st_grid(cols="14% 20% 62%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, time)
                    with g.cell(): st_write(bs.lbl, cycle)
                    with g.cell(): st_write(bs.txt, topic)
            st_write(bs.foot, "This morning: theory, and how GSE-One solves each problem. "
                     "This afternoon: you use GSE-One for the first time.", tag=t.div)
