"""Slide — The AI-TDD discipline and its golden rule."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """The AI-TDD discipline and its golden rule — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_golden_rule_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_golden_rule_foot")
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "build_golden_rule_th")
    table_txt = Style.create(s.project.titles.table_cell + s.center_txt, "build_golden_rule_td")
    table_lbl = Style.create(s.project.titles.table_label + s.center_txt, "build_golden_rule_tl")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'The Golden Rule', tag=t.div, toc_lvl='+1')
            with st_grid(cols='22% 22% 50%', gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, 'Step')
                with g.cell():
                    st_write(bs.table_hdr, 'Who')
                with g.cell():
                    st_write(bs.table_hdr, 'What')
            with st_grid(cols='22% 22% 50%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'RED')
                with g.cell():
                    st_write(bs.table_txt, 'You + agent')
                with g.cell():
                    st_write(
                        bs.table_txt,
                        'The agent drafts the test, ',
                        (bs.keyword, 'you'),
                        ' review it: it is your spec',
                    )
            with st_grid(cols='22% 22% 50%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'GREEN')
                with g.cell():
                    st_write(bs.table_txt, 'Agent')
                with g.cell():
                    st_write(bs.table_txt, 'Minimal code to pass. The test is not touched.')
            with st_grid(cols='22% 22% 50%', gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.table_lbl, 'REFACTOR')
                with g.cell():
                    st_write(bs.table_txt, 'You decide')
                with g.cell():
                    st_write(bs.table_txt, 'Clean up; the tests stay green')
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    (bs.keyword, 'Golden rule'),
                    ': never let the agent write the test ',
                    (bs.keyword, 'and'),
                    ' the code without your review in between.',
                )
            st_write(
                bs.foot,
                'Otherwise the test mirrors what the agent meant to write — it proves nothing.',
                tag=t.div,
            )
