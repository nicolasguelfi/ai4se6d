"""Slide — The plan-then-build workflow and when to use it."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Workflow styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    rule = Style.create(s.project.titles.body + s.center_txt, "pw_rule")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_NOTES = [
    ("The message",
     "Think first, then code: five steps that keep you in control of what the agent builds."),
    ("The loop",
     "Plan the whole feature with its constraints; review the plan (files, order, tests included?); push back; "
     "switch to build for step 1 only; check git diff and the tests, commit, then the next step."),
    ("Why step by step",
     "One step at a time keeps each diff small enough to review, and each commit is a point you can return to."),
    ("When to plan",
     "When the task touches 2+ files or needs a where / how decision. A typo? Just build."),
    ("The trap",
     "Approving the plan without reading it. Pushing back (« tests first », « split this step ») is the point of "
     "the plan stage."),
    ("Ask the room",
     "« What would you push back on in a plan that has no test step? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "Think First, Then Code", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Think First, Then Code", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ((bs.keyword, "Shift+Tab → plan"), ": describe the whole feature and its constraints"),
            ((bs.keyword, "Review"), ": files, order, tests included?"),
            ((bs.keyword, "Push back"), ": “tests first”, “split this step”"),
            ((bs.keyword, "Shift+Tab → build"), ": “implement step 1 only”"),
            ((bs.keyword, "git diff"), ", tests, commit — then the next step"),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(110), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(110), st_grid(cols="5% 90% 5%") as m:
            with m.cell():
                pass  # left margin
            with m.cell():
                with st_block(s.project.containers.callout):
                    st_write(
                        bs.rule, "Plan first when the task touches 2+ files or needs a ",
                        (bs.keyword, "where / how"), " decision. A typo? Just build.", tag=t.div,
                    )
            with m.cell():
                pass  # right margin
