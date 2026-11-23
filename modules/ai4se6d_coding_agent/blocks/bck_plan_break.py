"""Slide — Morning break (10:45 - 11:00)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Break slide styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "break_title")
    time = Style.create(s.project.titles.stat_hero, "break_time")
    body = Style.create(s.project.titles.body + s.center_txt, "break_body")
    keyword = s.project.titles.keyword
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine, before leaving. Everyone checks git status and commits or restores what "
     "the try-its left, so the workshop starts clean at 11:00."),
    ("The message",
     "Break from 10:45, back at 11:00 for the planning workshop."),
    ("Before leaving",
     "Each participant checks git status: a clean working tree, or commit / restore what is pending. The try-its "
     "of the opencode session may have left changes."),
    ("Why it matters",
     "The planning workshop starts from a clean state: the plan you commit drives your afternoon."),
    ("Next",
     "Your own plan for CalcApp v0.1."),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        # title and « i » on the same line (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="5% 90% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                pass  # balances the « i » column so the title stays centred
            with h.cell():
                st_write(bs.title, "Break", tag=t.div, toc_lvl="1", label="Break (10:45)")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Break", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(130):
            st_write(bs.time, "11:00", tag=t.div)
        st_space("v", "4vh")
        with st_zoom(120):
            st_write(bs.body, "Before you leave: ", (bs.keyword, "git status"), " clean? Commit or restore.", tag=t.div)
            st_space("v", "2vh")
            st_write(bs.body, "Next: your own plan for CalcApp v0.1.", tag=t.div)
