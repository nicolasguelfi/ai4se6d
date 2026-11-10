"""Slide — Section — AI-assisted code review."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Section — AI-assisted code review — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "review_title_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "review_title_subtitle")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_title_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, 'AI-Assisted Code Review', tag=t.div, toc_lvl="1")
            st_space("v", 1)
            st_write(bs.subtitle, 'Your code works. Is it good? How do you know?', tag=t.div)
            st_space("v", 2)
            st_write(bs.timer, '14:30 · 30 min', tag=t.div)
