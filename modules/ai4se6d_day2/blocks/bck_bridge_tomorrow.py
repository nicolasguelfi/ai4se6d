"""Slide — Preview of Day 3."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Preview of Day 3 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "bridge_tomorrow_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "bridge_tomorrow_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "bridge_tomorrow_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Next: Day 3 (Thu 3 Dec)', tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'GSE-One drives the loop you ran by hand today')
                with l.item():
                    st_write(bs.body, 'Start with ', (bs.cmd, '/gse-go'), ' inside your project')
                with l.item():
                    st_write(bs.body, 'CalcApp continues — recovery tag ', (bs.cmd, 'p3-start'))
                with l.item():
                    st_write(bs.body, 'Your work goes to GitHub, pushed every evening')
            st_write(
                bs.foot,
                'Keep your laptop as it is: opencode, model key, GSE-One v0.90.1, your tutor.',
                tag=t.div,
            )
