"""Slide — GSE-One in git (S1): opening the sprint (NG « OK série GSE », 2026-11-27).

What /gse:plan does in git (gse-one/src/activities/plan.md, Step 6 — Git Integration): it creates the sprint branch
gse/sprint-NN/integration from main (no commit) and writes a branch name into each task (branch_status: planned).
The task branches themselves are created later, by /gse:produce. Example: CalcApp sprint 01, from v0.1 (day 2).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from git_graph import INTEG, MAIN, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """GSE-One git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)

_TITLE = "GSE-One Git · Opening the Sprint"
_N = 3
_GRAPH_ZOOM = 62
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [("k", "main", MAIN), ("n", "docs", MAIN)] + [_E] * 4,
    [_E, ("c", "msg1 · tag v0.1")] + [_E] * 4,
    [_E, ("a", "↓", INTEG)] + [_E] * 4,
    [("k", "gse/sprint-01/integration", INTEG), ("p", "same commit", INTEG), _E,
     ("c", "the main line of the sprint: tasks branch from here, deliveries come back here"), _E, _E],
]
# The last commit of day 2, then the branch names /gse:plan writes into each task (examples of CalcApp sprint 01)
_MSGS = [
    ("msg1", "docs: README"),
]
_PLAN = [
    ("TASK-001", "gse/sprint-01/feat/edit-expense — REQ-001 edit an existing expense"),
    ("TASK-002", "gse/sprint-01/feat/sort-expenses — REQ-003 sort the expenses"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type: /gse:plan runs these git commands; you validate the plan at its Gate."),
    ("The message",
     "On day 2 your main line was mywork. With GSE-One, each sprint gets its own main line, "
     "gse/sprint-01/integration, created from main. main itself only moves at delivery."),
    ("Read the graph",
     "Blue = main, ending with v0.1 (the last commit of day 2, docs: README). Amber = the sprint branch: a new name "
     "on the same commit — no commit, nothing copied. The table under the graph shows the branch name the plan "
     "gives each task; those branches do not exist yet."),
    ("Branch names",
     "From the type of artefact the task produces: code → gse/sprint-01/feat/…, test → …/test/…, fix → …/fix/…, "
     "design or doc → …/docs/…, config → …/chore/…. Written in backlog.yaml (git.branch) with branch_status: "
     "planned; /gse:produce reads the name and does not re-derive it."),
    ("Full and Lightweight",
     "The sprint branch exists in both modes (produce.md, branch-only strategy: « created by /gse:plan Step 6 — Git "
     "Integration, in Full and Lightweight modes alike »). Only Micro mode has no plan and no sprint branch."),
    ("Never on main",
     "Sprint work is never committed on main: the protect-main hook refuses it. main receives the sprint once, at "
     "/gse:deliver."),
    # Command recap: every command of the slide, in plain words (NG, 2026-11-24)
    ("Command — git branch gse/sprint-01/integration main",
     "Creates the sprint branch on main's last commit, without switching to it. No file changes, no commit."),
    ("Source",
     "gse-one/src/activities/plan.md — Step 6 (Git Integration). produce.md — Step 2 (fallback if the sprint branch "
     "is missing)."),
]


def _steps(kw):
    return [
        ("1", ("/gse:plan creates the sprint branch on main's last commit: ",
               (kw, "git branch gse/sprint-01/integration main"), ". No commit.")),
        ("2", ("It writes one branch name into each task of the plan (table above). The branches are created "
               "later, one by one, by /gse:produce.",)),
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
        st_space("v", "1vh")
        legend(_PLAN, id_width=13)
        st_space("v", "1.5vh")
        steps(_steps(bs.keyword), zoom=60)
