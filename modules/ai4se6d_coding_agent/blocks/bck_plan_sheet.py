"""Slide — Planning exercise sheet: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise sheet styles."""
    heading = s.project.titles.heading
    label = s.project.titles.table_label
    text = s.project.titles.table_cell
    done = Style.create(s.project.titles.table_label + s.project.colors.success, "sheet_done")
bs = BlockStyles

_SHEET = [
    ("Done when", "git log --oneline on mywork shows “docs: v0.1 plan”; docs/plan.md has 5-8 tasks, one [next]"),
    ("Check", "is anything missing for the app to work end to end (wiring, entry point, assembly of the parts)? If so, add that task"),
    ("Mid-point (11:15)", "your user stories have testable acceptance criteria; you are splitting them"),
    ("If stuck", "1. your tutor window  2. cp docs/plan-example.md docs/plan.md, adapt it  3. raise your hand"),
    ("New file?", "git diff ignores untracked files: git add first, then git diff --staged"),
]

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Leave this sheet on screen during the plan exercise; at the 11:15 mid-"
     "point ask for hands up on testable criteria."),
    ("The message",
     "Participants check themselves: one line tells them when they are done, the others what to do on the way."),
    ("Done when",
     "The commit « docs: v0.1 plan » is on mywork and docs/plan.md has 5-8 tasks with exactly one [next]."),
    ("The check most people miss",
     "A plan of features can forget the wiring: entry point, assembly of the parts. Without that task the app "
     "never runs end to end."),
    ("Mid-point and rescue",
     "At 11:15 the stories should have testable criteria. Stuck: the tutor window, then docs/plan-example.md "
     "copied and adapted, then a raised hand."),
    ("Ask the room",
     "At the mid-point: « Hands up if your stories have testable acceptance criteria. »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git log --oneline",
     "Shows the history of the current branch, newest commit first. --oneline = one line per commit: a short id (7"
     " characters, e.g. a1b2c3d) then the first line of the message. Long output opens in a viewer: q to quit."),
    ("Command — cp docs/plan-example.md docs/plan.md",
     "cp = copy. First argument = the file to copy (the example shipped in the starter), second = the new file. "
     "Trap: if docs/plan.md already exists it is overwritten without warning."),
    ("Command — git add, then git diff --staged",
     "A new file is « untracked »: git diff ignores it. git add docs/plan.md stages it, then git diff --staged "
     "shows its content as it will be committed."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Your Plan — Check Yourself", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Your Plan — Check Yourself", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        # One row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 22% 68% 5%"
        cells = s.project.containers.rows(len(_SHEET), cols, filled=(2, 3))
        with st_zoom(100), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for label, text in _SHEET:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.done if label == "Done when" else bs.label, label, tag=t.div)
                with g.cell():
                    st_write(bs.text, text, tag=t.div)
                with g.cell():
                    pass  # right margin
