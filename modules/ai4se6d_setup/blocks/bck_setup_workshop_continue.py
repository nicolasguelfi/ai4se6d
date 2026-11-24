"""Slide — FreeSelfApp iteration 2 (14:45): the client wants one more feature (NG, 2026-11-24)."""
# @guideline: maximize-viewport
import streamlit as st
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Iteration 2 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
bs = BlockStyles

# The menu shown on the slide: generic features any small personal web app can take (NG, 2026-11-24:
# the coding agent may already have added the one announced, e.g. an export — then the learner picks another).
_MENU = [
    "data survives a page reload",
    "export to a file (CSV or JSON)",
    "search or filter the list",
    "edit an existing item",
    "undo the last action",
    "clear error messages on bad input",
    "a summary: counts or totals",
    "works on a phone screen",
]

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. At 14:45 announce ONE extra feature for everybody (e.g. « the data must "
     "survive a page reload »). Whoever already has it picks another one from the menu on the slide."),
    ("The message",
     "A real client always asks for more once they see v1. The point is not the feature: it is whether v1 still "
     "works afterwards, and who checks it."),
    ("Menu — more ideas if needed",
     "Import a file; sort by any column; tags or categories; confirm before delete; dark mode toggle; keyboard "
     "shortcuts; two languages (EN/FR); works offline; a chart of the data; share a link to one item."),
    ("What to watch while you walk around",
     "Does anyone re-test v1 before committing? Does anyone read the diff? Does the agent rewrite everything for a "
     "small feature? Note it for the questions at 16:30."),
    ("Timing",
     "14:45 feature announced · 14:55 feature done + commit · then iteration 3, the presentation."),
]

_ITEMS = [
    ("The client wants ", (bs.keyword, "one more feature"), " — the trainer names it"),
    ("Already there? ", (bs.keyword, "Pick another"), " from the menu below (open it)"),
    ("Check ", (bs.keyword, "v1 still works"), ", then ", (bs.keyword, "commit")),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Iteration 2 — The Client Wants More", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Iteration 2 — The Client Wants More", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One row per task, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(105):
            with st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
                for parts in _ITEMS:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
        st_space("v", "3vh")
        # Menu in a collapsed accordion: the trainer opens it only when needed (NG, 2026-11-24).
        # st.expander is interactivity (allowed); its content stays stx.
        with st_zoom(90), st.expander("**Menu — other features to pick from**", expanded=False):
            with st_grid(cols="1fr 1fr", gap="1vh 3vw", cell_styles=s.project.containers.row_cell_left) as g:
                for item in _MENU:
                    with g.cell():
                        st_write(bs.body, "• ", item, tag=t.div)
        st_space("v", "3vh")
        with st_zoom(100):
            st_write(bs.body, (bs.label, "14:55: "), "feature done + commit.", tag=t.div)
