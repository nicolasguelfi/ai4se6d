"""Slide — Triage findings — HIGH / MEDIUM / LOW."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Triage findings — HIGH / MEDIUM / LOW — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_review_triage_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_review_triage_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_review_triage_foot")
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "d2_review_triage_th")
    table_txt = Style.create(s.project.titles.table_cell + s.center_txt, "d2_review_triage_td")
    table_lbl = Style.create(s.project.titles.table_label + s.center_txt, "d2_review_triage_tl")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Triage: HIGH / MEDIUM / LOW', tag=t.div, toc_lvl='+1')
            with st_grid(cols='18% 42% 30%', gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, 'Severity')
                with g.cell():
                    st_write(bs.table_hdr, 'Typical finding')
                with g.cell():
                    st_write(bs.table_hdr, 'Action')
            with st_grid(cols='18% 42% 30%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'HIGH')
                with g.cell():
                    st_write(bs.table_txt, 'Crash, data loss, security hole')
                with g.cell():
                    st_write(bs.table_txt, 'Fix before delivering')
            with st_grid(cols='18% 42% 30%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'MEDIUM')
                with g.cell():
                    st_write(bs.table_txt, 'Missing error handling, hard to maintain')
                with g.cell():
                    st_write(bs.table_txt, 'Fix, or decide explicitly')
            with st_grid(cols='18% 42% 30%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'LOW')
                with g.cell():
                    st_write(bs.table_txt, 'Naming, style, documentation gap')
                with g.cell():
                    st_write(bs.table_txt, 'Note it; fix if cheap')
            st_write(bs.body, "The same scale as GSE-One's ", (bs.cmd, '/gse-review'), ' (Day 3).', tag=t.div)
            st_write(bs.foot, 'Not every finding is true: you are the judge, not the agent.', tag=t.div)
