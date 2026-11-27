"""Slide — The agent saying done ≠ done (was « The Todo List »; NG « ok », 2026-11-27, kit 7a28b0e).

opencode 2's todo tool (todowrite) is off by default (opt-in: "experimental": {"todo": true}); neither the kit nor
GSE-One enables it, so learners never see a todo list. What stays: watch the agent, stop it, check before commit.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Agent-says-done styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    intro = Style.create(s.project.titles.body + s.center_txt, "todo_intro")
    closing = Style.create(s.project.titles.body + s.project.colors.critical + s.bold + s.center_txt, "todo_closing")
bs = BlockStyles

_NOTES = [
    ("The message",
     "On multi-step work, watch what the agent does: stop it as soon as it drifts (Esc), and check nothing was "
     "skipped before you commit. Its « done » is a claim."),
    ("The trap",
     "Trusting the agent's summary. « Done, all tests pass » only means the agent believes it: run the tests "
     "yourself and read the diff."),
    ("Why no todo list",
     "In opencode 2 the todo tool is off by default (opt-in: \"experimental\": {\"todo\": true}); the course kit "
     "does not enable it, so learners never see one. Progress is tracked in your files instead: docs/plan.md "
     "today, the GSE-One backlog from day 3."),
    ("Definition of done",
     "Done = tests green + diff reviewed. The same rule returns in the build and review sessions this afternoon."),
    ("Ask the room",
     "« What would make you press Esc while the agent is working? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Key — Esc",
     "In opencode, Esc interrupts the agent while it works. Changes it already made stay in your files: check them"
     " with git diff (and git restore if needed)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "The Agent Saying Done ≠ Done", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Agent Saying Done ≠ Done", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(120):
            st_write(bs.intro, "On multi-step work, watch what the agent does.", tag=t.div)
        st_space("v", "3vh")

        # One row per use, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.keyword, "Stop"), " it as soon as it drifts (Esc)"),
            ((bs.keyword, "Check"), " nothing was skipped before you commit"),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(124), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(124):
            st_write(bs.closing, "Its « done » is a claim. Done = tests green + diff reviewed.", tag=t.div)
