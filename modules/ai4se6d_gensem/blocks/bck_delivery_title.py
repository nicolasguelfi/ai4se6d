"""Section — CCSET14: Delivery, Maintenance, Capitalisation (edition 2)."""
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
        st_write(bs.cycle, "CCSET14", tag=t.div)
        st_write(bs.title, "Delivery, Maintenance, Capitalisation", tag=t.div, toc_lvl="1", label="CCSET14 — Delivery, Maintenance, Capitalisation")
        st_write(bs.sub, "Ship it, keep it alive, learn from it", tag=t.div)
