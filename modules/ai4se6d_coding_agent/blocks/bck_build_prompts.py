"""Slide — Three prompts per task — RED, GREEN, REFACTOR (build agent)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Three prompts per task — RED, GREEN, REFACTOR — styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
bs = BlockStyles

_CODE_ZOOM = 82  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_RED = """\
@docs/plan.md Take the task marked [next]. This step writes its test only.
Write a failing test for its Accept: line, in tests/, and an empty shell of the
code the test calls (exists, returns nothing yet), so the test fails on its
expected value, not on a missing file. Test what the user sees, not internal names.
Do not implement the task. Run npm run test:run and show the failure."""

_GREEN = """\
Implement the minimal code that makes the new test in tests/ pass, for the task
marked [next]. Do not change what the test checks. Run npm run test:run."""

_REFACTOR = """\
@docs/plan.md Improve the design of the code of the task marked [next], same
behaviour: e.g. extract a function, rename, remove duplication. Do not change what
the test checks; if you rename something the test uses, rename it in the test too.
Run npm run test:run."""

_NOTES = [
    ("Why « Take the task », not « Build »",
     "The first line only picks the task; the second says this step is the test only — an opening « build » would "
     "read as « write the code »."),
    ("REFACTOR prompt",
     "Same behaviour, better structure: extract a function, rename, remove duplication; what the test checks does not "
     "change (a name renamed in the code is renamed in the test too) and it stays green. Nothing to improve is a valid result: then no refactor: commit."),
    ("Trainer action",
     "Read and comment — nothing to type. Show the three prompts and the review between RED and GREEN; learners copy "
     "them in the 11:45 exercise on task 1 of their plan."),
    ("The message",
     "Each task takes three prompts, never one: RED (the test only), then GREEN (the code) once you have "
     "reviewed the test, then REFACTOR (same behaviour, better structure)."),
    ("RED prompt",
     "Points at the plan (@docs/plan.md, only the task marked [next]), asks for the failing test of its Accept: "
     "line in tests/ with an empty shell of the code, asks to test what the user sees, forbids the implementation, and asks to run the tests and show the failure."),
    ("GREEN prompt",
     "Minimal code that makes the test file pass; what the test checks must not change."),
    ("Between the two",
     "Your review of the test — the golden rule. Skip it and the test only mirrors the code."),
    ("Detail",
     "In prompts, ask for npm run test:run (one shot): npm test is watch mode (q to quit), the agent would wait."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Prompt — RED (test only)",
     "@docs/plan.md adds your plan to the agent's context; « Take the task marked [next] » picks one task (T1 this "
     "morning) and « This step writes its test only » says what to do now. « Write a failing test for its Accept: "
     "line, in tests/ » = the acceptance criteria of that task become a test that must fail now. « and an empty "
     "shell of the code the test calls … not on a missing file » = the function or component exists but returns "
     "nothing, so red comes from the expected value, not from « cannot find module ». « Test what the user sees, not internal "
     "names » = the test looks at the screen (texts, buttons, labels), so renaming code later does not break it. "
     "« Do not implement the task » forbids the code. « Run npm run test:run and show the failure » makes the agent prove the test is "
     "red."),
    ("Prompt — GREEN (minimal code)",
     "« Minimal code » = just enough for the new test to pass, nothing more. « Do not change what the test checks » "
     "forbids weakening the test to make it pass; only you change a test, when the requirement changes. « Run npm run test:run » makes the agent show the green result. "
     "Paste it only after you have read the test."),
    ("Symbol — @docs/plan.md (in opencode)",
     "@ followed by a path adds that file to the agent's context: the agent reads its content with your message. "
     "Typing @ opens a fuzzy file search; Enter or Tab picks the file. The path is relative to the project folder"
     " (docs/plan.md = file plan.md in folder docs)."),
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Three Prompts per Task (Build Agent)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Three Prompts per Task (Build Agent)", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "1.2vh")
        with st_zoom(86):
            st_write(bs.label, '1 · RED — test + empty shell', tag=t.div)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_RED, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "1.2vh")
        with st_zoom(86):
            st_write(bs.label, '2 · GREEN — once you have reviewed the test', tag=t.div)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GREEN, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "1.2vh")
        with st_zoom(86):
            st_write(bs.label, '3 · REFACTOR — same behaviour, better structure; nothing to improve is a valid result',
                     tag=t.div)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_REFACTOR, language='text', line_numbers=False, font_size="30pt")
