"""Slide — Try It: Your First CE Command."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Plugin exercise slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Try It: Your First CE Command", tag=t.div, toc_lvl="1")
        st_space("v", 0.5)

        st_write(
            bs.body,
            (bs.stat, "Micro-exercise (5 min)"),
        )
        st_space("v", 0.5)

        st_write(
            bs.body,
            "Open your terminal. Run: ",
            (bs.keyword, "/ce:brainstorm [describe a feature for your mini-project]"),
        )

        st_space("v", 0.5)

        st_write(
            bs.body,
            "Observe: How does the AI structure the brainstorm? "
            "What questions does it ask? What risks does it surface?",
        )

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "Compare with a neighbor: did you get the same structure?",
            )
