"""Section — Day 3 afternoon: now with GSE-One, on your CalcApp (edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Section title styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "section_main")
    sub = Style.create(s.project.titles.body + s.center_txt, "section_sub")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.title, "Now with GSE-One", tag=t.div, toc_lvl="1", label="Day 3 afternoon — exercises with GSE-One")
        st_write(bs.sub, "Discover · Plan · Requirements and design — on your CalcApp", tag=t.div)
