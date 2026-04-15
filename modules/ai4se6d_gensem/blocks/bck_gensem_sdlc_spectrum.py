"""Slide — VibeCoding to Generative SE spectrum: 4 maturity levels."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Spectrum slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = s.project.titles.table_header
    cell_text = s.project.titles.table_cell
    level_name = s.project.titles.table_label
    level_active = s.project.titles.table_label_active
    message = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_spectrum_message",
    )
bs = BlockStyles

_HEADERS = ("Level", "Name", "Characteristics", "Best For")

_ROWS = [
    ("1", "VibeCoding", "No req/tests/review", "Personal prototypes", False),
    ("2", "Guided VibeCoding", "Informal req, manual eval", "Internal tools", False),
    ("3", "VibeEngineering", "Full RE + TDD + CI/CD", "Production code", False),
    ("4", "Generative SE", "Lifecycle + risk gov. + capitalization", "Professional engineering", True),
]

def build():
    st_marker("VibeCoding → Generative SE Spectrum")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "The Spectrum", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="VibeCoding to Generative SE Spectrum",
                        entries=[
                            ("4 maturity levels", "From naive prompt-and-pray (Level 1) to Generative Software Engineering as a full discipline (Level 4)."),
                            ("Key differentiator", "Each level adds process rigor: requirements, testing, review, lifecycle, risk governance, knowledge capitalization."),
                            ("Level 3 vs 4", "VibeEngineering (Level 3) reintroduces RE + TDD + CI/CD. Generative SE (Level 4) adds lifecycle management, risk governance, and knowledge capitalization."),
                            ("Course objective", "This training teaches Level 4: Generative SE as a discipline — using GSE-One as the methodology to practice it."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )

        with st_zoom(110):
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

            st_space("v", 2)
            st_write(bs.message, "This training teaches Level 4 \u2014 using GSE-One as your first Generative SE methodology.")
