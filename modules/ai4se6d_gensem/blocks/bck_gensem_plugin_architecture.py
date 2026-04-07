"""Slide — Plugin architecture: directory structure and components."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Plugin architecture slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Plugin Architecture", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="32px",
        ) as g:
            with g.cell():
                st_write(bs.label, "Directory Structure", tag=t.div)
                st_code(
                    s.none,
                    code=(
                        ".claude-plugin/\n"
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
                        "npm install -g @every-env/compound-plugin\n"
                        "ce init"
                    ),
                    language="bash",
                )
                st_space("v", 1)
                st_write(
                    bs.body,
                    "The plugin scaffolds the ",
                    (bs.keyword, ".claude-plugin/"),
                    " directory with sensible defaults. "
                    "Each component can be customized per project.",
                )
