"""Slide — TDD in one picture — red, green, refactor."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """TDD in one picture — red, green, refactor — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_tdd_cycle_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_tdd_cycle_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'TDD in One Picture', tag=t.div, toc_lvl='+1')
            with st_grid(cols='1fr 1fr', gap="24px", cell_styles=s.project.containers.grid_cell_centered) as g:
                with g.cell():
                    with st_block(s.center_txt):
                        st_image(s.none, width='100%', uri='images/pm/red_green_refactor_cycle.png')
                with g.cell():
                    with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, 'RED'), ' — write a test that fails')
                        with l.item():
                            st_write(bs.body, (bs.keyword, 'GREEN'), ' — the minimal code that passes')
                        with l.item():
                            st_write(bs.body, (bs.keyword, 'REFACTOR'), ' — clean up, tests stay green')
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        'A failing test ',
                        (bs.keyword, 'before'),
                        ' the code is the expected start, not a problem.',
                        tag=t.div,
                    )
            st_write(bs.foot, 'Code first, theory later: watch one full cycle.', tag=t.div)
