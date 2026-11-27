"""Slide — GSE-One in git (S0): what changes from day 2 (NG « OK série GSE », 2026-11-27).

Opens the GSE-One git series (S1-S8 are commit graphs): one row per habit of day 2 and what GSE-One does instead,
checked against gse-one/src/activities/{plan,produce,review,fix,deliver}.md and templates/config.yaml.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Day 2 → GSE-One table styles."""
    heading = s.project.titles.heading
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "gsegit_cmd")
bs = BlockStyles

_TITLE = "Day 2 → GSE-One Git"
_TABLE_ZOOM = 66

# (topic, day 2, GSE-One)
_ROWS = [
    ("Main line", ("mywork, then main at the end of the day.",),
     ("The sprint branch ", (bs.cmd, "gse/sprint-01/integration"), "; main only at delivery.")),
    ("Where a task lives", ("A branch in your one folder: commit or stash, then git switch.",),
     ("A branch and its own folder: ", (bs.cmd, ".worktrees/sprint-01-feat-edit-expense"), ".")),
    ("Test first", ("Unit test (red), code (green), maybe a refactor commit.",),
     ("The acceptance test of the REQ (red), then the code with its unit tests (green).",)),
    ("When tasks are merged", ("Right after each task, by fast-forward.",),
     ("Only at /gse:deliver, after review and fix.",)),
    ("How they are merged", ("Fast-forward: git only moves the name.",),
     ("Squash proposed (one commit per task) into the sprint; ", (bs.cmd, "merge --no-ff"), " into main.")),
    ("Safety net", ("None: you undo by hand.",),
     ("A ", (bs.cmd, "gse-backup/…"), " tag before each merge or deletion, kept 30 days; a version tag.")),
    ("Who types git", ("You.",), ("The agent. You decide at each Gate.",)),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Start from what they did on day 2; the next slides draw each row."),
    ("The message",
     "The habits of day 2 stay — one branch per task, the test before the code, review before keeping — but GSE-One "
     "runs them, adds a sprint branch between the tasks and main, one folder per task, and backup tags."),
    ("Row by row",
     "Main line: the sprint branch is created by /gse:plan. Where a task lives: git.strategy: worktree (default). "
     "Test first: testing.strategy: auto = atdd for code tasks with Given/When/Then. When merged: /gse:deliver. How: "
     "merge_strategy_default: squash, then merge --no-ff into main. Safety net: backup_before_destructive: true, "
     "backup_retention_days: 30, tag_on_deliver: true. Who types: every merge is a Gate."),
    ("All in .gse/config.yaml",
     "git.strategy (worktree | branch-only | none), git.merge_strategy_default (squash | merge | rebase), "
     "git.tag_on_deliver, git.cleanup_on_deliver, git.backup_retention_days, testing.strategy (auto | atdd | "
     "test-after). Change them with /gse:hug --update."),
    ("The next slides",
     "Opening the sprint (/gse:plan), One task (/gse:produce), Tasks in parallel (worktrees, spike), Review and fix, "
     "Tasks into the sprint, Sprint into main, Cleanup and undo (/gse:deliver), The quick path (/gse:task --quick)."),
    ("Source",
     "gse-one/src/activities/plan.md Step 6, produce.md Steps 2 and 3.1, review.md Step 1, fix.md Steps 2-4, "
     "deliver.md Steps 0-8, task.md (--quick, --spike); templates/config.yaml."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, _TITLE, tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — " + _TITLE, entries=_NOTES, position="left", width="50vw")
        st_space("v", "1.5vh")

        # Header row, then one row per habit, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "2% 20% 34% 42% 2%"
        base = s.project.containers.row_cell_left
        hc = s.project.containers.table_header_cell
        head = [base, hc, hc, hc, base]
        cells = head + s.project.containers.rows(len(_ROWS), cols, filled=(2, 3, 4))
        with st_zoom(_TABLE_ZOOM), st_grid(cols=cols, gap="1vh 0.5vw", cell_styles=cells) as g:
            for h in ("", "", "Day 2", "GSE-One", ""):
                with g.cell():
                    if h:
                        st_write(bs.th, h)
            for topic, day2, gse in _ROWS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.tl, topic)
                with g.cell():
                    st_write(bs.td, *day2)
                with g.cell():
                    st_write(bs.td, *gse)
                with g.cell():
                    pass  # right margin
