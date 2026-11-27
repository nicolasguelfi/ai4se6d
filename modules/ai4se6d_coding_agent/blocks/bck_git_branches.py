"""Slide — Pattern 3: one branch per task, drawn as learners do it on day 2 (NG « ok », 2026-11-27).

The graph shows every commit of one task of the plan (the same loop for every task) exactly as the exercise sheets ask: plan on mywork,
a task branch with test: (red) / feat: (green) / refactor:, git merge = fast-forward (mywork has not moved,
so no merge commit), docs: update plan labels on mywork, next task. The rest of the day (morning, review,
v0.1) and the case with a real merge commit are the next slides (bck_git_day_morning, bck_git_day_ship,
bck_git_main_moves).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.git_graph import MAIN, TASK, cols, draw, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """One-branch-per-task styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "gitbr_body")
    keyword = s.project.titles.keyword
bs = BlockStyles

_N = 5  # commits drawn: plan, one task (test, feat, refactor), plan labels — the same loop for every task
_E = (".",)
_L = ("l", TASK)
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [("k", "mywork", MAIN), ("n", "docs", MAIN)] + [_E] * 7 + [("n", "docs", MAIN)],
    [_E, ("c", "docs: v0.1 plan")] + [_E] * 7 + [("c", "docs: update plan labels")],
    [_E, _E, ("a", "↘", TASK)] + [_E] * 5 + [("a", "↗", TASK), _E],
    [("k", "feat/expense-type", TASK), _E, _E, ("n", "test", TASK), _L, ("n", "feat", TASK), _L, ("n", "ref", TASK),
     _E, _E],
    [_E, _E, _E, ("c", "test: … (red)"), _E, ("c", "feat: … (green)"), _E, ("c", "refactor: …"), _E, _E],
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Follow the graph left to right: it is exactly what learners do this "
     "afternoon for each task of their plan (Part 1: T1, Part 2: the next tasks)."),
    ("The message",
     "Third habit: one branch per task. Plan, red, green, refactor are commits inside ONE branch, not branches. "
     "The agent never works directly on your main line."),
    ("Read the graph",
     "Blue = mywork, your main line today. Green = the branch of one task of docs/plan.md (feat/expense-type for "
     "T1; your name comes from the Branch: line of the task). The same loop repeats for every task (T2 on "
     "feat/routing, …). Every commit is drawn; the type "
     "is in the circle, the message under it."),
    ("Why mywork has no line between its commits",
     "While a task is in progress, nobody commits on mywork: it stays on the plan commit. git merge then only moves "
     "the name mywork forward to the task's last commit (« Fast-forward »): no merge commit, and the history is "
     "one straight line — plan, test, feat, refactor, labels. The next slides show the whole day, then the only "
     "case with a real merge commit (the main line moved meanwhile)."),
    ("Why commit the red test",
     "The test: commit is the proof that the test existed, and failed, before the code. It is on the task branch, "
     "never on mywork: mywork only receives finished, green tasks."),
    ("When to branch — alone / in a team",
     "Branch when one answer is yes: several commits? may fail and be thrown away? may be interrupted? will be "
     "reviewed before you keep it? One branch = one task of the plan. Alone: the main line stays green and usable, "
     "a failed agent attempt goes with one command (git branch -D); a tiny safe change (a typo) and the plan itself "
     "(docs: plan) can go straight on the main line. In a team: mandatory — main is usually protected; each branch "
     "ends in a pull request, reviewed and tested before the merge, so the branch is also the unit of review; keep "
     "branches short-lived (one or two days) or main drifts away and conflicts grow; even the plan goes through a "
     "branch, since the team validates it."),
    ("Ask the room",
     "« What happens to mywork if the agent's attempt fails on a branch? » Nothing: git branch -D, start again."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git switch -c feat/expense-type",
     "Creates a new branch and moves onto it, starting from where you are now: be on mywork first. -c = create. "
     "The name comes from the Branch: line of the task; the / is just part of the name (feat/ = feature, fix/ = "
     "correction), not a folder. Older equivalent: git checkout -b feat/expense-type."),
    ("Command — git add -A && git commit -m \"test: …\"",
     "Stages every change and saves it as one commit with that message. Same for feat: and refactor:. « … » = your "
     "own short description."),
    ("Command — git switch mywork, then git merge feat/expense-type",
     "Go back to the main line, then bring the task's commits into it. mywork has not moved: git prints « "
     "Fast-forward » and just moves mywork forward. « CONFLICT » = both changed the same lines: raise your hand."),
    ("Command — docs: update plan labels",
     "On mywork, in docs/plan.md, the finished task becomes [done] and the next one [next]; then git add "
     "docs/plan.md && git commit -m \"docs: update plan labels\"."),
    ("Command — git branch -D feat/expense-type",
     "Throws away a failed task branch and its commits. -d (small) only deletes a merged branch. You cannot delete "
     "the branch you are on: git switch mywork first."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "3 · One Branch per Task", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — One Branch per Task", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "1vh")
        draw(cols(_N), _ROWS, zoom=64)
        st_space("v", "2vh")
        kw = bs.keyword
        steps([
            ("1", ("On mywork: ", (kw, "git switch -c feat/expense-type"), " — the Branch: line of the task.")),
            ("2", ("On the branch: commit ", (kw, "test: …"), " (red), then ", (kw, "feat: …"), " (green), then ",
                   (kw, "refactor: …"), " if any.")),
            ("3", ((kw, "git switch mywork"), " then ", (kw, "git merge feat/expense-type"),
                   ": « Fast-forward », mywork jumps to the task's last commit.")),
            ("4", ("On mywork: commit ", (kw, "docs: update plan labels"), ", then the next task from step 1.")),
        ], zoom=68)
