import setup  # noqa: F401 — configure sys.path for shared-blocks

import tomllib
import streamlit as st
import streamtex as stx
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
    page_title="Discovering VibeCoding & VibeEngineering",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject dark theme
sts.theme = dark

# Reduce default top margin
st.html("""
<style>
    .stMainBlockContainer { padding-top: 1vh !important; }
</style>
""")

# AI Image Generation
set_ai_image_config(AIImageConfig(
    provider="openai",
    default_size="1536x1024",
    output_dir="static/images/ai",
    auto_generate=True,
))

# Presentation mode (fullscreen 16/9)
set_presentation_config(PresentationConfig(
    title="Discovering VibeCoding & VibeEngineering — Session 1, Part 2",
    aspect_ratio="16/9",
    footer=True,
    center_content=False,
    hide_streamlit_header=False,
    enforce_ratio=False,
))

# Slide breaks
set_slide_break_config(SlideBreakConfig(
    mode=SlideBreakMode.HIDDEN,
    space="1vh",
    rule_margin_top="1vh",
    rule_margin_bottom="1vh",
))

# Table of Contents
toc = TOCConfig(
    numbering=NumberingMode.SIDEBAR_ONLY,
    toc_position=None,
    title_style=s.project.titles.slide_title + s.center_txt,
    content_style=s.large + s.text.colors.reset,
    sidebar_max_level=2,
    search=True,
)

# Navigation
marker_config = MarkerConfig(
    auto_marker_on_toc=1,
    next_keys=["PageDown", "ArrowRight"],
    prev_keys=["PageUp", "ArrowLeft"],
    draggable=True,
    collapsible=True,
)

# ── Bibliography ─────────────────────────────────────────────────────
set_bib_config(BibConfig(
    format=BibFormat.APA,
    citation_style=CitationStyle.AUTHOR_YEAR,
    hover_enabled=True,
    hover_show_abstract=True,
    sort_by="author",
))

# Orchestrate slides
st_book(
    [
        # --- OPENING ---
        blocks.bck_title,                        # Block 1
        blocks.bck_intro_review_habits,          # Block 2

        # --- ACT I: VIBECODING — THE CONCEPT ---
        blocks.bck_vibecoding_origin,            # Block 3  — Karpathy quotes
        blocks.bck_vibecoding_definition,        # Block 4  — Formal definition
        blocks.bck_vibecoding_paradigm,          # Block 5  — From Cook to Customer
        blocks.bck_vibecoding_intent,            # Block 6  — Principle 1
        blocks.bck_vibecoding_trust,             # Block 7  — Principle 2
        blocks.bck_vibecoding_conversation,      # Block 8  — Principle 3
        blocks.bck_vibecoding_low_barrier,       # Block 9  — Principle 4
        blocks.bck_vibecoding_analogy,           # Block 10 — Historical analogy

        # --- EXERCISE 2: PURE VIBECODING ---
        blocks.bck_exercise_vibecoding,          # Block 11

        # --- ACT II: THE REALITY CHECK ---
        blocks.bck_vibecoding_danger_intro,      # Block 12 — Billboard pivot
        blocks.bck_vibecoding_danger_vuln,       # Block 13 — 12-65% vulnerabilities
        blocks.bck_vibecoding_danger_halluc,     # Block 14 — Hallucinated deps
        blocks.bck_vibecoding_danger_debt,       # Block 15 — Tech debt iceberg
        blocks.bck_vibecoding_danger_paradox,    # Block 16 — AI Paradox 7h/week
        blocks.bck_vibecoding_danger_demo_prod,  # Block 17 — Demo vs Production
        blocks.bck_vibecoding_reality,           # Block 18 — Stats + gala pivot
        blocks.bck_vibecoding_bridge,            # Block 19 — Speed AND Quality?

        # --- ACT III: VIBEENGINEERING — THE DISCIPLINE ---
        blocks.bck_vibeeng_transition,           # Block 20 — Q5: What practices?
        blocks.bck_vibeeng_rebranding,           # Block 21 — Coding → Engineering
        blocks.bck_vibeeng_p_requirements,       # Block 22 — P1: Requirements
        blocks.bck_vibeeng_p_tdd,                # Block 23 — P2: TDD
        blocks.bck_vibeeng_p_architecture,       # Block 24 — P3: Architecture
        blocks.bck_vibeeng_p_iteration,          # Block 25 — P4: Iteration
        blocks.bck_vibeeng_p_review,             # Block 26 — P5: Review
        blocks.bck_vibeeng_p_context,            # Block 27 — P6: Context Eng.
        blocks.bck_vibeeng_spectrum,             # Block 28 — 4-level spectrum
        blocks.bck_vibeeng_evidence,             # Block 29 — FlowGen 15%

        # --- EXERCISE 3: REDO WITH DISCIPLINE ---
        blocks.bck_exercise_vibeeng,             # Block 30

        # --- ACT IV: TOOL ECOSYSTEM ---
        blocks.bck_ide_overview,                 # Block 31 — Section billboard
        blocks.bck_ide_autonomy,                 # Block 32 — 5 levels + agentic turn
        blocks.bck_ide_cursor,                   # Block 33 — Cursor detailed
        blocks.bck_ide_claude_code,              # Block 34 — Claude Code detailed
        blocks.bck_ide_others,                   # Block 35 — Windsurf + Copilot
        blocks.bck_ide_comparison,               # Block 36 — Comparison matrix
        blocks.bck_ide_mcp,                      # Block 37 — MCP protocol
        blocks.bck_ide_cursor_choice,            # Block 38 — Why Cursor

        # --- CLOSING ---
        blocks.bck_recap,                        # Block 39
        blocks.bck_closing,                      # Block 40 — Questions?
        blocks.bck_glossary,                     # Block 41
    ],
    toc_config=toc,
    marker_config=marker_config,
    paginate=True,
    banner=BannerConfig.hidden(),
    page_width=90,
    zoom=90,
    bib_sources=[str(_module_dir / "static" / "references.bib")],
    exports=[
        ExportConfig(
            format="html",
            mode=ExportMode.MANUAL if IS_EXPORTABLE else ExportMode.NEVER,
            output_dir="./exports",
            filename="ai4se-vibecoding",
            timestamp=True,
        ),
        ExportConfig(
            format="pdf",
            mode=ExportMode.MANUAL if IS_EXPORTABLE else ExportMode.NEVER,
            output_dir="./exports",
            filename="ai4se-vibecoding",
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
