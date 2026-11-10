"""Slide — Lunch break."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Lunch break — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "build_lunch_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "build_lunch_subtitle")
    body_center = Style.create(s.project.titles.body + s.center_txt, "build_lunch_body_c")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_lunch_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_lunch_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, 'Lunch', tag=t.div, toc_lvl="1", label='Lunch (12:15)')
            st_space("v", 1)
            st_write(bs.subtitle, 'Back at 13:15 sharp — re-orientation first', tag=t.div)
            st_space("v", 2)
            st_write(bs.timer, '12:15 → 13:15', tag=t.div)
            st_space("v", 1)
            st_write(
                bs.body_center,
                'Before you leave: ',
                (bs.cmd, 'git status'),
                ' must say ',
                (bs.keyword, 'nothing to commit'),
                '.',
                tag=t.div,
            )
