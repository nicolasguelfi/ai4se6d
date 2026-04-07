"""Slide — The Process Discipline Insight across all 4 multi-agent paradigms."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Process discipline insight styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    callout_body = s.project.titles.body
    message = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_mains_message",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "The Process Discipline Insight", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        # Key insight callout
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_body,
                (bs.stat, "Key insight: "),
                "Across ALL 4 paradigms, ",
                (bs.keyword, "structured SE processes improve outcomes"),
                ".",
            )

        st_space("v", 1)

        # Evidence list
        st_write(bs.body, "Evidence:")
        st_space("v", 0.5)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "MetaGPT SOPs"),
                    " \u2192 reduce cascading hallucinations across agent roles",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "ChatDev dehallucination"),
                    " \u2192 cross-agent dialogue improves code quality",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "FlowGen"),
                    " \u2192 ", (bs.stat, "15% improvement"),
                    " when structured processes are enforced",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "AutoGPT unconstrained"),
                    " \u2192 reliability degradation without process guardrails",
                )

        st_space("v", 2)
        st_write(
            bs.message,
            "Commercial tools with widest adoption embed process enforcement "
            "(hooks, rules, gates).",
        )
