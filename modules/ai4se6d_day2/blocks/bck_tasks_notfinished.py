"""Slide — If you did not finish Part 2."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """If you did not finish Part 2 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_notfinished_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_notfinished_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_notfinished_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'If You Did Not Finish', tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(
                        bs.body,
                        'v0.1 need not be complete to be reviewed: you review ',
                        (bs.keyword, 'what you have'),
                    )
                with l.item():
                    st_write(bs.body, 'Merge what is green; leave a red branch aside')
                with l.item():
                    st_write(
                        bs.body,
                        'App broken? Catch up with ',
                        (bs.cmd, 'j2-part1'),
                        ', or ',
                        (bs.cmd, 'j2-v0.1'),
                        ' to review the reference code',
                    )
                with l.item():
                    st_write(
                        bs.body,
                        'Then ',
                        (bs.cmd, 'npm run test:run'),
                        ' and ',
                        (bs.cmd, 'npm run dev'),
                        ' must work',
                    )
            st_write(
                bs.foot,
                'Being behind on code must never block the learning: 14:30 is about review.',
                tag=t.div,
            )
