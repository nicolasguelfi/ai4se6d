"""Slide — The Perception-Reality Gap."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    stat = s.project.titles.stat
    label = s.project.titles.label
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    st_marker("Perception vs Reality Gap")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Perception-Reality Gap", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="Perception vs Reality in AI Productivity",
                entries=[
                    ("METR gap", "Developers predicted +24% speed gain but were actually 19% slower — a 43-point perception error."),
                    ("Expert predictions", "Both economists and ML specialists predicted ~38-39% improvement — equally wrong."),
                    ("SO confidence drop", "Stack Overflow developer confidence in AI accuracy fell from 40% to 29% in one year."),
                    ("GSE-One link", "Systematic overestimation means process guardrails and measurement are essential, not optional."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(100):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        "METR developers estimated ",
                        (bs.stat, "+20% faster"),
                        " \u2192 actual ",
                        (s.bold + s.project.colors.critical, "\u221219% slower"),
                    )
                with l.item():
                    st_write(
                        bs.body,
                        "Economists predicted ",
                        (bs.stat, "39% improvement"),
                        " \u2192 wrong",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        "ML specialists predicted ",
                        (bs.stat, "38% improvement"),
                        " \u2192 wrong",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        "Stack Overflow accuracy confidence: fell from ",
                        (bs.label, "40%"), " to ", (bs.stat, "29%"),
                        " (2024\u21922025)",
                    )

            st_space("v", 2)
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    "We systematically overestimate AI\u2019s current impact on productivity.",
                )

            st_space("v", 1)
            st_write(bs.source, cite("metr2025"), ", ", cite("stackoverflow-survey2026"))
