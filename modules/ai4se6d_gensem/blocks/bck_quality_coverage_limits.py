"""Slide — What coverage does not tell you (Inozemtseva & Holmes) (CCSET13, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Coverage limits styles."""
    heading = s.project.titles.heading
    callout = Style.create(s.project.titles.body + s.center_txt, "coverage_callout")
    body = s.project.titles.body
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Coverage Is Not Quality", tag=t.div, toc_lvl="+1", label="Limits of coverage")
            with st_block(s.project.containers.callout):
                st_write(bs.callout, "Coverage counts the lines a test executed — not what it checked.", tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "A test with no assertion gives 100 % and proves nothing")
                with l.item(): st_write(bs.body, "Files no test loads may not even appear in the table")
                with l.item(): st_write(bs.body, "Low coverage is a warning; high coverage is not a proof")
                with l.item(): st_write(bs.body, "Better check: break the code — does a test fail? (the mutant trick)")
            st_write(bs.source, cite("inozemtseva-coverage2014"), tag=t.div)
