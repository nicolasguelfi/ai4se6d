"""Slide — Task — data layer (prompts)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Task — data layer (prompts) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_p2_data_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_p2_data_cmd")
bs = BlockStyles


_DATA_RED = """\
Write a failing integration test: `routes` in a memory router at "/add",
fill amount 42.50, category Food, description Lunch (fireEvent),
click Add, then expect the Dashboard to contain "42.50" and "Food".
Clear localStorage before each test. Test only."""

_DATA_GREEN = """\
Make it pass: Expense type; getExpenses/saveExpenses in storage.ts
(localStorage key "calcapp-data"); Dashboard lists the expenses with
a total; AddExpense saves, then navigates to "/" with useNavigate.
Do not modify the test."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Task: Data Layer', tag=t.div, toc_lvl='+1')
            st_write(
                bs.body,
                (bs.cmd, 'Expense'),
                ' type in ',
                (bs.cmd, 'src/types/expense.ts'),
                ', storage in ',
                (bs.cmd, 'src/utils/storage.ts'),
                '. localStorage is enough for v0.1.',
                tag=t.div,
            )
            st_write(bs.label, 'RED', tag=t.div)
            st_code(s.none, code=_DATA_RED, language='text', line_numbers=False, font_size="36pt")
            st_write(bs.label, 'GREEN', tag=t.div)
            st_code(s.none, code=_DATA_GREEN, language='text', line_numbers=False, font_size="36pt")
