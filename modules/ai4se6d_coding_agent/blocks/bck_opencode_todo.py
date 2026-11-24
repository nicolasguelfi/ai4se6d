"""Slide — The agent's todo list."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Todo list styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    intro = Style.create(s.project.titles.body + s.center_txt, "todo_intro")
    closing = Style.create(s.project.titles.body + s.project.colors.critical + s.bold + s.center_txt, "todo_closing")
bs = BlockStyles

_NOTES = [
    ("The message",
     "On multi-step work the agent writes a todo list and ticks items as it goes: a live view of its progress."),
    ("Three uses",
     "See where it is in the work; stop it with Esc as soon as it drifts; check that nothing was skipped before "
     "you commit."),
    ("The trap",
     "Trusting the ticks. A ticked item only means the agent believes it is done."),
    ("Definition of done",
     "Done = tests green + diff reviewed. The same rule returns in the build and review sessions this afternoon."),
    ("Ask the room",
     "« What would make you press Esc while the agent is working? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "The Todo List", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Todo List", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(120):
            st_write(bs.intro, "On multi-step work the agent writes a todo list and ticks items as it goes.",
                     tag=t.div)
        st_space("v", "3vh")

        # One row per use, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.keyword, "See"), " where it is in the work"),
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
            st_write(bs.closing, "Ticked is not done. Done = tests green + diff reviewed.", tag=t.div)
