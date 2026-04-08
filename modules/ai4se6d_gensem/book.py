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
    page_title="GenSEM — Generative Software Engineering Methods",
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
    title="GenSEM — Generative Software Engineering Methods",
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

# Orchestrate slides — v2 (~132 blocks, ~150 slides, ~3h)
st_book(
    [
        # ═══════════════════════════════════════════════════════════════
        # OPENING (4 blocks)
        # ═══════════════════════════════════════════════════════════════
        blocks.bck_gensem_title,
        blocks.bck_gensem_session_map,              # 3-parts journey overview
        blocks.bck_gensem_objectives,
        blocks.bck_gensem_day1_recall,               # Days 1-2 recap

        # ═══════════════════════════════════════════════════════════════
        # PART 1 — LE MÉTIER DU GENERATIVE SE (25 blocks)
        # ═══════════════════════════════════════════════════════════════

        # Sequence 1.1: Comment le SDLC change
        blocks.bck_gensem_sdlc_title,
        blocks.bck_gensem_sdlc_gravity,              # NEW — shifting center of gravity
        blocks.bck_gensem_sdlc_15tasks,              # NEW — 15 core tasks taxonomy
        blocks.bck_gensem_sdlc_re,                   # NEW — RE transformed (238 articles)
        blocks.bck_gensem_sdlc_phases,               # v1 enriched — 6 SDLC phases impact
        blocks.bck_gensem_sdlc_codegen,              # NEW — 3 paradigms (CHOP/VC/VE)
        blocks.bck_gensem_sdlc_testing,              # NEW — 102 studies, FlowGen
        blocks.bck_gensem_sdlc_spectrum,             # v1 — 4-level spectrum
        blocks.bck_gensem_sdlc_evidence,             # v1 — tool alone vs tool+process

        # Sequence 1.2: 15 concepts fondamentaux
        blocks.bck_gensem_concepts_title,            # NEW — section title
        blocks.bck_gensem_concepts_interaction,      # NEW — Layer 1 (C1-C3)
        blocks.bck_gensem_concepts_knowledge,        # NEW — Layer 2 (C4-C8)
        blocks.bck_gensem_concepts_execution,        # NEW — Layer 3 (C9-C14)
        blocks.bck_gensem_concepts_ecosystem,        # NEW — Layer 4 (C15)
        blocks.bck_gensem_concepts_insight,          # NEW — process insight
        blocks.bck_gensem_concepts_community,        # NEW — 9K+/800+/16.6K+ stats
        blocks.bck_gensem_concepts_convergence,      # NEW — universal convergence

        # Sequence 1.3: Le facteur humain
        blocks.bck_gensem_human_title,               # NEW — section title
        blocks.bck_gensem_human_11types,             # NEW — 11 interaction types
        blocks.bck_gensem_sdlc_human,                # v1 — roles evolution
        blocks.bck_gensem_human_junior_senior,       # NEW — Cui vs METR vs Daniotti
        blocks.bck_gensem_human_creativity,          # NEW — homogenization
        blocks.bck_gensem_human_fowler,              # NEW — Fowler warning
        blocks.bck_gensem_human_discussion,          # NEW — discussion moment

        # ═══════════════════════════════════════════════════════════════
        # PART 2 — L'ÉVIDENCE EMPIRIQUE (14 blocks)
        # ═══════════════════════════════════════════════════════════════
        blocks.bck_gensem_evidence_title,            # NEW
        blocks.bck_gensem_evidence_peng,             # NEW — RCT 1: +55.8%
        blocks.bck_gensem_evidence_cui,              # NEW — RCT 2: 4,867 devs
        blocks.bck_gensem_evidence_metr,             # NEW — RCT 3: -19%
        blocks.bck_gensem_evidence_paradox,          # NEW — Cui vs METR
        blocks.bck_gensem_evidence_perception,       # NEW — perception-reality gap
        blocks.bck_gensem_evidence_surveys,          # NEW — 5 developer surveys
        blocks.bck_gensem_evidence_daniotti,         # NEW — 160K GitHub devs
        blocks.bck_gensem_evidence_paradox_ai,       # NEW — 7h/week AI paradox
        blocks.bck_gensem_evidence_enterprise,       # NEW — 10% vs 25-30%
        blocks.bck_gensem_evidence_fowler,           # NEW — Fowler quote
        blocks.bck_gensem_evidence_synthesis,        # NEW — 3 takeaways
        blocks.bck_gensem_evidence_discussion,       # NEW — discussion
        blocks.bck_gensem_evidence_transition,       # NEW — transition

        # ═══════════════════════════════════════════════════════════════
        # PART 3 — FRAMEWORKS MÉTHODOLOGIQUES (30 blocks)
        # ═══════════════════════════════════════════════════════════════
        blocks.bck_gensem_frameworks_title,
        blocks.bck_gensem_fw_landscape,              # NEW — 3-category landscape
        blocks.bck_gensem_fw_overview,               # v1 — overview table

        # AgileGen (3 slides)
        blocks.bck_gensem_fw_agilegen,               # v1 — concept + Gherkin
        blocks.bck_gensem_fw_agilegen_memory,        # NEW — memory pool + frustrations
        blocks.bck_gensem_fw_agilegen_roadmap,       # NEW — research roadmap

        # Agentic DevOps (1 slide)
        blocks.bck_gensem_fw_agenticdevops,          # v1 — Microsoft vision

        # SE 3.0 (3 slides)
        blocks.bck_gensem_fw_se30,                   # v1 — overview + 5 characteristics
        blocks.bck_gensem_fw_se30_intent,            # NEW — intent + conversation
        blocks.bck_gensem_fw_se30_adaptive,          # NEW — adaptive + multi-objective

        # V-Bounce (3 slides)
        blocks.bck_gensem_fw_vbounce,                # v1 — concept
        blocks.bck_gensem_fw_vbounce_diagram,        # NEW — V diagram annotated
        blocks.bck_gensem_fw_vbounce_agents,         # NEW — 4 agent roles

        # Promptware Engineering (2 slides)
        blocks.bck_gensem_fw_promptware,             # v1 — concept
        blocks.bck_gensem_fw_promptware_crisis,      # NEW — promptware crisis parallel

        # Multi-Agent SE (6 slides)
        blocks.bck_gensem_fw_multiagent_title,       # NEW — section title
        blocks.bck_gensem_fw_multiagent_sop,         # NEW — Category 1: SOP-Driven
        blocks.bck_gensem_fw_multiagent_conv,        # NEW — Category 2: Conversational
        blocks.bck_gensem_fw_multiagent_aci,         # NEW — Category 3: ACI
        blocks.bck_gensem_fw_multiagent_ide,         # NEW — Category 4: Integrated IDEs
        blocks.bck_gensem_fw_multiagent_insight,     # NEW — process discipline insight

        # Synthesis + Risks + Roadmaps (5 slides)
        blocks.bck_gensem_fw_synthesis,              # v1 — comparison table (fix labels)
        blocks.bck_gensem_risks_overview,            # NEW — 6 risk categories
        blocks.bck_gensem_roadmap,                   # v1 — enterprise forecasts
        blocks.bck_gensem_fw_multiagent,             # v1 — compact overview (optional)
        blocks.bck_gensem_sota_takeaway,             # v1 — 3 takeaways

        # ═══════════════════════════════════════════════════════════════
        # PART 4 — COMPOUND ENGINEERING (35 blocks)
        # ═══════════════════════════════════════════════════════════════
        blocks.bck_gensem_ce_title,

        # Philosophy (3 slides)
        blocks.bck_gensem_ce_philosophy,
        blocks.bck_gensem_ce_8020_example,           # NEW — FreeSelfApp contrast
        blocks.bck_gensem_ce_five_phases,

        # Brainstorm (3 slides)
        blocks.bck_gensem_ce_brainstorm_plan,        # v1 — concept
        blocks.bck_gensem_ce_brainstorm_artifact,    # NEW — example output
        blocks.bck_gensem_ce_brainstorm_antipattern, # NEW — DON'T/DO

        # Plan (3 slides)
        blocks.bck_gensem_ce_plan_artifact,          # NEW — example plan
        blocks.bck_gensem_ce_plan_antipattern,       # NEW — vague plan anti-pattern

        # Work (2 slides)
        blocks.bck_gensem_ce_work_review,            # v1 — concept
        blocks.bck_gensem_ce_work_guardrails,        # NEW — 3 guardrails

        # Review (2 slides)
        blocks.bck_gensem_ce_review_nversion,        # NEW — n-version verification

        # Compound (3 slides)
        blocks.bck_gensem_ce_compound,               # v1 — 4 outputs
        blocks.bck_gensem_ce_compound_flywheel,      # NEW — knowledge flywheel

        # Architecture + Git (4 slides)
        blocks.bck_gensem_ce_toolsupport,
        blocks.bck_gensem_ce_git_profiles,
        blocks.bck_gensem_ce_git_mapping,            # NEW — phase-to-Git table

        # Specialization (4 slides)
        blocks.bck_gensem_ce_specialization,
        blocks.bck_gensem_ce_spec_5types,            # NEW — 5 types
        blocks.bck_gensem_ce_spec_research,          # NEW — CE as research platform

        # Orchestration + Preview (2 slides)
        blocks.bck_gensem_ce_demo_preview,

        # Exercise + Transition (3 slides)
        blocks.bck_gensem_ce_exercise_compound,      # NEW — hands-on exercise
        blocks.bck_gensem_ce_transition,

        # ═══════════════════════════════════════════════════════════════
        # PART 5 — CALCAPP v0.3 ACTIVITIES (10 blocks)
        # ═══════════════════════════════════════════════════════════════
        blocks.bck_gensem_calcapp_title,
        blocks.bck_gensem_calcapp_recap,
        blocks.bck_gensem_calcapp_v03_overview,
        blocks.bck_gensem_calcapp_fr_example,        # NEW — FR-001 full example
        blocks.bck_gensem_calcapp_nfr_example,       # NEW — NFR-002 full example
        blocks.bck_gensem_calcapp_v03_ce_mapping,
        blocks.bck_gensem_calcapp_v03_traceability,
        blocks.bck_gensem_calcapp_v03_prompts,
        blocks.bck_gensem_calcapp_discussion,        # NEW — discussion before practice
        blocks.bck_gensem_calcapp_v03_handover,

        # ═══════════════════════════════════════════════════════════════
        # PART 6 — GENSEMONE METHOD (Day 5, 15 blocks)
        # ═══════════════════════════════════════════════════════════════
        blocks.bck_gensem_day5_bridge,               # NEW — Day 5 re-entry
        blocks.bck_gensem_method_title,
        blocks.bck_gensem_method_why,
        blocks.bck_gensem_method_overview,
        blocks.bck_gensem_method_step0,
        blocks.bck_gensem_method_step0_filled,       # NEW — filled example
        blocks.bck_gensem_method_step1,
        blocks.bck_gensem_method_step1_output,       # NEW — output example
        blocks.bck_gensem_method_step2,
        blocks.bck_gensem_method_step3,
        blocks.bck_gensem_method_step4_5,
        blocks.bck_gensem_method_timeline,
        blocks.bck_gensem_method_vs_vibecoding,
        blocks.bck_gensem_method_adapt,              # NEW — customization exercise
        blocks.bck_gensem_method_fallback,           # NEW — Plan B
        blocks.bck_gensem_method_checklist,

        # ═══════════════════════════════════════════════════════════════
        # PART 7 — CE PLUGIN DEMO (Day 6, 12 blocks)
        # ═══════════════════════════════════════════════════════════════
        blocks.bck_gensem_plugin_title,
        blocks.bck_gensem_plugin_architecture,
        blocks.bck_gensem_plugin_demo_brainstorm,
        blocks.bck_gensem_plugin_demo_plan,
        blocks.bck_gensem_plugin_demo_work,
        blocks.bck_gensem_plugin_demo_review,
        blocks.bck_gensem_plugin_demo_compound,
        blocks.bck_gensem_plugin_lfg,
        blocks.bck_gensem_plugin_cursor,
        blocks.bck_gensem_plugin_sync,
        blocks.bck_gensem_plugin_exercise,           # NEW — micro-exercise
        blocks.bck_gensem_plugin_takeaway,

        # ═══════════════════════════════════════════════════════════════
        # CLOSING (2 blocks)
        # ═══════════════════════════════════════════════════════════════
        blocks.bck_gensem_glossary,
        blocks.bck_gensem_references,
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
            filename="ai4se-gensem",
            timestamp=True,
        ),
        ExportConfig(
            format="pdf",
            mode=ExportMode.MANUAL if IS_EXPORTABLE else ExportMode.NEVER,
            output_dir="./exports",
            filename="ai4se-gensem",
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
