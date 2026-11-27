"""Slide — GSE-One in git (S7): cleanup after delivery, and how to undo (NG « OK série GSE », 2026-11-27).

/gse:deliver Step 0 (backup tag class 2, before each task branch is deleted), Step 5 (cleanup), Step 8 (backup tags
older than backup_retention_days = 30 removed at the next delivery). Order drawn as corrected by ss2-ul-gse, who
reproduced two problems of deliver.md Step 5 (2026-11-27): git branch -d refuses a branch still checked out in a
worktree (so: worktree first), and refuses a squashed task branch (« not fully merged »). GSE-One patch proposed to NG.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from git_graph import INTEG, MAIN, MERGE, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """GSE-One git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)
_LM = ("l", MAIN)
_LI = ("l", INTEG)

_TITLE = "GSE-One Git · Cleanup and Undo"
_N = 4
_GRAPH_ZOOM = 60
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [_E, ("p", "tag3", MERGE)] + [_E] * 5 + [("p", "v0.2", MERGE)],
    [("k", "main", MAIN), ("n", "docs", MAIN), _LM, _LM, _LM, _LM, _LM, ("m", "M", "main_integ")],
    [_E, ("c", "msg1 · v0.1"), ("a", "↘", INTEG), _E, _E, _E, ("a", "↗", INTEG), ("c", "msg4")],
    [("c", "no branch name any more: the commits stay, reached from M"), _E, _E, ("n", "feat", INTEG), _LI,
     ("n", "feat", INTEG), _E, _E],
    [_E, _E, _E, ("c", "msg2"), _E, ("c", "msg3"), _E, _E],
]
_MSGS = [
    ("msg4", "gse(deliver): sprint S01 delivery"),
    ("tag3", "gse-backup/sprint-01-pre-main-merge — undo the delivery (kept 30 days, like every backup tag)"),
    ("tag4", "gse-backup/sprint-01-feat-edit-expense-deleted — recreate that branch"),
    ("tag5", "gse-backup/sprint-01-feat-sort-expenses-deleted"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type; show the two undo commands, they are the safety net of the whole cycle."),
    ("The message",
     "After delivery, the agent removes the task folders and the branch names; the commits are kept (main reaches "
     "them through M), and backup tags let you undo the delivery or bring back any deleted branch for 30 days."),
    ("Read the graph",
     "main after delivery: msg1 (v0.1), M (msg4, v0.2). The sprint's commits msg2 and msg3 still exist: M is their "
     "child. The names gse/sprint-01/integration and the task branches are gone. The backup tags remain: tag3 (before "
     "the main merge, on msg1), tag4-tag5 (on the last commit of each deleted task branch — those 4 + 2 commits are "
     "not drawn), and tag1-tag2 of the previous slide (before each task merge)."),
    ("Order of the cleanup, per task",
     "1. git tag gse-backup/sprint-01-feat-edit-expense-deleted (taken at the start of /gse:deliver, Step 0). "
     "2. git worktree remove .worktrees/sprint-01-feat-edit-expense — FIRST, because git refuses to delete a branch "
     "still open in a folder. 3. git branch -D gse/sprint-01/feat/edit-expense — -D (forced) because a squashed task "
     "branch is not « merged » for git; the tag keeps its commits. Then git branch -d gse/sprint-01/integration "
     "(merged into main by M: -d is enough)."),
    ("Known gap in GSE-One",
     "deliver.md Step 5 currently lists git branch -d before git worktree remove; ss2-ul-gse reproduced both refusals "
     "(2026-11-27) and proposed the patch. This slide shows the order that works."),
    ("Undo the delivery",
     "git checkout main && git reset --hard gse-backup/sprint-01-pre-main-merge: main is back on v0.1, as if the "
     "delivery never happened. reset --hard also throws away uncommitted changes of the folder: commit first."),
    ("Bring a branch back",
     "git checkout -b gse/sprint-01/feat/edit-expense gse-backup/sprint-01-feat-edit-expense-deleted recreates the "
     "branch exactly as it was, with its 4 commits."),
    ("30 days",
     "git.backup_retention_days: 30 in .gse/config.yaml. The next /gse:deliver deletes the backup tags older than "
     "that (git tag -l \"gse-backup/*\", then git tag -d)."),
    ("Source",
     "gse-one/src/activities/deliver.md — Step 0 (tag classes 2 and 3), Step 5 (Cleanup), Step 8 (Cleanup Backup "
     "Tags). templates/config.yaml — cleanup_on_deliver: true, backup_retention_days: 30."),
]


def _steps(kw):
    return [
        ("1", ("Per task: its backup tag, then ", (kw, "git worktree remove"), " (the folder), then ",
               (kw, "git branch -D"), " (the name). Then the sprint branch.")),
        ("2", ("Undo the delivery: ", (kw, "git checkout main && git reset --hard gse-backup/sprint-01-pre-main-merge"),
               ".")),
        ("3", ("Bring a branch back: ",
               (kw, "git checkout -b gse/sprint-01/feat/edit-expense gse-backup/sprint-01-feat-edit-expense-deleted"),
               ".")),
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
        legend(_MSGS, zoom=58)
        st_space("v", "1.5vh")
        steps(_steps(bs.keyword), zoom=56)
