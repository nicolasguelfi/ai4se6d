"""Act IV — Comparison: the same concepts across five agents, opencode first (state November 2026)."""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Agent comparison table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    row_label = s.project.titles.table_label
    caption = Style.create(
        s.large + s.italic + s.project.colors.muted + s.center_txt,
        "ide_comparison_caption",
    )
bs = BlockStyles


_COLS = "1.1fr 1.15fr 1.1fr 1.1fr 1.1fr 1.1fr"

_HEADERS = ("", "opencode", "Claude Code", "Cursor", "Copilot", "Codex CLI")

# (dimension, opencode, Claude Code, Cursor, GitHub Copilot, Codex CLI)
_ROWS = [
    ("Models", "Any provider, local too", "Claude only", "Several vendors", "Several vendors", "OpenAI"),
    ("Instructions", "AGENTS.md", "CLAUDE.md", "AGENTS.md + rules", "AGENTS.md + own file", "AGENTS.md"),
    ("Plan first", "plan agent (Shift+Tab)", "plan mode", "plan mode", "plan agent", "read-only mode"),
    ("Extensions", "MCP, agents, plugins", "MCP, hooks, skills", "MCP, rules, hooks", "MCP, agents", "MCP"),
    ("Open source", "Yes (MIT)", "No", "No", "Partly", "Yes (Apache-2.0)"),
]

# Row cell styles: dimension label, highlighted opencode column, then the four other tools
_ROW_CELLS = [s.project.containers.table_header_cell, s.project.containers.table_active_cell] + [
    s.project.containers.table_normal_cell
] * 4


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Same Ideas, New Names", tag=t.div, toc_lvl="1")

            with st_zoom(72):
                # Header row
                with st_grid(cols=_COLS, gap="8px", cell_styles=s.project.containers.table_header_cell) as g:
                    for header in _HEADERS:
                        with g.cell():
                            st_write(bs.header_text, header)

                # Data rows: the opencode column is highlighted
                for row in _ROWS:
                    with st_grid(cols=_COLS, gap="8px", cell_styles=_ROW_CELLS) as g:
                        with g.cell():
                            st_write(bs.row_label, row[0])
                        for value in row[1:]:
                            with g.cell():
                                st_write(bs.cell_text, value)

            st_write(
                bs.caption,
                "Learn the concept, not the menu.",
                tag=t.div,
            )
