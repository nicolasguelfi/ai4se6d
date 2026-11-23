"""Section title — Git first (09:15, 35 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Section title styles."""
    section = Style.create(s.project.titles.section_title + s.center_txt, "sec_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "sec_subtitle")
    info = Style.create(s.project.titles.caption + s.center_txt, "sec_info")
    quote = Style.create(s.project.titles.body + s.italic + s.center_txt, "sec_quote")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Before the agent touches anything, set up the safety net: every change it makes must be visible and "
     "reversible."),
    ("Timing",
     "35 minutes: 12 to show, 15 to try on CalcApp, 5 to debrief."),
    ("What comes",
     "Why Git matters more with AI, four words, the three areas, six commands, then three habits: review before "
     "stage, checkpoint commits, one branch per task."),
    ("The trap",
     "Treating Git as an expert topic. Six commands are enough for today."),
    ("Ask the room",
     "« Who has already lost work they could not get back? »"),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        # the « i » at the top right, on the first line (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                st_write(bs.info, "09:15 — 35 min · show 12 · try 15 · debrief 5", tag=t.div)
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Git First", entries=_NOTES, position="left", width="50vw")
        st_space("v", "18vh")
        with st_zoom(130):
            st_write(bs.section, "Git First", tag=t.div, toc_lvl="1")
            st_space("v", "2vh")
            st_write(bs.subtitle, "Your safety net — before the agent touches anything", tag=t.div)
            st_space("v", "6vh")
            st_write(bs.quote, "Coding without version control is a long game with no save button.", tag=t.div)
