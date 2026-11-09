"""Slide — Section — CalcApp v0.1 Part 2."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Section — CalcApp v0.1 Part 2 — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "d2_build_p2_title_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "d2_build_p2_title_subtitle")
    timer = Style.create(s.project.titles.stat + s.center_txt, "d2_build_p2_title_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, 'CalcApp v0.1 — Part 2', tag=t.div, toc_lvl="1", label='CalcApp v0.1 — Part 2 (routing, data, UI)')
            st_space("v", 1)
            st_write(bs.subtitle, 'Routing, data layer, minimal UI — driven by your plan', tag=t.div)
            st_space("v", 2)
            st_write(bs.timer, '13:15 · 75 min', tag=t.div)
