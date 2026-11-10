"""Slide — Five habits for an AI-friendly project."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Habits styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "AI-Friendly Project Habits", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, (bs.keyword, "Descriptive folders"), " — components/, pages/, utils/")
            with l.item(): st_write(bs.body, (bs.keyword, "Tests mirror src/"), " — same path, .test suffix")
            with l.item(): st_write(bs.body, (bs.keyword, "A README"), " — purpose, stack, commands")
            with l.item(): st_write(bs.body, (bs.keyword, "A short docs/architecture.md"))
            with l.item(): st_write(bs.body, (bs.keyword, "Small files"), " — one concern each")
