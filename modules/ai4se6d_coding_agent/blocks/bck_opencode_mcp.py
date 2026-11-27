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
     "1. At start, opencode connects to each enabled MCP server and asks for its tools (name, description, "
     "parameters). 2. With every request to the model, opencode sends that list along with the conversation and "
     "its own tools (read, edit, shell). 3. The model chooses: instead of text it answers with a tool call (which "
     "tool, which parameters). 4. opencode checks the permissions (asks you if the setting says so), then sends "
     "the call to the MCP server. 5. opencode returns the result to the model, which goes on: another call or the "
     "final answer. opencode never picks a tool itself: it controls what is offered (enabled servers, denied "
     "tools) and what may run (permissions)."),
    # Built-in tools vs MCP (NG « ok », 2026-11-27)
    ("git, gh and files: no MCP",
     "git, gh and files need no MCP: the agent runs them through its built-in bash and file tools. MCP adds what "
     "it lacks: live docs, a browser, a database."),
    ("How to add one",
     "opencode mcp add writes the server under mcp.servers in opencode.json — no hand-written JSON."),
    ("The trap",
     "Enabling every server available: every tool description is sent with every request, used or not — context "
     "space and cost. Enable few."),
    ("What comes next",
     "Context7, one MCP server that brings live library docs into the context."),
    ("Ask the room",
     "« Which tool would you plug in first for your own project? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — opencode mcp add",
     "Typed in the terminal (not in opencode): registers an MCP server, e.g. opencode mcp add context7 --url "
     "https://mcp.context7.com/mcp (name, then its address). Saved in the project's opencode.json; --global for "
     "every project. opencode mcp list shows the servers and whether they are ready."),
    ("Key — mcp.servers",
     "Dot notation: the key servers inside the key mcp of opencode.json. Each server sits under its own name "
     "there."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "MCP — Tools for the Agent", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — MCP — Tools for the Agent", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")
        # the model chooses, opencode runs; MCP is the protocol between opencode and the servers, not a box
        # (NG, 2026-11-25)
        with st_zoom(100), st_grid(cols="4% 0.6fr auto 1.25fr auto 1.75fr 4%", gap="12px",
                                    cell_styles=s.project.containers.grid_cell_centered) as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                with st_block(s.project.containers.table_header_cell):
                    st_write(bs.node, "model")
            with g.cell():
                st_write(bs.arrow, "⇄")
            with g.cell():
                with st_block(s.project.containers.table_active_cell):
                    st_write(bs.node, "opencode (MCP client)")
            with g.cell():
                st_write(bs.arrow, "⇄")
            with g.cell():
                with st_block(s.project.containers.table_normal_cell):
                    st_write(bs.node, "MCP servers: docs, DB, browser")
            with g.cell():
                pass  # right margin
        st_space("v", "4vh")

        # One row per fact, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.keyword, "Model Context Protocol"), ": an open standard"),
            ("Each server lists its ", (bs.keyword, "tools"), "; opencode sends their descriptions to the model, "
             "the ", (bs.keyword, "model chooses"), " one, opencode runs it and returns the result"),
            ("Added with ", (bs.keyword, "opencode mcp add"), ": written under ", (bs.keyword, "mcp.servers"),
             " in opencode.json"),
            ("Every tool description is sent with every request: ", (bs.keyword, "enable few")),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(96), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
