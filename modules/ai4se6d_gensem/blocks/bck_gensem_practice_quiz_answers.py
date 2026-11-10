"""Slide — Day 4 hands-up quiz: answers (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Quiz answer styles."""
    heading = s.project.titles.heading
    body = s.project.titles.table_cell
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Quiz — Answers", tag=t.div, toc_lvl="+1", label="Day 4 quiz answers")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.body, "Not necessarily: coverage says what ran, not what was checked.")
                with l.item(): st_write(bs.body, "Read which step failed, fix it on your branch, push again — before anything else.")
                with l.item(): st_write(bs.body, "The merge commit; squash keeps one commit per branch.")
                with l.item(): st_write(bs.body, "Adaptive maintenance.")
                with l.item(): st_write(bs.body, "One user, one problem — if it takes more, reduce.")
