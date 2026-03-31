"""Slide — Reality check: stats and bridge to VibeEngineering."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_vc_reality",
)

# Billboard centered
_page_fill_center = ns(
    "display:flex;flex-direction:column;justify-content:center;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_vc_reality_center",
)


class BlockStyles:
    """VibeCoding reality check slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    stat = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "vc_reality_stat",
    )
    source = s.project.titles.caption
    transition = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.accent,
        "vc_reality_transition",
    )
bs = BlockStyles


def build():
    # Sub-slide 1: Stats
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Reality Check", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Anthropic finding: "), (bs.stat, "60%"), " integrable, ", (bs.stat, "0\u201320%"), " fully delegable")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Bain: "), (bs.stat, "10%"), " gains without process change vs ", (bs.stat, "25\u201330%"), " with end-to-end redesign")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Impact varies: "), "juniors ", (bs.stat, "+27\u201339%"), ", seniors ", (bs.stat, "+8\u201313%"), " (or slower)")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Naive VibeCoding has its place"), " \u2014 prototypes, demos, learning")
                with l.item():
                    st_write(bs.body, (bs.stat, "NOT"), " production systems")

    st_slide_break()

    # Sub-slide 2: Bridge question
    with st_block(_page_fill_center):
        st_write(
            bs.transition,
            "Speed AND Quality?",
            tag=t.div,
        )
