"""Slide — Day 2 in git, the morning: every commit learners make before the build (NG « ok », 2026-11-27).

Git exercise: mywork from j2-start, practice branch feat/hello with docs: say hello (never merged). opencode
rules: docs: euro rule on mywork. Plan workshop: docs: v0.1 plan on mywork. Messages as on the exercise slides.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from git_graph import MAIN, SIDE, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Day-2 git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)

_TITLE = "Your Day 2 in Git · This Morning"
_N = 4
_GRAPH_ZOOM = 64
_LM = ("l", MAIN)
_ROWS = [
    [("k", "mywork", MAIN), ("n", "start", MAIN), _LM, _LM, _LM, ("n", "docs", MAIN), _LM, ("n", "docs", MAIN)],
    [_E, ("c", "j2-start + starter updates"), _E, _E, _E, ("c", "msg2"), _E, ("c", "msg3")],
    [_E, _E, ("a", "↘", SIDE), _E, _E, _E, _E, _E],
    [("k", "feat/hello", SIDE), _E, _E, ("n", "docs", SIDE), _E, _E, _E, _E],
    [_E, _E, _E, ("c", "msg1 — practice, never merged"), _E, _E, _E, _E],
]
_MSGS = [
    ("msg1", "docs: say hello"),
    ("msg2", "docs: euro rule"),
    ("msg3", "docs: v0.1 plan"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. The map of the morning: what each exercise leaves in the history."),
    ("The message",
     "By lunch, mywork holds the starter, your euro rule and your plan; feat/hello was only practice."),
    ("Read the graph",
     "Blue = mywork, created from the course tag j2-start. Purple = feat/hello, the practice branch of the Git "
     "exercise: one commit, never merged, it just stays aside (git branch still lists it). The euro rule "
     "(AGENTS.md) and the plan (docs/plan.md) are committed directly on mywork: they are the reference of every "
     "task, not a task."),
    ("Where each commit comes from",
     "docs: say hello = Git exercise (change one line of README.md). docs: euro rule = « Try It — Rules » "
     "(AGENTS.md). docs: v0.1 plan = the planning workshop (docs/plan.md)."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git checkout -b mywork j2-start",
     "Creates the branch mywork starting at the course tag j2-start and moves onto it: your main line today."),
    ("Command — git switch -c feat/hello",
     "Creates the practice branch feat/hello from where you are (mywork) and moves onto it."),
    ("Command — git switch mywork",
     "Back to the main line: needed before the euro rule, otherwise AGENTS.md would be committed on feat/hello. "
     "Git refuses if uncommitted changes would be lost: commit them first."),
    ("Command — git add (file) && git commit -m \"docs: …\"",
     "Stages the file and saves it as one commit with that message: README.md, then AGENTS.md, then docs/plan.md."),
]


def _steps(kw):
    return [
        ("1", ("Git exercise: ", (kw, "git checkout -b mywork j2-start"), " + ", (kw, "git merge origin/main"), ", then ", (kw, "git switch -c feat/hello"),
               " and commit msg1. feat/hello stays aside.")),
        ("2", ("Rules: ", (kw, "git switch mywork"), ", then commit msg2 (AGENTS.md).")),
        ("3", ("Plan: on mywork, commit msg3 (docs/plan.md). Every task branch starts here.")),
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
