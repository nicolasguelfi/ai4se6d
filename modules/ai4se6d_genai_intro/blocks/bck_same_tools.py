"""Same Tools, Different Discipline — Day 2 opening slide.

4 short lines → flex container distributes content across full viewport height.
Font sizes calibrated so every line fits on one row at zoom 80%.
- Title: giant (112pt) → ~90pt effective — fits on one line
- Body: huge (80pt) → ~64pt effective — fits on one line
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    page = Style(
        "display:flex;flex-direction:column;justify-content:flex-start;"
        "min-height:82vh;gap:3rem;",
        "page_fill"
    )
    title = s.project.colors.primary + s.bold + s.giant
    body = s.huge
    body_bold = s.huge + s.bold
bs = BlockStyles


def build():
    with st_block(bs.page):
        st_write(bs.title, "Same Tools, Different Discipline", tag=t.div, toc_lvl="1")
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item(): st_write(bs.body, "Yesterday you explored. Today you engineer.")
            with l.item(): st_write(bs.body, "The tools did not change. Cursor is still Cursor.")
            with l.item(): st_write(bs.body_bold, "What changes is how you use it.")
