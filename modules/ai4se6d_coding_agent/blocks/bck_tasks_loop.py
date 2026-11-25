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
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent
                       + Style("white-space: nowrap;", "tasks_loop_cmd_nowrap"), "tasks_loop_cmd")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. The loop they apply to every task; they run it from 13:30 in the"
     " Part 2 exercise."),
    ("The message",
     "Every task of the afternoon follows the same seven steps, on two slides — the AI-TDD loop of this morning "
     "(RED, GREEN, REFACTOR) plus a branch, a mutant check, a review and a merge."),
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
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git switch -c feat/routing",
     "Creates a new branch named feat/routing and moves onto it. A branch is a named line of commits: work on it "
     "does not touch the other branches. -c = create; the branch starts from the commit you are on, so be on "
     "mywork first. The prefix before the slash is only a naming habit (feat/ = feature, fix/ = correction). « "
     "already exists »? Use git switch feat/routing (without -c)."),
    ("Symbol — test: / feat: / fix: / docs: (commit messages)",
     "Not commands: the first word of a commit message (the « Conventional Commits » habit). test: = only tests, "
     "feat: = a new feature, fix: = a bug fix, docs: = documentation. The … on the slide is your own short "
     "description. A commit is a saved snapshot of the project, with that message."),
    ("Command — git add -A && git commit -m \"test: …\"",
     "How to make the commit. git add -A puts every change (new, modified, deleted files) in the staging area, "
     "the list of what goes into the next commit; -A = all. git commit -m \"…\" saves that snapshot; -m = the "
     "message, in quotes. && = run the second command only if the first succeeded. You can also ask the agent to "
     "commit, then check with git log --oneline."),
    ("Command — merge into mywork",
     "git switch mywork (go back to the main line), then git merge feat/routing (bring the task's commits into "
     "it). Do it only when npm run test:run is green on the branch."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Same Loop, Every Task (1/2)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Same Loop, Every Task (1/2)", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ('Create the branch named under the task in ', (bs.cmd, 'docs/plan.md'), ' (the line that starts with '
             'Branch:), e.g. ', (bs.cmd, 'git switch -c feat/routing'), '. Your name may differ: ask opencode “Create the branch of the [next] task in @docs/plan.md.”'),
            ('RED: ask for the test only. ', (bs.keyword, 'You'), ' read it, then commit it alone (', (bs.cmd, 'test: …'),
             ').'),
            ('GREEN: ask for the minimal code, without changing the test. Commit it (', (bs.cmd, 'feat: …'), ').'),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(98), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
