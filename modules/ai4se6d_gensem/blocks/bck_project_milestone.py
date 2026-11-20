"""Slide — Day 5 milestone: what the trainer checks in plan and requirements (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Milestone styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    lesson = Style.create(s.project.titles.body + s.bold + s.center_txt, "milestone_lesson")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "milestone_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Milestone: Plan and Requirements", tag=t.div, toc_lvl="+1", label="Day 5 milestone")
            st_write(bs.body, "What the trainer checks, in two minutes:", tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.body, "The plan holds in 8 to 10 points; each task traces to a requirement")
                with l.item(): st_write(bs.body, "2 to 5 requirements, each with Given / When / Then")
                with l.item(): st_write(bs.body, "At least one measurable non-functional requirement")
                with l.item(): st_write(bs.body, "What is out of scope sits in the backlog")
            with st_block(s.project.containers.callout):
                st_write(bs.lesson, "Delivered by 11:30 tomorrow? If not, cut now.", tag=t.div)
            st_write(bs.foot, "From 15:15 to 16:30, one by one: keep working until your turn.", tag=t.div)
