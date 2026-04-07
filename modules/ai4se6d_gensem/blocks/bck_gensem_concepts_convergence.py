"""Slide — Universal Convergence across AI coding tools."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Convergence slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    label = s.project.titles.label

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Universal Convergence", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    "All tools converge on the ",
                    (bs.keyword, "agentic triad"),
                    ": completion + chat + agent",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "Context engineering"),
                    " is the primary differentiator between tools",
                )
            with l.item():
                st_write(
                    bs.body,
                    "Only ",
                    (bs.stat, "Cursor, Claude Code, and Copilot"),
                    " have full hooks support",
                )
            with l.item():
                st_write(
                    bs.body,
                    "No single tool covers all ",
                    (bs.stat, "15 tasks + 15 concepts"),
                )

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "The methodology must be ",
                (bs.keyword, "tool-transcendent"),
                " \u2014 it expresses itself through whichever tool you use.",
            )
