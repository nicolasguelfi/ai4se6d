"""Slide — Afternoon break."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Afternoon break — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "d2_review_break_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "d2_review_break_subtitle")
    timer = Style.create(s.project.titles.stat + s.center_txt, "d2_review_break_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, 'Break', tag=t.div, toc_lvl="1", label='Break (15:00)')
            st_space("v", 1)
            st_write(bs.subtitle, "Next: you review today's diff", tag=t.div)
            st_space("v", 2)
            st_write(bs.timer, '15:00 → 15:15', tag=t.div)
