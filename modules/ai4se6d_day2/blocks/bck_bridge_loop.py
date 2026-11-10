"""Slide — Today's manual loop next to the GSE-One commands."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Today's manual loop next to the GSE-One commands — styles."""
    heading = s.project.titles.heading
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "bridge_loop_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "bridge_loop_foot")
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "bridge_loop_th")
    table_txt = Style.create(s.project.titles.table_cell + s.center_txt, "bridge_loop_td")
    table_lbl = Style.create(s.project.titles.table_label + s.center_txt, "bridge_loop_tl")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Today by Hand → GSE-One', tag=t.div, toc_lvl='1', label='Bridge to GSE-One')
            with st_grid(cols='50% 45%', gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, 'Today, by hand')
                with g.cell():
                    st_write(bs.table_hdr, 'GSE-One (Day 3)')
            with st_grid(cols='50% 45%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'Plan → tasks in ', (bs.cmd, 'docs/plan.md'))
                with g.cell():
                    st_write(bs.table_txt, (bs.cmd, '/gse-plan'))
            with st_grid(cols='50% 45%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'Test first, one branch per task')
                with g.cell():
                    st_write(bs.table_txt, (bs.cmd, '/gse-tests'), ' + ', (bs.cmd, '/gse-produce'))
            with st_grid(cols='50% 45%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'Review, triage HIGH / MEDIUM / LOW')
                with g.cell():
                    st_write(bs.table_txt, (bs.cmd, '/gse-review'))
            with st_grid(cols='50% 45%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'Fix on a branch, test first')
                with g.cell():
                    st_write(bs.table_txt, (bs.cmd, '/gse-fix'))
            with st_grid(cols='50% 45%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'Merge + tag ', (bs.cmd, 'v0.1'))
                with g.cell():
                    st_write(bs.table_txt, (bs.cmd, '/gse-deliver'))
            st_write(
                bs.foot,
                'Same loop, same severities — and GSE-One will not deliver over an open HIGH without your explicit decision.',
                tag=t.div,
            )
