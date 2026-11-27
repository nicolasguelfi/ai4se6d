"""Slide — When the main line moves: urgent fix during a task, wip commit, real merge commit (NG « ok », 2026-11-27).

Not an exercise of day 2 (there, every merge is a fast-forward): the case where mywork gets a commit while a
task is in progress — an urgent fix alone, or teammates' merges in a team. Commit (or stash) before git switch,
because uncommitted changes follow you onto the other branch (ss2-ul-gse remark, git-worktree-guide § 3).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.git_graph import MAIN, TASK, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Day-2 git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)

_TITLE = "When the Main Line Moves"
_N = 7
_GRAPH_ZOOM = 52
_LM = ("l", MAIN)
_LT = ("l", TASK)
_ROWS = [
    [("k", "mywork", MAIN), ("n", "docs", MAIN), _LM, _LM, _LM, _LM, _LM, ("n", "fix", MAIN), _LM, _LM, _LM, _LM, _LM,
     ("m", "M")],
    [_E, ("c", "msg1"), _E, _E, _E, _E, _E, ("c", "msg3 (urgent)"), _E, _E, _E, _E, _E,
     ("c", "msg5: merge commit, two parents")],
    [_E, _E, ("a", "↘", TASK), _E, _E, _E, _E, _E, _E, _E, _E, _E, ("a", "↗", TASK), _E],
    [("k", "feat/routing", TASK), _E, _E, ("n", "test", TASK), _LT, _LT, _LT, _LT, _LT, ("n", "feat", TASK), _LT, _LT,
     _E, _E],
    [_E, _E, _E, ("c", "msg2 (wip, red)"), _E, _E, _E, ("c", "⇅ git switch"), _E, ("c", "msg4 (green)"), _E, _E,
     _E, _E],
]
# Example messages: T4 of docs/plan-example.md (Branch: feat/routing); the urgent fix is an example
_MSGS = [
    ("msg1", "docs: update plan labels"),
    ("msg2", "test: T4 routes show Add Expense at /add (wip, red)"),
    ("msg3", "fix: amounts show two decimals"),
    ("msg4", "feat: T4 routes with a nav layout and an Add Expense page"),
    ("msg5", "Merge branch 'feat/routing'"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Not an exercise today: today every merge is a fast-forward. This is "
     "the case you will meet alone when something urgent comes up, and every day in a team."),
    ("The message",
     "If the main line gets a commit while your task is in progress, git merge makes a real merge commit with two "
     "parents. And before any git switch: commit (or stash) what you have."),
    ("Read the graph",
     "During T4 (feat/routing), an urgent bug on the amounts. 1) On the branch, commit what you have, even red: "
     "msg2, a test: commit marked (wip, red) — wip = work in progress. 2) git switch mywork, fix (test first), "
     "commit msg3. 3) git switch feat/routing, go on until green: msg4. 4) git switch mywork, git merge "
     "feat/routing: mywork has moved (msg3), so git creates msg5, whose two parents are msg3 and msg4."),
    ("Why commit before git switch",
     "Uncommitted changes are not on any branch: git switch carries them onto the other branch (or refuses if "
     "they clash). Without msg2, your half-done T4 test would end up in the fix commit msg3."),
    ("In a team",
     "The usual case: while you work on your branch, teammates' branches are merged into main. Your merge (or pull "
     "request) then makes a merge commit, and if both changed the same lines git stops with a CONFLICT: you "
     "choose. Short-lived branches keep conflicts small."),
    ("Alone, in parallel",
     "To work on two branches really at the same time, one folder per branch: git worktree add, one opencode "
     "session in each (GSE-One, from day 3). In one folder: one branch at a time."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git add -A && git commit -m \"test: T4 routes show Add Expense at /add (wip, red)\"",
     "Saves the half-done task on its branch: what it contains (the T4 test) and that it is unfinished (wip = work "
     "in progress, red). git status first: see what you save. The tests may be red: "
     "it is on the task branch, not on mywork."),
    ("Command — git stash / git stash pop",
     "Instead of the wip commit: git stash puts the uncommitted changes aside (the folder becomes clean); after "
     "the fix, back on the task branch, git stash pop brings them back."),
    ("Command — git merge feat/routing (mywork has moved)",
     "Creates the merge commit M and may open a text editor for its message (« Merge branch 'feat/routing' »): "
     "save and close it (nano: Ctrl+O, Enter, Ctrl+X; vim: Esc then :wq)."),
]


def _steps(kw):
    return [
        ("1", ("Urgent bug while the T4 test is still red? On the branch, first commit what you have: msg2 (or ",
               (kw, "git stash"), ").")),
        ("2", ((kw, "git switch mywork"), ", fix it, commit msg3; then ", (kw, "git switch feat/routing"),
               " and go on: msg4.")),
        ("3", ((kw, "git switch mywork"), " then ", (kw, "git merge feat/routing"), ": mywork moved, so git creates "
               "msg5 with two parents.")),
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
        draw(cols(_N), _ROWS, zoom=_GRAPH_ZOOM)
        st_space("v", "1vh")
        legend(_MSGS)
        st_space("v", "1.5vh")
        kw = bs.keyword
        steps(_steps(kw), zoom=60)
