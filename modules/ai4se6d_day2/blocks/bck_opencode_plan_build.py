"""Slide — Plan agent vs build agent (Tab)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Plan/build styles."""
    heading = s.project.titles.heading
    card_title = s.project.titles.subtitle
    text = s.project.titles.table_cell
    keyword = s.project.titles.table_label
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "pb_closing")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Plan Agent, Then Build Agent", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(cols=s.project.containers.responsive_2col, grid_style=s.project.containers.gap_24) as g:
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                    st_write(bs.card_title, "plan — think", tag=t.div)
                    with st_list(l_style=bs.text, li_style=bs.text, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.text, "Reads, analyses, proposes")
                        with l.item(): st_write(bs.text, "Can ask you questions")
                        with l.item(): st_write(bs.text, "Does not edit your files")
            with g.cell():
                with st_block(s.project.containers.cell_active_bg + s.project.containers.cell_pad_md):
                    st_write(bs.card_title, "build — do", tag=t.div)
                    with st_list(l_style=bs.text, li_style=bs.text, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.text, "All tools enabled")
                        with l.item(): st_write(bs.text, "Edits files, runs commands")
                        with l.item(): st_write(bs.text, "Follows the plan you approved")
        st_space("v", 1)
        st_write(bs.closing, "Press Tab to switch agents: opencode shows which one is active.", tag=t.div)
