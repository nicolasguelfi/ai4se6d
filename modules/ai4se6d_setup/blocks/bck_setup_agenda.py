"""Slide — This afternoon's timetable."""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Agenda table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    time_text = s.project.titles.table_label
    time_active = s.project.titles.table_label_active
bs = BlockStyles

_COLS = "18% 62% 20%"
_HEADERS = ("Time", "What", "Duration")
# (time, what, duration, hands-on)
_ROWS = [
    ("13:15", "Installation in the room", "75 min", True),
    ("14:30", "FreeSelfApp — part 1", "45 min", True),
    ("15:15", "Break", "15 min", False),
    ("15:30", "FreeSelfApp — part 2", "45 min", True),
    ("16:15", "Debrief + hands-up quiz", "30 min", False),
    ("16:45", "Buffer: late installs, questions", "15 min", False),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "This Afternoon", tag=t.div, toc_lvl="1")
            with st_zoom(90):
                _timetable()


def _timetable():
    """Render the timetable (header row + one grid per row)."""
    with st_grid(cols=_COLS, gap="8px", cell_styles=s.project.containers.table_header_cell) as g:
        for header in _HEADERS:
            with g.cell():
                st_write(bs.header_text, header)
    for time, what, duration, hands_on in _ROWS:
        cell = s.project.containers.table_active_cell if hands_on else s.project.containers.table_normal_cell
        with st_grid(cols=_COLS, gap="8px", cell_styles=cell) as g:
            with g.cell():
                st_write(bs.time_active if hands_on else bs.time_text, time)
            with g.cell():
                st_write(bs.cell_text, what)
            with g.cell():
                st_write(bs.cell_text, duration)
