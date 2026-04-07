"""Slide — Anti-pattern: The Vague Plan."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Plan anti-pattern slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    closing = s.project.titles.body + s.project.colors.highlight + s.bold
    dont_callout = Style.create(
        Style("background-color: rgba(231, 76, 60, 0.12);", "_pap_dont_bg")
        + Style("border: 0 solid; border-left: 4px solid #E74C3C; border-radius: 0;", "_pap_dont_brd")
        + Style("padding: 12px 16px;", "_pap_dont_pad"),
        "gs_plan_dont_callout",
    )
    do_callout = Style.create(
        Style("background-color: rgba(46, 196, 182, 0.12);", "_pap_do_bg")
        + Style("border: 0 solid; border-left: 4px solid #2EC4B6; border-radius: 0;", "_pap_do_brd")
        + Style("padding: 12px 16px;", "_pap_do_pad"),
        "gs_plan_do_callout",
    )

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Anti-pattern: The Vague Plan", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(bs.dont_callout):
            st_write(
                bs.body,
                (bs.stat, "DON'T: "),
                '"Make it work, fix the bugs, add tests"',
            )
            st_space("v", 0.3)
            st_write(
                bs.body,
                "\u2192 No file specs, no dependencies, no verification strategy. ",
                (bs.stat, "The AI will wander."),
            )

        st_space("v", 1)

        with st_block(bs.do_callout):
            st_write(
                bs.body,
                (bs.keyword, "DO: "),
                "Explicit task decomposition, file-level changes, interface contracts.",
            )

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "The plan is a CONTRACT that constrains the AI agent.",
            )
