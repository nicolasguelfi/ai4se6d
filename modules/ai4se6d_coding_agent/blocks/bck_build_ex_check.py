"""Slide — Exercise sheet — task 1: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


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
     "npm run test:run shows the new test passing, and git log --oneline shows test: before feat: (then "
     "refactor: if any) — at least two commits; the order is the proof that the test came first."),
    ("Mid-point (12:00)",
     "The RED test is committed. Not yet? Ask now."),
    ("Plan unclear or stuck",
     "Fallback prompts: ExpenseItem, then ExpenseForm (next two slides). Stuck: tutor window, recovery tag "
     "j2-start, raised hand."),
    ("Ahead",
     "Task 2 of the plan, same loop."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Or ask opencode",
     "Under « Done when », the same check asked to opencode (build agent): it gives the commands, runs them and "
     "shows the result. No prompt for the j2-start recovery: it starts from a new clone, outside opencode."),
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
    ("Command — git log --oneline",
     "Lists the commits of the branch you are on. --oneline = one line per commit: short id (7 characters, e.g. "
     "a1b2c3d) then the message. Newest at the TOP: « test: before feat: » in time means the feat: line is ABOVE "
     "the test: line. Long list? Space scrolls, q quits."),
    ("Symbol — test: / feat:",
     "The first word of the commit messages: test: = the commit with the test only, feat: = the commit with the "
     "code. Seeing both, in that order, proves the test came first."),
    ("Tag — j2-start",
     "A tag is a fixed label on one commit — here a checkpoint of the course: j2-start (start of day 2), j2-part1"
     " (end of Part 1), j2-v0.1 (v0.1 reference). Restarting from it uses the rescue commands two slides further "
     "(clone into a new folder, git checkout -b mywork j2-start, npm ci)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Task 1 — Am I Done?', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Task 1 — Am I Done?", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        # One row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.done_label, 'Done when'),
             ((bs.cmd, 'npm run test:run'), ' shows your new test passing, and ', (bs.cmd, 'git log --oneline'),
              ' shows ', (bs.cmd, 'test:'), ' before ', (bs.cmd, 'feat:'), ' (then ', (bs.cmd, 'refactor:'),
              ' if any) — at least two commits, e.g. ', (bs.cmd, 'test: expense with amount 0 is rejected'), ', ',
              (bs.cmd, 'feat: add expense validation'), '.')),
            ((bs.label, 'Mid-point (12:00)'), ('your RED test is committed. Not yet? Ask now.',)),
            ((bs.label, 'Plan unclear?'), ('use the ready-made prompts of the next slides: ExpenseItem first, then ExpenseForm.',)),
            ((bs.label, 'If stuck'), ('1. ', 'your tutor window', '  2. recovery tag ', (bs.cmd, 'j2-start'),
                                      '  3. raise your hand')),
            ((bs.label, 'Finished early?'), ('start task 2 of your plan, with the same steps.',)),
        ]
        # under « Done when », full width, the same check as a prompt for opencode — build agent (NG, 2026-11-25)
        prompts = {0: "Give me the commands to run the tests and show the last commits, then run them."}
        cols = "4% 22% 70% 4%"
        for i, (label, parts) in enumerate(items):
            if i:
                st_space("v", "1.2vh")
            cells = s.project.containers.rows(i + 1, cols, filled=(2, 3))[-4:]  # keeps the alternation
            with st_zoom(80), st_grid(cols=cols, gap="0 0.5vw", cell_styles=cells) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, label, tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
            if i in prompts:
                st_space("v", "0.4vh")
                st_ask_opencode(prompts[i], zoom=74, cols="4% 92% 4%")
