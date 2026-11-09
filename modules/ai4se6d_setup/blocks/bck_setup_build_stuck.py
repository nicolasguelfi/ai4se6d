"""Slide — If you get stuck while building (stays on screen during the workshop)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Build stuck slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    warn = s.bold + s.project.colors.highlight
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_bstuck_caption")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "If You Get Stuck", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Rephrase"), " — smaller, more precise request")
            with l.item():
                st_write(bs.body, (bs.keyword, "Paste the error"), " to the agent: “this fails with …”")
            with l.item():
                st_write(bs.body, "Ask ", (bs.keyword, "@tutor"))
            with l.item():
                st_write(bs.body, (bs.warn, "Raise your hand"), " — technical blockers")
        st_space("v", 1)
        st_write(bs.caption, "Do not worry about code quality today. There is no “right way” — just build.", tag=t.div)
