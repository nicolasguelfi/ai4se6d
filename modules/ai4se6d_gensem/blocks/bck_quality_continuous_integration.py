"""Slide — Continuous integration: every push is checked (Fowler) (CCSET13, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """CI styles."""
    heading = s.project.titles.heading
    step = Style.create(s.project.titles.table_label + s.center_txt, "ci_step")
    arrow = Style.create(s.project.titles.subtitle + s.center_txt, "ci_arrow")
    body = Style.create(s.project.titles.body + s.center_txt, "ci_body")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

STEPS = ["push", "install", "lint", "tests + coverage", "build", "green / red"]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Continuous Integration", tag=t.div, toc_lvl="+1", label="Continuous integration")
            with st_grid(cols="repeat(auto-fit, minmax(170px, 1fr))", gap="10px",
                         cell_styles=s.project.containers.table_normal_cell) as g:
                for name in STEPS:
                    with g.cell():
                        st_write(bs.step, name, tag=t.div)
            st_write(bs.body, "The same checks, on a clean machine, at every push — not only when someone remembers.", tag=t.div)
            st_write(bs.body, "Red means: stop and fix before anything else is merged.", tag=t.div)
            st_write(bs.source, cite("fowler-ci2006"), tag=t.div)
