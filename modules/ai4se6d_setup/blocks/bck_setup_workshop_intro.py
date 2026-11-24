"""Slide — FreeSelfApp workshop opener: a first prototype by pure prompting."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Workshop opener styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "setup_ws_subtitle")
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_ws_caption")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Your first prototype, built by pure prompting: you describe, opencode writes the code."),
    ("No rules, no plan — on purpose",
     "No method is imposed this time. What works and what goes wrong is the material of the debrief."),
    ("Timing",
     "14:30-15:15: v1, the client's feature (14:45), the presentation (14:55). 15:30 presentations, 16:30 questions, "
     "16:50 wrap-up and quiz."),
    ("Ask the room",
     "« What will you build? » — one sentence each, before the first prompt."),
]


def build():
    with st_block(s.project.containers.page_fill_center_noalign):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "FreeSelfApp Workshop", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — FreeSelfApp Workshop", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(130):
            st_write(bs.subtitle, "Your first prototype — by pure prompting", tag=t.div)
        # Reused from the vibecoding module (ex_vibecoding) — no new AI image.
        st_image(uri="images/setup_freeselfapp.webp", width="65%", max_vh=68, align="center")
        with st_zoom(130):
            st_write(bs.caption, "45 min · build, change, present · no rules, no plan — on purpose", tag=t.div)
