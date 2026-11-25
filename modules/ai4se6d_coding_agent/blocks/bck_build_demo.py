"""Slide — Live demo — one full red-green-refactor cycle in opencode."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Live demo — one full red-green-refactor cycle in opencode — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_demo_body")
    keyword = s.bold + s.project.colors.highlight
    number = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_demo_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_demo_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_demo_foot")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Live demo — you type it in opencode on CalcApp. One full red-green-refactor cycle on ExpenseItem in "
     "10 min max; learners repeat every step at 11:45 on task 1 of their plan."),
    ("The message",
     "One full cycle, live, in 10 minutes or less, on the demo feature: ExpenseItem shows « Lunch » and « €25.50 »."),
    ("RED",
     "Ask the build agent for the test plus an empty ExpenseItem shell (returns null), read the test, run npm run "
     "test:run: it fails on the expected value (« Lunch » and « €25.50 » not found), not on a missing file."),
    ("Empty shell first",
     "« Do NOT write the component » alone makes the test fail for the wrong reason: the import finds no file, so "
     "red only says « missing ». With an empty shell (the component exists and returns null), the test runs and "
     "fails on the expected value: red then proves the test checks the behaviour."),
    ("GREEN",
     "Ask for the minimal code, without touching the test; npm run test:run goes green."),
    ("The proof",
     "Break the code on purpose: a test must fail. Then two commits — test: … first, then feat: …"),
    ("Link to what follows",
     "Each step of the demo returns in the exercise on task 1 of your own plan."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — npm run test:run",
     "npm run (name) runs a script written in package.json; test:run = « vitest run »: Vitest runs every test "
     "file once (in tests/), prints ✓ or ✗ per test and a summary (« Tests 4 passed »), then gives the prompt "
     "back. Green = all pass; red = at least one fails, with the expected and the received value. Not to be "
     "confused with npm test (= vitest): in your terminal it stays in watch mode and re-runs at every save (q "
     "quits)."),
    ("Key — build agent (Shift+Tab)",
     "Step 1 uses the build agent, the one that edits files and runs commands; Shift+Tab switches between plan "
     "and build in opencode. Its name is shown under the input box."),
    ("Symbol — test: / feat: / fix: / docs: (commit messages)",
     "Not commands: the first word of a commit message (the « Conventional Commits » habit). test: = only tests, "
     "feat: = a new feature, fix: = a bug fix, docs: = documentation. The … on the slide is your own short "
     "description. A commit is a saved snapshot of the project, with that message."),
    ("Command — git add -A && git commit -m \"test: …\"",
     "How to make the commit. git add -A puts every change (new, modified, deleted files) in the staging area, "
     "the list of what goes into the next commit; -A = all. git commit -m \"…\" saves that snapshot; -m = the "
     "message, in quotes. && = run the second command only if the first succeeded. You can also ask the agent to "
     "commit, then check with git log --oneline."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Live Demo: One Full Cycle', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Live Demo: One Full Cycle", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(100):
            st_write(bs.timer, '≤ 10 min', tag=t.div)
        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ((bs.keyword, 'build'), ' agent: the ', (bs.keyword, 'test'), ' + an ', (bs.keyword, 'empty shell'),
             ' of the component → read the test'),
            ((bs.cmd, 'npm run test:run'), ' → ', (bs.keyword, 'RED'), ' on the expected value, not a missing file'),
            ('Ask for the minimal code — ', (bs.keyword, 'do not touch the test')),
            ((bs.cmd, 'npm run test:run'), ' → ', (bs.keyword, 'GREEN')),
            ('Break the code on purpose → a test must fail',),
            ('Two commits: ', (bs.cmd, 'test: …'), ' first, then ', (bs.cmd, 'feat: …')),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(96), st_grid(cols=cols, gap="1.4vh 0.5vw", cell_styles=cells) as g:
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
        with st_zoom(100):
            st_write(bs.foot, 'Demo feature: ExpenseItem shows “Lunch” and “€25.50”.', tag=t.div)
