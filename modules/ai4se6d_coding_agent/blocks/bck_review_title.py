"""Slide — Section — AI-assisted code review."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Section — AI-assisted code review — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "review_title_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "review_title_subtitle")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_title_timer")
bs = BlockStyles


_NOTES = [
    ("The message",
     "30 minutes from 14:30 on reviewing code written with an agent: the code works — is it good, and how do "
     "you know?"),
    ("The arc of the section",
     "Why review matters more with AI (speed paradox, scale), what review finds that tests miss, how much code "
     "per review, what AI review sees and misses, then prompts, triage and the reviewer's judgment."),
    ("Material",
     "The participants review their own CalcApp v0.1 code from Part 2 — or the reference tag j2-v0.1."),
    ("Ask the room",
     "« How did you decide this morning that the agent's code was good enough to merge? »"),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            # title and « i » on the same line (NG, 2026-11-23: same recipes as the intro module)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell():
                    st_write(bs.title, 'AI-Assisted Code Review', tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — AI-Assisted Code Review", entries=_NOTES,
                                     position="left", width="50vw")
            st_space("v", 2)
            with st_zoom(150):
                st_write(bs.subtitle, 'Your code works. Is it good? How do you know?', tag=t.div)
                st_space("v", 3)
                st_write(bs.timer, '14:30 · 30 min', tag=t.div)
