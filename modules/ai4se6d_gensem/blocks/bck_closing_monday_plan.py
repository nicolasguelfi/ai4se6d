"""Slide — Your Monday-morning plan: one concrete change at work (exercise E25, edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Monday plan styles."""
    heading = s.project.titles.heading
    template = Style.create(s.project.titles.body + s.bold + s.center_txt, "monday_template")
    body = s.project.titles.body
    label = s.project.titles.label
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "monday_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "Your Monday-Morning Plan", tag=t.div, toc_lvl="+1", label="Monday-morning plan")
            with st_block(s.project.containers.callout):
                st_write(bs.template, "On <day>, I will <one concrete action> on <project or team>. "
                         "First step: <…>. I will know it worked when <something I can see>.", tag=t.div)
            st_write(bs.label, "For example", tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "a written plan before asking an agent for code")
                with l.item(): st_write(bs.body, "one branch per task, tests first")
                with l.item(): st_write(bs.body, "the 3-question grid before merging an AI suggestion")
                with l.item(): st_write(bs.body, "a README that states its limits")
            st_write(bs.foot, "One action, small enough to start on Monday.", tag=t.div)
