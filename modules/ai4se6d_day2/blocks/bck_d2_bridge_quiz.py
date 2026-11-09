"""Slide — Hands-up quiz — 5 questions."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Hands-up quiz — 5 questions — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_bridge_quiz_body")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Hands-Up Quiz: Yes or No?', tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'A brand-new test fails before any code exists. Expected?')
                with l.item():
                    st_write(
                        bs.body,
                        'The agent wrote test + code in one go, all green. Merge without reading?',
                    )
                with l.item():
                    st_write(
                        bs.body,
                        'You sabotage the code and every test still passes. Are the tests useful?',
                    )
                with l.item():
                    st_write(bs.body, 'A 1,200-line diff: is one review pass enough?')
                with l.item():
                    st_write(bs.body, 'May you refuse a finding of the AI review?')
