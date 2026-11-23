"""Slide — Section — CalcApp v0.1 Part 1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Section — CalcApp v0.1 Part 1 — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "build_title_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "build_title_subtitle")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_title_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_title_foot")
bs = BlockStyles

_NOTES = [
    ("The message",
     "The plan is written; now we build it, one task at a time, test first."),
    ("Timing",
     "11:30, 45 min: a 15-min demo of one full red-green-refactor cycle, practice 11:45 → 12:10 on task 1 of "
     "your own plan, 5-min debrief."),
    ("What changes",
     "Until now the agent wrote what you asked. From here, you write (or review) the test first: the test is "
     "your specification, the agent writes the code that passes it."),
    ("Ask the room",
     "« Who has already written a test before the code? »"),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        # « i » top right, alone on its line; the section title stays centred (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                pass
            with h.cell():
                st_hover_tooltip(title="Trainer notes — CalcApp v0.1 — Part 1", entries=_NOTES,
                                 position="left", width="50vw")
        with st_block(s.center_txt), st_zoom(115):
            st_write(bs.title, 'CalcApp v0.1 — Part 1', tag=t.div, toc_lvl="1", label='CalcApp v0.1 — Part 1 (test first)')
            st_space("v", "3vh")
            st_write(bs.subtitle, 'Test-first development with an agent', tag=t.div)
            st_space("v", "6vh")
            st_write(bs.timer, '11:30 · 45 min', tag=t.div)
            st_write(bs.subtitle, 'demo 15 · practice 11:45 → 12:10 · debrief 5', tag=t.div)
            st_space("v", "4vh")
            st_write(bs.foot, 'You have a plan. Now build it — one task at a time.', tag=t.div)
