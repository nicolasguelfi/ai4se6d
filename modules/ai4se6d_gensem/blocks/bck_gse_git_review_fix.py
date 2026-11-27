"""Slide — GSE-One in git (S4): review and fix (NG « OK série GSE », 2026-11-27).

/gse:review reads the diff of a task against the sprint branch (review.md Step 1: git diff integration...task);
/gse:fix works in a fix branch and folder from the task branch, regression test first, then merges back with
--ff-only (fix.md Step 2 worktree strategy, Step 3.3 regression test, Step 3 item 8 trailers, Step 4 Merge Fix Back).
Example: CalcApp TASK-001, finding RVW-001.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from git_graph import FIX, TASK, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """GSE-One git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)
_LT = ("l", TASK)
_LF = ("l", FIX)

_TITLE = "GSE-One Git · Review and Fix"
_N = 4
_GRAPH_ZOOM = 60
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [("k", "gse/sprint-01/feat/edit-expense", TASK), ("n", "test", TASK), _LT, ("n", "feat", TASK), _E, _E, _E,
     ("c", "feat/edit-expense, after the merge")],
    [_E, ("c", "msg1"), _E, ("c", "msg2 · reviewed: RVW-001"), _E, _E, _E, _E],
    [_E, _E, _E, _E, ("a", "↘", FIX), _E, _E, ("a", "↑", TASK)],
    [("k", "gse/sprint-01/fix/rvw-001", FIX), _E, _E, _E, _E, ("n", "test", FIX), _LF, ("n", "fix", FIX)],
    [("c", "folder .worktrees/sprint-01-fix-rvw-001"), _E, _E, _E, _E, ("c", "msg3 (red)"), _E,
     ("c", "msg4 (green)")],
]
_MSGS = [
    ("msg1", "gse(sprint-01/test): acceptance test for REQ-001"),
    ("msg2", "gse(sprint-01/feat): edit an existing expense"),
    ("msg3", "gse(sprint-01/test): regression test for RVW-001"),
    ("msg4", "gse(sprint-01/fix): fix RVW-001 — an edited amount of 0 is rejected"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type: /gse:review and /gse:fix run these commands; you triage the findings."),
    ("The message",
     "Same idea as fix/review on day 2, but per task: the review reads only what the task changed, and each fix gets "
     "its own branch, its own folder and a test that reproduces the defect before the fix."),
    ("Read the graph",
     "Green = the task branch, produced (msg1, msg2). /gse:review finds RVW-001: editing an expense accepts an "
     "amount of 0. Red = the fix branch, started on the task's last commit: msg3 = a regression test that fails "
     "(it reproduces the defect), msg4 = the fix, the test now passes. git merge --ff-only moves the task branch "
     "name to msg4 (↑): same commits, no merge commit. Then the fix folder and branch are deleted."),
    ("What the review reads",
     "git diff gse/sprint-01/integration...gse/sprint-01/feat/edit-expense — the three dots mean: only what the task "
     "branch changed since it left the sprint branch. The review works on that diff, not on the whole project, and "
     "includes a devil's-advocate pass (another agent, fresh context)."),
    ("Regression test first",
     "With testing.strategy auto/atdd, a finding in code first gets an automated test that reproduces it, committed "
     "alone (msg3) and seen failing. It stays in the suite, so the defect cannot come back unnoticed. After the fix "
     "the test must pass and be unchanged since its commit (git diff --quiet <test commit> -- <test file>)."),
    ("Fix commit trailers",
     "Under msg4 the agent must write Root cause: (why the defect existed) and Evidence: (how it was shown), plus "
     "Sprint: and Traces: RVW-001."),
    ("Why --ff-only",
     "The fix branch starts on the task's last commit and the task branch has not moved: git only moves the name "
     "(fast-forward, as on day 2). --ff-only = refuse anything else, so a surprise merge commit can never appear "
     "here."),
    # Command recap: every command of the slide, in plain words (NG, 2026-11-24)
    ("Command — git branch gse/sprint-01/fix/rvw-001 gse/sprint-01/feat/edit-expense",
     "Creates the fix branch on the task's last commit; git worktree add .worktrees/sprint-01-fix-rvw-001 … gives it "
     "its folder."),
    ("Command — git merge --ff-only gse/sprint-01/fix/rvw-001",
     "Run on the task branch: moves it forward to the fix's last commit, or refuses if that is not possible."),
    ("Command — git worktree remove, then git branch -d",
     "git worktree remove .worktrees/sprint-01-fix-rvw-001 deletes the fix folder; git branch -d "
     "gse/sprint-01/fix/rvw-001 deletes the name (allowed: it is merged)."),
    ("Source",
     "gse-one/src/activities/review.md — Step 1 (diff). fix.md — Step 2 (Strategy: worktree), Step 3 items 3 and "
     "8-9 (regression test, trailers), Step 4 (Merge Fix Back)."),
]


def _steps(kw):
    return [
        ("1", ((kw, "/gse:review"), " reads what the task changed: ",
               (kw, "git diff gse/sprint-01/integration...gse/sprint-01/feat/edit-expense"), ". Finding RVW-001.")),
        ("2", ((kw, "/gse:fix"), ": a fix branch and folder from the task branch; msg3 reproduces the defect "
               "(red), msg4 fixes it (green).")),
        ("3", ((kw, "git merge --ff-only"), " into the task branch; the fix folder and branch are deleted. The task "
               "is ready to be delivered.")),
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
        legend(_MSGS, zoom=62)
        st_space("v", "1.5vh")
        steps(_steps(bs.keyword), zoom=58)
