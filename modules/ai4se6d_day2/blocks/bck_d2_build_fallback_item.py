"""Slide — Fallback prompt A — ExpenseItem."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Fallback prompt A — ExpenseItem — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_fallback_item_body")
bs = BlockStyles


_ITEM_RED = """\
Write a failing Vitest test in tests/components/ExpenseItem.test.tsx.
ExpenseItem receives an `expense` prop (id, amount, description,
category, date, createdAt) and an `onDelete` handler. It must show
the description and the amount in euros: "Lunch" and "€25.50"
for 25.50. Do NOT write the component. Run npx vitest run."""

_ITEM_GREEN = """\
Implement the minimal ExpenseItem (default export) that passes
tests/components/ExpenseItem.test.tsx. Do not modify the test."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Fallback A: ExpenseItem', tag=t.div, toc_lvl='+1')
            st_write(bs.body, 'Plan unclear or empty? Start with the canonical first feature.', tag=t.div)
            st_code(s.none, code=_ITEM_RED, language='text', line_numbers=False, font_size="36pt")
            st_code(s.none, code=_ITEM_GREEN, language='text', line_numbers=False, font_size="36pt")
