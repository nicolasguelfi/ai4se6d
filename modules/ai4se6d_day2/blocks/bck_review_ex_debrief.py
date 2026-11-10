"""Slide — Debrief — review practice."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Debrief — review practice — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_debrief_body")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_ex_debrief_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Debrief — Review (10 min)', tag=t.div, toc_lvl='+1')
            st_write(bs.timer, '16:05 → 16:15', tag=t.div)
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Most useful finding? What obvious problem did the AI miss?')
                with l.item():
                    st_write(bs.body, 'What did you refuse, and why?')
            with st_block(s.project.containers.callout):
                st_write(bs.body, 'Compare with your neighbour: similar code, similar findings? Why not?')
