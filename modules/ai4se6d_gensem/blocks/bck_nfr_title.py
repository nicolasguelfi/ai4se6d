"""Section — CCSET11: Non-Functional Requirements (edition 2)."""
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
        st_write(bs.cycle, "CCSET11", tag=t.div)
        st_write(bs.title, "Non-Functional Requirements", tag=t.div, toc_lvl="1", label="CCSET11 — Non-Functional Requirements")
        st_write(bs.sub, "Not what the system does, but how well it must do it", tag=t.div)
