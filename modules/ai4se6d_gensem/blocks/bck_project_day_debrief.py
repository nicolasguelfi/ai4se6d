"""Slide — Day 5 debrief at 16:30: the milestone and the deployment (cycle 16) (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Day 5 debrief styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    item = s.project.titles.table_cell
    card = Style.create(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md, "day5_debrief_card")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "day5_debrief_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "Day 5 Debrief", tag=t.div, toc_lvl="+1", label="Day 5 debrief")
            with st_grid(cols="repeat(auto-fit, minmax(460px, 1fr))", gap="24px", cell_styles=bs.card) as g:
                with g.cell():
                    st_write(bs.label, "The milestone", tag=t.div)
                    with st_list(l_style=bs.item, li_style=bs.item, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.item, "Is every plan validated?")
                        with l.item(): st_write(bs.item, "What went to the backlog to hold 11:30 tomorrow?")
                        with l.item(): st_write(bs.item, "Which Gate did you change, and why?")
                with g.cell():
                    st_write(bs.label, "The deployment (cycle 16)", tag=t.div)
                    with st_list(l_style=bs.item, li_style=bs.item, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.item, "What got stuck?")
                        with l.item(): st_write(bs.item, "Build log or runtime log: where did you look first?")
                        with l.item(): st_write(bs.item, "Was the live version the one you pushed?")
            st_write(bs.foot, "Before you leave: /gse-pause, then git push --all origin.", tag=t.div)
