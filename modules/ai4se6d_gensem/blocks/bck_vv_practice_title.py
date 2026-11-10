"""Section — CCSET12 in practice: Your Strategy, Then GSE-One (edition 2)."""
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
        st_write(bs.cycle, "CCSET12 in practice", tag=t.div)
        st_write(bs.title, "Your Strategy, Then GSE-One", tag=t.div, toc_lvl="1", label="CCSET12 in practice — Your Strategy, Then GSE-One")
        st_write(bs.sub, "Exercise E14: test strategy, production, review", tag=t.div)
