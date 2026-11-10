"""Slide — Verification versus validation (Boehm) (CCSET12, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """V&V definition styles."""
    heading = s.project.titles.heading
    name = Style.create(s.project.titles.subtitle + s.center_txt, "vv_def_name")
    quote = Style.create(s.project.titles.body + s.italic + s.center_txt, "vv_def_quote")
    txt = Style.create(s.project.titles.table_cell + s.center_txt, "vv_def_txt")
    source = s.project.citation + s.large + s.center_txt
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "vv_def_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(72):
            st_write(bs.heading, "Two Different Questions", tag=t.div, toc_lvl="+1", label="Verification versus validation")
            with st_grid(cols="repeat(auto-fit, minmax(420px, 1fr))", gap="24px",
                         cell_styles=s.project.containers.table_normal_cell) as g:
                with g.cell():
                    st_write(bs.name, "Verification", tag=t.div)
                    st_write(bs.quote, "\"Am I building the product right?\"", tag=t.div)
                    st_write(bs.txt, "against the design: unit and integration tests, review", tag=t.div)
                with g.cell():
                    st_write(bs.name, "Validation", tag=t.div)
                    st_write(bs.quote, "\"Am I building the right product?\"", tag=t.div)
                    st_write(bs.txt, "against the user's need: acceptance tests, demos", tag=t.div)
            st_write(bs.source, cite("boehm-vv1984"), tag=t.div)
            st_write(bs.foot, "90% coverage of a feature nobody needs: verified, not validated.", tag=t.div)
