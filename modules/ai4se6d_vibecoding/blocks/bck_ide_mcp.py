"""Slide 37 — Model Context Protocol: the open standard."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

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

# Text cell: vertically centred, left-aligned (NG, 2026-11-23)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ide_mcp_text_cell")

_NOTES = [
    ("The message",
     "MCP (Model Context Protocol) is an open protocol to plug tools and data into any agent: write a server once, "
     "every agent can use it."),
    ("The idea explained",
     "A public registry lists thousands of servers (browser, databases, issue trackers…). All five agents of the "
     "previous table speak MCP."),
    ("The trap",
     "Trust: a local MCP server runs code on your machine. Install it like a dependency — known source, read its "
     "permissions."),
    ("The image",
     "Your certified suppliers: vetted, traceable, always available — the kitchen does not buy from anyone."),
    ("Link to the course",
     "In opencode, MCP servers are declared in opencode.json (see the configuration slide)."),
    ("Ask the room",
     "« Which tool of your daily work would you like your agent to reach through MCP? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(85):
                st_write(bs.heading, "Model Context Protocol", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Model Context Protocol", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(
            cols="1.5fr 3.5fr",
            gap="3vw",
            cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
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

            with g.cell(), st_zoom(100):
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered,
                             text_align="left", item_gap=0.6) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Open protocol"), " \u2014 plug tools and data into any agent")
                    # REF: mcp-registry2025
                    with l.item():
                        st_write(bs.body, (bs.keyword_warn, "Thousands of servers"), " \u2014 public registry")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Universal"), " \u2014 all five agents")
                    with l.item():
                        st_write(bs.body, (bs.keyword_warn, "Trust"), " \u2014 a local server runs code on your machine")

                st_space("v", "2vh")
                st_write(
                    bs.emphasis,
                    "Your certified suppliers \u2014 vetted, traceable, always available.",
                )

        st_write(bs.source + s.center_txt, cite("mcp-registry2025"))
