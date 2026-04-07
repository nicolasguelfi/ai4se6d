"""Slide — Requirements Engineering Transformed (Cheng et al.)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """RE slide styles."""
    heading = Style.create(
        s.project.colors.primary + s.bold + s.huge + s.center_txt,
        "gs_re_heading",
    )
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    source = s.project.citation + s.large + s.center_txt

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Requirements Engineering Transformed", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    "GPT models dominate: ",
                    (bs.stat, "67.3%"),
                    " of studies",
                )
            with l.item():
                st_write(
                    bs.body,
                    "Focus on analysis ",
                    (bs.stat, "(30%)"),
                    " and elicitation ",
                    (bs.stat, "(22.1%)"),
                    "; management underexplored ",
                    (bs.keyword, "(6.8%)"),
                )
            with l.item():
                st_write(
                    bs.body,
                    "Core challenge triad: reproducibility ",
                    (bs.stat, "(66.8%)"),
                    ", hallucinations ",
                    (bs.stat, "(63.4%)"),
                    ", interpretability ",
                    (bs.stat, "(57.1%)"),
                )

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "Maturity gap: ",
                (bs.stat, "over 90%"),
                " of studies remain early-stage.",
            )

        st_space("v", 1)
        st_write(bs.source, "238 articles analyzed \u2014 ", cite("cheng-genai-re2025"))
