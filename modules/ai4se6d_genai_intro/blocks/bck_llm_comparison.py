"""Slide — LLM Comparison: table-roadmap pattern."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.bib import cite
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
    warning_text = Style.create(
        s.Large + s.italic + s.project.colors.accent + s.center_txt,
        "llm_warning_text",
    )
    source = s.project.citation + s.large + s.center_txt
    header_text = Style.create(
        s.text.sizes.pt32 + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "llm_header_text",
    )
    cell_text = Style.create(
        s.text.sizes.pt32 + s.text.wrap.hyphens,
        "llm_cell_text",
    )
    provider_name = Style.create(
        s.text.sizes.pt32 + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_provider_name",
    )
bs = BlockStyles


# Table data: (Provider, Known for, Primary use cases)
_HEADERS = ("Provider", "Known for", "Primary use cases")

_ROWS = [
    (
        "OpenAI",
        "Multimodal capabilities, fast iteration, broad general knowledge",
        "General-purpose tasks, vision, code generation",
    ),
    (
        "Anthropic",
        "Careful reasoning, safety-focused design, extended context processing",
        "Complex analysis, long document review, writing, code review",
    ),
    (
        "Google",
        "Deep ecosystem integration, multimodal native architecture",
        "Search-augmented tasks, workspace productivity, large-scale document processing",
    ),
]


def build():
    with st_zoom(120), st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "LLM Comparison", tag=t.div, toc_lvl="1")

            st_write(
                bs.warning_text,
                "⚠ This landscape evolves rapidly ⚠ ",
                (s.project.citation + s.Large, cite("artificialanalysis2026")),
            )

            st_space(size=1)

            # Header row
            with st_grid(
                cols="20% 40% 40%",
                gap="12px",
                cell_styles=_header_cell,
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)

            # Data rows
            for provider, known_for, use_cases in _ROWS:
                with st_zoom(105),st_grid(
                    cols="20% 40% 40%",
                    gap="12px",
                    cell_styles=_normal_cell,
                ) as g:
                    with g.cell():
                        st_write(bs.provider_name, provider)
                    with g.cell():
                        st_write(bs.cell_text, known_for)
                    with g.cell():
                        st_write(bs.cell_text, use_cases)

            st_space(size=2)
            st_write(bs.source, cite("artificialanalysis2026intelligence"), " · ", cite("artificialanalysis2026livecodebench"), " · ", cite("contextarena2026"))
