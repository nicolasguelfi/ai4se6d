"""Slide — CE in Cursor vs Claude Code: feature comparison."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Cursor vs Claude Code comparison slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    highlight_label = s.bold + s.project.colors.highlight
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "CE in Cursor vs Claude Code", tag=t.div, toc_lvl="1")
        st_space("v", 1)

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
                        st_write(bs.body, (bs.keyword, "Planning: "), "Plan Mode maps naturally to /ce:plan")
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
            "CE works with both \u2014 the discipline is tool-agnostic.",
        )
