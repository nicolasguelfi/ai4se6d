"""Slide — CE in Action: preview of Day 6 demo."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """CE demo preview slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    transition = s.project.titles.body + s.project.colors.highlight + s.bold
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "CE in Action \u2014 What You'll See on Day 6", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        st_write(bs.body, "Live demo with Claude Code \u2014 full 5-phase cycle:")
        st_space("v", 0.5)

        with st_list(li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "/ce:brainstorm"), " \u2014 explore requirements interactively with the AI")
            with l.item():
                st_write(bs.body, (bs.keyword, "/ce:plan"), " \u2014 generate implementation blueprint with task graph")
            with l.item():
                st_write(bs.body, (bs.keyword, "/ce:work"), " \u2014 execute tasks with plan-constrained agent")
            with l.item():
                st_write(bs.body, (bs.keyword, "/ce:review"), " \u2014 multi-perspective review of the result")
            with l.item():
                st_write(bs.body, (bs.keyword, "/ce:compound"), " \u2014 codify learnings into project rules and skills")

        st_space("v", 2)

        with st_block(s.project.containers.callout):
            st_write(
                bs.transition,
                "But first: today you'll practice the PRINCIPLES behind CE \u2014 "
                "manually, with Cursor, on CalcApp v0.3.",
            )
