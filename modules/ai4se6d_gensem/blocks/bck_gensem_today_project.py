"""Slide — Day 5 agenda: deployment (CCSET16), then the mini-project sprint (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Day 5 agenda styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "today_project_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "today_project_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "today_project_foot")
bs = BlockStyles

ROWS = [
    ("09:15", "CCSET16", "Deployment: from code to a service"),
    ("09:45", "E20 · E21", "Your sprint: the plan, then the requirements on two models"),
    ("11:00", "E20 · E19", "The sprint goes on; deployment waves 1 and 2 (CalcApp)"),
    ("13:15", "E20 · E19", "The sprint goes on; waves 3 and 4"),
    ("15:15", "Milestone", "The trainer validates your plan and requirements, one by one"),
    ("16:30", "Debrief", "The milestone and the deployment; push, /gse-pause"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Day 5 — Your Sprint Starts", tag=t.div, toc_lvl="1", label="Day 5 agenda")
            with st_grid(cols="14% 20% 62%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Time")
                with g.cell(): st_write(bs.hdr, "Cycle / sheet")
                with g.cell(): st_write(bs.hdr, "Topic")
            for time, cycle, topic in ROWS:
                with st_grid(cols="14% 20% 62%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, time)
                    with g.cell(): st_write(bs.lbl, cycle)
                    with g.cell(): st_write(bs.txt, topic)
            st_write(bs.foot, "One new cycle today (deployment); the rest of the time is your project.", tag=t.div)
