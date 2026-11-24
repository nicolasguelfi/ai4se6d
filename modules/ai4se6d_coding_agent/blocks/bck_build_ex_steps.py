"""Slide — Exercise sheet — task 1 of your own plan (goal and steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise sheet — task 1 of your own plan (goal and steps) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_ex_steps_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    number = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_ex_steps_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_ex_steps_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_ex_steps_foot")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Exercise 11:45 → 12:10: task 1 of their plan, test first, on its "
     "own branch; leave this slide on screen while they work."),
    ("The message",
     "25 minutes, 11:45 → 12:10: deliver the first task of docs/plan.md, test first, on its own branch."),
    ("The loop",
     "New branch feat/task-1; RED prompt, read the test, commit test: …; GREEN prompt, npm run "
     "test:run green, commit feat: …; mutant check, undo; back to mywork and merge."),
    ("Why its own branch",
     "One task = one branch: if the task goes wrong, mywork is untouched. mywork is the main line since this "
     "morning: every finished task is merged into it."),
    ("The trap",
     "Skipping the reading of the test, or one commit for test and code together: you lose the proof that the "
     "test came first."),
    ("Link to what follows",
     "The next slide says when you are done, what to do at the mid-point and if stuck."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git switch -c feat/task-1",
     "Creates a new branch named feat/task-1 and moves onto it. A branch is a named line of commits: work on it "
     "does not touch the other branches. -c = create; the branch starts from the commit you are on, so be on "
     "mywork first. The prefix before the slash is only a naming habit (feat/ = feature, fix/ = correction). « "
     "already exists »? Use git switch feat/task-1 (without -c)."),
    ("Symbol — test: / feat: / fix: / docs: (commit messages)",
     "Not commands: the first word of a commit message (the « Conventional Commits » habit). test: = only tests, "
     "feat: = a new feature, fix: = a bug fix, docs: = documentation. The … on the slide is your own short "
     "description. A commit is a saved snapshot of the project, with that message."),
    ("Command — git add -A && git commit -m \"test: …\"",
     "How to make the commit. git add -A puts every change (new, modified, deleted files) in the staging area, "
     "the list of what goes into the next commit; -A = all. git commit -m \"…\" saves that snapshot; -m = the "
     "message, in quotes. && = run the second command only if the first succeeded. You can also ask the agent to "
     "commit, then check with git log --oneline."),
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
    ("Command — git switch mywork",
     "Moves you onto the existing branch mywork (your main line since this morning): the files in the folder "
     "become mywork's version. Git refuses if uncommitted changes would be lost: commit first (git status shows "
     "them)."),
    ("Command — git merge feat/task-1",
     "Brings the commits of branch feat/task-1 into the branch you are on (mywork). If mywork has not moved "
     "meanwhile, git just moves it forward (« Fast-forward »). Otherwise it creates a merge commit and may open a"
     " text editor for its message: save and close it (nano: Ctrl+O, Enter, Ctrl+X; vim: Esc then :wq). « "
     "CONFLICT » = both branches changed the same lines: raise your hand."),
    ("Symbol — →",
     "Only means « then » on the slide: type the two commands one after the other, not the arrow."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Exercise — Task 1 of YOUR Plan', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise — Task 1 of YOUR Plan", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(90):
            st_write(bs.timer, '11:45 → 12:10 · 25 min', tag=t.div)
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                'deliver the first task of ',
                (bs.cmd, 'docs/plan.md'),
                ', test first, on its own branch.',
                tag=t.div,
            )
        st_space("v", "1vh")
        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ((bs.cmd, 'git switch -c feat/task-1'),),
            ('RED prompt → ', (bs.keyword, 'read the test'), ' → commit ', (bs.cmd, 'test: …')),
            ('GREEN prompt → ', (bs.cmd, 'npm run test:run'), ' green → commit ', (bs.cmd, 'feat: …')),
            ('Mutant check, then undo the sabotage',),
            ((bs.cmd, 'git switch mywork'), ' → ', (bs.cmd, 'git merge feat/task-1')),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(107), st_grid(cols=cols, gap="1.2vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "1vh")
        with st_zoom(84):
            st_write(
                bs.foot,
                'mywork is your main line since this morning: every finished task is merged into it.',
                tag=t.div,
            )
