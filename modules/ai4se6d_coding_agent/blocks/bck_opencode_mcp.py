"""Slide — MCP: plug tools into the agent."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """MCP styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    node = Style.create(s.project.titles.table_label + s.center_txt, "mcp_node")
    arrow = Style.create(s.project.titles.subtitle + s.center_txt, "mcp_arrow")
bs = BlockStyles

_NOTES = [
    ("The message",
     "MCP (Model Context Protocol) is an open standard to plug tools into the agent: opencode talks to MCP "
     "servers — docs, databases, a browser."),
    ("How it works",
     "Each server exposes tools; the agent calls them when it needs them."),
    ("How to add one",
     "opencode mcp add writes the server under mcp.servers in opencode.json — no hand-written JSON."),
    ("The trap",
     "Enabling every server available. Every tool takes context space: enable few."),
    ("What comes next",
     "Context7, one MCP server that brings live library docs into the context."),
    ("Ask the room",
     "« Which tool would you plug in first for your own project? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "MCP — Tools for the Agent", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — MCP — Tools for the Agent", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(110), st_grid(cols="5% 1fr auto 1fr auto 1.4fr 5%", gap="12px",
                                    cell_styles=s.project.containers.grid_cell_centered) as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                with st_block(s.project.containers.table_active_cell):
                    st_write(bs.node, "opencode")
            with g.cell():
                st_write(bs.arrow, "⇄")
            with g.cell():
                with st_block(s.project.containers.table_header_cell):
                    st_write(bs.node, "MCP")
            with g.cell():
                st_write(bs.arrow, "⇄")
            with g.cell():
                with st_block(s.project.containers.table_normal_cell):
                    st_write(bs.node, "servers: docs, DB, browser")
            with g.cell():
                pass  # right margin
        st_space("v", "4vh")

        # One row per fact, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.keyword, "Model Context Protocol"), ": an open standard"),
            ("Each server exposes ", (bs.keyword, "tools"), " the agent calls when it needs them"),
            ("Added with ", (bs.keyword, "opencode mcp add"), ": written under ", (bs.keyword, "mcp.servers"),
             " in opencode.json"),
            ("Every tool takes context space: ", (bs.keyword, "enable few")),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(110), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
