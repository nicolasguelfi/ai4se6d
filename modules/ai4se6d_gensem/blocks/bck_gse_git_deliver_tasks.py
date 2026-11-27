"""Slide — GSE-One in git (S5): delivery 1, the tasks into the sprint branch (NG « OK série GSE », 2026-11-27).

/gse:deliver Step 0 (backup tag class 1 before each merge into the sprint branch) and Step 2 (Gate per branch:
squash = merge_strategy_default in config.yaml, or merge --no-ff, or rebase). Example: CalcApp sprint 01, two tasks.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from git_graph import INTEG, MAIN, MERGE, TASK, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """GSE-One git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)
_LI = ("l", INTEG)

_TITLE = "GSE-One Git · Tasks into the Sprint"
_N = 3
_GRAPH_ZOOM = 62
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [_E, ("p", "tag1", MERGE), _E, ("p", "tag2", MERGE), _E, _E],
    [("k", "gse/sprint-01/integration", INTEG), ("n", "docs", MAIN), _LI, ("n", "feat", INTEG), _LI,
     ("n", "feat", INTEG)],
    [_E, ("c", "msg1 · v0.1 (main)"), _E, ("c", "msg2 · squash"), _E, ("c", "msg3 · squash")],
    [_E, _E, _E, ("a", "↑", TASK), _E, ("a", "↑", TASK)],
    [("k", "task branches", TASK), _E, _E, ("c", "feat/edit-expense: its 4 commits"), _E,
     ("c", "feat/sort-expenses: its 2 commits")],
]
_MSGS = [
    ("msg1", "docs: README"),
    ("msg2", "gse(sprint-01/feat): edit an existing expense"),
    ("msg3", "gse(sprint-01/feat): sort the expenses by date or amount"),
    ("tag1", "gse-backup/sprint-01-pre-merge-feat-edit-expense"),
    ("tag2", "gse-backup/sprint-01-pre-merge-feat-sort-expenses"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment. At the Gate, the learners choose the merge strategy for each task: say why squash is "
     "proposed, and that the other two are fine too."),
    ("The message",
     "On day 2 each task was merged as soon as it was finished. With GSE-One, finished tasks wait; /gse:deliver "
     "brings them all into the sprint branch, one by one, with a backup tag before each merge."),
    ("Read the graph",
     "Amber = the sprint branch, which started on v0.1 (msg1, the last commit of main). Green = the two task branches "
     "(edit-expense: acceptance test, code, regression test, fix = 4 commits; sort-expenses: 2). Squash turns each "
     "task into ONE new commit on the sprint branch (msg2, msg3). tag1 and tag2 are backup tags put on the sprint "
     "branch just before each merge."),
    ("The Gate — three strategies",
     "squash (proposed: merge_strategy_default: squash) = one clean commit per task, the task's own commits stay on "
     "its branch only. merge = git merge --no-ff, every commit kept plus a merge commit. rebase = the task's commits "
     "replayed on the sprint branch, then a fast-forward. A beginner sees two words: « Clean summary » (squash) or "
     "« Full history » (merge)."),
    ("Backup tags (class 1)",
     "git tag gse-backup/sprint-01-pre-merge-feat-edit-expense on the sprint branch before merging that task. A bad "
     "merge is undone with git checkout gse/sprint-01/integration && git reset --hard <that tag>. Kept 30 days."),
    ("Checks before merging",
     "Pre-flight: every task reviewed and fixed, its tests green, and git merge-tree predicts the conflicts before "
     "any merge is made. Tasks are merged in dependency order."),
    ("main has not moved",
     "Everything on this slide happens on the sprint branch; main still ends at v0.1. The next slide brings the "
     "sprint into main."),
    ("Squash message",
     "deliver.md gives the command (git merge --squash … && git commit) but not the message: the agent writes it. "
     "msg2 and msg3 are examples in the course's commit style."),
    # Command recap: every command of the slide, in plain words (NG, 2026-11-24)
    ("Command — git merge --squash gse/sprint-01/feat/edit-expense && git commit",
     "Run on the sprint branch: puts all the task's changes into the folder and the index, then ONE commit records "
     "them. The task branch itself is not marked as merged."),
    ("Source",
     "gse-one/src/activities/deliver.md — Step 0 (tag class 1), Step 1 (pre-flight), Step 2 (Merge Features into "
     "Sprint Branch). templates/config.yaml — git.merge_strategy_default: squash."),
]


def _steps(kw):
    return [
        ("1", ((kw, "/gse:deliver"), " checks each task: reviewed, tests green, no conflict predicted.")),
        ("2", ("Before each merge, a backup tag on the sprint branch (tag1, tag2). Gate: ", (kw, "squash"),
               " (proposed), merge or rebase.")),
        ("3", ("Squash: each task becomes one commit on the sprint branch (msg2, msg3). main has not moved.",)),
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
        legend(_MSGS, zoom=60)
        st_space("v", "1.5vh")
        steps(_steps(bs.keyword), zoom=58)
