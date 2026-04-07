"""Slide — SE 3.0: intent-centric, conversation-oriented development."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """SE 3.0 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    number = s.bold + s.project.colors.primary
    assessment = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_se30_assessment",
    )
    source = s.project.titles.caption + s.center_txt
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "SE 3.0", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        st_write(bs.body, "Hassan et al. propose a paradigm shift with ", (bs.keyword, "5 characteristics"), ":")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Intent-centric: "), "Developers express what, AI determines how")
            with l.item():
                st_write(bs.body, (bs.keyword, "Conversation-oriented: "), "Iterative dialogue replaces specification documents")
            with l.item():
                st_write(bs.body, (bs.keyword, "Adaptive partnership: "), "AI adapts to developer skill level and style")
            with l.item():
                st_write(bs.body, (bs.keyword, "Multi-objective: "), "Balances functionality, performance, security, maintainability")
            with l.item():
                st_write(bs.body, (bs.keyword, "SLA-aware: "), "Generated code meets service-level agreements by design")

        st_space("v", 2)
        st_write(bs.assessment, "Assessment: Most ambitious vision, but remains largely theoretical.")
        st_write(bs.source, "Hassan et al. \u2014 SE 3.0 Vision Paper, 2024")
