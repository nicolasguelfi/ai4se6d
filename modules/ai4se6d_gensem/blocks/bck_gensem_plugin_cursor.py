"""Slide — GSE-One in Cursor vs Claude Code: feature comparison."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Cursor vs Claude Code comparison slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    highlight_label = s.bold + s.project.colors.highlight
bs = BlockStyles

def build():
    st_marker("Cursor vs Claude Code")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                st_write(bs.heading, "GSE-One in Cursor vs Claude Code", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="Tool Comparison",
                    entries=[
                        ("Cursor strengths", "Visual IDE with inline diff, file-scoped context, and Plan Mode that maps naturally to /gse:plan."),
                        ("Claude Code strengths", "Terminal-native with MCP servers, git worktrees, background agents, and layered CLAUDE.md rules."),
                        ("GSE-One principle", "The methodology is tool-agnostic -- the discipline transfers across tools."),
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
                    st_write(bs.label, "Cursor", tag=t.div)
                    st_space("v", 1)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Rules: "), ".cursor/rules/*.mdc with glob-scoped activation")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Artifacts: "), "Notepads as structured knowledge documents")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Planning: "), "Plan Mode maps naturally to /gse:plan")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Strengths: "), "Visual IDE, inline diff, file-scoped context")

                with g.cell():
                    st_write(bs.label, "Claude Code", tag=t.div)
                    st_space("v", 1)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Rules: "), "Layered CLAUDE.md (project, user, global)")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Artifacts: "), "Skills with arguments, composable workflows")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Hooks: "), "17 lifecycle event types for automated enforcement")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Strengths: "), "MCP servers, terminal-native, git worktrees, background agents")

            st_space("v", 2)
            st_write(
                bs.body,
                (bs.highlight_label, "Key difference: "),
                "Cursor excels at interactive editing within files; Claude Code excels at autonomous multi-file orchestration. "
                "GSE-One works with both \u2014 the discipline is tool-agnostic.",
            )
