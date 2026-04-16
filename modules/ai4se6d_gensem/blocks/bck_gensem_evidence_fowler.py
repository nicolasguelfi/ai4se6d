"""Slide — Fowler's Warning on replacing developers."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.project.titles.keyword
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "Fowler\u2019s Warning", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "\u201cCurrent enthusiasm for replacing developers with AI "
                "fundamentally misunderstands what makes software development "
                "valuable.\u201d",
            )

        st_space("v", 2)
        st_write(
            bs.body,
            "Coding assistants are ", (bs.keyword, "NOT"),
            " replacing pair programming.",
        )
        st_space("v", 1)
        st_write(
            bs.body,
            "Writing code \u2260 building software.",
        )
