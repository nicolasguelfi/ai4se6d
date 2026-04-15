"""Slide — Where We Left Off: key takeaways from Days 1-2."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Day 1 recall styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    transition = s.project.titles.body_accent + s.center_txt

bs = BlockStyles


def build():
    st_marker("Days 1-2 Recall")
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Where We Left Off", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="Previous Sessions Recap",
            entries=[
                ("Days 1-2 covered", "VibeCoding definition, dangers (vulnerabilities, paradox), and VibeEngineering principles."),
                ("Key insight", "VibeCoding is fast but fragile -- VibeEngineering reintroduces the discipline AI-assisted dev needs."),
                ("Bridge to today", "Now we formalize these practices into a complete methodology: GSE-One."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 1)

        with st_zoom(110):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "VibeCoding"),
                        " = intent over implementation, but ",
                        (bs.stat, "12-65%"),
                        " vulnerabilities, ",
                        (bs.stat, "7h/week"),
                        " paradox",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "VibeEngineering"),
                        " = 6 principles: requirements, TDD, architecture, iteration, review, context",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Cursor mastery"),
                        ": rules, Plan/Act mode, MCP, Context7",
                    )

            st_space("v", 2)
            st_write(
                bs.transition+s.project.colors.success ,
                "Today: the METHODS that orchestrate these practices.",
            )
