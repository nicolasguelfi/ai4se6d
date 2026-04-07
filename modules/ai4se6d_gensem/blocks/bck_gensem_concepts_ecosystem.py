"""Slide — Layer 4: Ecosystem (C15)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Ecosystem layer styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    takeaway = s.project.titles.body_accent + s.center_txt

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Layer 4: Ecosystem (C15)", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "Plugins & Marketplaces"),
                    " \u2014 shareable extensions, community-driven growth",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "Cross-tool Portability"),
                    " \u2014 rules and skills that work across IDEs",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "AGENTS.md"),
                    " (Linux Foundation) \u2014 tool-agnostic project rules standard",
                )

        st_space("v", 2)
        st_write(
            bs.takeaway,
            "A plugin ecosystem = methodology distribution channel.",
        )
