"""Slide — Today's Objectives: Morning / Afternoon schedule table."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_intro_objective",
)

# Cell styles — alternating rows
_cell_primary = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "obj_cell_primary",
)
_cell_accent = Style.create(
    s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "obj_cell_accent",
)
_cell_header = Style.create(
    s.project.containers.cell_active_bg + s.project.containers.cell_pad_md
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "obj_cell_header",
)


class BlockStyles:
    """Slide: Today's Objectives — table-roadmap archetype."""
    heading = s.project.titles.slide_title + s.center_txt
    col_title = Style.create(
        s.project.colors.highlight + s.bold + s.Large + s.text.wrap.hyphens,
        "obj_col_title",
    )
    item = Style.create(
        s.Large + s.text.wrap.hyphens,
        "obj_item",
    )
    keyword = Style.create(
        s.project.colors.accent + s.bold + s.Large + s.text.wrap.hyphens,
        "obj_keyword",
    )


bs = BlockStyles

# Schedule data: (text, is_keyword, cell_style)
# Morning and Afternoon items paired row by row
_ROWS = [
    # Row 1: headers
    ("Morning", "Afternoon", _cell_header, True),
    # Row 2
    ("Training Group Discovery", "Dev Environment Setup", _cell_primary, False),
    # Row 3
    ("Training Content", "Naive Project — Part 1", _cell_accent, False),
    # Row 4 — keyword rows
    ("Understand GenAI and LLMs", "Break", _cell_primary, False),
    # Row 5
    ("Break", "NaiveProject — Part 2", _cell_accent, False),
    # Row 6
    ("Discover Vibe...ing discipline", "Debrief & Discussion", _cell_primary, False),
    # Row 7
    ("GenAI Tools Ecosystem", "", _cell_accent, False),
]

# Keywords to highlight in accent color
_KEYWORDS = {
    "GenAI", "LLMs", "VibeCoding", "VibeEngineering",
    "Naive Prototype", "GenAI Tools Ecosystem",
    "Debrief", "Dev Environment Setup",
}


def _has_keyword(text):
    """Check if text contains a keyword to highlight."""
    return any(kw in text for kw in _KEYWORDS)


def _render_text(text, is_header):
    """Render a cell text, highlighting keywords."""
    if is_header:
        st_write(bs.col_title, text)
    elif _has_keyword(text):
        st_write(bs.keyword, text)
    else:
        st_write(bs.item, text)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Today's Objectives", tag=t.div, toc_lvl="1")

        # Two-column schedule table
        for morning, afternoon, cell, is_header in _ROWS:
            with st_grid(cols="1fr 1fr", gap="12px", cell_styles=cell) as g:
                with g.cell():
                    _render_text(morning, is_header)
                with g.cell():
                    _render_text(afternoon, is_header)
