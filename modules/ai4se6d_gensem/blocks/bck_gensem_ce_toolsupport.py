"""Slide — CE Tool Support: 10+ environments via plugin architecture."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Tool support slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    tool_name = s.bold + s.project.colors.primary + s.Large
    note_label = s.bold + s.project.colors.highlight + s.Large
    note_body = s.project.titles.body
bs = BlockStyles

_TOOLS = [
    "Claude Code", "Cursor", "Codex", "GitHub Copilot", "Devin CLI", "Factory Droid",
    "Qwen Code", "OpenCode", "Pi", "Kimi Code CLI", "Grok Build CLI", "Antigravity CLI",
]

_TOOL_NOTES = [
    ("Claude Code", ".claude-plugin/ manifest — skills exposed as /ce-<skill> slash commands"),
    ("Cursor", ".cursor-plugin/ manifest for native Cursor installation"),
    ("Codex", "supported as both Codex App and Codex CLI"),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "Tool Support \u2014 10+ Environments", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        st_write(bs.body, (bs.keyword, "Plugin architecture: "), ".claude-plugin/ + .cursor-plugin/ manifests, native plugin installation per platform (marketplace or CLI).")
        st_space("v", 1)

        st_write(bs.tool_name, "Supported Tools", tag=t.div)
        st_space("v", 0.5)
        with st_grid(
            cols="repeat(auto-fit, minmax(200px, 1fr))",
            gap="10px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_sm
            + s.project.containers.grid_cell_centered,
        ) as g:
            for tool in _TOOLS:
                with g.cell():
                    st_write(bs.body, tool)

        st_space("v", 1)
        st_write(bs.tool_name, "Tool-Specific Notes", tag=t.div)
        st_space("v", 0.5)
        with st_list(li_style=bs.note_body, list_type=lt.unordered) as l:
            for tool, note in _TOOL_NOTES:
                with l.item():
                    st_write(bs.note_body, (bs.note_label, f"{tool}: "), note)
