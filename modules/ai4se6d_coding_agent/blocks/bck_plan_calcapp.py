"""Slide — Introducing CalcApp and its core features."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """CalcApp intro styles."""
    heading = s.project.titles.heading
    pitch = Style.create(s.project.titles.body_accent + s.center_txt, "calc_pitch")
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    note = Style.create(s.project.titles.caption + s.center_txt, "calc_note")
bs = BlockStyles

_FEATURES = [
    ("Add an expense", "amount, category, date"),
    ("List expenses", "filter by month and category"),
    ("Set a monthly budget", "per category, e.g. 300 EUR for groceries"),
    ("See what is left", "warn when close to or over budget"),
]

_NOTES = [
    ("The message",
     "CalcApp is the budget tracker participants build today: track expenses, set budgets, see what is left."),
    ("Four features",
     "Add an expense; list expenses with filters; set a monthly budget per category; see what is left, with a "
     "warning when close to or over budget."),
    ("The stack",
     "React + TypeScript in the browser, built test-first — the stack pinned in the starter's AGENTS.md."),
    ("Why this app",
     "Small enough for one day, yet it has data, rules (budgets, warnings) and pages: enough to plan, test and "
     "review for real."),
    ("Ask the room",
     "« Which of the four features hides the most decisions? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "CalcApp: Budget Tracker", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — CalcApp: Budget Tracker", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(128):
            st_write(bs.pitch, "Track expenses, set budgets, see what is left.", tag=t.div)
        st_space("v", "3vh")

        # Header row, then one row per feature, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 32% 58% 5%"
        base = s.project.containers.row_cell_left
        head = [base, s.project.containers.table_header_cell, s.project.containers.table_header_cell, base]
        cells = head + s.project.containers.rows(len(_FEATURES), cols, filled=(2, 3))
        with st_zoom(123), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for h in ("", "Feature", "What it means", ""):
                with g.cell():
                    if h:
                        st_write(bs.th, h)
            for feature, detail in _FEATURES:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.tl, feature)
                with g.cell():
                    st_write(bs.td, detail)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(128):
            st_write(bs.note, "React + TypeScript in the browser, built test-first.", tag=t.div)
