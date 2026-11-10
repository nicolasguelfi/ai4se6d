"""Slide — Day 4 hands-up quiz, with answers on the next slide (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Quiz styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "practice_quiz_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Hands-Up Quiz", tag=t.div, toc_lvl="1", label="Day 4 quiz")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.body, "100 % coverage: are the tests good?")
                with l.item(): st_write(bs.body, "The CI is red after your push. What do you do first?")
                with l.item(): st_write(bs.body, "Squash or merge commit: which keeps every step?")
                with l.item(): st_write(bs.body, "A new browser version breaks the app: which kind of maintenance?")
                with l.item(): st_write(bs.body, "Your mini-project in one sentence?")
            st_write(bs.foot, "Before you leave: push both repositories, then /gse-pause.", tag=t.div)
