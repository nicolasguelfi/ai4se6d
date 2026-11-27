"""Slide — GSE-One in git (S2): one task, acceptance test first (NG « OK série GSE », 2026-11-27).

What /gse:produce does in git for ONE code task, as written in gse-one/src/activities/produce.md (Step 2 — worktree
strategy, Step 3.1 — Acceptance Test First, Step 4 — canonical test run, Finalize — status: review). Example: CalcApp
TASK-001 traces REQ-001 « Edit existing expense ». Same drawing as the day-2 graphs (shared-blocks/git_graph.py).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from git_graph import INTEG, TASK, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """GSE-One git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)
_L = ("l", TASK)

_TITLE = "GSE-One Git · One Task"
_N = 4
_GRAPH_ZOOM = 62
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [("k", "gse/sprint-01/integration", INTEG), ("p", "v0.1", INTEG)] + [_E] * 6,
    [_E, ("c", "no commit: does not move")] + [_E] * 6,
    [("k", "gse/sprint-01/feat/edit-expense", TASK), _E, ("a", "↘", TASK), ("n", "test", TASK), _L,
     ("n", "feat", TASK), _E, ("p", "all green", TASK)],
    [("c", "folder .worktrees/sprint-01-feat-edit-expense"), _E, _E, ("c", "msg1 (red)"), _E, ("c", "msg2 (green)"),
     _E, ("c", "whole suite · status: review")],
]
# Messages as produce.md Step 3.1 writes them (trailers Sprint: / Task: / Traces: under each)
_MSGS = [
    ("msg1", "gse(sprint-01/test): acceptance test for REQ-001"),
    ("msg2", "gse(sprint-01/feat): edit an existing expense"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type: the agent runs every git command of this slide during /gse:produce."),
    ("The message",
     "Same habit as day 2 — one branch per task, the test before the code — with three changes: the branch starts "
     "from the sprint branch, it lives in its own folder (a worktree), and the first test is the ACCEPTANCE test of "
     "the requirement, not a unit test."),
    ("Read the graph",
     "Amber = gse/sprint-01/integration, the main line of the sprint; it was created by /gse:plan on main's last "
     "commit (v0.1) and gets no commit while tasks are produced. Green = the task branch of TASK-001 (REQ-001, edit "
     "an existing expense). msg1 = the acceptance test, seen failing; msg2 = the code and its unit tests, the "
     "acceptance test now passes. Then the canonical test run (the whole suite, a TCP report, test_evidence) — not "
     "a commit. The task becomes status: review; nothing is merged yet."),
    ("Acceptance test first (ATDD)",
     "testing.strategy: auto (the default) = atdd for a code task whose REQ has Given/When/Then criteria. The agent "
     "writes one test per scenario, runs only these tests and checks they fail for the right reason: the feature "
     "is missing (assertion fails, function not found), not a typo. Never weakened to make it fail."),
    ("The test cannot be changed afterwards",
     "Before the code commit, git diff --quiet <test commit> -- <test files> must be clean: the agent may not edit "
     "the acceptance test to make its code pass. If it thinks the test is wrong, it stops and asks (Gate: Fix the "
     "test / Keep it / Discuss)."),
    ("Differences with day 2",
     "No unit-level red/green micro-steps and no refactor commit: unit and integration tests are written with the "
     "code, in msg2. No merge after the task: the task waits for /gse:review, and merges happen only at "
     "/gse:deliver."),
    ("Worktree",
     "A worktree is a second working folder of the same repository, on another branch: "
     ".worktrees/sprint-01-feat-edit-expense holds feat/edit-expense while your main folder stays where it was. "
     "Several tasks can then be worked on at once without git switch (next slide). git.strategy: worktree is the "
     "default in .gse/config.yaml; branch-only uses git switch as on day 2."),
    ("Commit trailers",
     "Every GSE-One commit carries three lines under the message: Sprint: 01, Task: TASK-001, Traces: REQ-001. "
     "They link each commit to its task and requirement (scope reconciliation, review)."),
    # Command recap: every command of the slide, in plain words (NG, 2026-11-24)
    ("Command — git branch gse/sprint-01/feat/edit-expense gse/sprint-01/integration",
     "Creates the task branch on the sprint branch's last commit, without switching to it. The name comes from the "
     "plan (plan.yaml, decided by /gse:plan)."),
    ("Command — git worktree add .worktrees/sprint-01-feat-edit-expense gse/sprint-01/feat/edit-expense",
     "Creates the folder .worktrees/sprint-01-feat-edit-expense with that branch checked out in it. All the task's "
     "files are written there."),
    ("Source",
     "gse-one/src/activities/produce.md — Step 2 (Strategy: worktree), Step 3.1 (Acceptance Test First), Step 4 "
     "(canonical test run), Finalize (status: review)."),
]


def _steps(kw):
    return [
        ("1", ("The agent creates the branch from the sprint branch and its folder: ",
               (kw, "git worktree add .worktrees/sprint-01-feat-edit-expense"), ".")),
        ("2", ("It writes the acceptance test of REQ-001 and runs it: it fails because the feature is missing. "
               "Commit msg1.",)),
        ("3", ("It writes the code and its unit tests without touching that test: it passes. Commit msg2, then the "
               "whole suite runs. The sprint branch has not moved.",)),
    ]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, _TITLE, tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — " + _TITLE, entries=_NOTES, position="left", width="50vw")
        st_space("v", "1vh")
        draw(cols(_N, label="3.4fr"), _ROWS, zoom=_GRAPH_ZOOM)
        st_space("v", "1vh")
        legend(_MSGS)
        st_space("v", "1.5vh")
        steps(_steps(bs.keyword), zoom=60)
