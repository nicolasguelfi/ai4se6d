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

_doc_version = tomllib.loads(
    (Path(__file__).parent.parent.parent / "pyproject.toml").read_text()
).get("project", {}).get("version", "?")
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
    page_title="GSE-One — Generative Software Engineering",
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
    title="GSE-One — Generative Software Engineering",
    aspect_ratio="16/9",
    footer=True,
    center_content=False,
    hide_streamlit_header=False,
    enforce_ratio=False,
))

# Slide breaks
set_slide_break_config(SlideBreakConfig(
    mode=SlideBreakMode.FULL,
    space="1vh",
    space_before="30vh",
    rule_margin_top="1vh",
    rule_margin_bottom="1vh",
    marker_hidden=False,
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
    auto_marker_on_toc=0,
    next_keys=["PageDown", "ArrowRight"],
    prev_keys=["PageUp", "ArrowLeft"],
    draggable=True,
    collapsible=True,
)

# Bibliography
set_bib_config(BibConfig(
    format=BibFormat.APA,
    citation_style=CitationStyle.AUTHOR_YEAR,
    hover_enabled=True,
    hover_show_abstract=True,
    sort_by="author",
))

# ── Orchestrate slides ──────────────────────────────────────────────
st_book(
    [
        # ═══════════════════════════════════════════════════════════════
        # SESSION 1 — "Why a method? From chaos to discipline"
        # ═══════════════════════════════════════════════════════════════

        # ── Opening ─────────────────────────────────────────────────
        blocks.bck_gensem_title,                    # Module hero title
        blocks.bck_gensem_objectives,               # 5 learning objectives (Bloom)
        blocks.bck_gensem_day1_recall,              # Days 1-2 recall bridge

        # ── T1 Séq 1.1 — The SDLC Transformed ─────────────────────
        blocks.bck_gensem_sdlc_title,               # GSE-One promo video
        ## ── P1 — Practice: Free Discovery of GSE-One ──────────────
        blocks.bck_gensem_practice_p1,              # Briefing + Timer + Debrief (3 slides)
        blocks.bck_gensem_sdlc_gravity,             # Shifting Center of Gravity
        blocks.bck_gensem_sdlc_15tasks,             # NEW / ELEVATED / TRANSFORMED (4 slides)
        blocks.bck_gensem_sdlc_spectrum,            # 4 levels: VibeCoding → VibeEngineering
        blocks.bck_gensem_sdlc_orchestrator,        # Implementer → Orchestrator + 3 pillars
        blocks.bck_gensem_sdlc_paradigms,           # RE + Testing + 3 Paradigms → GSE-One
        blocks.bck_gensem_sdlc_phases,              # 6 SDLC phases × GenAI impact
        blocks.bck_gensem_sdlc_evidence,            # Tool alone vs Tool + Process

        # ── T1 Séq 1.2 — Empirical Evidence ───────────────────────
        blocks.bck_gensem_evidence_rcts,            # The Productivity Paradox (synthesis image)
        blocks.bck_gensem_evidence_perception,      # Perception vs Reality gap
        blocks.bck_gensem_evidence_enterprise,      # 10%/25-30% + Fowler + Junior/Senior (3 slides)
        #blocks.bck_gensem_evidence_synthesis,        # 3 takeaways + Homogenization (2 slides)

        # ── T1 Séq 1.3 — Risks ────────────────────────────────────
        blocks.bck_gensem_risks,                    # 6 risk cards + More AI ≠ fix + Gap (3 slides)

        # ── T1 Séq 1.4 — Methodological Frameworks ────────────────
        blocks.bck_gensem_fw_landscape,             # 3 categories overview
        blocks.bck_gensem_fw_agilegen,              # AgileGen (Zhang 2025)
        blocks.bck_gensem_fw_agenticdevops,         # Agentic DevOps (Microsoft)
        blocks.bck_gensem_fw_se30,                  # SE 3.0 (Hassan) — 5 characteristics
        blocks.bck_gensem_fw_vbounce,               # V-Bounce (Hymel 2024)
        blocks.bck_gensem_fw_promptware,            # Promptware Engineering (Chen 2025)
        blocks.bck_gensem_fw_synthesis,             # Comparison table (8 frameworks)
        blocks.bck_gensem_roadmap,                  # Enterprise roadmap 2025-2030
        blocks.bck_gensem_sota_takeaway,            # 3 takeaways → GSE-One transition

        # ── P1 — Practice: Free Discovery of GSE-One ──────────────
        blocks.bck_gensem_practice_p1,              # Briefing + Timer + Debrief (3 slides)

        # ═══════════════════════════════════════════════════════════════
        # SESSION 2 — "Discover and plan before building"
        # ═══════════════════════════════════════════════════════════════

        # ── T2 Séq 2.1 — Philosophy & 80/20 ───────────────────────
        blocks.bck_gensem_ce_philosophy,            # 80/20 rule + artifact-driven composition
        blocks.bck_gensem_ce_8020_example,          # FreeSelfApp Day 1 recall
        blocks.bck_gensem_method_vs_vibecoding,     # GSE-One vs VibeCoding comparison

        blocks.bck_gensem_t2_agile_bridge,         # Agile → GSE-One concept mapping

        # ── T2 Séq 2.2 — Lifecycle & HUG ──────────────────────────
        blocks.bck_gensem_t2_cmd_hug,               # /gse:hug — 13-dimension user profile
        blocks.bck_gensem_t2_philosophy,            # 6 Principles + Lifecycle + HUG + 3 Modes + GPS/Map (6 slides)
        blocks.bck_gensem_ce_five_phases,           # 5-phase CE lifecycle hero image

        # ── T2 Séq 2.3 — Commands & Agents ────────────────────────
        blocks.bck_gensem_t2_commands,              # 23 commands + 9 agents + .gse/ + Session (4 slides)
        blocks.bck_gensem_t2_cmd_go,                # /gse:go — The Single Entry Point
        blocks.bck_gensem_t2_cmd_status,            # /gse:status — Where Am I?
        blocks.bck_gensem_t2_cmd_pause_resume,      # /gse:pause + /gse:resume — Session continuity
        blocks.bck_gensem_t2_cmd_task,              # /gse:task — Ad-hoc work & spikes
        blocks.bck_gensem_t2_cmd_backlog,           # /gse:backlog — Unified work items

        # ── P2 — Debriefing + Exploration .gse/ ───────────────────
        blocks.bck_gensem_practice_p2,

        # ── T3 Séq 3.1-3.2 — COLLECT + ASSESS ────────────────────
        blocks.bck_gensem_t3_discovery,             # COLLECT + ASSESS + PLAN + Worktrees (4 slides)
        blocks.bck_gensem_t3_cmd_collect,           # /gse:collect — What Do We Have?
        blocks.bck_gensem_t3_cmd_assess,            # /gse:assess — What Is Missing?

        # ── T3 Séq 3.3 — PLAN deep-dive ───────────────────────────
        blocks.bck_gensem_ce_brainstorm_plan,       # Brainstorm & Plan phases detail
        blocks.bck_gensem_t3_cmd_plan,              # /gse:plan — Plan at Every Level
        blocks.bck_gensem_ce_plan_antipattern,      # Plan = contract DON'T/DO
        blocks.bck_gensem_ce_plan_artifact,         # plan.md example with tasks
        blocks.bck_gensem_t3_frontmatter,           # YAML frontmatter: traceability in practice

        # ── T3 Séq 3.4 — Worktrees & Git ──────────────────────────
        blocks.bck_gensem_ce_git_profiles,          # 3 Git workflow profiles
        blocks.bck_gensem_ce_git_mapping,           # Phase → git operation mapping

        # ── P3 — Sprint Planning on CalcApp ────────────────────────
        blocks.bck_gensem_practice_p3,

        # ── T4 — Decisions, Risks & AI Integrity ──────────────────
        blocks.bck_gensem_t4_decisions,             # P7 + P8 + P11 + P15-P16 + P4 + P13 (6 slides)

        # ── P4 — Decision Classification ───────────────────────────
        blocks.bck_gensem_practice_p4,

        # ═══════════════════════════════════════════════════════════════
        # SESSION 3 — "Build with discipline"
        # ═══════════════════════════════════════════════════════════════

        # # ── T5 Séq 5.1 — Requirements ─────────────────────────────
        # blocks.bck_gensem_t5_requirements,          # REQS + DESIGN + PREVIEW + Traceability (3 slides)
        # blocks.bck_gensem_t5_cmd_reqs,              # /gse:reqs — What Should It Do?
        # blocks.bck_gensem_t5_cmd_design,            # /gse:design — How Should It Work?
        # blocks.bck_gensem_calcapp_fr_example,       # FR-001 full Given/When/Then example
        # blocks.bck_gensem_calcapp_nfr_example,      # NFR-002 WCAG accessibility example

        # # ── T5 Séq 5.2 — Preview ──────────────────────────────────
        # blocks.bck_gensem_t5_cmd_preview,           # /gse:preview — See before building

        # # ── T5 Séq 5.4 — Traceability ─────────────────────────────
        # blocks.bck_gensem_calcapp_v03_traceability, # Traceability chain + 78 tests
        # blocks.bck_gensem_calcapp_v03_prompts,      # Good vs Bad prompting strategy

        # # ── P5 — Requirements & Design on CalcApp ──────────────────
        # blocks.bck_gensem_practice_p5,

        # # ── T6 Séq 6.1-6.2 — PRODUCE + TESTS ─────────────────────
        # blocks.bck_gensem_t6_engineering,           # PRODUCE + TESTS + REVIEW + FIX (5 slides)
        # blocks.bck_gensem_t6_cmd_tests,             # /gse:tests — How Do We Verify?
        # blocks.bck_gensem_t6_cmd_produce,           # /gse:produce — Build It Right
        # blocks.bck_gensem_ce_work_guardrails,       # Scope enforcement + test-first

        # # ── T6 Séq 6.3 — REVIEW ───────────────────────────────────
        # blocks.bck_gensem_ce_review_nversion,       # N-version verification analogy
        # blocks.bck_gensem_t6_cmd_review,            # /gse:review — Challenge Everything
        # blocks.bck_gensem_t6_cmd_fix,               # /gse:fix — Fix What Was Found

        # # ── P6 — Produce + Test + Review on CalcApp ────────────────
        # blocks.bck_gensem_practice_p6,

        # ═══════════════════════════════════════════════════════════════
        # SESSION 4 — "Deliver, capitalize and master"
        # ═══════════════════════════════════════════════════════════════

        # # ── T7 Séq 7.1-7.2 — DELIVER + COMPOUND ───────────────────
        # blocks.bck_gensem_t7_delivery,              # DELIVER + COMPOUND + INTEGRATE (3 slides)
        # blocks.bck_gensem_t7_cmd_deliver,           # /gse:deliver — Ship the Sprint
        # blocks.bck_gensem_t7_cmd_health,            # /gse:health — 8-dimension dashboard
        # blocks.bck_gensem_ce_compound,              # 4 compound outputs detail
        # blocks.bck_gensem_ce_compound_flywheel,     # Knowledge flywheel progression
        # blocks.bck_gensem_t7_cmd_compound,          # /gse:compound — What Did We Learn?
        # blocks.bck_gensem_t7_cmd_integrate,         # /gse:integrate — Make It Stick
        # blocks.bck_gensem_t7_cmd_deploy,            # /gse:deploy — From zero to live

        # # ── P7 — Full Cycle on CalcApp ─────────────────────────────
        # blocks.bck_gensem_practice_p7,

        # # ── T8 Séq 8.1 — Plugin & Cross-Tool ──────────────────────
        # blocks.bck_gensem_t8_advanced,              # Cross-tool + Learning + Project prep (3 slides)
        # blocks.bck_gensem_t8_cmd_learn,             # /gse:learn — 3 modes + competency map (2 slides)
        # blocks.bck_gensem_plugin_architecture,      # Plugin structure + 4 components
        # blocks.bck_gensem_plugin_cursor,            # Claude Code vs Cursor comparison

        # # ── T8 Séq 8.2 — Specializations ──────────────────────────
        # blocks.bck_gensem_ce_specialization,        # Making GSE-One your own
        # blocks.bck_gensem_ce_spec_5types,           # 5 types of specialization

        # # ── T8 Séq 8.3 — Frameworks positioning ───────────────────
        # blocks.bck_gensem_frameworks,               # Gaps + Comparison + Roadmap + Takeaways (5 slides)

        # # ── T8 Séq 8.4 — Project Preparation ──────────────────────
        # blocks.bck_gensem_t8_modes,                 # 3 modes comparison table (Micro/Lightweight/Full)

        # # ── P8 — Autonomous Sprint ─────────────────────────────────
        # blocks.bck_gensem_practice_p8,              # Feature selection + Go! (2 slides)

        # # ── Closing ────────────────────────────────────────────────
        # blocks.bck_gensem_method_checklist,         # Quick reference checklist
        # blocks.bck_gensem_glossary,                 # 37+ terms glossary
        # blocks.bck_gensem_references,               # Auto bibliography
    ],
    toc_config=toc,
    marker_config=marker_config,
    paginate=True,
    banner=BannerConfig.hidden(),
    page_width=90,
    zoom=80,
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
