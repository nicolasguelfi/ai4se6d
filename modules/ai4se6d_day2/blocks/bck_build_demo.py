"""Slide — Live demo — one full red-green-refactor cycle in opencode."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Live demo — one full red-green-refactor cycle in opencode — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_demo_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_demo_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_demo_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_demo_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Live Demo: One Full Cycle', tag=t.div, toc_lvl='+1')
            st_write(bs.timer, '≤ 10 min', tag=t.div)
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, 'build'),
                        ' agent: ask for the ',
                        (bs.keyword, 'test only'),
                        ' → read it',
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.cmd, 'npm run test:run'),
                        ' → ',
                        (bs.keyword, 'RED'),
                        ' (the component does not exist)',
                    )
                with l.item():
                    st_write(bs.body, 'Ask for the minimal code — ', (bs.keyword, 'do not touch the test'))
                with l.item():
                    st_write(bs.body, (bs.cmd, 'npm run test:run'), ' → ', (bs.keyword, 'GREEN'))
                with l.item():
                    st_write(bs.body, 'Break the code on purpose → a test must fail')
                with l.item():
                    st_write(
                        bs.body,
                        'Two commits: ',
                        (bs.cmd, 'test: …'),
                        ' first, then ',
                        (bs.cmd, 'feat: …'),
                    )
            st_write(bs.foot, 'Demo feature: ExpenseItem shows “Lunch” and “€25.50”.', tag=t.div)
