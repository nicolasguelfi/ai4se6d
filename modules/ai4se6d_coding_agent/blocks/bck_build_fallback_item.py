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

_CODE_ZOOM = 126  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_ITEM_RED = """\
Write a failing Vitest test in tests/components/ExpenseItem.test.tsx.
ExpenseItem receives an `expense` prop (id, amount, description,
category, date, createdAt) and an `onDelete` handler. It must show
the description and the amount in euros: "Lunch" and "€25.50"
for 25.50. Create only an empty ExpenseItem shell (default export
returning null). Do NOT implement it. Run npm run test:run."""

_ITEM_GREEN = """\
Implement the minimal ExpenseItem (default export) that passes
tests/components/ExpenseItem.test.tsx. Do not modify the test."""

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Only those whose plan is unclear or empty: they paste fallback A "
     "instead of their own task 1 during the 11:45 exercise."),
    ("The message",
     "Plan unclear or empty? Nobody stays blocked: start with the canonical first feature, the one of the demo."),
    ("RED prompt",
     "A failing Vitest test in tests/components/ExpenseItem.test.tsx: the component receives an expense and "
     "an onDelete handler, and must show « Lunch » and « €25.50 » for 25.50. Only an empty shell of the "
     "component exists (returns null), so the test fails on the expected text, not on a missing file."),
    ("GREEN prompt",
     "The minimal ExpenseItem (default export) that passes the test, without modifying it."),
    ("Same loop",
     "Read the test between the two prompts, two commits, mutant check — as for a task of your own plan."),
    ("Link to what follows",
     "Fallback B (ExpenseForm) is the second feature, for those who finish A."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Prompt — fallback A, RED",
     "« Write a failing Vitest test in tests/components/ExpenseItem.test.tsx » = the exact file to create (the "
     "folder is created if missing). It then describes the component's inputs (props): `expense`, an object with "
     "id, amount, description, category, date, createdAt, and `onDelete`, a function called to delete. Expected "
     "display: « Lunch » and « €25.50 » for 25.50. « Create only an empty ExpenseItem shell … Do NOT "
     "implement it » + « Run npm run test:run » = see it red on the expected text, not on a missing file."),
    ("Prompt — fallback A, GREEN",
     "« Minimal ExpenseItem (default export) » = the smallest component that passes; default export = the file's "
     "main export, imported as « import ExpenseItem from … ». « Do not modify the test » keeps your specification"
     " intact."),
    ("Words — prop, handler, .tsx",
     "A prop is a value given to a React component (like a function argument). A handler is a function the "
     "component calls when something happens (here onDelete). .tsx = a TypeScript file that contains React "
     "markup."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Fallback A: ExpenseItem', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Fallback A: ExpenseItem", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(120):
            st_write(bs.body, 'Plan unclear or empty? Start with the canonical first feature.', tag=t.div)
        st_space("v", "2vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_ITEM_RED, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "5vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_ITEM_GREEN, language='text', line_numbers=False, font_size="30pt")
