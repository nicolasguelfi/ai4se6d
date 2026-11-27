"""Slide — GSE-One in git (S3): several tasks, several worktrees, and a spike (NG « OK série GSE », 2026-11-27).

Two task branches produced as on the previous slide (produce.md Step 2 / 3.1), each in its own folder, and one spike
created by /gse:task --spike (task.md: branch gse/sprint-NN/task/{slug}, Step 4; spike rules 1-5: max 3 points, a DEC-,
worktree removed, backup tag, git branch -D — never merged). Example: CalcApp sprint 01.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from git_graph import INTEG, SIDE, TASK, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """GSE-One git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)
_L = ("l", TASK)

_TITLE = "GSE-One Git · Tasks in Parallel"
_N = 4
_GRAPH_ZOOM = 50
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [("k", "gse/sprint-01/integration", INTEG), ("p", "v0.1", INTEG)] + [_E] * 6,
    [_E, ("c", "still no commit")] + [_E] * 6,
    [("k", "gse/sprint-01/feat/edit-expense", TASK), _E, ("a", "↘", TASK), ("n", "test", TASK), _L,
     ("n", "feat", TASK), _E, _E],
    [("c", "folder .worktrees/sprint-01-feat-edit-expense"), _E, _E, ("c", "msg1"), _E, ("c", "msg2"), _E, _E],
    [("k", "gse/sprint-01/feat/sort-expenses", TASK), _E, ("a", "↘", TASK), ("n", "test", TASK), _L,
     ("n", "feat", TASK), _E, _E],
    [("c", "folder .worktrees/sprint-01-feat-sort-expenses"), _E, _E, ("c", "msg3"), _E, ("c", "msg4"), _E, _E],
    [("k", "gse/sprint-01/task/chart-library", SIDE), _E, ("a", "↘", SIDE), ("n", "task", SIDE), _E, _E, _E,
     ("a", "✕", SIDE)],
    [("c", "spike · folder .worktrees/sprint-01-task-chart-library"), _E, _E, ("c", "msg5"), _E, _E, _E,
     ("c", "deleted, never merged")],
]
_MSGS = [
    ("msg1", "gse(sprint-01/test): acceptance test for REQ-001"),
    ("msg2", "gse(sprint-01/feat): edit an existing expense"),
    ("msg3", "gse(sprint-01/test): acceptance test for REQ-003"),
    ("msg4", "gse(sprint-01/feat): sort the expenses by date or amount"),
    ("msg5", "gse(sprint-01/task): try a chart library for the monthly summary"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type: the agent creates every branch and folder of this slide."),
    ("The message",
     "Each task has its own branch AND its own folder (worktree), so several tasks can be produced at once without "
     "git switch and without mixing files. The sprint branch still does not move. A spike is an experiment: its "
     "code is thrown away, only its decision (DEC-) is kept."),
    ("Read the graph",
     "Amber = the sprint branch, still on v0.1. Green = two tasks of the plan, each with its acceptance test (msg1, "
     "msg3) then its code (msg2, msg4), in its own folder under .worktrees/. Purple = a spike: one experiment "
     "commit (msg5), then the branch is deleted — never merged."),
    ("Why worktrees",
     "On day 2, git switch changed the files of your one folder, so you had to commit or stash first. With one "
     "folder per task, nothing has to be put aside: each folder keeps its branch. The agent can even give each task "
     "to a separate sub-agent (produce.md: « Agent tool with isolation: worktree »)."),
    ("The spike (/gse:task --spike)",
     "A question to answer before building, e.g. « which chart library for the monthly summary? ». Rules: at most 3 "
     "complexity points; no REQ and no test first (the question is the requirement, the experiment is the test); it "
     "must end with a DEC- (question, approach, answer, next step). If useful code comes out, a NEW normal task "
     "rebuilds it properly with REQ and tests."),
    ("How the spike branch is removed",
     "Once the DEC- is written: git worktree remove .worktrees/sprint-01-task-chart-library, then git tag "
     "gse-backup/sprint-01-task-chart-library-deleted gse/sprint-01/task/chart-library (keeps the experiment), then "
     "git branch -D gse/sprint-01/task/chart-library (-D: forced, because it is never merged)."),
    ("Name of the spike branch",
     "Every /gse:task branch (spike included, except --quick) is gse/sprint-NN/task/{slug}, in the folder "
     ".worktrees/sprint-NN-task-{slug}; its commits use the task scope: gse(sprint-01/task): …"),
    # Command recap: every command of the slide, in plain words (NG, 2026-11-24)
    ("Command — git worktree list",
     "Lists the folders of the repository and the branch of each: your main folder plus one line per .worktrees/… "
     "folder. Useful to see what the agent has opened."),
    ("Source",
     "gse-one/src/activities/produce.md — Step 2, Step 3.1. task.md — --spike, Spike rules 1-5, Step 4 (Git "
     "Setup), Step 5 (commit scope task)."),
]


def _steps(kw):
    return [
        ("1", ("Each task of the plan: its branch from the sprint branch, its folder under .worktrees/, its test "
               "then its code. See them with ", (kw, "git worktree list"), ".")),
        ("2", ("A question before building? ", (kw, "/gse:task --spike"), ": a small experiment (max 3 points) "
               "that ends with a decision DEC-.")),
        ("3", ("Then its folder and its branch are deleted, a backup tag keeps the experiment: the spike is never "
               "merged.",)),
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
        legend(_MSGS, zoom=56)
        st_space("v", "1vh")
        steps(_steps(bs.keyword), zoom=58)
