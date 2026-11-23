"""Slide — VibeCoding to VibeEngineering spectrum: 4 levels."""
# @guideline: maximize-viewport
# @pattern: ptn_comparison_table
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
    evidence = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "spectrum_evidence",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


# Colour per row, red (level 1) → green (level 4), level 4 in the former green of the header; the header in blue,
# a colour far from the four rows (NG, 2026-11-23). Block-local: only this slide uses them.
def _tone(rgb, hexa, key):
    """Cell (tinted fill + border) and label (bold text) styles of one colour."""
    cell = Style.create(
        Style(f"background-color: rgba({rgb}, 0.15); border: 2px solid {hexa}; border-radius: 10px; "
              "padding: 8px 12px;", f"spectrum_cell_{key}")
        + s.container.layouts.vertical_center_layout + s.center_txt,
        f"spectrum_cell_{key}_c",
    )
    label = Style.create(s.project.titles.table_label + Style(f"color: {hexa};", f"spectrum_fg_{key}"),
                         f"spectrum_label_{key}")
    return cell, label


_HEADER_TONE = _tone("122, 184, 245", "#7AB8F5", "header")   # blue: apart from the red → green rows (NG, 2026-11-23)
_ROW_TONES = [
    _tone("231, 76, 60", "#E74C3C", "red"),       # 1 — Naive VibeCoding
    _tone("230, 126, 34", "#E67E22", "orange"),   # 2 — Guided
    _tone("241, 196, 15", "#F1C40F", "yellow"),   # 3 — Structured
    _tone("46, 196, 182", "#2EC4B6", "green"),    # 4 — VibeEngineering (was the header)
]

_NOTES = [
    ('The message',
     'VibeCoding and VibeEngineering are not two camps but the two ends of a spectrum: the more rigour (requirements, tests, review), the further right — and the right level depends on what the code is for.'),
    ('Reading the table',
     'Level 1 Naive VibeCoding (no requirements, no tests, no review) is fine for a personal prototype; level 4 VibeEngineering (full requirements, test-driven generation, architecture, CI/CD, systematic review) is what production needs. Levels 2 and 3 add rigour step by step.'),
    ('The trap',
     'A level-1 prototype that quietly becomes production: the demo works, so it ships, without the requirements, tests and review that level 4 assumes.'),
    ('Link to the course',
     "This afternoon's FreeSelfApp sits at level 1 on purpose; tomorrow's CalcApp aims at level 4."),
    ('Ask the room',
     '« At which level is the code you wrote with AI last month — and at which level is it used? »'),
]

# Table data: (Level, Name, Characteristics, Best For, is_active)
_HEADERS = ("L.", "Name", "Characteristics", "Best For")

_ROWS = [
    ("1", "Naive VibeCoding", "No requirements, no tests, no review", "Personal prototypes only", False),
    ("2", "Guided VibeCoding", "Informal requirements, manual evaluation", "Internal tools", False),
    ("3", "Structured VibeCoding", "Written requirements, some tests, review of critical paths", "Team projects", False),
    ("4", "VibeEngineering", "Full requirements, test-driven generation, architecture, CI/CD, systematic review", "Production", True),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "The Spectrum", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — The Spectrum", entries=_NOTES,
                                     position="left", width="50vw")
            st_space("v", "2vh")

            # Header row
            with st_zoom(105), st_grid(
                cols="6% 24% 42% 28%",
                gap="8px",
                cell_styles=_HEADER_TONE[0],
            ) as g:
                for header in _HEADERS:
                    with g.cell():
                        st_write(_HEADER_TONE[1], header)

            # Data rows
            for (level, name, characteristics, best_for, _active), (cell, name_style) in zip(_ROWS, _ROW_TONES):
                with st_zoom(105):
                    with st_grid(
                        cols="6% 24% 42% 28%",
                        gap="8px",
                        cell_styles=cell,
                    ) as g:
                        with g.cell():
                            st_write(name_style, level)
                        with g.cell():
                            st_write(name_style, name)
                        with g.cell():
                            st_write(name_style, characteristics)
                        with g.cell():
                            st_write(name_style, best_for)

            st_space("v", "2vh")
