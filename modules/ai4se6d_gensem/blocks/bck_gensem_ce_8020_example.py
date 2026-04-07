"""Slide — The 80/20 Rule: From Your Experience."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """80/20 rule slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "The 80/20 Rule \u2014 From Your Experience", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                (bs.stat, "Day 1 FreeSelfApp: "),
                "you spent ~90% coding, ~10% planning. Result? ",
                (bs.keyword, "Tech debt"),
                ", missing features, broken tests, ",
                (bs.stat, "1h45 of chaos"),
                ".",
            )

        st_space("v", 0.5)

        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                (bs.keyword, "CE inverts this: "),
                "~80% planning and review, ~20% execution. ",
                "The AI handles the 20% in ",
                (bs.stat, "minutes"),
                ".",
            )

        st_space("v", 0.5)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "Your job shifts from WRITING code to DIRECTING the AI with precision.",
            )
