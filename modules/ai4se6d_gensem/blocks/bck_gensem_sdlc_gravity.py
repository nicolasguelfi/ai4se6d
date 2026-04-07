"""Slide — The Shifting Center of Gravity: 5 tasks that define GenSE."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """SDLC gravity slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    label = s.project.titles.label
    takeaway = s.project.titles.body_accent + s.center_txt

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "The Shifting Center of Gravity", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "T1 Intent Specification"),
                    " \u2014 was implicit, now ",
                    (bs.stat, "primary skill"),
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "T2 Context Engineering"),
                    " \u2014 did not exist, now ",
                    (bs.stat, "critical"),
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "T5 Code Review & Validation"),
                    " \u2014 was periodic, now ",
                    (bs.stat, "continuous"),
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "T13 Agent Supervision"),
                    " \u2014 ",
                    (bs.keyword, "entirely new"),
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "T14 Knowledge Curation"),
                    " \u2014 project rules, memory \u2014 ",
                    (bs.keyword, "entirely new"),
                )

        st_space("v", 2)
        st_write(
            bs.takeaway,
            "Direct code writing recedes. You become an orchestrator.",
        )
