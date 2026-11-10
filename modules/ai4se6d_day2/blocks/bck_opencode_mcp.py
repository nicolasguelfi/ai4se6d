"""Slide — MCP: plug tools into the agent."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """MCP styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    node = Style.create(s.project.titles.table_label + s.center_txt, "mcp_node")
    arrow = Style.create(s.project.titles.subtitle + s.center_txt, "mcp_arrow")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "MCP — Tools for the Agent", tag=t.div, toc_lvl="+1")
        st_space("v", 0.5)
        with st_grid(cols="1fr auto 1fr auto 1.4fr", gap="12px", cell_styles=s.project.containers.grid_cell_centered) as g:
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
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item(): st_write(bs.body, (bs.keyword, "Model Context Protocol"), ": an open standard")
            with l.item(): st_write(bs.body, "Each server exposes ", (bs.keyword, "tools"), " the agent calls when it needs them")
            with l.item(): st_write(bs.body, "Declared under ", (bs.keyword, "mcp"), " in opencode.json")
            with l.item(): st_write(bs.body, "Every tool takes context space: ", (bs.keyword, "enable few"))
