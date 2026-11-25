"""Slide — Section — CalcApp v0.1 Part 2."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Section — CalcApp v0.1 Part 2 — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "tasks_title_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "tasks_title_subtitle")
    timer = Style.create(s.project.titles.stat + s.center_txt, "tasks_title_timer")
bs = BlockStyles


_NOTES = [
    ("The message",
     "Part 2 of CalcApp v0.1: the next tasks of the participant's own plan — routing, data layer, minimal UI — "
     "each with the same test-first loop as this morning."),
    ("Timing",
     "75 minutes from 13:15: 15 to re-start after lunch, practice from 13:30 to 14:20, 10 minutes of debrief."),
    ("Driven by your plan",
     "The plan written this morning (docs/plan.md) decides the order; the prompts on the next slides are there "
     "when the plan's wording is unclear."),
    ("Link to what follows",
     "At 14:30 the code produced here is the material of the AI-assisted code review section."),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            # title and « i » on the same line (NG, 2026-11-23: same recipes as the intro module)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell():
                    st_write(bs.title, 'CalcApp v0.1 — Part 2', tag=t.div, toc_lvl="1",
                             label='CalcApp v0.1 — Part 2 (routing, data, UI)')
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — CalcApp v0.1, Part 2", entries=_NOTES,
                                     position="left", width="50vw")
            st_space("v", 2)
            with st_zoom(120):
                st_write(bs.subtitle, 'Routing, data layer, minimal UI — driven by your plan', tag=t.div)
                st_space("v", 3)
                st_write(bs.timer, '13:15 · 75 min', tag=t.div)
                st_space("v", "2vh")
                st_write(bs.subtitle, 'Restart: 15 min · Practice: 13:30 to 14:20 · Debrief: 10 min', tag=t.div)
