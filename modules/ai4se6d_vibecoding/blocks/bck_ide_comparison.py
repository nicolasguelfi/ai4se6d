"""Slide 36 — IDE Comparison: table-roadmap grid."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """IDE comparison table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    tool_name = s.project.titles.table_label
    tool_active = s.project.titles.table_label_active
bs = BlockStyles

# Comparison data: (Tool, Autonomy, IDE Integration, Best For, is_active)
_HEADERS = ("Tool", "Autonomy", "IDE Integration", "Best For")

_TOOLS = [
    ("Cursor", "High", "Native IDE", "Full-stack development", True),
    ("Claude Code", "Highest", "Terminal CLI", "Complex reasoning, SDK", True),
    ("Windsurf", "Medium", "VS Code fork", "Guided assistance", False),
    ("GitHub Copilot", "Medium", "VS Code plugin", "Inline completions", False),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Comparison", tag=t.div, toc_lvl="1")

            # Header row
            with st_grid(
                cols="20% 20% 30% 30%",
                gap="8px",
                cell_styles=s.project.containers.table_header_cell,
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)

            # Data rows
            for tool, autonomy, integration, best_for, is_active in _TOOLS:
                cell = s.project.containers.table_active_cell if is_active else s.project.containers.table_normal_cell
                name_style = bs.tool_active if is_active else bs.tool_name
                with st_grid(
                    cols="20% 20% 30% 30%",
                    gap="8px",
                    cell_styles=cell,
                ) as g:
                    with g.cell():
                        st_write(name_style, tool)
                    with g.cell():
                        st_write(bs.cell_text, autonomy)
                    with g.cell():
                        st_write(bs.cell_text, integration)
                    with g.cell():
                        st_write(bs.cell_text, best_for)
