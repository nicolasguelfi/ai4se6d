"""Section — CCSET16: Deployment (edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Section title styles."""
    cycle = Style.create(s.project.titles.subtitle + s.center_txt, "section_cycle")
    title = Style.create(s.project.titles.section_title + s.center_txt, "section_main")
    sub = Style.create(s.project.titles.body + s.center_txt, "section_sub")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.cycle, "CCSET16", tag=t.div)
        st_write(bs.title, "Deployment", tag=t.div, toc_lvl="1", label="CCSET16 — Deployment")
        st_write(bs.sub, "From code to a service", tag=t.div)
