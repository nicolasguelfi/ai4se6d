"""Slide — Introducing CalcApp and its core features."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """CalcApp intro styles."""
    heading = s.project.titles.heading
    pitch = Style.create(s.project.titles.body_accent + s.center_txt, "d2_calc_pitch")
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    note = Style.create(s.project.titles.caption + s.center_txt, "d2_calc_note")
bs = BlockStyles

_FEATURES = [
    ("Add an expense", "amount, category, date"),
    ("List expenses", "filter by month and category"),
    ("Set a monthly budget", "per category, e.g. 300 EUR for groceries"),
    ("See what is left", "warn when close to or over budget"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "CalcApp: Budget Tracker", tag=t.div, toc_lvl="+1")
        st_write(bs.pitch, "Track expenses, set budgets, see what is left.", tag=t.div)
        st_space("v", 0.5)
        with st_grid(cols="35% 65%", gap="4px") as g:
            for h in ("Feature", "What it means"):
                with g.cell():
                    with st_block(s.project.containers.table_header_cell):
                        st_write(bs.th, h)
            for feature, detail in _FEATURES:
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(bs.tl, feature)
                with g.cell():
                    with st_block(s.project.containers.table_normal_cell):
                        st_write(bs.td, detail)
        st_write(bs.note, "React + TypeScript in the browser, built test-first.", tag=t.div)
