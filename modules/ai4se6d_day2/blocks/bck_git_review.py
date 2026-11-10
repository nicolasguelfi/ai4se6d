"""Slide — Pattern 1: review before stage."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Review-before-stage styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "gitrev_closing")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "1 · Review Before Stage", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.body, (bs.keyword, "git status"), " — which files did the agent touch?")
            with l.item(): st_write(bs.body, (bs.keyword, "git diff"), " — read every change")
            with l.item(): st_write(bs.body, (bs.keyword, "git add &lt;file&gt;"), " — only what you approve")
            with l.item(): st_write(bs.body, (bs.keyword, "git diff --staged"), " — last look")
            with l.item(): st_write(bs.body, (bs.keyword, "git commit"), " — a message that says what and why")
        st_space("v", 1)
        st_write(bs.closing, "Never skip step 2: the diff is your review.", tag=t.div)
