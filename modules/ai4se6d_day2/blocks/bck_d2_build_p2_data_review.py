"""Slide — Review checklist — data layer."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Review checklist — data layer — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_p2_data_review_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_p2_data_review_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_p2_data_review_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, "Review the Agent's Data Layer", tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(
                        bs.body,
                        'Types in ',
                        (bs.cmd, 'src/types/expense.ts'),
                        ', no ',
                        (bs.cmd, 'any'),
                        '?',
                    )
                with l.item():
                    st_write(bs.body, 'Storage really uses localStorage — not just React state?')
                with l.item():
                    st_write(
                        bs.body,
                        'Form inputs controlled (',
                        (bs.cmd, 'value'),
                        ' + ',
                        (bs.cmd, 'onChange'),
                        ')?',
                    )
                with l.item():
                    st_write(
                        bs.body,
                        'After Add, back to ',
                        (bs.cmd, '/'),
                        ' with ',
                        (bs.cmd, 'useNavigate'),
                        '?',
                    )
                with l.item():
                    st_write(bs.body, 'Refresh the browser: is your expense still there?')
            st_write(
                bs.foot,
                'Most common slip: data kept in React state only — gone at the first refresh.',
                tag=t.div,
            )
