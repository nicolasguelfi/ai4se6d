"""Slide — Review checklist — routing."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Review checklist — routing — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_routing_review_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_routing_review_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_routing_review_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, "Review the Agent's Routing", tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.cmd, 'react-router'),
                        ' in ',
                        (bs.cmd, 'package.json'),
                        ', no ',
                        (bs.cmd, 'react-router-dom'),
                        '?',
                    )
                with l.item():
                    st_write(
                        bs.body,
                        'Navigation with ',
                        (bs.cmd, 'Link'),
                        ', not ',
                        (bs.cmd, '&lt;a href&gt;'),
                        ' (no full reload)?',
                    )
                with l.item():
                    st_write(bs.body, 'One file per page in ', (bs.cmd, 'src/pages/'), '?')
                with l.item():
                    st_write(bs.body, 'Test untouched? ', (bs.cmd, 'git diff -- tests/'), ' shows nothing')
                with l.item():
                    st_write(bs.body, (bs.cmd, 'npm run dev'), ': click both links, back button works?')
            st_write(bs.foot, 'Trust, but verify — you will need this habit at 14:30.', tag=t.div)
