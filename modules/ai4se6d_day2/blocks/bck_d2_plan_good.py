"""Slide — What good requirements look like."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Requirement quality styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    good = Style.create(s.project.titles.table_cell + s.project.colors.success, "d2_good_ex")
    bad = Style.create(s.project.titles.table_cell + s.project.colors.critical, "d2_bad_ex")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Good Requirements", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Testable"), tag=t.div)
                st_write(bs.good, "✓ Amount 0 or negative → a validation error is shown", tag=t.div)
                st_write(bs.bad, "✗ The app handles expenses well", tag=t.div)
            with l.item(): st_write(bs.body, (bs.keyword, "Small"), " — fits 30-45 min of work with the agent")
            with l.item(): st_write(bs.body, (bs.keyword, "Independent"), " — buildable in any order, as far as possible")
