"""Slide — The Trust Crisis: developer confidence in AI is falling."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Trust Crisis stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = Style.create(
        s.GIANT + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_danger_trust_stat",
    )
    sub_stat = Style.create(
        s.Large + s.project.colors.muted + s.center_txt,
        "vc_danger_trust_sub",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large + s.center_txt
    closing = Style.create(
        s.Large + s.bold + s.center_txt + s.project.colors.accent,
        "vc_danger_trust_closing",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Trust Crisis", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            st_write(bs.stat, "29%")
            st_write(
                bs.sub_stat,
                "of developers trust AI output accuracy (2025)",
            )
            st_write(
                bs.sub_stat,
                "down from 43% in 2024",
            )
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword_warn, "46%"),
                        " actively ",
                        (bs.keyword_warn, "distrust"),
                        " AI-generated code",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "45%"),
                        " top frustration: ",
                        "\u201calmost right, but not quite\u201d",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword_warn, "66%"),
                        " spend ",
                        (bs.keyword_warn, "more time fixing"),
                        " AI code than writing it themselves",
                    )

            st_space("v", 1)
            # REF: Stack Overflow Developer Survey 2025
            st_write(bs.source, cite("stackoverflow-survey2026"))
            st_space("v", 1)
            st_write(
                bs.closing,
                "Adoption is rising. Trust is falling. This is unsustainable.",
            )
