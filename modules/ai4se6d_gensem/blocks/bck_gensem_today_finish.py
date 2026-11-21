"""Slide — Day 6 agenda: finish, deliver, audit, gallery, lessons, closing (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Day 6 agenda styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "today_finish_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "today_finish_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "today_finish_foot")
bs = BlockStyles

ROWS = [
    ("09:15", "E20", "Finish the sprint; from 11:00, its last task: empty shells, README"),
    ("11:30", "E22", "Deliver, tag demo; 12:00 freeze: rehearse your demo"),
    ("12:15", "E23", "Audit your project: AI Act, licences, secrets, data"),
    ("13:45", "E24", "Prepare your demo; gallery in two rotations (14:00, 14:45)"),
    ("15:45", "E25", "Lessons learned; your Monday-morning plan"),
    ("16:35", "Closing", "Final questionnaire, certificates, resources"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Day 6 — Finish, Show, Look Back", tag=t.div, toc_lvl="1", label="Day 6 agenda")
            with st_grid(cols="14% 16% 66%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Time")
                with g.cell(): st_write(bs.hdr, "Sheet")
                with g.cell(): st_write(bs.hdr, "Topic")
            for time, sheet, topic in ROWS:
                with st_grid(cols="14% 16% 66%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, time)
                    with g.cell(): st_write(bs.lbl, sheet)
                    with g.cell(): st_write(bs.txt, topic)
            st_write(bs.foot, "First: tutor update in the tutor window, then /gse-resume in your project.", tag=t.div)
