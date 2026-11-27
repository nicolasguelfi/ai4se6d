"""Slide — Day 2 in git, the end: review branch, fast-forward merge, tag v0.1, main (NG « ok », 2026-11-27).

After the last task: fix/review with fix: RVW-1 … (test first) and docs: README, merged into mywork
(fast-forward), tag v0.1, git switch -C main mywork. Messages and commands as on the exercise slides
(bck_review_ex_steps, bck_review_ex_fix, bck_review_readme_ex, bck_ship_release).
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

_TITLE = "Your Day 2 in Git · Review and v0.1"
_N = 4
_GRAPH_ZOOM = 64
_LT = ("l", TASK)
_ROWS = [
    [("k", "mywork", MAIN), ("n", "docs", MAIN), _E, _E, _E, _E, _E, ("p", "v0.1 · main", MAIN)],
    [_E, ("c", "msg1 (last task)"), _E, _E, _E, _E, _E, ("c", "and mywork: on msg3, no new commit")],
    [_E, _E, ("a", "↘", TASK), _E, _E, _E, ("a", "↗", TASK), _E],
    [("k", "fix/review", TASK), _E, _E, ("n", "fix", TASK), _LT, ("n", "docs", TASK), _E, _E],
    [_E, _E, _E, ("c", "msg2 (test first)"), _E, ("c", "msg3"), _E, _E],
]
# Example messages, as on the exercise slides (bck_review_ex_fix, bck_review_readme_ex)
_MSGS = [
    ("msg1", "docs: update plan labels"),
    ("msg2", "fix: RVW-1 corrupt JSON no longer crashes"),
    ("msg3", "docs: README"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. The end of the day: the review fixes, then v0.1."),
    ("The message",
     "The review is one more branch, merged like a task; v0.1 is a name on a commit, not a new commit."),
    ("Read the graph",
     "Blue = mywork after the last task. Green = fix/review: one commit per fixed finding (fix: RVW-1 …, a failing "
     "test first, then the fix) and the README (docs: README). git merge is a fast-forward again: mywork jumps to "
     "docs: README. Then three names point to that same commit: the tag v0.1, main and mywork."),
    ("Why main only now",
     "main held only the starter all day (AGENTS.md: never commit directly to main). git switch -C main mywork "
     "moves main onto your v0.1: from day 3, GSE-One takes main as the reference."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git switch -c fix/review",
     "Creates the review branch from mywork and moves onto it. Be on mywork first."),
    ("Command — git switch mywork && git merge fix/review",
     "Back to the main line, then bring the review commits into it: « Fast-forward ». Also merge any finished feat/ "
     "branch not merged yet. Then npm run test:run: all green before tagging."),
    ("Command — git tag v0.1",
     "Puts the name v0.1 on the current commit, for good. git tag lists the tags; wrong commit? git tag -d v0.1, "
     "then tag again."),
    ("Command — git switch -C main mywork",
     "-C = create or reset: main now points to the same commit as mywork, and you are on main. Check with git "
     "branch -v: main and mywork on the same commit."),
]


def _steps(kw):
    return [
        ("1", ((kw, "git switch -c fix/review"), ": commit msg2 (failing test first), then msg3.")),
        ("2", ((kw, "git switch mywork"), " then ", (kw, "git merge fix/review"), ": « Fast-forward » again; tests "
               "all green.")),
        ("3", ((kw, "git tag v0.1"), " then ", (kw, "git switch -C main mywork"), ": three names, one commit — no "
               "new commit.")),
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
