"""Slide — Driving opencode: what to remember."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Takeaways styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "What to Remember", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, (bs.keyword, "Structure + AGENTS.md"), " = your standing prompt")
            with l.item(): st_write(bs.body, (bs.keyword, "Context is finite"), ": @ the right files, no secrets, /new per task")
            with l.item(): st_write(bs.body, (bs.keyword, "Shift+Tab"), ": plan first, build second")
            with l.item(): st_write(bs.body, (bs.keyword, "Todo ticked ≠ done"), ": tests + reviewed diff")
            with l.item(): st_write(bs.body, (bs.keyword, "MCP"), " adds tools; ", (bs.keyword, "Context7"), " adds live docs")
