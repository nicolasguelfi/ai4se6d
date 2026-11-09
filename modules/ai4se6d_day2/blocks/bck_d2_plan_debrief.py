"""Slide — Planning debrief: share and review (5 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Debrief styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    pair = Style.create(s.project.titles.body_accent + s.center_txt, "d2_plandeb_pair")
    next_step = Style.create(s.project.titles.body + s.project.colors.highlight + s.bold + s.center_txt, "d2_plandeb_next")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Debrief — 5 min", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, "What did the plan agent ask or propose that you had not thought of?")
            with l.item(): st_write(bs.body, "Which task did you split or rewrite — and why?")
        st_space("v", 1)
        st_write(bs.pair, "Compare with your neighbour: different plans are normal. Are both testable?", tag=t.div)
        st_space("v", 1)
        st_write(bs.next_step, "11:30 — TDD on your [next] task, on its own branch.", tag=t.div)
