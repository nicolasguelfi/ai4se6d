"""Slides — SDLC phases impact: 6 phases with GenAI impact split into 2 slides of 3."""
# @guideline: minimalist-visual + maximize-viewport
from multiprocessing.context import set_spawning_popen
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """SDLC phases impact table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_PHASES = [
    ("Requirements Engineering", "GPT-dominated generation of user stories, acceptance criteria, and Gherkin specs", "67.3% GPT"),
    ("Architecture & Design", "AI-assisted design decisions, pattern selection, and trade-off analysis", "Is the focus of 38% of GenAI studies"),
    ("Code Generation", "Three paradigms: completion, chat-based, agentic autonomous coding", "3 paradigms"),
    ("Testing", "Automated test generation, mutation testing, property-based testing with LLMs", "15% improvement"),
    ("Maintenance", "Bug localization, refactoring suggestions, documentation generation", "less mature"),
    ("Deployment", "Agentic DevOps: AI agents managing CI/CD pipelines and infrastructure", "Emerging"),
]

_HEADERS = ("Phase", "GenAI Impact", "Keys")

def _render_table(phases):
    """Render a header row + data rows for a subset of phases."""
    with st_grid(
        cols="20% 55% 25%",
        gap="8px",
        cell_styles=s.project.containers.table_header_cell,
    ) as g:
        for header in _HEADERS:
            with g.cell():
                st_write(s.project.titles.table_header, header)

    for name, description, stat in phases:
        with st_grid(
            cols="20% 55% 25%",
            gap="8px",
            cell_styles=s.project.containers.table_normal_cell,
        ) as g:
            with g.cell():
                st_write(s.project.titles.table_label, name)
            with g.cell():
                st_write(s.project.titles.table_cell, description)
            with g.cell():
                st_write(s.project.titles.table_label_active, stat)


def build():

    tt_entries=[
                ("6 phases covered", "Requirements, Architecture, Code Generation, Testing, Maintenance, and Deployment — each with distinct AI impact patterns."),
                ("Methodology", "Based on systematic literature review of GenAI applications across the full software development lifecycle."),
                ("Key insight", "Code generation gets the most attention but requirements engineering (67.3% GPT) and testing show the highest structured impact."),
                ("GSE-One link", "Understanding phase-specific impact helps design process that leverages AI where it actually helps most."),
            ]

    st_slide_break(marker_label="GenAI Impact Across SDLC (1/2)")

    # ── Slide 1: Requirements, Architecture, Code Generation ───────
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "GenAI Impact Across SDLC (1/2)", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="GenAI Impact Across SDLC Phases",
                        entries=tt_entries,
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

        with st_zoom(90):
            _render_table(_PHASES[:3])
            st_space("v", 1)
            st_write(bs.source, cite("soen101-2024"), "  ", cite("esposito-architecture2025"))

    st_slide_break(marker_label="GenAI Impact Across SDLC (2/2)")

    # ── Slide 2: Testing, Maintenance, Deployment ──────────────────
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "GenAI Impact Across SDLC (2/2)", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="GenAI Impact Across SDLC Phases",
                        entries=tt_entries,
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)
        with st_zoom(90):
            _render_table(_PHASES[3:])
            st_space("v", 1)
            st_write(bs.source, cite("soen101-2024"), "  ", cite("gao-maintenance2025"), "  ", cite("esposito-architecture2025"))

    st_space("v", "30vh")