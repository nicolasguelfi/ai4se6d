"""Slide — When the main line moves: urgent fix during a task, wip commit, real merge commit (NG « ok », 2026-11-27).

Not an exercise of day 2 (there, every merge is a fast-forward): the case where mywork gets a commit while a
task is in progress — an urgent fix alone, or teammates' merges in a team. Commit (or stash) before git switch,
because uncommitted changes follow you onto the other branch (ss2-ul-gse remark, git-worktree-guide § 3).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.git_graph import MAIN, TASK, cols, draw, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Day-2 git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)

_TITLE = "When the Main Line Moves"
_N = 7
_GRAPH_ZOOM = 60
_LM = ("l", MAIN)
_LT = ("l", TASK)
_ROWS = [
    [("k", "mywork", MAIN), ("n", "docs", MAIN), _LM, _LM, _LM, _LM, _LM, ("n", "fix", MAIN), _LM, _LM, _LM, _LM, _LM,
     ("m", "M")],
    [_E, ("c", "docs: v0.1 plan"), _E, _E, _E, _E, _E, ("c", "fix: total (urgent)"), _E, _E, _E, _E, _E,
     ("c", "merge commit, two parents")],
    [_E, _E, ("a", "↘", TASK), _E, _E, _E, _E, _E, _E, _E, _E, _E, ("a", "↗", TASK), _E],
    [("k", "feat/routing", TASK), _E, _E, ("n", "test", TASK), _LT, ("n", "wip", TASK), _LT, _LT, _LT,
     ("n", "feat", TASK), _LT, ("n", "ref", TASK), _E, _E],
    [_E, _E, _E, ("c", "test: … (red)"), _E, ("c", "chore: wip"), _E, ("c", "⇅ git switch"), _E,
     ("c", "feat: … (green)"), _E, ("c", "refactor: …"), _E, _E],
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Not an exercise today: today every merge is a fast-forward. This is "
     "the case you will meet alone when something urgent comes up, and every day in a team."),
    ("The message",
     "If the main line gets a commit while your task is in progress, git merge makes a real merge commit with two "
     "parents. And before any git switch: commit (or stash) what you have."),
    ("Read the graph",
     "During feat/routing, an urgent bug on the total. 1) On the branch, commit what you have, even red: chore: "
     "wip. 2) git switch mywork, fix (test first), commit fix: total. 3) git switch feat/routing, go on: feat:, "
     "refactor:. 4) git switch mywork, git merge feat/routing: mywork has moved (fix: total), so git creates M, "
     "whose two parents are fix: total and refactor:."),
    ("Why commit before git switch",
     "Uncommitted changes are not on any branch: git switch carries them onto the other branch (or refuses if "
     "they clash). Without the wip commit, your half-done task would end up in the fix: total commit."),
    ("In a team",
     "The usual case: while you work on your branch, teammates' branches are merged into main. Your merge (or pull "
     "request) then makes a merge commit, and if both changed the same lines git stops with a CONFLICT: you "
     "choose. Short-lived branches keep conflicts small."),
    ("Alone, in parallel",
     "To work on two branches really at the same time, one folder per branch: git worktree add, one opencode "
     "session in each (GSE-One, from day 3). In one folder: one branch at a time."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git add -A && git commit -m \"chore: wip\"",
     "Saves the half-done task on its branch. chore: = housekeeping; wip = work in progress. The tests may be red: "
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
        ("1", ("Urgent bug during a task? On the branch, first ", (kw, "git add -A && git commit -m \"chore: wip\""),
               " (or ", (kw, "git stash"), ").")),
        ("2", ((kw, "git switch mywork"), ", fix it, commit ", (kw, "fix: total"), "; then ",
               (kw, "git switch feat/routing"), " and go on.")),
        ("3", ((kw, "git switch mywork"), " then ", (kw, "git merge feat/routing"), ": mywork moved, so git creates M "
               "with two parents.")),
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
        st_space("v", "2vh")
        kw = bs.keyword
        steps(_steps(kw), zoom=68)
