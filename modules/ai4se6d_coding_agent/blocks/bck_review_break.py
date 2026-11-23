"""Slide — Afternoon break."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Afternoon break — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "review_break_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "review_break_subtitle")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_break_timer")
bs = BlockStyles

_NOTES = [
    ("The message",
     "A 15-minute break, 15:00 → 15:15. Right after it, everyone reviews the diff of everything they changed "
     "today."),
    ("Before the break",
     "Make sure your work is committed: the review exercise starts from git diff j2-start on your mywork branch."),
    ("After the break",
     "The review exercise (35 min): run the review prompt with the plan agent, triage in docs/review.md, fix "
     "2-3 HIGH/MEDIUM findings test first, refuse at least one with a reason."),
    ("Ask the room",
     "« Who is not yet at a green test suite? Tell me now, before the review starts. »"),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            # title and « i » on the same line (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(130):
                    st_write(bs.title, 'Break', tag=t.div, toc_lvl="1", label='Break (15:00)')
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — Break", entries=_NOTES,
                                     position="left", width="50vw")
            st_space("v", "5vh")
            with st_zoom(130):
                st_write(bs.subtitle, "Next: you review today's diff", tag=t.div)
            st_space("v", "6vh")
            with st_zoom(150):
                st_write(bs.timer, '15:00 → 15:15', tag=t.div)
