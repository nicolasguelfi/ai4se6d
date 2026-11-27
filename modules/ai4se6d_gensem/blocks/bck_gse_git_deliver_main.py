"""Slide — GSE-One in git (S6): delivery 2, the sprint into main and the version tag (NG « OK série GSE », 2026-11-27).

/gse:deliver Step 0 (backup tag class 3 on main), Step 3 (Gate: merge --no-ff = default, squash, defer; the exact
merge message) and Step 4 (annotated tag v{version}, major / minor / patch from the sprint content, tag_on_deliver:
true). Example: CalcApp sprint 01 → v0.2.
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

_TITLE = "GSE-One Git · Sprint into Main"
_N = 4
_GRAPH_ZOOM = 56
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [_E, ("p", "tag3", MERGE)] + [_E] * 5 + [("p", "v0.2", MERGE)],
    [("k", "main", MAIN), ("n", "docs", MAIN), _LM, _LM, _LM, _LM, _LM, ("m", "M", "main_integ")],
    [_E, ("c", "msg1 · v0.1"), ("a", "↘", INTEG), _E, _E, _E, ("a", "↗", INTEG), ("c", "msg4")],
    [("k", "gse/sprint-01/integration", INTEG), _E, _E, ("n", "feat", INTEG), _LI, ("n", "feat", INTEG), _E, _E],
    [_E, _E, _E, ("c", "msg2"), _E, ("c", "msg3"), _E, _E],
]
_MSGS = [
    ("msg1", "docs: README"),
    ("msg2", "gse(sprint-01/feat): edit an existing expense"),
    ("msg3", "gse(sprint-01/feat): sort the expenses by date or amount"),
    ("msg4", "gse(deliver): sprint S01 delivery"),
    ("tag3", "gse-backup/sprint-01-pre-main-merge"),
    ("v0.2", "git tag -a v0.2 -m \"Release v0.2 — Sprint 01\""),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — the learners answer one Gate (merge, squash or defer) and check the version proposed."),
    ("The message",
     "main receives the sprint once, as one merge commit that keeps the sprint visible in the history, and gets a "
     "version tag. A backup tag on main makes the whole delivery reversible."),
    ("Read the graph",
     "Blue = main, still on v0.1 (msg1) during the whole sprint. Amber = the sprint branch with one commit per task "
     "(msg2, msg3, from the previous slide). M = msg4, a real merge commit with two parents: msg1 (main) and msg3 "
     "(the sprint). tag3 = the backup tag on main before the merge; v0.2 = the version tag on M."),
    ("Why --no-ff here",
     "main has not moved since the sprint started, so git could fast-forward. --no-ff forces a merge commit anyway: "
     "the sprint stays one visible block in main's history (« preserves sprint boundary »), and one revert undoes it. "
     "The other options at the Gate: squash (the whole sprint becomes one commit) or defer (keep the sprint branch, "
     "do not merge yet)."),
    ("The version",
     "The agent reads the last tag (v0.1) and proposes the next one from the sprint's content: major = breaking "
     "changes or major new features, minor = new features without breaking anything, patch = only fixes, docs, "
     "refactoring. Two new features → minor → v0.2. Annotated tag: it has its own message."),
    ("Undo the delivery",
     "git checkout main && git reset --hard gse-backup/sprint-01-pre-main-merge puts main back where it was before "
     "M (tag class 3, kept 30 days). Also offered by the post-delivery Gate (Rollback)."),
    ("No remote yet?",
     "At the first delivery, if the project has no remote, the agent asks once whether to set one up (GitHub, "
     "GitLab) to protect the work against a disk failure. It never pushes on its own."),
    # Command recap: every command of the slide, in plain words (NG, 2026-11-24)
    ("Command — git merge --no-ff gse/sprint-01/integration -m \"gse(deliver): sprint S01 delivery\"",
     "Run on main: creates the merge commit M with that message, even though a fast-forward was possible."),
    ("Command — git tag -a v0.2 -m \"Release v0.2 — Sprint 01\"",
     "-a = annotated tag: a name fixed on M, with an author, a date and a message. git tag lists the tags; "
     "git show v0.2 shows it."),
    ("Source",
     "gse-one/src/activities/deliver.md — Step 0 (tag class 3), Step 3 (Merge Sprint into Main), Step 4 (Tag "
     "Release), Step 7 (Rollback). templates/config.yaml — tag_on_deliver: true."),
]


def _steps(kw):
    return [
        ("1", ("Backup tag on main (tag3), then the Gate: ", (kw, "merge --no-ff"), " (proposed), squash or defer.")),
        ("2", ((kw, "git merge --no-ff gse/sprint-01/integration"), ": the merge commit M (msg4) on main.")),
        ("3", ("The version tag on M: two new features = minor, so ", (kw, "v0.2"), ".")),
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
        st_space("v", "1.5vh")
        steps(_steps(bs.keyword), zoom=58)
