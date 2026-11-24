"""Slide — What good requirements look like."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Requirement quality styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    good = Style.create(s.project.titles.table_cell + s.project.colors.success, "good_ex")
    bad = Style.create(s.project.titles.table_cell + s.project.colors.critical, "bad_ex")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Three qualities to check on every requirement the agent proposes: testable, small, independent."),
    ("Testable",
     "A test can say yes or no: « amount 0 or negative → a validation error is shown ». « The app handles "
     "expenses well » cannot be tested, so it cannot be checked."),
    ("Small and independent",
     "Small: fits 30-45 min of work with the agent. Independent: buildable in any order, as far as possible — "
     "so one blocked task does not block the others."),
    ("Link to what follows",
     "Testable acceptance criteria become the RED tests of the afternoon (test first, code second)."),
    ("Ask the room",
     "« Pick one of your stories: can you write the test that proves it? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Good Requirements", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Good Requirements", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")
        # One row per quality, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 28% 62% 5%"
        cells = s.project.containers.rows(3, cols, filled=(2, 3))
        with st_zoom(141), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(bs.body, (bs.keyword, "Testable"), tag=t.div)
            with g.cell():
                st_write(bs.good, "✓ Amount 0 or negative → a validation error is shown", tag=t.div)
                st_write(bs.bad, "✗ The app handles expenses well", tag=t.div)
            with g.cell():
                pass  # right margin
            with g.cell():
                pass
            with g.cell():
                st_write(bs.body, (bs.keyword, "Small"), tag=t.div)
            with g.cell():
                st_write(bs.body, "fits 30-45 min of work with the agent", tag=t.div)
            with g.cell():
                pass
            with g.cell():
                pass
            with g.cell():
                st_write(bs.body, (bs.keyword, "Independent"), tag=t.div)
            with g.cell():
                st_write(bs.body, "buildable in any order, as far as possible", tag=t.div)
            with g.cell():
                pass
