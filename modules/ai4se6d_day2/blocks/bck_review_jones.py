"""Slide — Formal inspection vs testing — defect removal efficiency."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Formal inspection vs testing — defect removal efficiency — styles."""
    heading = s.project.titles.heading
    body_center = Style.create(s.project.titles.body + s.center_txt, "review_jones_body_c")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_jones_foot")
    source = s.project.citation + s.large + s.center_txt
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "review_jones_th")
    table_txt = Style.create(s.project.titles.table_cell + s.center_txt, "review_jones_td")
    table_lbl = Style.create(s.project.titles.table_label + s.center_txt, "review_jones_tl")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, 'Review vs Tests', tag=t.div, toc_lvl='+1')
            with st_grid(cols='40% 25% 25%', gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, 'Practice')
                with g.cell():
                    st_write(bs.table_hdr, 'Minimum')
                with g.cell():
                    st_write(bs.table_hdr, 'Average')
            with st_grid(cols='40% 25% 25%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'Formal code inspection')
                with g.cell():
                    st_write(bs.table_txt, '60%')
                with g.cell():
                    st_write(bs.table_txt, '85%')
            with st_grid(cols='40% 25% 25%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'Unit testing (automated)')
                with g.cell():
                    st_write(bs.table_txt, '20%')
                with g.cell():
                    st_write(bs.table_txt, '40%')
            with st_grid(cols='40% 25% 25%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'Function testing')
                with g.cell():
                    st_write(bs.table_txt, '33%')
                with g.cell():
                    st_write(bs.table_txt, '40%')
            st_write(
                bs.body_center,
                'Share of the defects present that each practice removes (data from 13,000+ projects).',
                tag=t.div,
            )
            st_write(bs.source, cite('jones-dre2011'), tag=t.div)
            st_write(bs.foot, 'Not tests OR review: you need both — today you did both.', tag=t.div)
