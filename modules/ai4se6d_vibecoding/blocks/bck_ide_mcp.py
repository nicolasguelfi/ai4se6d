"""Slide 37 — Model Context Protocol: the open standard."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """MCP slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.italic + s.project.colors.accent + s.center_txt,
        "ide_mcp_emphasis",
    )
    source = s.project.citation + s.large
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} Central hub circle in amber with six spokes to peripheral circles "
    "in electric blue and teal with different icons. "
    f"{_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Model Context Protocol", tag=t.div, toc_lvl="1")

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
                        name="ide_mcp",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Open protocol"), " \u2014 standardized tool-to-model communication")
                        # REF: mcp-registry2025
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "16,670+ servers"), " \u2014 rapidly growing ecosystem")
                        with l.item():
                            st_write(bs.body, "Domains: ", (bs.keyword_accent, "version control"), ", ", (bs.keyword_accent, "testing"), ", ", (bs.keyword_accent, "databases"), ", ", (bs.keyword_accent, "cloud"), ", ", (bs.keyword_accent, "observability"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Universal"), " \u2014 works with Cursor, Claude Code, Copilot, Windsurf")

                    st_space("v", 1)
                    st_write(
                        bs.emphasis,
                        "Your certified suppliers \u2014 vetted, traceable, always available.",
                    )

            st_write(bs.source, cite("mcp-registry2025"))
