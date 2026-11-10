"""Shared layout — exercise sheet slides (edition 2, standard sheet P14).

Single source: the sheet data live in exercise_sheets.py; the same data give the slides (this
module) and the syllabus text (scripts/sheets_markdown.py), so slides and syllabus cannot drift.
Design: one row per field, label | content (inspired by the GAI4AS21H practicals).

A sheet takes two slides, each in its own block:
    exercise_sheet("discover", part="steps")   # goal, time, steps
    exercise_sheet("discover", part="check")   # done when, mid-point, if stuck, debrief
"""
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt

from shared_styles import Styles as s
from exercise_sheets import SHEETS

_CYCLE = Style.create(s.project.titles.caption + s.center_txt, "sheet_cycle")
_HEADING = s.project.titles.heading
_LABEL = Style.create(s.project.titles.table_label, "sheet_label")
_TEXT = Style.create(s.project.titles.table_cell, "sheet_text")
_CMD = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "sheet_cmd")
_COLS = "20% 78%"
_LABEL_CELL = Style.create(s.project.containers.table_header_cell, "sheet_label_cell")
_TEXT_CELL = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md, "sheet_text_cell"
)


def _parts(text):
    """Split a sheet string on backticks: `x` becomes monospace accent, the rest plain."""
    out = []
    for i, chunk in enumerate(text.split("`")):
        if chunk:
            out.append((_CMD, chunk) if i % 2 else chunk)
    return out


def _row(label, content):
    with st_grid(cols=_COLS, gap="6px") as g:
        with g.cell(), st_block(_LABEL_CELL):
            st_write(_LABEL, label)
        with g.cell(), st_block(_TEXT_CELL):
            if isinstance(content, list):
                with st_list(l_style=_TEXT, li_style=_TEXT, list_type=lt.ordered) as l:
                    for step in content:
                        with l.item():
                            st_write(_TEXT, *_parts(step))
            else:
                st_write(_TEXT, *_parts(content))


def exercise_sheet(key, part="steps", zoom=58):
    """Render one part of the sheet ``key`` of SHEETS: "steps" or "check"."""
    sh = SHEETS[key]
    title = sh["title"] if part == "steps" else sh["title"] + " — Check"
    label = f"Exercise sheet — {sh['title']}" + ("" if part == "steps" else " (check)")
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(zoom):
            st_write(_CYCLE, f"{sh['cycle']} · {sh['time']}", tag=t.div)
            st_write(_HEADING, title, tag=t.div, toc_lvl="+1", label=label)
            if part == "steps":
                _row("Goal", sh["goal"])
                _row("Steps", sh["steps"])
            else:
                _row("Done when", sh["done_when"])
                if sh.get("midpoint"):
                    _row("Mid-point", sh["midpoint"])
                _row("If stuck", sh["if_stuck"])
                _row("Debrief", sh["debrief"])
