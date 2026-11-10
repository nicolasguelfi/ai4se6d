"""Slide — Day 3 hands-up quiz (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Quiz styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "concepts_quiz_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Hands-Up Quiz", tag=t.div, toc_lvl="1", label="Day 3 quiz")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.body, "\"The app is fast.\" Requirement or wish?")
                with l.item(): st_write(bs.body, "Name two elicitation techniques, and when to use each.")
                with l.item(): st_write(bs.body, "Verification or validation: a demo to the user?")
                with l.item(): st_write(bs.body, "Why should the expected result not come from the code?")
                with l.item(): st_write(bs.body, "Which GSE-One file says where your project is?")
            st_write(bs.foot, "Before you leave: push to GitHub, then /gse-pause.", tag=t.div)
