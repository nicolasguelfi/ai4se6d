"""Slide — Try it: write and commit docs/plan.md (steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise steps styles."""
    heading = s.project.titles.heading
    timer = Style.create(s.project.titles.stat + s.center_txt, "plan_ex_timer")
    step = s.project.titles.table_cell
    keyword = s.project.titles.table_label
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine, 20 min. Everyone elicits with the plan agent, splits into 5-8 tasks and "
     "commits docs/plan.md on mywork; walk around."),
    ("The message",
     "20 minutes, one deliverable: docs/plan.md committed on your mywork branch."),
    ("The steps",
     "Plan agent first (elicitation prompt, answer its questions, split into 5-8 atomic tasks, tests first). "
     "Then the build agent writes the file in the slide format. You edit, mark T1 [next], stage, read the "
     "staged diff, commit."),
    ("The step not to skip",
     "Push back at least once: too big? not testable? The plan is yours, not the agent's."),
    ("Why git diff --staged",
     "A new file is untracked: git diff ignores it. git add first, then git diff --staged shows what you commit."),
    ("Link to what follows",
     "Task 1 of this plan is the exercise of the next part: test first, on its own branch."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, "Try It: Your docs/plan.md", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Try It: Your docs/plan.md", entries=_NOTES,
                                 position="left", width="50vw")
        st_write(bs.timer, "20 min · goal: a committed plan", tag=t.div)
        st_space("v", "1vh")
        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ((bs.keyword, "git switch mywork"), ", ", (bs.keyword, "opencode"), ", ", (bs.keyword, "Shift+Tab → plan")),
            ("Paste the elicitation prompt, answer its questions",),
            ("“Split into 5-8 atomic tasks, tests first, with acceptance criteria.”",),
            ("Push back at least once: too big? not testable?",),
            ((bs.keyword, "Shift+Tab → build"), ": “Write docs/plan.md in the slide format.”"),
            ("Edit, mark T1 ", (bs.keyword, "[next]"), ", ", (bs.keyword, "git add"), " it, ", (bs.keyword, "git diff --staged")),
            ((bs.keyword, "git commit -m \"docs: v0.1 plan\""),),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(115), st_grid(cols=cols, gap="1.2vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.step + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.step, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
