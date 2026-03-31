"""Slide — Today's Objectives: two-part session framing."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_intro_objective",
)


class BlockStyles:
    """Slide: Today's Objectives — maximize-viewport archetype: bullet list."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Today's Objectives", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Part 1 (45 min)"),
                        (bs.body, " — Understand what Generative AI is and how LLMs work"),
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Part 2 (45 min)"),
                        (bs.body, " — Discover VibeCoding and the VibeEngineering discipline"),
                    )
