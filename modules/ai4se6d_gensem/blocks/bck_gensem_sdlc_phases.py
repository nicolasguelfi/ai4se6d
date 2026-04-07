"""Slide — SDLC phases impact: 6 phases with GenAI impact (transposed table)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """SDLC phases impact table styles."""
    heading = s.project.titles.slide_title + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_PHASES = [
    ("Requirements Engineering", "GPT-dominated generation of user stories, acceptance criteria, and Gherkin specs", "67.3% GPT"),
    ("Architecture & Design", "AI-assisted design decisions, pattern selection, and trade-off analysis", "38% of studies"),
    ("Code Generation", "Three paradigms: completion, chat-based, agentic autonomous coding", "3 paradigms"),
    ("Testing", "Automated test generation, mutation testing, property-based testing with LLMs", "15% improvement"),
    ("Maintenance", "Bug localization, refactoring suggestions, documentation generation", "26 challenges"),
    ("Deployment", "Agentic DevOps: AI agents managing CI/CD pipelines and infrastructure", "Emerging"),
]

_HEADERS = ("Phase", "GenAI Impact", "Key Stat")

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "GenAI Impact Across SDLC Phases", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        # Header row
        with st_grid(
            cols="20% 55% 25%",
            gap="8px",
            cell_styles=s.project.containers.table_header_cell,
        ) as g:
            for header in _HEADERS:
                with g.cell():
                    st_write(s.project.titles.table_header, header)

        # Data rows
        for name, description, stat in _PHASES:
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

        st_space("v", 1)
        st_write(bs.source, cite("soen101-2024"))
