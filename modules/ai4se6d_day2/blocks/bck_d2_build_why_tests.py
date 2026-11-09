"""Slide — Why start with tests?."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Why start with tests? — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_why_tests_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_why_tests_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Why Start with Tests?', tag=t.div, toc_lvl='+1')
            st_write(
                bs.body,
                'The #1 risk with a coding agent: ',
                (bs.keyword, 'losing control'),
                '.',
                tag=t.div,
            )
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Code arrives fast — but does it work?')
                with l.item():
                    st_write(bs.body, 'Clicking through the app is not a proof')
                with l.item():
                    st_write(bs.body, 'A test answers in milliseconds: ', (bs.keyword, 'yes or no'))
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    (bs.keyword, 'You'),
                    ' set the specification (the test). The ',
                    (bs.keyword, 'agent'),
                    " writes the implementation. You stay in the driver's seat.",
                )
            st_write(bs.foot, 'Tests = control. No tests = hope.', tag=t.div)
