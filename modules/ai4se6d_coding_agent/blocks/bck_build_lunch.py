"""Slide — Lunch break."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Lunch break — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "build_lunch_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "build_lunch_subtitle")
    body_center = Style.create(s.project.titles.body + s.center_txt, "build_lunch_body_c")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_lunch_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_lunch_timer")
bs = BlockStyles


_NOTES = [
    ("The message",
     "One hour of lunch, and a clean repository before leaving: git status must say « nothing to commit »."),
    ("Why a clean status",
     "Everything done this morning is then saved in a commit. After lunch, nobody wonders which change was half "
     "finished, and the re-orientation checks start from a known state."),
    ("Back at 13:15 sharp",
     "The afternoon opens with a 5-minute re-orientation: git status clean on mywork, Part 1 tests green, the app "
     "renders, the next task of the plan."),
    ("Ask the room",
     "« Who has uncommitted changes right now? » — fix it before leaving the room."),
]


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            # title and « i » on the same line (NG, 2026-11-23: same recipes as the intro module)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell():
                    st_write(bs.title, 'Lunch', tag=t.div, toc_lvl="1", label='Lunch (12:15)')
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — Lunch", entries=_NOTES,
                                     position="left", width="50vw")
            st_space("v", 2)
            with st_zoom(130):
                st_write(bs.subtitle, 'Back at 13:15 sharp — re-orientation first', tag=t.div)
                st_space("v", 2)
                st_write(bs.timer, '12:15 → 13:15', tag=t.div)
                st_space("v", 2)
                st_write(
                    bs.body_center,
                    'Before you leave: ',
                    (bs.cmd, 'git status'),
                    ' must say ',
                    (bs.keyword, 'nothing to commit'),
                    '.',
                    tag=t.div,
                )
