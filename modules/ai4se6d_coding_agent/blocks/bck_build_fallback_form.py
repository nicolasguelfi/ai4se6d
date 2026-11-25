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

_CODE_ZOOM = 90  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_FORM_RED = """\
Write a failing Vitest test in tests/components/ExpenseForm.test.tsx.
Render ExpenseForm, fill the labelled inputs amount (4.50),
description (Coffee), category (Food), date (2026-03-01), click
"Add Expense", and assert onSubmit was called with that data,
amount as a number. Use getByLabelText / getByRole.
Create only an empty ExpenseForm shell (default export returning null).
Do NOT implement it. Run npm run test:run."""

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Only those who finished fallback A: same loop on ExpenseForm "
     "during the 11:45 exercise."),
    ("The message",
     "The second fallback feature: the form that adds an expense, tested through what the user does."),
    ("RED prompt",
     "Render the form, fill the labelled inputs, click « Add Expense », and assert that onSubmit received the "
     "data with the amount as a number. Queries by label and role (getByLabelText / getByRole)."),
    ("Review the test",
     "Correct import paths? Accessible queries? The behaviour YOU want? The test is your specification."),
    ("GREEN and mutant",
     "GREEN: same prompt as fallback A. Mutant: remove the parseFloat on the amount — the test must go red."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Prompt — fallback B, RED",
     "The test renders ExpenseForm, fills the inputs found by their label (amount 4.50, description Coffee, "
     "category Food, date 2026-03-01), clicks the « Add Expense » button, and checks that the onSubmit function "
     "received that data with amount as a number (4.5, not the text « 4.50 »). « Create only an empty ExpenseForm "
     "shell … Do NOT implement it. Run npm run test:run » = see it red on the expected behaviour, not on a missing "
     "file."),
    ("Words — getByLabelText / getByRole",
     "React Testing Library queries: getByLabelText(\"Amount\") finds the input whose label says Amount; "
     "getByRole(\"button\", { name: \"Add Expense\" }) finds the button by its role and text. They find elements as a"
     " user (or a screen reader) does, so the form must have real labels."),
    ("Words — parseFloat",
     "JavaScript function that turns text into a number: parseFloat(\"4.50\") = 4.5. Form inputs always give text; "
     "removing parseFloat (the mutant) sends « 4.50 » as text and the test must go red."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Fallback B: ExpenseForm', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Fallback B: ExpenseForm", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_FORM_RED, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "2vh")
        with st_zoom(108):
            st_write(
                bs.body,
                'Review the test: are the import paths correct? Does it find the inputs by their label? Does it '
                'check the behaviour ',
                (bs.keyword, 'you'),
                ' want?',
                tag=t.div,
            )
            st_space("v", "2vh")
            st_write(
                bs.foot,
                'GREEN: “Implement the minimal ExpenseForm (default export) that passes tests/components/ExpenseForm.test.tsx. Do not change what the test checks.” Mutant: remove the parseFloat on the amount.',
                tag=t.div,
            )
