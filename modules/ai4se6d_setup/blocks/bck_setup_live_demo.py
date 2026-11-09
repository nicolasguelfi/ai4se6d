"""Slide — Live demo (5 min): what to watch while the trainer drives opencode."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Live demo slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
    caption = s.project.titles.caption
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Live Demo — 5 min", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        st_write(bs.label, "Watch:", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, "What I type — ", (bs.keyword, "one plain sentence"))
            with l.item():
                st_write(bs.body, "The agent ", (bs.keyword, "reads the folder"), " (empty)")
            with l.item():
                st_write(bs.body, "It ", (bs.keyword, "creates files"), " on its own")
            with l.item():
                st_write(bs.body, "What it ", (bs.keyword, "asks me"), " — and what I answer")
            with l.item():
                st_write(bs.body, "Something I can ", (bs.keyword, "open and run"))
