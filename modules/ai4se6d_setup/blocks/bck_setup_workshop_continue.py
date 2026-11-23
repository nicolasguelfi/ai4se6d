"""Slide — FreeSelfApp part 2 (after the break): keep going."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Part 2 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
bs = BlockStyles

_NOTES = [
    ("The message",
     "After the break, the same app, one step further: one feature you really want, one file explained, "
     "a commit after each working step, notes kept up to date."),
    ("Explain one file",
     "Ask the agent to explain one file of YOUR app — do you get it? This is the first time the participants "
     "look at the code they did not write."),
    ("Commit rhythm",
     "One commit after each working step: a broken next prompt then costs one step, not the afternoon."),
    ("Timing",
     "Mid-point at 15:50 (1 new feature + 1 commit); at 16:10 last commit and notes ready for the 16:15 debrief."),
    ("Ask the room",
     "« Who understood the file the agent explained? Who would dare change it by hand? »"),
]

_ITEMS = [
    ("Add ", (bs.keyword, "one feature"), " you really want"),
    ("Ask the agent to ", (bs.keyword, "explain one file"), " — do you get it?"),
    ((bs.keyword, "Commit"), " after each working step"),
    ("Update ", (bs.keyword, "notes.md")),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Part 2 — Keep Going", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Part 2 — Keep Going", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One row per task, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(110):
            with st_grid(cols=cols, gap="6vh 0.5vw", cell_styles=cells) as g:
                for parts in _ITEMS:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "6vh")
            with st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=s.project.containers.row_cell_left) as g:
                for label, text in [("Mid-point (15:50): ", "1 new feature + 1 commit."),
                                    ("16:10: ", "last commit, notes ready for the debrief.")]:
                    with g.cell():
                        pass
                    with g.cell():
                        st_write(bs.body, (bs.label, label), text, tag=t.div)
                    with g.cell():
                        pass
