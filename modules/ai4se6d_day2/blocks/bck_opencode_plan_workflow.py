"""Slide — The plan-then-build workflow and when to use it."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Workflow styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    rule = Style.create(s.project.titles.body + s.center_txt, "pw_rule")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Think First, Then Code", tag=t.div, toc_lvl="+1")
        st_space("v", 0.5)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, (bs.keyword, "Tab → plan"), ": describe the whole feature and its constraints")
            with l.item(): st_write(bs.body, (bs.keyword, "Review"), ": files, order, tests included?")
            with l.item(): st_write(bs.body, (bs.keyword, "Push back"), ": “tests first”, “split this step”")
            with l.item(): st_write(bs.body, (bs.keyword, "Tab → build"), ": “implement step 1 only”")
            with l.item(): st_write(bs.body, (bs.keyword, "git diff"), ", tests, commit — then the next step")
        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.rule, "Plan first when the task touches 2+ files or needs a ",
                (bs.keyword, "where / how"), " decision. A typo? Just build.", tag=t.div,
            )
