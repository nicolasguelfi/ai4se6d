"""Slide — Section title: The Human Factor in Generative SE."""
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
            st_write(bs.heading, "The Human Factor in Generative SE", tag=t.div, toc_lvl="1")
