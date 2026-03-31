"""Slide 3 — 6-Day Journey roadmap (3 sections: D1-D2, D3-D4, D5-D6)."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# P1: viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:0.8rem;",
    "roadmap_page_fill",
)

# Cell style: background + border + vertical/horizontal centering
_today_cell_style = Style.create(
    ns("background-color: rgba(243, 156, 18, 0.15); "
       "border: 2px solid #F39C12; border-radius: 10px; "
       "padding: 8px 12px;", "today_cell_bg")
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "today_cell",
)
_normal_cell_style = Style.create(
    ns("background-color: rgba(122, 184, 245, 0.08); "
       "border: 1px solid rgba(122, 184, 245, 0.3); border-radius: 10px; "
       "padding: 8px 12px;", "normal_cell_bg")
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "normal_cell",
)


class BlockStyles:
    """Slide: Roadmap — maximize-viewport archetype: structured grid."""
    heading = s.project.titles.section_title + s.center_txt
    day_label = Style.create(
        s.project.colors.primary + s.bold + s.Large + s.text.wrap.hyphens,
        "day_label",
    )
    day_label_active = Style.create(
        s.project.colors.highlight + s.bold + s.Large + s.text.wrap.hyphens,
        "day_label_active",
    )
    session = Style.create(
        s.Large + s.text.wrap.hyphens,
        "session",
    )
    session_active = Style.create(
        s.project.colors.highlight + s.Large + s.text.wrap.hyphens,
        "session_active",
    )
bs = BlockStyles


# Day data: (day, morning_label, afternoon_label, is_today)
DAYS = [
    (1, "Fundamentals of GenAI", "VibeCoding / VibeEngineering", True),
    (2, "Mastering Cursor", "Cursor Advanced", False),
    (3, "Git + Requirements", "Iterative Improvement", False),
    (4, "Reliable AI Code", "Testing + Refactoring", False),
    (5, "Mini-project (Part 1)", "Mini-project (Part 2)", False),
    (6, "Ethics + Governance", "Presentations + Wrap-up", False),
]

# Pairs for each section
_SECTIONS = [(DAYS[0], DAYS[1]), (DAYS[2], DAYS[3]), (DAYS[4], DAYS[5])]


def _render_day(day_num, am_label, pm_label, is_today):
    """Render one day: full-width day label row + 2-column content row."""
    cell = _today_cell_style if is_today else _normal_cell_style
    day_style = bs.day_label_active if is_today else bs.day_label
    label_style = bs.session_active if is_today else bs.session

    # Row 1: Day label — full width
    with st_grid(cols="1fr", gap="12px", cell_styles=cell) as g:
        with g.cell():
            st_write(day_style, f"Day {day_num}")

    # Row 2: AM / PM — 2 columns
    with st_grid(cols="1fr 1fr", gap="12px", cell_styles=cell) as g:
        with g.cell():
            st_write(label_style, am_label)
        with g.cell():
            st_write(label_style, pm_label)


def build():
    for idx, (day_a, day_b) in enumerate(_SECTIONS):
        with st_block(_page_fill):
            with st_block(s.center_txt):
                lvl = "1" if idx == 0 else "2"
                st_write(bs.heading, "6-Day Journey", tag=t.div, toc_lvl=lvl)

                _render_day(*day_a)
                st_space("v", 4)
                _render_day(*day_b)

        if idx < len(_SECTIONS) - 1:
            st_slide_break()
