"""Slide — Plan B: If You Fall Behind."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Fallback plan slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Plan B: If You Fall Behind", tag=t.div, toc_lvl="1")
        st_space("v", 0.5)

        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                (bs.stat, "8 FRs in 1.5 days"),
                " is ambitious. Here's your fallback plan:",
            )

        st_space("v", 0.5)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Priority 1 (MUST): "),
                    "FR-001 to FR-004 \u2014 core functionality ",
                    (bs.stat, "(2h)"),
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Priority 2 (SHOULD): "),
                    "FR-005 to FR-006 \u2014 enhanced features ",
                    (bs.stat, "(1.5h)"),
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Priority 3 (COULD): "),
                    "FR-007 to FR-008 \u2014 nice-to-have ",
                    (bs.stat, "(1h)"),
                )

        st_space("v", 0.5)

        st_write(
            bs.body,
            "If stuck on Priority 1 by end of Day 5 PM \u2192 skip Priority 3, focus on ",
            (bs.keyword, "review (Step 4)"),
            ".",
        )

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "A polished 4-FR app beats a broken 8-FR app.",
            )
