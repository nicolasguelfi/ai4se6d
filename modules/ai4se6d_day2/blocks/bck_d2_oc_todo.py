"""Slide — The agent's todo list."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Todo list styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    intro = Style.create(s.project.titles.body + s.center_txt, "d2_todo_intro")
    closing = Style.create(s.project.titles.body + s.project.colors.critical + s.bold + s.center_txt, "d2_todo_closing")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "The Todo List", tag=t.div, toc_lvl="+1")
        st_space("v", 0.5)
        st_write(bs.intro, "On multi-step work the agent writes a todo list and ticks items as it goes.", tag=t.div)
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item(): st_write(bs.body, (bs.keyword, "See"), " where it is in the work")
            with l.item(): st_write(bs.body, (bs.keyword, "Stop"), " it as soon as it drifts (Esc)")
            with l.item(): st_write(bs.body, (bs.keyword, "Check"), " nothing was skipped before you commit")
        st_space("v", 1)
        st_write(bs.closing, "Ticked is not done. Done = tests green + diff reviewed.", tag=t.div)
