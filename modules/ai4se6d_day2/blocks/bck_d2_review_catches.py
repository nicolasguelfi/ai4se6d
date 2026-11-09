"""Slide — What AI review catches well and what it misses."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """What AI review catches well and what it misses — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_review_catches_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_review_catches_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'What AI Review Sees and Misses', tag=t.div, toc_lvl='+1')
            with st_grid(cols='1fr 1fr', gap="24px", cell_styles=s.project.containers.cell_pad_sm) as g:
                with g.cell():
                    st_write(bs.label, 'Catches well — breadth', tag=t.div)
                    with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                        with l.item():
                            st_write(bs.body, 'Missing error handling')
                        with l.item():
                            st_write(bs.body, 'null / undefined risks')
                        with l.item():
                            st_write(bs.body, 'Type slips, dead code')
                        with l.item():
                            st_write(bs.body, 'Hook dependency mistakes')
                        with l.item():
                            st_write(bs.body, 'Known security anti-patterns')
                with g.cell():
                    st_write(bs.label, 'Misses — depth: you', tag=t.div)
                    with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                        with l.item():
                            st_write(bs.body, 'Does it do what the ', (bs.keyword, 'user'), ' needs?')
                        with l.item():
                            st_write(bs.body, 'Is this the right place in the design?')
                        with l.item():
                            st_write(bs.body, 'Effects across distant files')
                        with l.item():
                            st_write(bs.body, 'Subtle authorization rules')
                        with l.item():
                            st_write(bs.body, 'Should this code exist at all?')
            st_write(bs.foot, 'AI = breadth, you = depth. Neither alone is enough.', tag=t.div)
