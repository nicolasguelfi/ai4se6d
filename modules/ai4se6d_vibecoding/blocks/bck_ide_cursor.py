"""Slide 33 — Cursor: AI-native IDE deep dive."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Cursor slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.titles.caption
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A cursor arrow icon in amber centered inside a fully-featured IDE window "
    "in electric blue radiating interaction lines. "
    f"{_SUFFIX}"
)

def build():
    # Slide 1 — Cursor overview
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Cursor", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ide_cursor",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "AI-native IDE"), " \u2014 built from the ground up for AI")
                        # REF: cursor-ainative2025
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "$29.3B valuation"), " \u2014 fastest-growing dev tool")
                        # REF: cursor-ainative2025
                        with l.item():
                            st_write(bs.body, (bs.keyword, "1M+ DAU"), " \u2014 daily active users")
                        # REF: cursor-ainative2025
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "8 parallel agents"), " for concurrent tasks")
                        with l.item():
                            st_write(bs.body, "Modes: ", (bs.keyword_accent, "Tab"), " / ", (bs.keyword_accent, "Chat"), " / ", (bs.keyword_accent, "Agent"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Plugin Marketplace"), " \u2014 extensible ecosystem")

            st_write(bs.source, cite("cursor-ainative2025"))

    st_slide_break()

    # Slide 2 — Cursor Agent Architecture
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.subheading, "Cursor Agent Architecture", tag=t.div, toc_lvl="2")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Agent Mode"), " \u2014 autonomous planning, file edits, terminal commands")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Rules cascade"), " \u2014 project rules (.cursorrules) + user rules + auto-attached context")
                # REF: cursor-ainative2025
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "8 background agents"), " \u2014 run tasks in parallel while you keep working")
                with l.item():
                    st_write(bs.body, (bs.keyword, "MCP integration"), " \u2014 connect external tools and data sources")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Pricing (Q1 2026)"), " \u2014 $20/month Pro, $40/month Business (SAML/SSO)")

            st_write(bs.source, cite("cursor-ainative2025"))
