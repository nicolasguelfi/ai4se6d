"""Slide — Morning break (10:45 - 11:00)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Break slide styles."""
    title = Style.create(s.project.titles.section_title + s.center_txt, "break_title")
    time = Style.create(s.project.titles.stat_hero, "break_time")
    body = Style.create(s.project.titles.body + s.center_txt, "break_body")
    keyword = s.project.titles.keyword
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.title, "Break", tag=t.div, toc_lvl="1", label="Break (10:45)")
        st_write(bs.time, "11:00", tag=t.div)
        st_space("v", 1)
        st_write(bs.body, "Before you leave: ", (bs.keyword, "git status"), " clean? Commit or restore.", tag=t.div)
        st_write(bs.body, "Next: your own plan for CalcApp v0.1.", tag=t.div)
