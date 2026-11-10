"""Slide — The 3-question grid to apply at every Gate (decision P13, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Gate grid styles."""
    heading = s.project.titles.heading
    question = Style.create(s.project.titles.body + s.bold, "gate_grid_question")
    body = s.project.titles.body
    rule = Style.create(s.project.titles.body_accent + s.center_txt, "gate_grid_rule")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "gate_grid_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "At Every Gate: 3 Questions", tag=t.div, toc_lvl="+1", label="The Gate grid")
            with st_block(s.project.containers.callout):
                with st_list(l_style=bs.question, li_style=bs.question, list_type=lt.ordered) as l:
                    with l.item(): st_write(bs.question, "Do I understand what is proposed?")
                    with l.item(): st_write(bs.question, "What do I lose if it is wrong?")
                    with l.item(): st_write(bs.question, "Would I have chosen differently?")
            st_write(bs.rule, "At least one change or one refusal per activity — written in the tracking sheet.", tag=t.div)
            st_write(bs.foot, "\"Looks good\" is not a review. A Gate you always accept is not a Gate.", tag=t.div)
