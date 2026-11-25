"""Slide — Exercise sheet — next tasks of your plan (goal and steps)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


class BlockStyles:
    """Exercise sheet — next tasks of your plan (goal and steps) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_ex_steps_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_ex_steps_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "tasks_ex_steps_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_ex_steps_foot")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_STEP_ZOOM = 74    # tuned by measure: content bottom <= 1000 px at 1920x1080
_PROMPT_ZOOM = 68   # the « Or ask opencode » line: smaller than the step it replaces


_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Exercise 13:30 → 14:20: the next tasks of their plan, one branch "
     "each, test first; leave this slide on screen while they work."),
    ("The message",
     "The exercise of Part 2: 50 minutes, 13:30 → 14:20, to deliver the next tasks of the participant's plan "
     "(routing, data, UI)."),
    ("The four steps",
     "One branch per task; RED → review → commit test: …; GREEN → review checklist → commit feat: …; merge into "
     "mywork when green, then the next task."),
    ("Where the prompts are",
     "The plan gives the tasks; the previous slides give ready-made RED / GREEN prompts when the plan's wording "
     "is unclear."),
    ("What to watch while walking around",
     "Commits that mix test and code, a branch that was never merged, a review checklist skipped."),
    ("Link",
     "The next slide says when Part 2 is done, the mid-point at 13:55, and what to do if stuck."),
    ("Or ask opencode",
     "Under each step, the same thing asked to opencode (build agent): it gives the commands first, then runs "
     "them and shows the result. Accept if it asks permission. Git specialists can skip these lines."),
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
    ("Command — merge into mywork, next task",
     "git switch mywork then git merge feat/routing; then git switch -c feat/data for the next task (each new "
     "branch starts from mywork, which now contains the previous task)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Exercise — Your Next Tasks', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise, Your Next Tasks", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(92):
            st_write(bs.timer, '13:30 → 14:20 · 50 min', tag=t.div)
            st_space("v", "1vh")
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                "deliver your plan's next tasks (routing, data, UI), one branch each, test first.",
                tag=t.div,
            )
        st_space("v", "2vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23); under each step, full
        # width, the same thing asked to opencode — build agent (NG, 2026-11-25)
        items = [
            (('One task = one branch ', (bs.cmd, 'feat/routing')),
             "Give me the git command to create and switch to a branch for my task (e.g. feat/routing), then run it."),
            (('RED → review → commit ', (bs.cmd, 'test: …')),
             "Give me the git commands to commit only the new test as 'test: …', then run them."),
            (('GREEN → review checklist → commit ', (bs.cmd, 'feat: …')),
             "Give me the commands to run the tests, then commit the code as 'feat: …' if green; run them."),
            (('Merge into ', (bs.cmd, 'mywork'), ' when green, next task'),
             "Give me the git commands to merge my task branch into mywork, then run them."),
        ]
        cols = "5% 5% 85% 5%"
        for i, (parts, prompt) in enumerate(items):
            if i:
                st_space("v", "0.6vh")
            cells = s.project.containers.rows(i + 1, cols, filled=(2, 3))[-4:]  # keeps the alternation
            with st_zoom(_STEP_ZOOM), st_grid(cols=cols, gap="0 0.5vw", cell_styles=cells) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{i + 1}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
            if prompt:
                st_space("v", "0.4vh")
                st_ask_opencode(prompt, zoom=_PROMPT_ZOOM, cols="5% 90% 5%")
        st_space("v", "2vh")
        with st_zoom(92):
            st_write(
                bs.foot,
                "Your plan's wording is unclear? Use the prompts of the previous slides.",
                tag=t.div,
            )
