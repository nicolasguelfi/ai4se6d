"""Slide — What you will be able to do by 10:45."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Objectives styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "By 10:45 You Can", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, "Make a project ", (bs.keyword, "readable"), " for the agent")
            with l.item(): st_write(bs.body, "Write project rules in ", (bs.keyword, "AGENTS.md"))
            with l.item(): st_write(bs.body, "Feed the right context with ", (bs.keyword, "@file"))
            with l.item(): st_write(bs.body, (bs.keyword, "Plan"), " with the plan agent, then ", (bs.keyword, "build"))
            with l.item(): st_write(bs.body, "Follow the agent’s ", (bs.keyword, "todo list"))
            with l.item(): st_write(bs.body, "Add live docs with ", (bs.keyword, "MCP + Context7"))
