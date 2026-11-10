"""Slide — Day 3 hands-up quiz: answers (edition 2)."""
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
            st_write(bs.heading, "Quiz — Answers", tag=t.div, toc_lvl="+1", label="Day 3 quiz answers")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.body, "A wish, until it has a scale, a meter and a goal.")
                with l.item(): st_write(bs.body, "Interview for goals and the \"why\"; observation for the real work; "
                                        "prototype when the user cannot describe it.")
                with l.item(): st_write(bs.body, "Validation: is it the right product?")
                with l.item(): st_write(bs.body, "A test that copies the code copies its bugs: take it from the requirement.")
                with l.item(): st_write(bs.body, ".gse/status.yaml — or simply /gse-status.")
