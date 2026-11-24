"""Slide — Day 2 agenda (from plan B)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Agenda styles."""
    heading = s.project.titles.heading
    col_title = Style.create(s.project.titles.subtitle + s.center_txt, "agenda_col")
    time = Style.create(s.project.titles.table_label + Style("white-space:nowrap;", "nowrap"), "agenda_time")
    item = s.project.titles.table_cell
    pause = Style.create(s.project.titles.table_cell + s.project.colors.muted + s.italic, "agenda_pause")
    first = Style.create(s.project.titles.table_cell + s.center_txt, "agenda_first")
    label = s.project.titles.table_label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "agenda_cmd")
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

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Everyone runs ~/ai4se/ai4se-kit/tutor update now (the « First » line) "
     "while you walk through the agenda."),
    ("The message",
     "The day follows the artifact chain: Git, opencode, a plan, the build, the review, the delivery — then the "
     "bridge to GSE-One."),
    ("First thing",
     "Everyone runs ~/ai4se/ai4se-kit/tutor update to get today's course notes in their tutor window."),
    ("Morning",
     "Git first (09:15), driving opencode (09:50), technical planning (11:00), then the first part of the CalcApp "
     "v0.1 build (11:30)."),
    ("Afternoon",
     "The build continues (13:15), code review with AI (14:30), review of today's diff (15:15), delivery of v0.1 "
     "(16:15), bridge to GSE-One (16:30), buffer and questions at 17:00."),
    ("If someone falls behind",
     "Recovery tags of the CalcApp starter let anyone restart at the start of the day, after the morning build or at "
     "v0.1 (next slides)."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — ~/ai4se/ai4se-kit/tutor update",
     "Runs the course kit's tutor script with « update »: it downloads the latest version of the kit (course "
     "notes, sheets) with git pull, then checks GSE-One. ~ = your home folder (/home/student in the course VM); "
     "~/ai4se/ai4se-kit/ = the folder of the course kit; tutor = the script; update = what we ask it to do. Close "
     "and reopen the tutor window afterwards."),
]


def _column(title, rows):
    st_write(bs.col_title, title, tag=t.div)
    st_space("v", "1.5vh")
    # one row per slot, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
    cols = "22% 78%"
    cells = s.project.containers.rows(len(rows), cols, filled=(1, 2))
    with st_grid(cols=cols, gap="1.6vh 0.3vw", cell_styles=cells) as g:
        for time, label, is_pause in rows:
            with g.cell():
                st_write(bs.time, time)
            with g.cell():
                st_write(bs.pause if is_pause else bs.item, label)


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Today’s Agenda", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Today’s Agenda", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(85):
            st_write(bs.first, (bs.label, "First: "), (bs.cmd, "~/ai4se/ai4se-kit/tutor update"),
                     " — get today's course notes", tag=t.div)
        st_space("v", "1vh")
        with st_zoom(105), st_grid(cols="5% 42.5% 42.5% 5%", gap="2vw") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                _column("Morning", _MORNING)
            with g.cell():
                _column("Afternoon", _AFTERNOON)
            with g.cell():
                pass  # right margin
