"""Slide — LLM Comparison: table-roadmap pattern."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_top

# Header cell: accent background + bold
_header_cell = Style.create(
    s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "llm_header_cell",
)

# Normal cell: semi-transparent bordered
_normal_cell = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "llm_normal_cell",
)


class BlockStyles:
    """Slide: LLM Comparison — maximize-viewport archetype: table-roadmap."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "llm_header_text",
    )
    cell_text = Style.create(
        s.text.sizes.pt36 + s.text.wrap.hyphens,
        "llm_cell_text",
    )
    model_name = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_model_name",
    )
bs = BlockStyles


# Table data: (Model, Strengths, Best for, Provider)
_HEADERS = ("Model", "Strengths", "Best for", "Provider")

_ROWS = [
    ("ChatGPT", "Multimodal, fast, broad knowledge", "General tasks, vision, coding", "OpenAI"),
    ("Claude", "Long context, careful reasoning, safety", "Analysis, writing, code review", "Anthropic"),
    ("Gemini", "Google integration, multimodal native", "Search, workspace, Android", "Google"),
]


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "LLM Comparison", tag=t.div, toc_lvl="1")

            # Header row
            with st_grid(
                cols="20% 30% 30% 20%",
                gap="12px",
                cell_styles=_header_cell,
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)

            # Data rows
            for model, strengths, best_for, provider in _ROWS:
                with st_grid(
                    cols="20% 30% 30% 20%",
                    gap="12px",
                    cell_styles=_normal_cell,
                ) as g:
                    with g.cell():
                        st_write(bs.model_name, model)
                    with g.cell():
                        st_write(bs.cell_text, strengths)
                    with g.cell():
                        st_write(bs.cell_text, best_for)
                    with g.cell():
                        st_write(bs.cell_text, provider)
