"""Slide — Why requirements matter: the cost of a late fix (CCSET10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Cost of late fixes styles."""
    heading = s.project.titles.heading
    stat = s.project.titles.stat_hero
    body = Style.create(s.project.titles.body + s.center_txt, "elicitation_cost_body")
    source = s.project.citation + s.large + s.center_txt
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "elicitation_cost_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, "The Problem: Building the Wrong Thing", tag=t.div, toc_lvl="+1",
                     label="Why requirements matter")
            st_write(bs.stat, "×100", tag=t.div)
            st_write(bs.body, "Finding and fixing a severe problem after delivery is often 100 times more "
                     "expensive than during requirements and design.", tag=t.div)
            st_write(bs.source, cite("boehm-basili-top10-2001"), tag=t.div)
            st_write(bs.foot, "With an agent, code is cheap. A wrong requirement is still expensive: "
                     "the agent builds it fast, and well.", tag=t.div)
