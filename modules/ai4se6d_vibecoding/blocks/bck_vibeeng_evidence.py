"""Slide 29 — The Evidence: FlowGen experiment stat-hero."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Evidence slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    body = s.project.titles.body + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Evidence", tag=t.div, toc_lvl="1")
            st_space("v", 1)
            with st_zoom(80):
                st_write(bs.stat, "15%")
            st_space("v", 1)
            with st_zoom(130):
                st_write(
                    bs.body,
                    "fewer code smells when incorporating design and code review activities",
                )
                st_write(bs.body, "FlowGen experiment — structured processes beat ad-hoc coding")
                # REF: https://arxiv.org/abs/2403.15852
                st_write(bs.source, cite("soen101-2024"))
