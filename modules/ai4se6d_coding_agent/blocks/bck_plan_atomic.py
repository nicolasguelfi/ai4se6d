"""Slide — From stories to atomic tasks (example)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Atomic tasks styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "atomic_body")
    keyword = s.project.titles.keyword
    item = s.project.titles.table_cell
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "From Stories to Atomic Tasks", tag=t.div, toc_lvl="+1")
        st_write(
            bs.body, "One thing · ", (bs.keyword, "verifiable"), " · ordered",
            tag=t.div,
        )
        st_space("v", 1)
        with st_block(s.project.containers.callout):
            with st_list(l_style=bs.item, li_style=bs.item, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.item, "Expense type + test: an amount ≤ 0 is rejected")
                with l.item(): st_write(bs.item, "Test then code: a saved expense is loaded back from localStorage")
                with l.item(): st_write(bs.item, "Test then code: the list shows items and the monthly total")
                with l.item(): st_write(bs.item, "Test then code: routes / and /add, with a navigation bar")
        st_space("v", 1)
        st_write(bs.body, "Test first, code second — in every task.", tag=t.div)
