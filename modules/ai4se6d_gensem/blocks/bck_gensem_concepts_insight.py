"""Slide — The Process Insight: rules, skills, hooks, plugins."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Process insight styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    callout_text = Style.create(
        s.project.titles.body + s.project.colors.highlight,
        "gs_insight_callout",
    )
    coda = s.project.titles.body + s.center_txt

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center_noalign):
        with st_zoom(90):
            st_write(bs.heading, "The Process Insight", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_text,
                "A ",
                (bs.keyword, "rules file"),
                " is a process artifact.",
            )
            st_space("v", 0.5)
            st_write(
                bs.callout_text,
                "A ",
                (bs.keyword, "skill"),
                " is a reusable process fragment.",
            )
            st_space("v", 0.5)
            st_write(
                bs.callout_text,
                "A ",
                (bs.keyword, "hook"),
                " is process enforcement.",
            )
            st_space("v", 0.5)
            st_write(
                bs.callout_text,
                "A ",
                (bs.keyword, "plugin"),
                " is a methodology distribution channel.",
            )

        st_space("v", 2)
        st_write(
            bs.coda,
            "The tools are different. The need for process discipline is universal.",
        )
