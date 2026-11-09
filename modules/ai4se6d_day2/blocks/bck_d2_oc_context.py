"""Slide — What fills the context window."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Context window styles."""
    heading = s.project.titles.heading
    layer = Style.create(s.project.titles.table_label + s.center_txt, "d2_ctx_layer")
    body = s.project.titles.table_cell
    keyword = s.project.titles.table_label
bs = BlockStyles

_LAYERS = [
    "Rules — AGENTS.md",
    "Your prompt",
    "Files you @mention or it reads",
    "Conversation history",
    "Tool results — commands, tests, MCP",
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "The Context Window", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(cols="repeat(auto-fit, minmax(520px, 1fr))", grid_style=s.project.containers.gap_32) as g:
            with g.cell():
                for layer in _LAYERS:
                    with st_block(s.project.containers.table_normal_cell + Style("margin-bottom:8px;", "d2_ctx_gap")):
                        st_write(bs.layer, layer)
            with g.cell():
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item(): st_write(bs.body, "All of it is sent to the model, ", (bs.keyword, "every turn"))
                    with l.item(): st_write(bs.body, "The window has a ", (bs.keyword, "fixed size"))
                    with l.item(): st_write(bs.body, "Too full: early details get lost")
                    with l.item(): st_write(bs.body, (bs.keyword, "/compact"), " summarises, ", (bs.keyword, "/new"), " starts clean")
