"""Slide — GSE-One in git (S8): the quick path, /gse:task --quick (NG « OK série GSE », 2026-11-27).

task.md, Quick path Q1-Q6: eligibility (≤ 1 point, one concern, nothing security-sensitive, no migration, no new
dependency), branch gse/quick/{short-name} from main without worktree, change + test + backlog entry in ONE commit
« fix|docs|chore: {summary} (quick, TASK-{ID}) », tests re-run green, one merge question (git merge --no-ff into main,
then the branch is deleted), no tag, no release notes. Example: CalcApp after v0.2.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from git_graph import MAIN, MERGE, TASK, cols, draw, legend, steps
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """GSE-One git graph slide styles."""
    heading = s.project.titles.heading
    keyword = s.project.titles.keyword
bs = BlockStyles

_E = (".",)
_LM = ("l", MAIN)

_TITLE = "GSE-One Git · The Quick Path"
_N = 3
_GRAPH_ZOOM = 64
# Columns: 0 = branch name, node i at 1 + 2i, line after node i at 2 + 2i
_ROWS = [
    [_E, ("p", "v0.2", MERGE), _E, _E, _E, ("p", "no tag", MAIN)],
    [("k", "main", MAIN), ("m", "M", "main_integ"), _LM, _LM, _LM, ("m", "M")],
    [_E, ("c", "msg1"), ("a", "↘", TASK), _E, ("a", "↗", TASK), ("c", "msg3")],
    [("k", "gse/quick/total-decimals", TASK), _E, _E, ("n", "fix", TASK), _E, _E],
    [("c", "no folder: a plain branch"), _E, _E, ("c", "msg2 · tests green"), _E, _E],
]
_MSGS = [
    ("msg1", "gse(deliver): sprint S01 delivery"),
    ("msg2", "fix: the total shows two decimals (quick, TASK-014)"),
    ("msg3", "Merge branch 'gse/quick/total-decimals'"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — learners use it for a typo, a missing import, a one-line bug; never to squeeze a real task "
     "past the sprint."),
    ("The message",
     "A small fix costs minutes, not a sprint: one short branch from main, one commit, the tests, one question. It "
     "keeps the two protections that matter — the change is isolated until merged, and the tests prove nothing "
     "broke."),
    ("Read the graph",
     "Blue = main after the sprint-01 delivery (msg1 = M, v0.2). Green = gse/quick/total-decimals, from main, "
     "without a folder of its own: ONE commit with the change, its test and the backlog entry (msg2). The project's "
     "tests are re-run and green; one question; git merge --no-ff gives the merge commit msg3, then the branch is "
     "deleted. No version tag."),
    ("Who may take it",
     "Eligible only when ALL hold: at most 1 complexity point; one concern; no security-sensitive area "
     "(authentication, authorisation, cryptography, secrets, validation of untrusted input); no data migration or "
     "deletion; no new dependency. Otherwise the agent says why in one line and follows the normal path."),
    ("When a test fails",
     "If the change breaks a test and the fix is not obvious, the quick path stops: the branch is kept and the "
     "normal path is proposed. Never weaken or delete a test to get green."),
    ("Frozen sprint",
     "The quick path works even when the sprint is delivered (frozen): it writes no sprint, only a pool TASK "
     "(sprint: null, origin_ref: quick, status: delivered)."),
    ("What it skips",
     "No worktree, no plan, no review (requires_review: false), no backup tag, no version tag, no release notes. If "
     "you want a version for it, ask for it explicitly."),
    ("Merge message",
     "task.md gives the command git merge --no-ff without -m: git writes its default message, « Merge branch "
     "'gse/quick/total-decimals' » (msg3)."),
    # Command recap: every command of the slide, in plain words (NG, 2026-11-24)
    ("Command — /gse:task --quick",
     "Starts the quick path with your description, e.g. /gse:task --quick the total shows too many decimals."),
    ("Command — git checkout main && git merge --no-ff gse/quick/total-decimals",
     "The one merge question, option 1 (recommended): a merge commit on main, then git branch -d "
     "gse/quick/total-decimals."),
    ("Source",
     "gse-one/src/activities/task.md — Quick path, Q1 (eligibility) to Q6 (close)."),
]


def _steps(kw):
    return [
        ("1", ((kw, "/gse:task --quick"), " checks the change is small: 1 point, one concern, nothing "
               "security-sensitive, no new library.")),
        ("2", ("A branch from main, no folder: the change, its test and the backlog entry in one commit (msg2). "
               "All tests re-run green.",)),
        ("3", ("One question, then ", (kw, "git merge --no-ff"), " into main (msg3) and the branch is deleted. "
               "No tag.")),
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
