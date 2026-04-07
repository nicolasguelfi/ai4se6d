"""Slide — VibeCoding to VibeEngineering spectrum: 4 levels."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Spectrum slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    level_name = s.project.titles.table_label
    level_active = s.project.titles.table_label_active
    evidence = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "spectrum_evidence",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

# Table data: (Level, Name, Characteristics, Best For, is_active)
_HEADERS = ("Level", "Name", "Characteristics", "Best For")

_ROWS = [
    ("1", "Naive VibeCoding", "No requirements, no tests, no review", "Personal prototypes only", False),
    ("2", "Guided VibeCoding", "Informal requirements, manual evaluation", "Internal tools", False),
    ("3", "Structured VibeCoding", "Written requirements, some tests, review of critical paths", "Team projects", False),
    ("4", "VibeEngineering", "Full requirements, TDD, architecture, CI/CD, systematic review", "Production", True),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Spectrum", tag=t.div, toc_lvl="1")

            # Header row
            with st_grid(
                cols="8% 22% 40% 30%",
                gap="8px",
                cell_styles=s.project.containers.table_header_cell,
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)

            # Data rows
            for level, name, characteristics, best_for, is_active in _ROWS:
                cell = s.project.containers.table_active_cell if is_active else s.project.containers.table_normal_cell
                name_style = bs.level_active if is_active else bs.level_name
                with st_grid(
                    cols="8% 22% 40% 30%",
                    gap="8px",
                    cell_styles=cell,
                ) as g:
                    with g.cell():
                        st_write(name_style, level)
                    with g.cell():
                        st_write(name_style, name)
                    with g.cell():
                        st_write(bs.cell_text, characteristics)
                    with g.cell():
                        st_write(bs.cell_text, best_for)

            st_space("v", 1)
            # REF: https://arxiv.org/abs/2403.15852
            st_write(bs.source, cite("qian2024soen101"))
            st_write(bs.evidence, "FlowGen: 15% fewer code smells with structured processes")
            st_write(bs.source, "Planning/review 80% — execution 20%")
            # REF: xiao-longitudinal2025 (observation), compound-engineering (prescription)
            st_write(bs.source, cite("xiao-longitudinal2025"))
