import setup  # noqa: F401 — configure sys.path for shared-blocks

import streamlit as st
import streamtex as stx
from streamtex import (
    st_book, TOCConfig, NumberingMode, MarkerConfig, BannerConfig,
    PresentationConfig, set_presentation_config,
    PdfConfig, ExportConfig, ExportMode,
    set_ai_image_config, AIImageConfig,
    SlideBreakConfig, SlideBreakMode, set_slide_break_config,
)
from pathlib import Path

from custom.styles import Styles as s
from custom.themes import dark
from custom.config import IS_EXPORTABLE
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

# Orchestrate slides
st_book(
    [
        # Opening
        blocks.bck_title,
        blocks.bck_intro_review_habits,
        # VibeCoding — The Concept
        blocks.bck_vibecoding_origin,
        blocks.bck_vibecoding_principles,
        blocks.bck_vibecoding_analogy,
        # Exercise 2 — Pure VibeCoding
        blocks.bck_exercise_vibecoding,
        # Dangers of Naive VibeCoding
        blocks.bck_vibecoding_dangers,
        blocks.bck_vibecoding_reality,
        # VibeEngineering — The Discipline
        blocks.bck_vibeeng_transition,
        blocks.bck_vibeeng_principles,
        blocks.bck_vibeeng_spectrum,
        # Exercise 3 — VibeEngineering in Practice
        blocks.bck_exercise_vibeeng,
        # IDE Ecosystem
        blocks.bck_ide_ecosystem,
        # Closing
        blocks.bck_recap,
        blocks.bck_glossary,
    ],
    toc_config=toc,
    marker_config=marker_config,
    paginate=True,
    banner=BannerConfig.hidden(),
    page_width=90,
    zoom=90,
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
)
