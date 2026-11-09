"""Slide — Debrief: three questions, neighbour first."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Debrief questions styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Three Questions", tag=t.div, toc_lvl="1")
        st_write(bs.body, (bs.label, "3 min with your neighbour, then together:"))
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, "When did the agent ", (bs.keyword, "surprise"), " you — good or bad?")
            with l.item():
                st_write(bs.body, "What ", (bs.keyword, "broke"), ", and who fixed it?")
            with l.item():
                st_write(bs.body, "Would you give this app to a ", (bs.keyword, "client"), " tomorrow? Why not?")
