"""Slide — Presentations (15:30): 9 × 6 min on Google Meet, all questions at 16:30 (NG, 2026-11-24)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Presentations slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    warn = s.bold + s.project.colors.highlight
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — each one presents. Call the names in order, time 6 minutes strictly, no questions now. "
     "Fill your observation grid (see « Iteration 3 » tooltip) while they speak."),
    ("Timing",
     "15:30 → 16:30: 9 × 6 min + ~30 s to switch the shared screen. 16:30: questions on any project."),
    ("Meet",
     "Each presenter shares the browser window (or the VM window). Everyone else stays muted, speakers off."),
]

_ITEMS = [
    ((bs.keyword, "6 minutes"), " each — strict"),
    ((bs.warn, "No questions now"), " — note yours, on ANY project"),
    ("All questions together at ", (bs.keyword, "16:30")),
    ("Share your screen on ", (bs.keyword, "Google Meet"), " when the trainer calls you"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Presentations", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Presentations", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(115):
            with st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
                for parts in _ITEMS:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
