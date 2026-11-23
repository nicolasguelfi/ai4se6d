"""Slide — The docs/plan.md format."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Plan format styles."""
    heading = s.project.titles.heading
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "fmt_closing")
bs = BlockStyles

_PLAN_MD = """\
# CalcApp v0.1 - plan

## T1 - Expense type with validation        [next]
Accept: a test rejects amount <= 0; a valid expense passes
Branch: feat/expense-type

## T2 - Save and load expenses (localStorage)   [todo]
Accept: a test saves an expense and loads it back
Branch: feat/expense-storage"""

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Show the docs/plan.md format; learners have the build agent write theirs"
     " in the plan exercise (step 4)."),
    ("The message",
     "The plan lives in the repository, in docs/plan.md, in one fixed format: the agent and you read the same "
     "file in every session."),
    ("The format",
     "One heading per task (T1, T2, …) with a status ([next], [todo]), an Accept line with the acceptance "
     "criteria, and the Branch on which the task will be built."),
    ("The rules",
     "5-8 tasks, each with acceptance criteria. Exactly one [next]: the task you build now."),
    ("Link to what follows",
     "This afternoon the RED prompt starts with « @docs/plan.md Task 1 only »: the plan drives the build."),
    ("Ask the room",
     "« Why only one [next] at a time? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, "docs/plan.md — the Format", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — docs/plan.md — the Format", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        st_code(s.none, code=_PLAN_MD, language="markdown", line_numbers=False, font_size="34pt")
        st_space("v", "3vh")
        with st_zoom(115):
            st_write(bs.closing, "5-8 tasks, each with acceptance criteria. Exactly one [next].", tag=t.div)
