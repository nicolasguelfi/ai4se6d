"""Slide 11 — What GenAI Cannot Do: five limitations with amber keywords."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


# Viewport-filling container: space-between distribution
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_limitations",
)


class BlockStyles:
    """Slide: Limitations — maximize-viewport archetype: bullet list with warning keywords."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.highlight


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "What GenAI Cannot Do", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "Guarantee truth"), " — hallucinations are real")
                with l.item(): st_write(bs.body, (bs.keyword, "Replace judgment"), " — no domain expertise")
                with l.item(): st_write(bs.body, (bs.keyword, "Access real-time data"), " — training cutoff date")
                with l.item(): st_write(bs.body, (bs.keyword, "Understand deeply"), " — pattern matching, not comprehension")
                with l.item(): st_write(bs.body, (bs.keyword, "Be deterministic"), " — same prompt, different outputs")
