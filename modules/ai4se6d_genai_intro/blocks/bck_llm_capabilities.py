"""Slide 10 — What GenAI Can Do: five capabilities with accent keywords."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


# Viewport-filling container: space-between distribution
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:top;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_capabilities",
)


class BlockStyles:
    """Slide: Capabilities — maximize-viewport archetype: bullet list with accent keywords."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "What GenAI Can Do", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "Generate code"), " — from natural language descriptions")
                with l.item(): st_write(bs.body, (bs.keyword, "Write & summarize"), " — documents, emails, reports")
                with l.item(): st_write(bs.body, (bs.keyword, "Analyze data"), " — patterns, trends, anomalies")
                with l.item(): st_write(bs.body, (bs.keyword, "Create images"), " — from text prompts (DALL-E, Midjourney)")
                with l.item(): st_write(bs.body, (bs.keyword, "Reason & plan"), " — multi-step problem solving")
