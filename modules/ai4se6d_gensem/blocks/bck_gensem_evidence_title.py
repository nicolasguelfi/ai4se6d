"""Slide — Section title: What Does the Evidence Say?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_zoom(90):
            st_write(bs.heading, "What Does the Evidence Say?", tag=t.div, toc_lvl="1")
        st_space("v", 2)
        st_write(
            bs.body,
            "Three randomized controlled trials, five developer surveys, "
            "and one uncomfortable paradox.",
        )
