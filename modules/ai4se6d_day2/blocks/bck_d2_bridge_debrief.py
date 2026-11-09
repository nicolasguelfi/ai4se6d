"""Slide — Debrief — the whole day."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Debrief — the whole day — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_bridge_debrief_body")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Debrief — the Day (10 min)', tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Which step of the loop did you skip or rush? What did it cost you?')
                with l.item():
                    st_write(bs.body, 'Which step would you hand to a tool — and which must stay yours?')
            with st_block(s.project.containers.callout):
                st_write(bs.body, 'Compare with your neighbour, then 2-3 answers for the room.')
