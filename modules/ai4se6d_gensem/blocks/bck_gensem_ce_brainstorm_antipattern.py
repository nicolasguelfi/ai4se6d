"""Slide — Anti-pattern: Jumping to Code."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Brainstorm anti-pattern slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    label = s.project.titles.label
    dont_callout = Style.create(
        Style("background-color: rgba(231, 76, 60, 0.12);", "_dont_bg")
        + Style("border: 0 solid; border-left: 4px solid #E74C3C; border-radius: 0;", "_dont_brd")
        + Style("padding: 12px 16px;", "_dont_pad"),
        "gs_dont_callout",
    )
    do_callout = Style.create(
        Style("background-color: rgba(46, 196, 182, 0.12);", "_do_bg")
        + Style("border: 0 solid; border-left: 4px solid #2EC4B6; border-radius: 0;", "_do_brd")
        + Style("padding: 12px 16px;", "_do_pad"),
        "gs_do_callout",
    )

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Anti-pattern: Jumping to Code", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(bs.dont_callout):
            st_write(bs.body, (bs.stat, "DON'T: "), '"Add budget alerts to the app"')
            st_space("v", 0.3)
            st_write(
                bs.body,
                "\u2192 AI generates 500 lines, wrong architecture, missing edge cases, ",
                (bs.stat, "2 hours debugging"),
                ".",
            )

        st_space("v", 1)

        with st_block(bs.do_callout):
            st_write(bs.body, (bs.keyword, "DO: "), '"/ce:brainstorm budget alerts"')
            st_space("v", 0.3)
            st_write(
                bs.body,
                "\u2192 5 min conversation, clarified requirements, ",
                (bs.keyword, "3 architecture options"),
                ", risks surfaced. ",
                (bs.label, "THEN"),
                " code.",
            )
