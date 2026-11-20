"""Slide — The 3-question grid of the gallery visitors (exercise E24, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Visitor grid styles."""
    heading = s.project.titles.heading
    question = Style.create(s.project.titles.body + s.bold, "visitor_grid_question")
    rule = Style.create(s.project.titles.body_accent + s.center_txt, "visitor_grid_rule")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "visitor_grid_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(72):
            st_write(bs.heading, "Visitors: 3 Questions", tag=t.div, toc_lvl="+1", label="Visitor grid")
            with st_block(s.project.containers.callout):
                with st_list(l_style=bs.question, li_style=bs.question, list_type=lt.ordered) as l:
                    with l.item(): st_write(bs.question, "Does it solve the problem announced? Try it yourself.")
                    with l.item(): st_write(bs.question, "Can they show one requirement and the test that checks it?")
                    with l.item(): st_write(bs.question, "Which limit or risk would you point out?")
            st_write(bs.rule, "One line of notes per project you visit.", tag=t.div)
            st_write(bs.foot, "Kind and precise: the same grid will be used on your project.", tag=t.div)
