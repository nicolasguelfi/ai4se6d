"""Slide — Section — CalcApp v0.1 Part 1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Section — CalcApp v0.1 Part 1 — styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "d2_build_title_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "d2_build_title_subtitle")
    timer = Style.create(s.project.titles.stat + s.center_txt, "d2_build_title_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_title_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, 'CalcApp v0.1 — Part 1', tag=t.div, toc_lvl="1", label='CalcApp v0.1 — Part 1 (test first)')
            st_space("v", 1)
            st_write(bs.subtitle, 'Test-first development with an agent', tag=t.div)
            st_space("v", 2)
            st_write(bs.timer, '11:30 · 45 min', tag=t.div)
            st_write(bs.subtitle, 'demo 15 · practice 11:45 → 12:10 · debrief 5', tag=t.div)
            st_space("v", 1)
            st_write(bs.foot, 'You have a plan. Now build it — one task at a time.', tag=t.div)
