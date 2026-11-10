"""Slide — Static and dynamic verification: review, analysis, tests (CCSET12, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Static and dynamic styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    body = s.project.titles.body
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "static_dynamic_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Without and With Running the Code", tag=t.div, toc_lvl="+1",
                     label="Static and dynamic verification")
            with st_grid(cols="repeat(auto-fit, minmax(420px, 1fr))", gap="32px") as g:
                with g.cell():
                    st_write(bs.label, "Static — read it", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, "Review of the requirements and the design")
                        with l.item(): st_write(bs.body, "Code review (day 2)")
                        with l.item(): st_write(bs.body, "Lint, type checks (day 4)")
                with g.cell():
                    st_write(bs.label, "Dynamic — run it", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, "Unit, integration, end-to-end tests")
                        with l.item(): st_write(bs.body, "Performance measures")
                        with l.item(): st_write(bs.body, "Demo to the user")
            st_write(bs.foot, "Review finds what tests cannot run into; tests find what readers miss.", tag=t.div)
