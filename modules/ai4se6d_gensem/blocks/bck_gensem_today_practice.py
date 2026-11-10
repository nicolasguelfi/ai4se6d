"""Slide — Day 4 agenda: test, measure, deliver, frame your project (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Day 4 agenda styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "today_practice_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "today_practice_tl")
    txt = s.project.titles.table_cell
bs = BlockStyles

ROWS = [
    ("09:15", "CCSET12", "E14 — your test strategy, then tests, production, review"),
    ("11:45", "CCSET13", "Measuring quality — E15"),
    ("13:15", "CCSET14", "Delivery, maintenance, capitalisation — E16"),
    ("15:00", "CCSET15", "Framing a project — E17 and E18: your mini-project starts"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(72):
            st_write(bs.heading, "Day 4 — Close the Loop", tag=t.div, toc_lvl="1", label="Day 4 agenda")
            with st_grid(cols="14% 20% 62%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Time")
                with g.cell(): st_write(bs.hdr, "Cycle")
                with g.cell(): st_write(bs.hdr, "Topic")
            for time, cycle, topic in ROWS:
                with st_grid(cols="14% 20% 62%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, time)
                    with g.cell(): st_write(bs.lbl, cycle)
                    with g.cell(): st_write(bs.txt, topic)
