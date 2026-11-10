"""Slide — User stories and the INVEST checklist (CCSET10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """User stories styles."""
    heading = s.project.titles.heading
    story = Style.create(s.project.titles.body + s.italic + s.center_txt, "stories_story")
    letter = Style.create(s.project.titles.stat + s.center_txt, "stories_letter")
    word = Style.create(s.project.titles.table_cell + s.center_txt, "stories_word")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

INVEST = [("I", "Independent"), ("N", "Negotiable"), ("V", "Valuable"),
          ("E", "Estimable"), ("S", "Small"), ("T", "Testable")]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "User Stories", tag=t.div, toc_lvl="+1", label="User stories and INVEST")
            with st_block(s.project.containers.callout):
                st_write(bs.story, "As a person on a budget, I want to see my monthly total by category, "
                         "so that I know where my money goes.", tag=t.div)
            with st_grid(cols="repeat(auto-fit, minmax(180px, 1fr))", gap="12px",
                         cell_styles=s.project.containers.table_normal_cell) as g:
                for letter, word in INVEST:
                    with g.cell():
                        st_write(bs.letter, letter, tag=t.div)
                        st_write(bs.word, word, tag=t.div)
            st_write(bs.source, cite("wake-invest2003"), tag=t.div)
