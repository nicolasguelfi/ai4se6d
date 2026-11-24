"""Slide — Two prompts per task — RED then GREEN."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Two prompts per task — RED then GREEN — styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_prompts_foot")
bs = BlockStyles

_CODE_ZOOM = 113  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_RED = """\
@docs/plan.md Task 1 only. Write the failing test first, in tests/.
Do NOT write the implementation. Run npm run test:run and show the failure."""

_GREEN = """\
Implement the minimal code that makes the new test in tests/ pass.
Do not modify the test file. Run npm run test:run."""

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Show the two prompts and the review between them; learners copy "
     "them in the 11:45 exercise on task 1 of their plan."),
    ("The message",
     "Each task takes two prompts, never one: RED (the test only), then GREEN (the code) once you have "
     "reviewed the test."),
    ("RED prompt",
     "Points at the plan (@docs/plan.md, Task 1 only), asks for the failing test in tests/, forbids the "
     "implementation, and asks to run the tests and show the failure."),
    ("GREEN prompt",
     "Minimal code that makes the test file pass; the test file must not be modified."),
    ("Between the two",
     "Your review of the test — the golden rule. Skip it and the test only mirrors the code."),
    ("Detail",
     "In prompts, ask for npm run test:run (one shot): npm test is watch mode (q to quit), the agent would wait."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Prompt — RED (test only)",
     "@docs/plan.md adds your plan to the agent's context; « Task 1 only » limits it to one task. « Write the "
     "failing test first, in tests/ » = a test that must fail now, because the code does not exist. « Do NOT "
     "write the implementation » forbids the code. « Run npm run test:run and show the failure » makes the agent "
     "prove the test is red."),
    ("Prompt — GREEN (minimal code)",
     "« Minimal code » = just enough for the new test to pass, nothing more. « Do not modify the test file » "
     "forbids changing the test to make it pass. « Run npm run test:run » makes the agent show the green result. "
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
                st_write(bs.heading, 'Two Prompts per Task', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Two Prompts per Task", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(120):
            st_write(bs.label, '1 · RED — test only (build agent)', tag=t.div)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_RED, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "5vh")
        with st_zoom(120):
            st_write(bs.label, '2 · GREEN — once you have reviewed the test', tag=t.div)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GREEN, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "5vh")
        with st_zoom(120):
            st_write(
                bs.foot,
                'In prompts, ask for npm run test:run (one shot): npm test is watch mode (q to quit), the agent would wait.',
                tag=t.div,
            )
