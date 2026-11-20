"""Slide — Day 5 afternoon: sprint, deployment waves 3-4, milestone validation on the fly (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Afternoon agenda styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "project_pm_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "project_pm_tl")
    txt = s.project.titles.table_cell
bs = BlockStyles

ROWS = [
    ("13:15", "Sprint (E20) · deployment waves 3 (13:15) and 4 (14:00) (E19)"),
    ("15:00", "Break"),
    ("15:15", "Sprint · the trainer validates plans and requirements, one by one"),
    ("16:30", "Milestone and debrief: the day, the deployment"),
    ("16:45", "Push, /gse-pause, buffer"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Day 5 Afternoon", tag=t.div, toc_lvl="1", label="Day 5 afternoon")
            with st_grid(cols="16% 80%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Time")
                with g.cell(): st_write(bs.hdr, "What")
            for time, what in ROWS:
                with st_grid(cols="16% 80%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, time)
                    with g.cell(): st_write(bs.txt, what)
