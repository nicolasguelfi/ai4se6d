"""Section title — Technical planning workshop (11:00, 30 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Section title styles."""
    section = Style.create(s.project.titles.section_title + s.center_txt, "d2_sec_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "d2_sec_subtitle")
    info = Style.create(s.project.titles.caption + s.center_txt, "d2_sec_info")
    body = s.project.titles.body
    keyword = s.project.titles.keyword
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.info, "11:00 — 30 min · frame 5 · practice 20 · debrief 5", tag=t.div)
        st_write(bs.section, "Workshop: Technical Planning", tag=t.div, toc_lvl="1")
        st_write(bs.subtitle, "From a vision to docs/plan.md", tag=t.div)
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered, block_align="center") as l:
            with l.item(): st_write(bs.body, "Elicit requirements with the ", (bs.keyword, "plan agent"))
            with l.item(): st_write(bs.body, "Split them into ", (bs.keyword, "atomic, testable tasks"))
            with l.item(): st_write(bs.body, (bs.keyword, "Commit"), " the plan that drives your afternoon")
