"""Slide — Agentic IDE Tools: Cursor, Claude Code, Windsurf, Copilot."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = s.project.containers.page_fill_top

# Cell styles for comparison table
_header_cell = Style.create(
    s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "ide_header_cell",
)

_normal_cell = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "ide_normal_cell",
)

_active_cell = Style.create(
    s.project.containers.cell_active_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "ide_active_cell",
)


class BlockStyles:
    """IDE ecosystem slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    header_text = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "ide_header_text",
    )
    cell_text = Style.create(
        s.text.sizes.pt36 + s.text.wrap.hyphens,
        "ide_cell_text",
    )
    tool_name = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ide_tool_name",
    )
    tool_active = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.highlight + s.text.wrap.hyphens,
        "ide_tool_active",
    )
bs = BlockStyles


# Comparison data: (Tool, Autonomy, IDE Integration, Best For, is_primary)
_HEADERS = ("Tool", "Autonomy", "IDE Integration", "Best For")

_TOOLS = [
    ("Cursor", "High", "Native IDE", "Full-stack development", True),
    ("Claude Code", "Highest", "Terminal CLI", "Complex reasoning, SDK", True),
    ("Windsurf", "Medium", "VS Code fork", "Guided assistance", False),
    ("GitHub Copilot", "Medium", "VS Code plugin", "Inline completions", False),
]


def build():
    # Sub-slide 1: Autonomy spectrum (from LaTeX L.453-461)
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Autonomy Spectrum", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "Passive assistance"), " — responds only when invoked")
                with l.item(): st_write(bs.body, (bs.keyword, "Proactive copiloting"), " — suggests unprompted, you decide")
                with l.item(): st_write(bs.body, (bs.keyword_accent, "Task-level delegation"), " — you describe, AI executes")
                with l.item(): st_write(bs.body, (bs.keyword_warn, "Autonomous agents"), " — AI plans, executes, tests, iterates")
                with l.item(): st_write(bs.body, (bs.keyword_warn, "Multi-agent orchestration"), " — specialized AI teams collaborate")

    st_slide_break()

    # Sub-slide 2: Cursor
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.subheading, "Cursor", tag=t.div, toc_lvl="2")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "AI-native IDE"), " \u2014 built from the ground up for AI")
                with l.item(): st_write(bs.body, (bs.keyword_warn, "$29.3B valuation"), " \u2014 fastest-growing dev tool")
                with l.item(): st_write(bs.body, (bs.keyword, "8 parallel agents"), " for concurrent tasks")
                with l.item(): st_write(bs.body, "Modes: ", (bs.keyword_accent, "Tab"), " / ", (bs.keyword_accent, "Chat"), " / ", (bs.keyword_accent, "Agent"))
                with l.item(): st_write(bs.body, (bs.keyword_warn, "Primary tool"), " for this training")

    st_slide_break()

    # Sub-slide 3: Claude Code
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.subheading, "Claude Code", tag=t.div, toc_lvl="2")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "Terminal CLI-first"), " \u2014 runs in your shell")
                with l.item(): st_write(bs.body, (bs.keyword_accent, "Highest autonomy"), " \u2014 agentic by design")
                with l.item(): st_write(bs.body, (bs.keyword, "Agent SDK"), " \u2014 build custom AI agents")
                with l.item(): st_write(bs.body, "Deep reasoning with ", (bs.keyword_warn, "extended thinking"))

    st_slide_break()

    # Sub-slide 4: Windsurf + Copilot
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.subheading, "Other Notable Tools", tag=t.div, toc_lvl="2")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "Windsurf"), " \u2014 VS Code fork with guided AI flows")
                with l.item(): st_write(bs.body, (bs.keyword, "GitHub Copilot"), " \u2014 inline completions, deep VS Code integration")

    st_slide_break()

    # Sub-slide 5: Comparison matrix
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.subheading, "Comparison", tag=t.div, toc_lvl="2")

            # Header row
            with st_grid(
                cols="20% 20% 30% 30%",
                gap="8px",
                cell_styles=_header_cell,
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)

            # Data rows
            for tool, autonomy, integration, best_for, is_primary in _TOOLS:
                cell = _active_cell if is_primary else _normal_cell
                name_style = bs.tool_active if is_primary else bs.tool_name
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
