"""Slide — Testing in the GenAI Era (Wang et al.)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Testing slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    stat_hero = Style.create(
        s.project.colors.highlight + s.bold + s.Huge + s.center_txt,
        "gs_test_hero",
    )
    hero_label = s.project.titles.body + s.center_txt
    source = s.project.titles.source

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Testing in the GenAI Era", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(s.center_txt):
            st_write(bs.stat_hero, "102", tag=t.div)
            st_write(bs.hero_label, "studies surveyed")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    "LLM-refactored code is ",
                    (bs.stat, "\"not always reliable\""),
                    " (Haque)",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "FlowGen"),
                    ": structured SE processes improve quality \u2014 design + code review = ",
                    (bs.stat, "15%"),
                    " reduction in code smells",
                )

        st_space("v", 2)
        st_write(bs.source, cite("wang-llm-testing2025"))
        st_write(bs.source, cite("soen101-2024"))
