"""Slide — LLM Comparison: table-roadmap pattern.

Situation in November 2026 (NG, 2026-11-22). Named at family level on purpose: point versions change
every few weeks. Checked against openai.com (GPT-6 Astra/Sol/Luna, GPT-6.2 on 2026-11-17), blog.google
(Gemini 4 Argon, Carbon — developers 2026-11-10, Hydrogen 2026-11-16), anthropic.com (Claude Fable 5.2,
Opus 5.5) and the Artificial Analysis leaderboard (Kimi K3.1 Pro top open-weights model).
"""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
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
    model_names = Style.create(
        s.text.sizes.pt24 + s.italic + s.text.wrap.hyphens,
        "llm_model_names",
    )
    provider_name = Style.create(
        s.text.sizes.pt32 + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_provider_name",
    )
bs = BlockStyles


# Table data: (Provider, current models, Known for, Primary use cases) — November 2026
_HEADERS = ("Provider", "Known for", "Primary use cases")

_ROWS = [
    (
        "OpenAI",
        "GPT-6 — Astra, Sol, Luna",
        "Widest reach (ChatGPT)",
        "General-purpose home assistant, coding with Codex",
    ),
    (
        "Anthropic",
        "Claude 5 — Fable, Opus, Sonnet",
        "Careful reasoning, long autonomous agent sessions",
        "Agentic coding (Claude Code), complex analysis",
    ),
    (
        "Google",
        "Gemini 4 — Carbon, Argon, Hydrogen",
        "Natively multimodal, built into Search and Workspace",
        "Workspace productivity, search-augmented tasks",
    ),
    (
        "Open weights",
        "Kimi, Qwen, DeepSeek, Mistral",
        "Weights you download and run yourself; a few months behind the frontier",
        "On-premise and sovereign hosting, sensitive data, fine-tuning",
    ),
]


def build():
    with st_zoom(100), st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "LLM Comparison", tag=t.div, toc_lvl="1")

            st_write(
                bs.warning_text+"zoom:0.7;",
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
            for provider, models, known_for, use_cases in _ROWS:
                with st_zoom(100),st_grid(
                    cols="20% 40% 40%",
                    gap="12px",
                    cell_styles=_normal_cell,
                ) as g:
                    with g.cell():
                        st_write(bs.provider_name, provider, tag=t.div)
                        st_write(bs.model_names, models, tag=t.div)
                    with g.cell():
                        st_write(bs.cell_text, known_for)
                    with g.cell():
                        st_write(bs.cell_text, use_cases)

            st_space(size=2)
            st_write(bs.source, cite("artificialanalysis2026intelligence"), " · ", cite("artificialanalysis2026livecodebench"), " · ", cite("contextarena2026"))
