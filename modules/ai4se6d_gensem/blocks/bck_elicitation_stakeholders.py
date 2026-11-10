"""Slide — Stakeholders and sources of requirements (CCSET10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Stakeholders styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    body = s.project.titles.body
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "stakeholders_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Who and Where to Ask", tag=t.div, toc_lvl="+1", label="Stakeholders and sources")
            with st_grid(cols="repeat(auto-fit, minmax(420px, 1fr))", gap="32px") as g:
                with g.cell():
                    st_write(bs.label, "Stakeholders", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, "Users — each kind of user")
                        with l.item(): st_write(bs.body, "The customer, who pays")
                        with l.item(): st_write(bs.body, "Operations and support")
                        with l.item(): st_write(bs.body, "Regulators: law, data protection")
                with g.cell():
                    st_write(bs.label, "Sources", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, "The current process and its tools")
                        with l.item(): st_write(bs.body, "Existing documents and systems")
                        with l.item(): st_write(bs.body, "Complaints and support tickets")
                        with l.item(): st_write(bs.body, "Competing products")
            st_write(bs.foot, "A requirement nobody can trace to a stakeholder is a guess.", tag=t.div)
