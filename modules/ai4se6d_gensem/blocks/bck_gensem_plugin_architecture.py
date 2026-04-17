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
                        ("What it is", "A directory-based plugin system that organizes agents, skills, rules, hooks, and MCP integrations for AI-assisted development."),
                        ("Inventory", "23 skills, 19 templates, 9 agents \u2014 57 files total (shared source + platform-specific manifests and hooks)."),
                        ("Commands = skills", "On Cursor, skills are exposed as slash commands; on Claude Code, each command is backed by the same skill definition. The 23 /gse:* commands map 1:1 onto the 23 skills."),
                        ("Tool-agnostic", "The plugin installs on both Cursor and Claude Code; only the orchestrator deployment location differs per platform (rules/ vs agents/). The .gse/ project state is identical on both."),
                        ("Composable", "Each component (agents, skills, rules, hooks, MCP) can be customized independently per project."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )
        st_space("v", 1)

        with st_zoom(100):
            with st_grid(
                cols=s.project.containers.responsive_2col,
                gap="32px",
            ) as g:
                with g.cell():
                    st_write(bs.label, "Directory Structure", tag=t.div)
                    st_code(
                        s.none,
                        code=(
                            "plugin/                          # GSE-One plugin (installed)\n"
                            "\u251c\u2500\u2500 agents/\n"
                            "\u2502   \u251c\u2500\u2500 gse-orchestrator.md      # Claude Code only (identity)\n"
                            "\u2502   \u2514\u2500\u2500 {8 specialists}.md       # both platforms\n"
                            "\u251c\u2500\u2500 rules/\n"
                            "\u2502   \u2514\u2500\u2500 gse-orchestrator.mdc     # Cursor only (identity)\n"
                            "\u251c\u2500\u2500 skills/                      # parameterized prompt chains\n"
                            "\u251c\u2500\u2500 hooks/                       # lifecycle events\n"
                            "\u251c\u2500\u2500 commands/                    # /gse:* slash commands\n"
                            "\u2514\u2500\u2500 tools/                       # dashboard, helpers\n"
                            "\n"
                            ".gse/                            # project state (created at install)\n"
                            "\u251c\u2500\u2500 config.yaml, profile.yaml, status.yaml\n"
                            "\u251c\u2500\u2500 plan.yaml, backlog.yaml, decisions.md\n"
                            "\u2514\u2500\u2500 sources.yaml"
                        ),
                        language="text",
                    )
                    st_space("v", 1)
                    st_write(bs.label, "Five Core Components", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Agents"), " \u2014 8 specialized delegates + 1 always-on orchestrator identity (9 total)")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Skills"), " \u2014 23 parameterized prompt chains, one per /gse:* command")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Templates"), " \u2014 19 shared artefact and config templates")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Rules"), " \u2014 declarative constraints that guide every AI response")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Hooks"), " \u2014 17 lifecycle events (pre-commit, post-review, on-error, etc.)")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "MCP Integration"), " \u2014 connect external tools, databases, and services")
                    st_space("v", 0.5)
                    st_write(bs.body, (bs.keyword, "Total: "), "57 files (shared source + platform-specific manifests and hooks).")

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
                        "The plugin installs to your IDE\u2019s plugin directory with sensible defaults. "
                        "The ",
                        (bs.keyword, ".gse/"),
                        " project state is created on first use. "
                        "Each component can be customized per project.",
                    )
