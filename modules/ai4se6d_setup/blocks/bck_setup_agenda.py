"""Slide — This afternoon's timetable."""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Agenda table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    time_text = s.project.titles.table_label
    time_active = s.project.titles.table_label_active
bs = BlockStyles

# Outer 5 % margin columns (NG, 2026-11-23: same recipes as the intro module)
_COLS = "5% 15% 55% 20% 5%"
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

_NOTES = [
    ("The message",
     "Three and a half hours, mostly hands-on: the highlighted rows (install, FreeSelfApp part 1 and part 2) are "
     "the ones where you work at your machine."),
    ("Installation first",
     "75 min in the room. Mid-point at 13:50: you should be at step 4 or beyond."),
    ("FreeSelfApp",
     "Two blocks of 45 min around the break: a first prototype by pure prompting."),
    ("Debrief and buffer",
     "16:15: debrief and a hands-up quiz. 16:45: buffer for late installs and questions — nobody leaves without a "
     "working toolchain."),
    ("Ask the room",
     "« Whose laptop is managed by an IT department? » — those are the installs to start first."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "This Afternoon", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — This Afternoon", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(130):
            _timetable()


def _timetable():
    """Render the timetable (header row + one grid per row), between two empty margin columns."""
    header = [s.none] + [s.project.containers.table_header_cell] * 3 + [s.none]
    with st_grid(cols=_COLS, gap="8px", cell_styles=header) as g:
        with g.cell():
            pass  # left margin
        for title in _HEADERS:
            with g.cell():
                st_write(bs.header_text, title)
        with g.cell():
            pass  # right margin
    for time, what, duration, hands_on in _ROWS:
        cell = s.project.containers.table_active_cell if hands_on else s.project.containers.table_normal_cell
        with st_grid(cols=_COLS, gap="8px", cell_styles=[s.none, cell, cell, cell, s.none]) as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(bs.time_active if hands_on else bs.time_text, time)
            with g.cell():
                st_write(bs.cell_text, what)
            with g.cell():
                st_write(bs.cell_text, duration)
            with g.cell():
                pass  # right margin
