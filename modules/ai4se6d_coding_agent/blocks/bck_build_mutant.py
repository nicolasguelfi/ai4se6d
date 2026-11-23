"""Slide — The mutant test trick."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """The mutant test trick — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_mutant_body")
    keyword = s.bold + s.project.colors.highlight
    number = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_mutant_foot")
bs = BlockStyles


_MUTANT = """\
ExpenseItem:  amount.toFixed(2)  →  amount.toFixed(0)
"€25.50" becomes "€26": the test must go red."""

_NOTES = [
    ("The message",
     "A green test is only worth something if it can go red. After GREEN, sabotage your own code to check it."),
    ("How",
     "Break the implementation on purpose, run the tests. One fails: the test is real, undo the sabotage. None "
     "fails: the test proves nothing, fix the test."),
    ("The example",
     "In ExpenseItem, amount.toFixed(2) becomes amount.toFixed(0): « €25.50 » becomes « €26 », and the test "
     "must go red."),
    ("Why it matters with an agent",
     "An agent can write tests that pass whatever the code does. Ten seconds of sabotage saves hours of false "
     "confidence."),
    ("Ask the room",
     "« Which line of your own code would you break to test your test? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'The Mutant Test Trick', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Mutant Test Trick", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(110):
            st_write(bs.body, 'After GREEN, sabotage your own code:', tag=t.div)
        st_space("v", "1vh")
        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        steps = [
            ('Break the implementation on purpose',),
            ('Run the tests — does one fail?',),
            ((bs.keyword, 'Yes'), ' → the test is real. Undo the sabotage.'),
            ((bs.keyword, 'No'), ' → the test proves nothing. Fix the test.'),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(steps), cols, filled=(2, 3))
        with st_zoom(115), st_grid(cols=cols, gap="1.8vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(steps, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "2vh")
        st_code(s.none, code=_MUTANT, language='text', line_numbers=False, font_size="32pt")
        st_space("v", "2vh")
        with st_zoom(100):
            st_write(bs.foot, 'Ten seconds of sabotage saves hours of false confidence.', tag=t.div)
