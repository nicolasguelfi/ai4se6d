"""Slide 36 — IDE Comparison: table-roadmap grid."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

<<<<<<< HEAD

# Viewport-filling container
_page_fill = s.project.containers.page_fill_top

# Cell styles for comparison table
_header_cell = Style.create(
    s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "ide_cmp_header_cell",
)

_normal_cell = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "ide_cmp_normal_cell",
)

_active_cell = Style.create(
    s.project.containers.cell_active_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "ide_cmp_active_cell",
)


class BlockStyles:
    """IDE comparison table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "ide_cmp_header_text",
    )
    cell_text = Style.create(
        s.text.sizes.pt36 + s.text.wrap.hyphens,
        "ide_cmp_cell_text",
    )
    tool_name = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ide_cmp_tool_name",
    )
    tool_active = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.highlight + s.text.wrap.hyphens,
        "ide_cmp_tool_active",
    )
bs = BlockStyles


=======
class BlockStyles:
    """IDE comparison table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    tool_name = s.project.titles.table_label
    tool_active = s.project.titles.table_label_active
bs = BlockStyles

>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
# Comparison data: (Tool, Autonomy, IDE Integration, Best For, is_active)
_HEADERS = ("Tool", "Autonomy", "IDE Integration", "Best For")

_TOOLS = [
    ("Cursor", "High", "Native IDE", "Full-stack development", True),
    ("Claude Code", "Highest", "Terminal CLI", "Complex reasoning, SDK", True),
    ("Windsurf", "Medium", "VS Code fork", "Guided assistance", False),
    ("GitHub Copilot", "Medium", "VS Code plugin", "Inline completions", False),
]

<<<<<<< HEAD

def build():
    with st_block(_page_fill):
=======
def build():
    with st_block(s.project.containers.page_fill_top):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "Comparison", tag=t.div, toc_lvl="1")

            # Header row
            with st_grid(
                cols="20% 20% 30% 30%",
                gap="8px",
<<<<<<< HEAD
                cell_styles=_header_cell,
=======
                cell_styles=s.project.containers.table_header_cell,
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)

            # Data rows
            for tool, autonomy, integration, best_for, is_active in _TOOLS:
<<<<<<< HEAD
                cell = _active_cell if is_active else _normal_cell
=======
                cell = s.project.containers.table_active_cell if is_active else s.project.containers.table_normal_cell
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
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
