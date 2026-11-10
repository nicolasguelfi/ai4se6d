"""Section — CCSET09 (edition 2): software engineering concepts, defining your GenSEM (edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Section title styles."""
    cycle = Style.create(s.project.titles.subtitle + s.center_txt, "concepts_title_cycle")
    title = Style.create(s.project.titles.section_title + s.center_txt, "concepts_title_main")
    sub = Style.create(s.project.titles.body + s.center_txt, "concepts_title_sub")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.cycle, "CCSET09", tag=t.div)
        st_write(bs.title, "Software Engineering Concepts", tag=t.div, toc_lvl="1", label="CCSET09 — SE concepts, your GenSEM")
        st_write(bs.sub, "Why a method, what the research says, what a GenSEM must define", tag=t.div)
