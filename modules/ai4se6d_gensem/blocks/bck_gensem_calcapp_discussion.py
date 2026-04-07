"""Slide — Before You Start: Discussion prompt."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Discussion prompt slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Before You Start", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "Looking at ",
                (bs.keyword, "FR-001"),
                " and ",
                (bs.keyword, "NFR-002"),
                ": how would you prompt Cursor to implement these? "
                "What context would you load? What constraints would you set?",
            )

        st_space("v", 1)

        st_write(
            bs.closing,
            "Take 2 minutes to think, then Tiago will guide the practice.",
        )
