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


_RED = """\
@docs/plan.md Task 1 only. Write the failing test first, in tests/.
Do NOT write the implementation. Run npm run test:run and show the failure."""

_GREEN = """\
Implement the minimal code that makes tests/<file>.test.tsx pass.
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
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Two Prompts per Task', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Two Prompts per Task", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(110):
            st_write(bs.label, '1 · RED — test only (build agent)', tag=t.div)
        st_code(s.none, code=_RED, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "5vh")
        with st_zoom(110):
            st_write(bs.label, '2 · GREEN — once you have reviewed the test', tag=t.div)
        st_code(s.none, code=_GREEN, language='text', line_numbers=False, font_size="30pt")
        st_space("v", "5vh")
        with st_zoom(100):
            st_write(
                bs.foot,
                'In prompts, ask for npm run test:run (one shot): npm test is watch mode (q to quit), the agent would wait.',
                tag=t.div,
            )
