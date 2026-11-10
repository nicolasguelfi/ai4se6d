"""Slide — Tomorrow (day 2): CalcApp, git first, you drive the agent with a plan."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Day 2 preview styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_day2_caption")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Tomorrow — Day 2", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "CalcApp"), " — a shared starter project")
            with l.item():
                st_write(bs.body, (bs.keyword, "Git first"), " — status, diff, commit, branch")
            with l.item():
                st_write(bs.body, "You ", (bs.keyword, "drive the agent with your plan"))
            with l.item():
                st_write(bs.body, (bs.keyword, "AI code review"), " — HIGH / MEDIUM / LOW")
        st_space("v", 1)
        st_write(bs.caption, "Same tools, different discipline. No homework — keep your key sheet.", tag=t.div)
