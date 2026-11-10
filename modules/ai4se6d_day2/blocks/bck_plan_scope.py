"""Slide — v0.1 scope today, the rest later."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Scope styles."""
    heading = s.project.titles.heading
    card_title = s.project.titles.subtitle
    text = s.project.titles.table_cell
    ask = Style.create(s.project.titles.body_accent + s.center_txt, "scope_ask")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "v0.1 Today, the Rest Later", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(cols=s.project.containers.responsive_2col, grid_style=s.project.containers.gap_24) as g:
            with g.cell():
                with st_block(s.project.containers.cell_active_bg + s.project.containers.cell_pad_md):
                    st_write(bs.card_title, "v0.1 — today", tag=t.div)
                    with st_list(l_style=bs.text, li_style=bs.text, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.text, "Add an expense, with validation")
                        with l.item(): st_write(bs.text, "List expenses with a monthly total")
                        with l.item(): st_write(bs.text, "Two pages and a navigation bar")
                        with l.item(): st_write(bs.text, "Data kept in the browser (localStorage)")
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                    st_write(bs.card_title, "Later versions", tag=t.div)
                    with st_list(l_style=bs.text, li_style=bs.text, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.text, "Budgets per category")
                        with l.item(): st_write(bs.text, "Remaining budget and warnings")
                        with l.item(): st_write(bs.text, "Your own ideas")
        st_space("v", 1)
        st_write(bs.ask, "2 minutes, on paper: 2-3 features you would want as a user.", tag=t.div)
