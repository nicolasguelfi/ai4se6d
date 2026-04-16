"""Slide — Cross-tool synchronization with ce sync."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Sync slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Cross-Tool Synchronization", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, "One process definition, multiple IDE implementations. The ", (bs.keyword, "ce sync"), " command keeps all tools aligned.")

        st_space("v", 1)
        st_write(bs.label, "The Problem", tag=t.div)
        st_write(bs.body, "Teams use Cursor, Claude Code, and Copilot simultaneously. Rules defined in one tool are invisible to the others.")

        st_space("v", 1)
        st_write(bs.label, "The Solution", tag=t.div)
        st_code(
            s.none,
            code=(
                "# Write your rule once in the canonical source\n"
                "cat .cursor/rules/testing.mdc\n"
                "# > Always write tests before implementation.\n"
                "# > Use pytest with fixtures, never unittest.\n"
                "\n"
                "# Sync to all configured tools\n"
                "ce sync\n"
                "\n"
                "# Result: rule propagated to:\n"
                "#   .claude-plugin/rules/testing.md\n"
                "#   .github/copilot-instructions.md\n"
                "#   .claude/CLAUDE.md (appended)"
            ),
            language="bash",
        )

        st_space("v", 1)
        st_write(bs.label, "Sync Targets", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, ".cursor/rules/"), " \u2192 Cursor MDC rules")
            with l.item():
                st_write(bs.body, (bs.keyword, ".claude-plugin/rules/"), " \u2192 Claude Code plugin rules")
            with l.item():
                st_write(bs.body, (bs.keyword, ".github/copilot-instructions.md"), " \u2192 GitHub Copilot instructions")
