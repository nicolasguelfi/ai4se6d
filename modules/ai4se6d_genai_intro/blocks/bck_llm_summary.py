"""Slide — In Summary: bullet list with accent keywords."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_top


class BlockStyles:
    """Slide: In Summary — maximize-viewport archetype: bullet list with accent keywords."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "In Summary", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "Prediction engine"), " — Next-token prediction at massive scale")
                with l.item(): st_write(bs.body, (bs.keyword, "Trained on trillions"), " — Internet, books, code repositories")
                with l.item(): st_write(bs.body, (bs.keyword, "Aligned"), " — RLHF makes raw models useful assistants")
                with l.item(): st_write(bs.body, (bs.keyword, "Emergent"), " — Reasoning, coding, writing from one principle")
