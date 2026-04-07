"""Slide — GenSEMOne 6-step process overview."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Method overview slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    timing = s.bold + s.project.colors.highlight
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "GenSEMOne \u2014 6-Step Process", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Step 0 \u2014 Seed"), " ", (bs.timing, "(15 min)"), " \u2014 Define scope + create .cursor/rules/project.mdc")
            with l.item():
                st_write(bs.body, (bs.keyword, "Step 1 \u2014 Requirements"), " ", (bs.timing, "(30 min)"), " \u2014 Plan Mode brainstorm, write docs/requirements.md")
            with l.item():
                st_write(bs.body, (bs.keyword, "Step 2 \u2014 Architecture Plan"), " ", (bs.timing, "(15 min)"), " \u2014 Plan Mode: project structure + todo list")
            with l.item():
                st_write(bs.body, (bs.keyword, "Step 3 \u2014 Iterate"), " ", (bs.timing, "(4\u20135h)"), " \u2014 For each FR: test first \u2192 implement \u2192 verify \u2192 commit")
            with l.item():
                st_write(bs.body, (bs.keyword, "Step 4 \u2014 Review"), " ", (bs.timing, "(30 min)"), " \u2014 Plan Mode review against requirements")
            with l.item():
                st_write(bs.body, (bs.keyword, "Step 5 \u2014 Compound"), " ", (bs.timing, "(15 min)"), " \u2014 Update .cursor/rules with lessons learned")
