"""Slide — Day 5: Where We Left Off."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Day 5 bridge slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    transition = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_day5_transition",
    )

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Day 5: Where We Left Off", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "SOTA: "),
                    (bs.stat, "15 tasks"),
                    ", ",
                    (bs.stat, "15 concepts"),
                    ", evidence shows methodology = the multiplier",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "CE: "),
                    "5-phase workflow (brainstorm \u2192 plan \u2192 work \u2192 review \u2192 compound), ",
                    (bs.stat, "80/20 rule"),
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "CalcApp v0.3: "),
                    "requirements-driven development with traceability",
                )

        st_space("v", 2)

        st_write(
            bs.transition,
            "Today: GenSEMOne \u2014 your lightweight method for the professional mini-project.",
        )
