"""Slide — The same loop for every task."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """The same loop for every task — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_p2_loop_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_p2_loop_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_p2_loop_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Same Loop, Every Task', tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Branch: ', (bs.cmd, 'git switch -c feat/&lt;task-name&gt;'))
                with l.item():
                    st_write(
                        bs.body,
                        'RED: test only → ',
                        (bs.keyword, 'you'),
                        ' review → commit ',
                        (bs.cmd, 'test: …'),
                    )
                with l.item():
                    st_write(bs.body, 'GREEN: minimal code, test untouched → commit ', (bs.cmd, 'feat: …'))
                with l.item():
                    st_write(bs.body, 'Mutant check → undo')
                with l.item():
                    st_write(bs.body, "Review the agent's code (checklists ahead)")
                with l.item():
                    st_write(bs.body, 'Merge into ', (bs.cmd, 'mywork'), ' only when green')
            st_write(bs.foot, "Typical order: routing → data → UI. Follow your plan's order.", tag=t.div)
