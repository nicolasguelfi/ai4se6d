"""Slide — The four areas of Git (diagram)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Diagram slide styles."""
    heading = s.project.titles.heading
    caption = Style.create(s.project.titles.body + s.center_txt, "areas_caption")
    keyword = s.project.titles.keyword
bs = BlockStyles


_NOTES = [
    ("The message",
     "A change goes through areas before it is saved in the history: you choose what goes into the next snapshot."),
    ("Read the diagram",
     "git add moves a change into the staging area — it chooses what goes into the next snapshot; git commit takes "
     "that snapshot into the repository."),
    ("Why it matters with an agent",
     "The agent may change many files; staging lets you commit only the changes you have reviewed and approved."),
    ("The trap",
     "Thinking that a saved file is a committed file: until git commit, the change is not in the history."),
    ("Ask the room",
     "« After git add, where is your change? And after git commit? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "Where Your Changes Live", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Where Your Changes Live", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", 1)
        st_image(uri="images/am/bck_git_areas_image_00.png", width="100%", max_vh=72, align="center")
        st_space("v", 1)
        st_write(
            bs.caption, (bs.keyword, "git add"), " chooses what goes into the next snapshot — ",
            (bs.keyword, "git commit"), " takes it.", tag=t.div,
        )
