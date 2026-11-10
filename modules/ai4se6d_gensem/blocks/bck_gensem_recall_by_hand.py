"""Slide — Recall of days 1-2: what you did by hand, and what it cost (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Recall styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    body = s.project.titles.body
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "recall_hand_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Days 1-2, by Hand", tag=t.div, toc_lvl="+1", label="Recall of days 1-2")
            with st_grid(cols="repeat(auto-fit, minmax(420px, 1fr))", gap="32px") as g:
                with g.cell():
                    st_write(bs.label, "What you did", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, "Vibe coded FreeSelfApp")
                        with l.item(): st_write(bs.body, "Wrote a plan of small, testable tasks")
                        with l.item(): st_write(bs.body, "Tests first, one branch per task")
                        with l.item(): st_write(bs.body, "Reviewed the diff, triaged, refused")
                        with l.item(): st_write(bs.body, "Shipped CalcApp v0.1")
                with g.cell():
                    st_write(bs.label, "What it cost", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, "Re-explaining the project to the agent")
                        with l.item(): st_write(bs.body, "Keeping the plan up to date yourself")
                        with l.item(): st_write(bs.body, "Remembering every check, every time")
                        with l.item(): st_write(bs.body, "No trace of your decisions")
            st_write(bs.foot, "Today: why a method helps — then a method that carries this discipline for you.", tag=t.div)
