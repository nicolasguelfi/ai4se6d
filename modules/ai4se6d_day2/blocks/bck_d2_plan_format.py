"""Slide — The docs/plan.md format."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Plan format styles."""
    heading = s.project.titles.heading
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "d2_fmt_closing")
bs = BlockStyles

_PLAN_MD = """\
# CalcApp v0.1 - plan

## T1 - Expense type with validation        [next]
Accept: a test rejects amount <= 0; a valid expense passes
Branch: feat/expense-type

## T2 - Save and load expenses (localStorage)   [todo]
Accept: a test saves an expense and loads it back
Branch: feat/expense-storage"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "docs/plan.md — the Format", tag=t.div, toc_lvl="+1")
        st_space("v", 0.5)
        st_code(s.none, code=_PLAN_MD, language="markdown", line_numbers=False, font_size="22pt")
        st_space("v", 0.5)
        st_write(bs.closing, "5-8 tasks, each with acceptance criteria. Exactly one [next].", tag=t.div)
