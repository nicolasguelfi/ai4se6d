"""Slide — From stories to atomic tasks (example)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Atomic tasks styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "atomic_body")
    keyword = s.project.titles.keyword
    item = s.project.titles.table_cell
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_NOTES = [
    ("The message",
     "A user story is too big for one prompt. Split it into atomic tasks: one thing each, verifiable, in order."),
    ("Reading the example",
     "Four tasks for v0.1: the expense type with its validation test, then save/load from localStorage, then "
     "the list with the monthly total, then the routes and the navigation bar. Each one starts with a test."),
    ("Why atomic",
     "One task = one prompt, one branch, one review. If it goes wrong you lose one small task, not the app."),
    ("The trap",
     "Forgetting the task that wires the parts together (entry point, assembly): the check of the exercise "
     "sheet asks for it."),
    ("Ask the room",
     "« Which of your stories needs to be split the most? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "From Stories to Atomic Tasks", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — From Stories to Atomic Tasks", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(136):
            st_write(
                bs.body, "One thing · ", (bs.keyword, "verifiable"), " · ordered",
                tag=t.div,
            )
        st_space("v", "3vh")
        # One numbered row per task, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        tasks = [
            "Expense type + test: an amount ≤ 0 is rejected",
            "Test then code: a saved expense is loaded back from localStorage",
            "Test then code: the list shows items and the monthly total",
            "Test then code: routes / and /add, with a navigation bar",
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(tasks), cols, filled=(2, 3))
        with st_zoom(130), st_grid(cols=cols, gap="2.5vh 0.5vw", cell_styles=cells) as g:
            for n, task in enumerate(tasks, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.item + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.item, task, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "4vh")
        with st_zoom(136):
            st_write(bs.body, "Test first, code second — in every task.", tag=t.div)
