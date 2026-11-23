"""Slide — Exercise sheet — task 1: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise sheet — task 1: done when, mid-point, if stuck — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_ex_check_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_ex_check_cmd")
    done_label = Style.create(s.bold + s.project.colors.success, "build_ex_check_done")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Same exercise: they check themselves against « Done when »; walk "
     "around at the 12:00 mid-point and ask who has not committed the RED test."),
    ("The message",
     "Participants check themselves: when they are done, where they should be at 12:00, what to do if stuck "
     "or ahead."),
    ("Done when",
     "npm run test:run shows the new test passing, and git log --oneline shows test: before feat: — the proof "
     "that the test came first."),
    ("Mid-point (12:00)",
     "The RED test is committed. Not yet? Ask now."),
    ("Plan unclear or stuck",
     "Fallback prompts: ExpenseItem, then ExpenseForm (next two slides). Stuck: tutor window, recovery tag "
     "j2-start, raised hand."),
    ("Ahead",
     "Task 2 of the plan, same loop."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Task 1 — Am I Done?', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Task 1 — Am I Done?", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        # One row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.done_label, 'Done when'),
             ((bs.cmd, 'npm run test:run'), ' shows your new test passing, and ', (bs.cmd, 'git log --oneline'),
              ' shows ', (bs.cmd, 'test:'), ' before ', (bs.cmd, 'feat:'), '.')),
            ((bs.label, 'Mid-point (12:00)'), ('your RED test is committed. Not yet? Ask now.',)),
            ((bs.label, 'Plan unclear?'), ('use the fallback prompts: ExpenseItem, then ExpenseForm.',)),
            ((bs.label, 'If stuck'), ('1. ', 'your tutor window', '  2. recovery tag ', (bs.cmd, 'j2-start'),
                                      '  3. raise your hand')),
            ((bs.label, 'Ahead?'), ('task 2 of your plan, same loop.',)),
        ]
        cols = "5% 22% 68% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(95), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for label, parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, label, tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
