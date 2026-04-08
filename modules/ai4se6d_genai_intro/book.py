import setup  # noqa: F401 — configure sys.path for shared-blocks

import tomllib
import streamlit as st
import streamtex as stx
from pathlib import Path
from streamtex import (
    st_book, TOCConfig, NumberingMode, MarkerConfig, BannerConfig,
    PresentationConfig, set_presentation_config,
    PdfConfig, ExportConfig, ExportMode,
    set_ai_image_config, AIImageConfig,
    SlideBreakConfig, SlideBreakMode, set_slide_break_config,
)
from streamtex.bib import BibConfig, BibFormat, CitationStyle, set_bib_config
from pathlib import Path

from custom.styles import Styles as s
from custom.themes import dark
from custom.config import IS_EXPORTABLE

_doc_version = tomllib.loads((Path(__file__).parent.parent.parent / "pyproject.toml").read_text()).get("project", {}).get("version", "?")
import streamtex.styles as sts
import blocks

# Configure static sources (module + shared-blocks)
_module_dir = Path(__file__).parent
_shared_static = _module_dir.parent / "shared-blocks" / "static"
stx.set_static_sources([
    str(_module_dir / "static"),
    str(_shared_static),
])

# Page configuration
st.set_page_config(
    page_title="AI for Software Engineering",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject dark theme
sts.theme = dark

# ── Reduce default top margin on main block container ────────────────
st.html("""
<style>
    .stMainBlockContainer { padding-top: 1vh !important; }
</style>
""")

# ── AI Image Generation ───────────────────────────────────────────────
set_ai_image_config(AIImageConfig(
    provider="openai",
    default_size="1536x1024",
    output_dir="static/images/ai",
    auto_generate=True,
))

# ── Presentation mode (fullscreen 16/9) ──────────────────────────────
set_presentation_config(PresentationConfig(
    title="AI for Software Engineering — Session 1",
    aspect_ratio="16/9",
    footer=True,
    center_content=False,
    hide_streamlit_header=False,
    enforce_ratio=False,
))

# ── Slide breaks (minimal space in paginated mode) ────────────────────
set_slide_break_config(SlideBreakConfig(
    mode=SlideBreakMode.HIDDEN,
    space="1vh",
    rule_margin_top="1vh",
    rule_margin_bottom="1vh",
))

# ── Table of Contents (sidebar only, level 1) ────────────────────────
toc = TOCConfig(
    numbering=NumberingMode.SIDEBAR_ONLY,
    toc_position=None,
    title_style=s.project.titles.slide_title + s.center_txt,
    content_style=s.large + s.text.colors.reset,
    sidebar_max_level=2,
    search=True,
)

# ── Navigation (PageDown/PageUp + arrow keys) ────────────────────────
marker_config = MarkerConfig(
    auto_marker_on_toc=1,
    next_keys=["PageDown", "ArrowRight"],
    prev_keys=["PageUp", "ArrowLeft"],
    draggable=True,
    collapsible=True,
)

# ── Unwired blocks (present in blocks/ but not in the slide sequence) ─
# bck_title            — template: generic title (from project init)
# bck_conclusion       — template: generic conclusion (from project init)
# bck_features         — template: feature showcase (from project init)
# bck_grid_demo        — demo: responsive grid patterns
# bck_lists_demo       — demo: list rendering patterns
# bck_trainer_team     — deprecated: replaced by bck_trainer_ng + bck_trainer_ts
# bck_same_tools       — planned: "Same Tools, Different Discipline" slide
# bck_llm_tokens       — planned: token visualization (complement to tokenization)
# bck_llm_next_token   — planned: next-token prediction detail
# bck_llm_layers       — planned: network layers visualization
# bck_llm_training     — planned: training process overview

# ── Bibliography ─────────────────────────────────────────────────────
set_bib_config(BibConfig(
    format=BibFormat.APA,
    citation_style=CitationStyle.AUTHOR_YEAR,
    hover_enabled=True,
    hover_show_abstract=True,
    sort_by="author",
))

# ── Orchestrate slides ───────────────────────────────────────────────
st_book(
    [
        # Introduction
        blocks.bck_intro_title,
        blocks.bck_trainer_ng,
        blocks.bck_trainer_ts,
        blocks.bck_intro_round_table,
        blocks.bck_poll_ai_experience,
        blocks.bck_poll_ai_result,
        blocks.bck_intro_roadmap,
        blocks.bck_intro_objective,
        # Fundamentals — AI
        blocks.bck_ai_definition,
        blocks.bck_ai_mccarthy,
        blocks.bck_ai_vs_genai,
        blocks.bck_ai_discriminative,
        blocks.bck_ai_generative,
        blocks.bck_ai_era_symbolic,
        blocks.bck_ai_era_ml,
        blocks.bck_ai_era_dl,
        blocks.bck_ai_era_genai,
        # Fundamentals — Generative AI
        blocks.bck_genai_revolution,
        blocks.bck_genai_for_devs,
        blocks.bck_genai_landscape,
        # Fundamentals — LLMs
        blocks.bck_llm_comparison,
        blocks.bck_llm_how_work,
        blocks.bck_llm_transformers_in_60s_title,
        blocks.bck_llm_teaser,
        blocks.bck_llm_transformer_demo,
        # Sequence 3A — How LLMs Generate Text (inference)
        blocks.bck_llm_pipeline,
        blocks.bck_llm_tokenization,
        blocks.bck_llm_vocabulary,
        blocks.bck_llm_embeddings,
        blocks.bck_llm_semantic_space,
        blocks.bck_llm_attention,
        blocks.bck_llm_attention_viz,
        blocks.bck_llm_prediction,
        blocks.bck_llm_autoregressive,
        blocks.bck_llm_context_window,
        blocks.bck_llm_context_benchmark,
        # Sequence 3B — How LLMs Are Built (engineering)
        blocks.bck_llm_how_built,
        blocks.bck_llm_pretraining,
        blocks.bck_llm_finetuning,
        blocks.bck_llm_alignment,
        # Synthesis
        #blocks.bck_llm_summary,
        # Capabilities & Limitations
        blocks.bck_llm_capabilities,
        blocks.bck_llm_limitations,
        # Fundamentals — Cross-cutting
        blocks.bck_ai_ethics,
        blocks.bck_genai_takeaways,
        # Reference
        blocks.bck_shared_glossary,
        blocks.bck_references,
    ],
    toc_config=toc,
    marker_config=marker_config,
    paginate=True,
    banner=BannerConfig.hidden(),
    page_width=90,
    zoom=90,
    bib_sources=[str(_shared_static / "references.bib")],
    exports=[
        ExportConfig(
            format="html",
            mode=ExportMode.MANUAL if IS_EXPORTABLE else ExportMode.NEVER,
            output_dir="./exports",
            filename="ai4se-session1",
            timestamp=True,
        ),
        ExportConfig(
            format="pdf",
            mode=ExportMode.MANUAL if IS_EXPORTABLE else ExportMode.NEVER,
            output_dir="./exports",
            filename="ai4se-session1",
            timestamp=True,
            pdf=PdfConfig(
                format="16:10",
                landscape=True,
                print_background=True,
                page_numbers=True,
                scale=0.8,
                content_width=90,
                margin_top="0mm", margin_bottom="0mm",
                margin_left="0mm", margin_right="0mm",
            ),
        ),
    ],
    doc_version=_doc_version,
)
