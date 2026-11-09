"""Slide — FreeSelfApp part 2 (after the break): keep going."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Part 2 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Part 2 — Keep Going", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, "Add ", (bs.keyword, "one feature"), " you really want")
            with l.item():
                st_write(bs.body, "Ask the agent to ", (bs.keyword, "explain one file"), " — do you get it?")
            with l.item():
                st_write(bs.body, (bs.keyword, "Commit"), " after each working step")
            with l.item():
                st_write(bs.body, "Update ", (bs.keyword, "notes.md"))
        st_space("v", 1)
        st_write(bs.body, (bs.label, "16:10: "), "last commit, notes ready for the debrief.")
