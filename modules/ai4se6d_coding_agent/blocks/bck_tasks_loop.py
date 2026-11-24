"""Slide — The same loop for every task."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """The same loop for every task — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_loop_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_loop_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_loop_foot")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. The loop they apply to every task; they run it from 13:30 in the"
     " Part 2 exercise."),
    ("The message",
     "Every task of the afternoon follows the same six steps — the AI-TDD loop of this morning plus a branch, "
     "a review and a merge."),
    ("Branch, then RED",
     "One branch per task (feat/routing). The agent writes the test only; YOU review it — it is your spec — "
     "then commit test: …"),
    ("GREEN and the mutant",
     "Minimal code, the test untouched, commit feat: …; then break the code on purpose: a test must fail. Undo."),
    ("Review, then merge",
     "Read the agent's code with the checklists of the next slides; merge into mywork only when everything is "
     "green."),
    ("The trap",
     "Skipping the review because the tests pass: green tests say the code does what the test checks, "
     "not that the code is right."),
    ("Order",
     "Typical order routing → data → UI, but the participant's plan decides."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Same Loop, Every Task', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Same Loop, Every Task", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ('Branch: ', (bs.cmd, 'git switch -c feat/routing')),
            ('RED: test only → ', (bs.keyword, 'you'), ' review → commit ', (bs.cmd, 'test: …')),
            ('GREEN: minimal code, test untouched → commit ', (bs.cmd, 'feat: …')),
            ('Mutant check → undo',),
            ("Review the agent's code (checklists ahead)",),
            ('Merge into ', (bs.cmd, 'mywork'), ' only when green'),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(100), st_grid(cols=cols, gap="2.5vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(100):
            st_write(bs.foot, "Typical order: routing → data → UI. Follow your plan's order.", tag=t.div)
