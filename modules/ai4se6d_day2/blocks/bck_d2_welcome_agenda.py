"""Slide — Day 2 agenda (from plan B)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Agenda styles."""
    heading = s.project.titles.heading
    col_title = Style.create(s.project.titles.subtitle + s.center_txt, "d2_agenda_col")
    time = Style.create(s.project.titles.table_label + Style("white-space:nowrap;", "d2_nowrap"), "d2_agenda_time")
    item = s.project.titles.table_cell
    pause = Style.create(s.project.titles.table_cell + s.project.colors.muted + s.italic, "d2_agenda_pause")
bs = BlockStyles

_MORNING = [
    ("09:15", "Git first", False),
    ("09:50", "Driving opencode", False),
    ("10:45", "Break", True),
    ("11:00", "Technical planning", False),
    ("11:30", "CalcApp v0.1 — part 1", False),
    ("12:15", "Lunch", True),
]
_AFTERNOON = [
    ("13:15", "CalcApp v0.1 — part 2", False),
    ("14:30", "Code review with AI", False),
    ("15:00", "Break", True),
    ("15:15", "Review today’s diff", False),
    ("16:15", "Deliver v0.1", False),
    ("16:30", "Bridge to GSE-One", False),
    ("17:00", "Buffer, questions", True),
]


def _column(title, rows):
    st_write(bs.col_title, title, tag=t.div)
    st_space("v", 0.5)
    with st_grid(cols="auto 1fr", gap="6px 24px") as g:
        for time, label, is_pause in rows:
            with g.cell():
                st_write(bs.time, time)
            with g.cell():
                st_write(bs.pause if is_pause else bs.item, label)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Today’s Agenda", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(cols=s.project.containers.responsive_2col, grid_style=s.project.containers.gap_32) as g:
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                    _column("Morning", _MORNING)
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                    _column("Afternoon", _AFTERNOON)
