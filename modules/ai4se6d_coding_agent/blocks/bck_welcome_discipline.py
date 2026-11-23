"""Slide — Same tools, different discipline."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Framing slide styles."""
    heading = s.project.titles.heading
    line = Style.create(s.project.titles.body + s.center_txt, "disc_line")
    punch = Style.create(
        s.huge + s.bold + s.project.colors.highlight + s.center_txt, "disc_punch",
    )
bs = BlockStyles

_NOTES = [
    ("The message",
     "Day 1 was exploration, day 2 is engineering. The tool does not change: opencode is still opencode."),
    ("The idea",
     "What changes is how you drive it: a plan before the build, tests before the code, Git as a safety net, a "
     "review of every diff."),
    ("The trap",
     "Expecting a better result from a better tool or a better model. The gain of the day comes from the method."),
    ("Link to the rest of the day",
     "Each session of the day adds one piece of that discipline: Git, opencode context, planning, tests, review, "
     "delivery."),
    ("Ask the room",
     "« Yesterday, what did you let the agent decide that you would decide yourself today? »"),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        # title and « i » on the same line (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "Same Tools, New Discipline", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Same Tools, New Discipline", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "10vh")
        with st_zoom(130):
            st_write(bs.line, "Yesterday you explored. Today you engineer.", tag=t.div)
            st_space("v", "3vh")
            st_write(bs.line, "opencode is still opencode.", tag=t.div)
            st_space("v", "6vh")
            st_write(bs.punch, "What changes is how you drive it.", tag=t.div)
