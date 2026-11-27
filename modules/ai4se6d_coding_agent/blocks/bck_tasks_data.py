"""Slide — Example prompts for the storage task (T3 of the reference plan; NG « ok », 2026-11-27)."""
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

_CODE_ZOOM = 84  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_DATA_RED = """\
Write a failing test in tests/storage.test.ts: loadExpenses() returns
exactly what saveExpenses() wrote, and [] for a missing key or corrupt
JSON. In tests/setup.ts, add an afterEach that clears localStorage and
restores mocks. Test only."""

_DATA_GREEN = """\
Make it pass: saveExpenses / loadExpenses in src/storage.ts, one
localStorage key "calcapp.expenses", JSON inside; reuse the Expense
type of src/expense.ts. Do not change what the test checks."""

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Show the two prompts; learners use them in the 13:30 exercise when "
     "their plan has a storage task (T3 in the reference plan)."),
    ("The message",
     "Example prompts for the storage task: a small module that saves and loads the expenses in localStorage. "
     "The Expense type already exists (T1). The pages are wired to it later, by the form and add-flow tasks (T5, "
     "T6). localStorage is enough for v0.1."),
    ("The RED prompt",
     "A unit test of the storage module alone: what is saved comes back identical, and a missing key or broken "
     "JSON gives an empty list instead of a crash. tests/setup.ts clears localStorage after each test, so tests "
     "do not see each other's data."),
    ("The GREEN prompt",
     "Names the file, the functions (saveExpenses / loadExpenses) and the key (calcapp.expenses, as in the "
     "recovery tags) — and « Do not change what the test checks »."),
    ("The trap",
     "Asking for the whole data layer at once (type, storage, pages): one big prompt, one big diff. One task = "
     "one small piece; the add flow (T6) is where a refresh must keep the expense — the review checklist of the "
     "next slide checks it."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Prompt — data, RED",
     "A test file of its own, tests/storage.test.ts: save a list, load it, compare; then load with no key, and "
     "with the key holding broken JSON — both must give []. afterEach in tests/setup.ts runs after every test: "
     "localStorage.clear() and vi.restoreAllMocks(). « Test only »."),
    ("Prompt — data, GREEN",
     "saveExpenses / loadExpenses = two functions in src/storage.ts that write and read the list in localStorage "
     "under one key, as JSON text (JSON.stringify / JSON.parse). Reusing the Expense type of T1 avoids a second, "
     "different description of an expense. « Do not change what the test checks »."),
    ("Words — localStorage",
     "A small storage space of the browser, per site, that survives a page refresh: text values saved under a "
     "name (the key). Visible in the browser's developer tools (F12 → Application → Local Storage)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Example Prompts: Save and Load (T3)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Example Prompts: Save and Load (T3)", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(94):
            st_write(
                bs.body,
                'If your plan has a storage task: saving and loading go in ',
                (bs.cmd, 'src/storage.ts'),
                ', with the ',
                (bs.cmd, 'Expense'),
                ' type of T1. Keeping the data in the browser (localStorage) is enough for v0.1.',
                tag=t.div,
            )
            st_space("v", "1vh")
            st_write(bs.label, 'RED', tag=t.div)
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_DATA_RED, language='text', line_numbers=False, font_size="36pt")
            st_write(bs.label, 'GREEN', tag=t.div)
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_DATA_GREEN, language='text', line_numbers=False, font_size="36pt")
