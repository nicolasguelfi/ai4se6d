"""Slide — Fallback prompt B — ExpenseForm."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Fallback prompt B — ExpenseForm — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_fallback_form_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_fallback_form_foot")
bs = BlockStyles


_FORM_RED = """\
Write a failing Vitest test in tests/components/ExpenseForm.test.tsx.
Render ExpenseForm, fill the labelled inputs amount (4.50),
description (Coffee), category (Food), date (2026-03-01), click
"Add Expense", and assert onSubmit was called with that data,
amount as a number. Use getByLabelText / getByRole.
Do NOT write the component. Run npm run test:run."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Fallback B: ExpenseForm', tag=t.div, toc_lvl='+1')
            st_code(s.none, code=_FORM_RED, language='text', line_numbers=False, font_size="36pt")
            st_write(
                bs.body,
                'Review: correct import paths? accessible queries? the behaviour ',
                (bs.keyword, 'you'),
                ' want?',
                tag=t.div,
            )
            st_write(
                bs.foot,
                'GREEN: same prompt as A. Mutant: remove the parseFloat on the amount.',
                tag=t.div,
            )
