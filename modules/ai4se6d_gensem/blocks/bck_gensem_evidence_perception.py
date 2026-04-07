"""Slide — The Perception-Reality Gap."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    stat = s.project.titles.stat
    label = s.project.titles.label
    source = s.project.titles.caption + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Perception-Reality Gap", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    "METR developers estimated ",
                    (bs.stat, "+20% faster"),
                    " \u2192 actual ",
                    (s.bold + s.project.colors.critical, "\u221219% slower"),
                )
            with l.item():
                st_write(
                    bs.body,
                    "Economists predicted ",
                    (bs.stat, "39% improvement"),
                    " \u2192 wrong",
                )
            with l.item():
                st_write(
                    bs.body,
                    "ML specialists predicted ",
                    (bs.stat, "38% improvement"),
                    " \u2192 wrong",
                )
            with l.item():
                st_write(
                    bs.body,
                    "Stack Overflow accuracy confidence: fell from ",
                    (bs.label, "40%"), " to ", (bs.stat, "29%"),
                    " (2024\u21922025)",
                )

        st_space("v", 2)
        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "We systematically overestimate AI\u2019s current impact on productivity.",
            )

        st_space("v", 1)
        st_write(bs.source, cite("metr2025"), ", ", cite("stackoverflow-survey2025"))
