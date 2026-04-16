"""Slide — Plugin architecture: directory structure and components."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Plugin architecture slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
bs = BlockStyles

def build():
    st_marker("Plugin Architecture")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                with st_zoom(90):
                    st_write(bs.heading, "Plugin Architecture", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="GSE-One Plugin Architecture",
                    entries=[
                        ("What it is", "A directory-based plugin system that organizes skills, rules, hooks, and MCP integrations for AI-assisted development."),
                        ("Tool-agnostic", "The .gse/ directory structure works with both Cursor and Claude Code -- install once, use everywhere."),
                        ("Composable", "Each component (skills, rules, hooks, MCP) can be customized independently per project."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )
        st_space("v", 1)

        with st_zoom(120):
            with st_grid(
                cols=s.project.containers.responsive_2col,
                gap="32px",
            ) as g:
                with g.cell():
                    st_write(bs.label, "Directory Structure", tag=t.div)
                    st_code(
                        s.none,
                        code=(
                            ".gse/\n"
                            "\u251c\u2500\u2500 skills/          # Reusable prompt workflows\n"
                            "\u251c\u2500\u2500 rules/           # Project-specific constraints\n"
                            "\u251c\u2500\u2500 hooks/           # Lifecycle event handlers\n"
                            "\u2514\u2500\u2500 mcp/             # Model Context Protocol servers"
                        ),
                        language="text",
                    )
                    st_space("v", 1)
                    st_write(bs.label, "Four Core Components", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Skills"), " \u2014 parameterized prompt chains (brainstorm, plan, work, review, compound)")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Rules"), " \u2014 declarative constraints that guide every AI response")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Hooks"), " \u2014 17 lifecycle events (pre-commit, post-review, on-error, etc.)")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "MCP Integration"), " \u2014 connect external tools, databases, and services")

                with g.cell():
                    st_write(bs.label, "Installation", tag=t.div)
                    st_code(
                        s.none,
                        code=(
                            "# For Cursor\n"
                            "gse install --target cursor\n\n"
                            "# For Claude Code\n"
                            "gse install --target claude-code"
                        ),
                        language="bash",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "The plugin scaffolds the ",
                        (bs.keyword, ".gse/"),
                        " directory with sensible defaults. "
                        "Each component can be customized per project.",
                    )
