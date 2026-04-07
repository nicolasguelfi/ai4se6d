"""Slide — Section title: The Implementation Layer: Multi-Agent Systems."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Multi-agent section title styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.heading, "The Implementation Layer: Multi-Agent Systems", tag=t.div, toc_lvl="1")
        st_space("v", 2)
        st_write(bs.body, "4 architectural categories, each with different trade-offs.")
