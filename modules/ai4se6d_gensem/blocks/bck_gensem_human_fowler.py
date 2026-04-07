"""Slide — Fowler's Warning: writing code != building software."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Fowler warning styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    quote_text = Style.create(
        s.project.titles.body + s.project.colors.highlight + s.italic,
        "gs_fowler_quote",
    )

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Fowler\u2019s Warning", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.quote_text,
                "\"Current enthusiasm for replacing developers with AI "
                "fundamentally misunderstands what makes software "
                "development valuable.\"",
            )

        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    "Distinction: ",
                    (bs.stat, "writing code"),
                    " \u2260 ",
                    (bs.stat, "building software"),
                )
            with l.item():
                st_write(
                    bs.body,
                    "Coding assistants are ",
                    (bs.keyword, "NOT replacing pair programming"),
                )
            with l.item():
                st_write(
                    bs.body,
                    "Booch: \"",
                    (bs.keyword, "third golden age"),
                    "\" \u2014 deep SE foundations become MORE important as the field accelerates",
                )
