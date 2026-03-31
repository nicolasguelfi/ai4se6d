"""Slide — 4 Principles of VibeCoding."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_vc_principles",
)


class BlockStyles:
    """VibeCoding principles slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "4 Principles of VibeCoding", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Intent over Implementation"), " \u2014 describe WHAT, not HOW")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Trust in Output"), " \u2014 if it works = good enough")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Conversational Iteration"), " \u2014 describe bugs back to AI")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Low Barrier to Entry"), " \u2014 non-programmers can build prototypes")
