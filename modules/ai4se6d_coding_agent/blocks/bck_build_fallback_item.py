"""Slide — Fallback prompt A — ExpenseItem."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Fallback prompt A — ExpenseItem — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_fallback_item_body")
bs = BlockStyles


_ITEM_RED = """\
Write a failing Vitest test in tests/components/ExpenseItem.test.tsx.
ExpenseItem receives an `expense` prop (id, amount, description,
category, date, createdAt) and an `onDelete` handler. It must show
the description and the amount in euros: "Lunch" and "€25.50"
for 25.50. Do NOT write the component. Run npm run test:run."""

_ITEM_GREEN = """\
Implement the minimal ExpenseItem (default export) that passes
tests/components/ExpenseItem.test.tsx. Do not modify the test."""

_NOTES = [
    ("The message",
     "Plan unclear or empty? Nobody stays blocked: start with the canonical first feature, the one of the demo."),
    ("RED prompt",
     "A failing Vitest test in tests/components/ExpenseItem.test.tsx: the component receives an expense and "
     "an onDelete handler, and must show « Lunch » and « €25.50 » for 25.50. The component is not written."),
    ("GREEN prompt",
     "The minimal ExpenseItem (default export) that passes the test, without modifying it."),
    ("Same loop",
     "Read the test between the two prompts, two commits, mutant check — as for a task of your own plan."),
    ("Link to what follows",
     "Fallback B (ExpenseForm) is the second feature, for those who finish A."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Fallback A: ExpenseItem', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Fallback A: ExpenseItem", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(110):
            st_write(bs.body, 'Plan unclear or empty? Start with the canonical first feature.', tag=t.div)
        st_space("v", "2vh")
        st_code(s.none, code=_ITEM_RED, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "5vh")
        st_code(s.none, code=_ITEM_GREEN, language='text', line_numbers=False, font_size="30pt")
