import setup  # noqa: F401 — configure sys.path for shared-blocks

import tomllib
import streamlit as st
import streamtex as stx
from streamtex import (
    st_book, TOCConfig, NumberingMode, MarkerConfig,
    BannerConfig, PresentationConfig, set_presentation_config,
    PdfConfig, ExportConfig, ExportMode,
    SlideBreakConfig, SlideBreakMode, set_slide_break_config,
)
from pathlib import Path

from custom.styles import Styles as s
from custom.themes import dark

import streamtex.styles as sts
import blocks

_doc_version = tomllib.loads(
    (Path(__file__).parent.parent.parent / "pyproject.toml").read_text()
).get("project", {}).get("version", "?")

# Configure static sources
_module_dir = Path(__file__).parent
_shared_static = _module_dir.parent / "shared-blocks" / "static"
stx.set_static_sources([
    str(_module_dir / "static"),
    str(_shared_static),
])

# Page configuration
st.set_page_config(
    page_title="AI4SE 6D — Q&A Companion",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Dark theme (projection-optimised, aligned with other modules)
sts.theme = dark

# Reduce default top margin
st.html('<style>.stMainBlockContainer { padding-top: 1vh !important; }</style>')

# ── Presentation mode (fullscreen 16/9) ──────────────────────────────
set_presentation_config(PresentationConfig(
    title="AI4SE 6D — Q&A Companion",
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

# ── Table of Contents ────────────────────────────────────────────────
toc = TOCConfig(
    numbering=NumberingMode.SIDEBAR_ONLY,
    toc_position=None,
    title_style=s.project.titles.slide_title + s.center_txt,
    content_style=s.large + s.text.colors.reset,
    sidebar_max_level=2,
    search=True,
)

# ── Navigation ───────────────────────────────────────────────────────
marker_config = MarkerConfig(
    auto_marker_on_toc=2,
    next_keys=["PageDown", "ArrowRight"],
    prev_keys=["PageUp", "ArrowLeft"],
    draggable=True,
    collapsible=True,
)

# ── Orchestrate blocks ───────────────────────────────────────────────
st_book(
    [
        # --- NAVIGATION ---
        blocks.bck_where_slides,            # Where are all the slides?

        # --- PART I: CONCEPTS ---
        blocks.bck_ai_agent_concepts,       # Abstract intro & key principles

        # --- PART II: GENERIC ARCHITECTURE ---
        blocks.bck_generic_architecture,     # Overview + 3 detail diagrams
        blocks.bck_generic_execution,        # Sequence diagram (5 turns)
        blocks.bck_tool_control,             # Controlling agent tools

        # --- PART III: CASE STUDY — MARIA'S WEBSHOP ---
        blocks.bck_case_study_maria,         # Context, prompt, agents, MCP
        blocks.bck_maria_architecture,       # Overview + 3 detail diagrams
        blocks.bck_maria_execution,          # Sequence diagram (7 turns)
    ],
    toc_config=toc,
    marker_config=marker_config,
    paginate=True,
    banner=BannerConfig.hidden(),
    page_width=90,
    zoom=90,
    exports=[
        ExportConfig(
            format="pdf",
            mode=ExportMode.MANUAL,
            output_dir="./exports",
            filename="ai4se6d-qa-companion",
            timestamp=True,
            pdf=PdfConfig(
                format="16:10",
                landscape=True,
                print_background=True,
                page_numbers=True,
                scale=0.8,
                content_width=90,
                margin_top="0mm",
                margin_bottom="0mm",
                margin_left="0mm",
                margin_right="0mm",
            ),
        ),
    ],
    doc_version=_doc_version,
)
