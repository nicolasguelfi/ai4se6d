"""Slide — VibeCoding to VibeEngineering spectrum: 4 levels."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_vibeeng_spectrum",
)

# Cell styles
_normal_cell = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "spectrum_normal_cell",
)

_active_cell = Style.create(
    s.project.containers.cell_active_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "spectrum_active_cell",
)

_header_cell = Style.create(
    s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "spectrum_header_cell",
)


class BlockStyles:
    """Spectrum slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    header_text = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "spectrum_header_text",
    )
    cell_text = Style.create(
        s.text.sizes.pt36 + s.text.wrap.hyphens,
        "spectrum_cell_text",
    )
    level_name = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "spectrum_level_name",
    )
    level_active = Style.create(
        s.text.sizes.pt36 + s.bold + s.project.colors.highlight + s.text.wrap.hyphens,
        "spectrum_level_active",
    )
    evidence = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "spectrum_evidence",
    )
    source = s.project.titles.caption + s.center_txt
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
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Spectrum", tag=t.div, toc_lvl="1")

            # Header row
            with st_grid(
                cols="8% 22% 40% 30%",
                gap="8px",
                cell_styles=_header_cell,
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(bs.header_text, header)

            # Data rows
            for level, name, characteristics, best_for, is_active in _ROWS:
                cell = _active_cell if is_active else _normal_cell
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
            st_write(bs.evidence, "FlowGen: 15% fewer code smells with structured processes")
            st_write(bs.source, "80/20 rule: 80% effort in planning/review, 20% in execution")
