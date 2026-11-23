"""Slide — Driving opencode: what to remember."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Takeaways styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_NOTES = [
    ("The message",
     "Five takeaways of the opencode session, one per part: structure and rules, context, plan/build, todo list, "
     "MCP."),
    ("Standing prompt",
     "Project structure and AGENTS.md are read before any prompt: write them once, benefit at every session."),
    ("Finite context",
     "@ the right files, never secrets, /new per task."),
    ("Plan, then build",
     "Shift+Tab: plan first, build second. And a ticked todo is not done: tests + reviewed diff."),
    ("Tools",
     "MCP adds tools; Context7 adds live docs — enable few."),
    ("Ask the room",
     "« Which of the five will you apply first in the planning workshop? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "What to Remember", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What to Remember", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")

        # One numbered row per takeaway, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.keyword, "Structure + AGENTS.md"), " = your standing prompt"),
            ((bs.keyword, "Context is finite"), ": @ the right files, no secrets, /new per task"),
            ((bs.keyword, "Shift+Tab"), ": plan first, build second"),
            ((bs.keyword, "Todo ticked ≠ done"), ": tests + reviewed diff"),
            ((bs.keyword, "MCP"), " adds tools; ", (bs.keyword, "Context7"), " adds live docs"),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(115), st_grid(cols=cols, gap="4.5vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
