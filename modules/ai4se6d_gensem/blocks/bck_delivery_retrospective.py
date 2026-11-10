"""Slide — Capitalising: the retrospective (Derby & Larsen) (CCSET14, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Retrospective styles."""
    heading = s.project.titles.heading
    question = Style.create(s.project.titles.body + s.bold, "retro_question")
    body = Style.create(s.project.titles.body + s.center_txt, "retro_body")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Learn Before the Next Cycle", tag=t.div, toc_lvl="+1", label="Retrospective")
            with st_block(s.project.containers.callout):
                with st_list(l_style=bs.question, li_style=bs.question, list_type=lt.ordered) as l:
                    with l.item(): st_write(bs.question, "What went well — keep it")
                    with l.item(): st_write(bs.question, "What hurt — change it")
                    with l.item(): st_write(bs.question, "One action for the next cycle, with an owner")
            st_write(bs.body, "A lesson that is not written down is lost at the next session.", tag=t.div)
            st_write(bs.source, cite("derby-larsen-retro2006"), tag=t.div)
