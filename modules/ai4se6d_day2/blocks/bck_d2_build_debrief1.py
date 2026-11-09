"""Slide — Debrief — Part 1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Debrief — Part 1 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_debrief1_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_debrief1_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "d2_build_debrief1_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Debrief — Part 1 (5 min)', tag=t.div, toc_lvl='+1')
            st_write(bs.timer, '12:10 → 12:15', tag=t.div)
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Did the agent respect “test only”? If not, what did you do?')
                with l.item():
                    st_write(bs.body, 'Did your mutant check reveal a test that proved nothing?')
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    'Compare with your neighbour: show each other your ',
                    (bs.cmd, 'git log --oneline'),
                    '.',
                )
