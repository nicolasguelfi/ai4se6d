"""Slide — Why GenSEMOne? Problem and solution."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Why GenSEMOne slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    callout_text = s.project.titles.body + s.project.colors.highlight
    closing = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_method_why_closing",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Why GenSEMOne?", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_text,
                "1.5 days to build a project. Without method: "
                "VibeCoding \u2192 debt \u2192 run out of time.",
            )

        st_space("v", 1)
        st_write(bs.body, (bs.keyword, "Solution: "), "GenSEMOne maps CE principles to Cursor native features:")
        st_space("v", 0.5)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, ".cursor/rules/*.mdc"), " = CE Compound output")
            with l.item():
                st_write(bs.body, (bs.keyword, "Plan Mode"), " = CE Brainstorm + Plan")
            with l.item():
                st_write(bs.body, (bs.keyword, "Act Mode"), " = CE Work")
            with l.item():
                st_write(bs.body, (bs.keyword, "Todo system"), " = CE task tracking")
            with l.item():
                st_write(bs.body, (bs.keyword, "MCP + Context7"), " = external knowledge")

        st_space("v", 2)
        with st_block(s.center_txt):
            st_write(bs.closing, "No new tools to learn \u2014 everything from Days 1\u20134, now orchestrated.")
