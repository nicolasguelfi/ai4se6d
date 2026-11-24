"""Slide — Today's manual loop next to the GSE-One commands."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Today's manual loop next to the GSE-One commands — styles."""
    heading = s.project.titles.heading
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "bridge_loop_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "bridge_loop_foot")
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "bridge_loop_th")
    table_txt = Style.create(s.project.titles.table_cell, "bridge_loop_td")
    table_lbl = Style.create(s.project.titles.table_label, "bridge_loop_tl")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Map today's manual loop onto the GSE-One commands; learners run "
     "them from day 3."),
    ("The message",
     "Everything done by hand today has a GSE-One command tomorrow. Same loop, same severities."),
    ("Row by row",
     "Plan → tasks in docs/plan.md: /gse-plan. Test first, from the acceptance criteria, one branch per task: "
     "/gse-produce writes the acceptance test, shows it failing, commits it, then the code (/gse-tests plans "
     "the tests in Full mode). Review and triage HIGH / MEDIUM / LOW: /gse-review. Fix on a branch, regression "
     "test first: /gse-fix. "
     "Merge and tag v0.1: /gse-deliver."),
    ("The golden rule",
     "GSE-One shows you each failing acceptance test before it writes the code: read it, it is your spec; say "
     "stop to change it. With a beginner profile (or hands-on), it waits for your confirmation."),
    ("The guardrail",
     "GSE-One will not deliver over an open HIGH finding without your explicit decision."),
    ("Why by hand first",
     "Having run each step yourself, you know what the command does and can judge its output — the plugin "
     "automates the loop, it does not replace your decisions."),
    ("Ask the room",
     "« Which of today's steps do you most want automated, and which would you never hand over? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Symbol — /gse-… commands",
     "Typed in opencode's input box, not in the terminal: a message starting with / runs a command; the GSE-One "
     "plugin adds the /gse-… ones (typing / shows the list). Each accepts --help for its options."),
    ("Command — /gse-plan (GSE-One, day 3)",
     "Selects backlog items for the sprint and writes the sprint plan in .gse/plan.yaml (not docs/plan.md). "
     "--strategic = sprint level, --tactical = reorder or adjust within the current plan."),
    ("Command — /gse-produce (GSE-One, day 3)",
     "Runs the next pending task: its own branch (by default its own working folder too), acceptance test "
     "written, seen failing, committed, then the code. --task TASK-ID = a given task; --dry-run = show only."),
    ("Command — /gse-review (GSE-One, day 3)",
     "Numbered findings RVW-… ranked HIGH / MEDIUM / LOW on the sprint's branches, plus a devil's advocate pass."),
    ("Command — /gse-fix (GSE-One, day 3)",
     "Fixes the kept findings on a separate branch; --finding RVW-001 = one finding."),
    ("Command — /gse-deliver (GSE-One, day 3)",
     "Merges the finished branches, tags the version, cleans up; stops on an open HIGH finding for your decision."
     " --dry-run = show the plan only."),
]

_ROWS = [
    (('Plan → tasks in ', (bs.cmd, 'docs/plan.md')), ((bs.cmd, '/gse-plan'),)),
    (('Test first (acceptance test), one branch per task',), ((bs.cmd, '/gse-produce'),)),
    (('Review, triage HIGH / MEDIUM / LOW',), ((bs.cmd, '/gse-review'),)),
    (('Fix on a branch, regression test first',), ((bs.cmd, '/gse-fix'),)),
    (('Merge + tag ', (bs.cmd, 'v0.1')), ((bs.cmd, '/gse-deliver'),)),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Today by Hand → GSE-One', tag=t.div, toc_lvl='1', label='Bridge to GSE-One')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Today by Hand → GSE-One", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # header row + one row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 47% 43% 5%"
        cells = s.project.containers.rows(len(_ROWS) + 1, cols, filled=(2, 3))
        cells[1:3] = [s.project.containers.table_header_cell] * 2
        with st_zoom(107), st_grid(cols=cols, gap="1.5vh 0.5vw", cell_styles=cells) as g:
            for cell in ('', 'Today, by hand', 'GSE-One (Day 3)', ''):
                with g.cell():
                    if cell:
                        st_write(bs.table_hdr, cell)
            for left, right in _ROWS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.table_lbl, *left, tag=t.div)
                with g.cell():
                    st_write(bs.table_txt, *right, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "2vh")
        with st_zoom(96):
            st_write(
                bs.foot,
                'Same loop — GSE-One shows you each failing acceptance test before the code: read it.',
                tag=t.div,
            )
