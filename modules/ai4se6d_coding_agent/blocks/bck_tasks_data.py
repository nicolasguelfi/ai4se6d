"""Slide — Task — data layer (prompts)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Task — data layer (prompts) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_data_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_data_cmd")
bs = BlockStyles

_CODE_ZOOM = 94  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_DATA_RED = """\
Write a failing integration test: `routes` in a memory router at "/add",
fill amount 42.50, category Food, description Lunch (fireEvent),
click the form's "Add Expense" button, then expect the Dashboard to contain
"42.50" and "Food".
Clear localStorage before each test. Test only."""

_DATA_GREEN = """\
Make it pass: Expense type; getExpenses/saveExpenses in storage.ts
(localStorage key "calcapp-data"); Dashboard lists the expenses with
a total; AddExpense saves, then navigates to "/" with useNavigate.
Do not modify the test."""

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Show the integration-test prompts; learners use them in the "
     "13:30 exercise, after routing."),
    ("The message",
     "The second task: the data layer — an Expense type, a small storage module on localStorage, and the two "
     "pages wired to it. localStorage is enough for v0.1."),
    ("The RED prompt",
     "An INTEGRATION test this time (= several parts tested together: router, pages and storage, unlike this "
     "morning's test of one component alone): start at /add, fill the form (42.50, Food, Lunch), click the form's "
     "Add Expense button (not the menu link of the same name), and expect "
     "the Dashboard to show the expense. localStorage is cleared before each test."),
    ("The GREEN prompt",
     "Names the files and the key (calcapp-data), the functions (getExpenses / saveExpenses), the redirect to / "
     "with useNavigate — and « Do not modify the test »."),
    ("The trap",
     "The agent may keep the data in React state only: the test can pass, and the expense vanishes at the first "
     "browser refresh. The review checklist of the next slide checks it."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Prompt — data, RED",
     "An integration test: it mounts the app's routes in a memory router at /add, fills the form with fireEvent "
     "(amount 42.50, category Food, description Lunch), clicks Add, and expects the Dashboard to show « 42.50 » "
     "and « Food ». « Clear localStorage before each test » = start every test with empty storage "
     "(localStorage.clear() in a beforeEach). « Test only »."),
    ("Prompt — data, GREEN",
     "Expense type = the TypeScript description of an expense. getExpenses / saveExpenses = two functions in "
     "storage.ts that read and write the list in localStorage under the key « calcapp-data ». Dashboard lists the"
     " expenses with a total; AddExpense saves then goes back to / with useNavigate (react-router's function to "
     "change page from code). « Do not modify the test »."),
    ("Words — localStorage",
     "A small storage space of the browser, per site, that survives a page refresh: text values saved under a "
     "name (the key). Visible in the browser's developer tools (F12 → Application → Local Storage)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Task: Data Layer', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Task: Data Layer", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(94):
            st_write(
                bs.body,
                (bs.cmd, 'Expense'),
                ' type in ',
                (bs.cmd, 'src/expense.ts'),
                ', storage in ',
                (bs.cmd, 'src/storage.ts'),
                '. localStorage is enough for v0.1.',
                tag=t.div,
            )
            st_space("v", "1vh")
            st_write(bs.label, 'RED', tag=t.div)
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_DATA_RED, language='text', line_numbers=False, font_size="36pt")
            st_write(bs.label, 'GREEN', tag=t.div)
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_DATA_GREEN, language='text', line_numbers=False, font_size="36pt")
