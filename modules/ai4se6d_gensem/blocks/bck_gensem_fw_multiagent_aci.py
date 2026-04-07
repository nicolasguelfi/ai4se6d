"""Slide — Category 3: Agent-Computer Interface (SWE-bench, OpenHands, SWE-agent, Devin)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """ACI category styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat
    source = s.project.titles.source
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Category 3: Agent-Computer Interface (ACI)", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "SWE-bench"), ": ",
                    (bs.stat, "2,294 problems"),
                    " across 12 Python repos. ",
                    (bs.keyword, "THE standard benchmark"),
                    " for evaluating autonomous coding agents.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "OpenHands"), " (ICLR 2025, ", (bs.stat, "64K\u2605"), "): "
                    "Most comprehensive open-source ACI. ",
                    (bs.keyword, "Sandboxed, model-agnostic"),
                    ". Supports multiple agent architectures.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "SWE-agent"), ": ",
                    (bs.stat, "12.5%"), " at publication \u2192 ",
                    (bs.stat, "20\u201355%"), " on SWE-bench Verified (March 2026). "
                    "Rapid improvement trajectory demonstrates ",
                    (bs.keyword, "ACI maturation"),
                    ".",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "Devin"), ": Fully autonomous agent. ",
                    (bs.keyword, "Limited independent validation"),
                    " \u2014 commercial claims exceed published evidence.",
                )

        st_space("v", 1)
        st_write(bs.source, cite("yang-openhands2025"))
