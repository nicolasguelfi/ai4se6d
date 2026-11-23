"""Slide — Fallback prompt B — ExpenseForm."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Fallback prompt B — ExpenseForm — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_fallback_form_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_fallback_form_foot")
bs = BlockStyles


_FORM_RED = """\
Write a failing Vitest test in tests/components/ExpenseForm.test.tsx.
Render ExpenseForm, fill the labelled inputs amount (4.50),
description (Coffee), category (Food), date (2026-03-01), click
"Add Expense", and assert onSubmit was called with that data,
amount as a number. Use getByLabelText / getByRole.
Do NOT write the component. Run npm run test:run."""

_NOTES = [
    ("The message",
     "The second fallback feature: the form that adds an expense, tested through what the user does."),
    ("RED prompt",
     "Render the form, fill the labelled inputs, click « Add Expense », and assert that onSubmit received the "
     "data with the amount as a number. Queries by label and role (getByLabelText / getByRole)."),
    ("Review the test",
     "Correct import paths? Accessible queries? The behaviour YOU want? The test is your specification."),
    ("GREEN and mutant",
     "GREEN: same prompt as fallback A. Mutant: remove the parseFloat on the amount — the test must go red."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Fallback B: ExpenseForm', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Fallback B: ExpenseForm", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        st_code(s.none, code=_FORM_RED, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "5vh")
        with st_zoom(125):
            st_write(
                bs.body,
                'Review: correct import paths? accessible queries? the behaviour ',
                (bs.keyword, 'you'),
                ' want?',
                tag=t.div,
            )
            st_space("v", "3vh")
            st_write(
                bs.foot,
                'GREEN: same prompt as A. Mutant: remove the parseFloat on the amount.',
                tag=t.div,
            )
