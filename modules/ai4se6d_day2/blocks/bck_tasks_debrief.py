"""Slide — Debrief — Part 2."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Debrief — Part 2 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_debrief_body")
    timer = Style.create(s.project.titles.stat + s.center_txt, "tasks_debrief_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Debrief — Part 2 (10 min)', tag=t.div, toc_lvl='+1')
            st_write(bs.timer, '14:20 → 14:30', tag=t.div)
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Where did the agent change a test, or do more than you asked?')
                with l.item():
                    st_write(bs.body, 'Which review-checklist item caught something real?')
            with st_block(s.project.containers.callout):
                st_write(bs.body, 'Compare with your neighbour: same task, same code? Why not?')
