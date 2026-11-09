"""Slide — Git debrief (5 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Debrief styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    pair = Style.create(s.project.titles.body_accent + s.center_txt, "d2_gitdeb_pair")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Debrief — 5 min", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, "What did ", (bs.keyword, "git diff"), " show when you broke the file — and after ", (bs.keyword, "git restore"), "?")
            with l.item(): st_write(bs.body, "The agent just edited 5 files. Which command do you run first, and why?")
        st_space("v", 2)
        st_write(bs.pair, "Compare git log --oneline with your neighbour: same history?", tag=t.div)
