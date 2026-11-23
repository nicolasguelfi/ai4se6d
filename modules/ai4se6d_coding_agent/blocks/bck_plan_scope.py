"""Slide — v0.1 scope today, the rest later."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Scope styles."""
    heading = s.project.titles.heading
    card_title = s.project.titles.subtitle
    text = s.project.titles.table_cell
    ask = Style.create(s.project.titles.body_accent + s.center_txt, "scope_ask")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Today we build v0.1 only: add an expense with validation, list expenses with a monthly total, two pages "
     "with a navigation bar, data kept in the browser (localStorage)."),
    ("Why so small",
     "A small, fixed scope is what lets the plan fit the day: each task stays small and testable. Budgets per "
     "category, remaining budget and warnings come in later versions."),
    ("The trap",
     "Putting every idea into v0.1. Ideas that do not fit today go to « later », not into the code."),
    ("Link to what follows",
     "Your 2-3 features feed the elicitation prompt of the next slide (« My extra ideas: <yours> »)."),
    ("Ask the room",
     "« As a user, which 2-3 features would you want? » — 2 minutes, on paper."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, "v0.1 Today, the Rest Later", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — v0.1 Today, the Rest Later", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(100), st_grid(cols="5% 1fr 1fr 5%", gap="2vw") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                with st_block(s.project.containers.cell_active_bg + s.project.containers.cell_pad_md):
                    st_write(bs.card_title, "v0.1 — today", tag=t.div)
                    with st_list(l_style=bs.text, li_style=bs.text, list_type=lt.unordered,
                                 text_align="left", item_gap=0.6) as l:
                        with l.item(): st_write(bs.text, "Add an expense, with validation")
                        with l.item(): st_write(bs.text, "List expenses with a monthly total")
                        with l.item(): st_write(bs.text, "Two pages and a navigation bar")
                        with l.item(): st_write(bs.text, "Data kept in the browser (localStorage)")
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                    st_write(bs.card_title, "Later versions", tag=t.div)
                    with st_list(l_style=bs.text, li_style=bs.text, list_type=lt.unordered,
                                 text_align="left", item_gap=0.6) as l:
                        with l.item(): st_write(bs.text, "Budgets per category")
                        with l.item(): st_write(bs.text, "Remaining budget and warnings")
                        with l.item(): st_write(bs.text, "Your own ideas")
            with g.cell():
                pass  # right margin
        st_space("v", "5vh")
        with st_zoom(120):
            st_write(bs.ask, "2 minutes, on paper: 2-3 features you would want as a user.", tag=t.div)
