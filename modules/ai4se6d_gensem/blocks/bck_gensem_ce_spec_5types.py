"""Slide — 5 Types of CE Specialization."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """CE specialization types slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "5 Types of CE Specialization", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Redefine phases"),
                    " (e.g., threat-model \u2192 design \u2192 implement \u2192 pentest \u2192 harden)",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Add or remove phases"),
                    ' (e.g., add "ethical review" phase)',
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Redefine artifacts"),
                    " (exact structure, content, format per phase)",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Strengthen quality gates"),
                    " (domain-specific verification criteria)",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Encode domain knowledge"),
                    " (medical, financial, safety-critical rules)",
                )

        st_space("v", 2)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "Not a fork \u2014 builds on CE infrastructure.",
            )
