"""Slide — The mutant test trick."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """The mutant test trick — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_mutant_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_mutant_foot")
bs = BlockStyles


_MUTANT = """\
ExpenseItem:  amount.toFixed(2)  →  amount.toFixed(0)
"€25.50" becomes "€26": the test must go red."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'The Mutant Test Trick', tag=t.div, toc_lvl='+1')
            st_write(bs.body, 'After GREEN, sabotage your own code:', tag=t.div)
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Break the implementation on purpose')
                with l.item():
                    st_write(bs.body, 'Run the tests — does one fail?')
                with l.item():
                    st_write(bs.body, (bs.keyword, 'Yes'), ' → the test is real. Undo the sabotage.')
                with l.item():
                    st_write(bs.body, (bs.keyword, 'No'), ' → the test proves nothing. Fix the test.')
            st_code(s.none, code=_MUTANT, language='text', line_numbers=False, font_size="36pt")
            st_write(bs.foot, 'Ten seconds of sabotage saves hours of false confidence.', tag=t.div)
