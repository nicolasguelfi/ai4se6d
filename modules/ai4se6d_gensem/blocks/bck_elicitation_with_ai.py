"""Slide — Eliciting with an AI: what helps, what to watch (CCSET10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Eliciting with AI styles."""
    heading = s.project.titles.heading
    good = Style.create(s.project.titles.label + s.project.colors.success, "elicit_ai_good")
    bad = Style.create(s.project.titles.label + s.project.colors.critical, "elicit_ai_bad")
    body = s.project.titles.body
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "Eliciting with an AI", tag=t.div, toc_lvl="+1", label="Elicitation with an AI")
            with st_grid(cols="repeat(auto-fit, minmax(420px, 1fr))", gap="32px") as g:
                with g.cell():
                    st_write(bs.good, "It helps", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, "Asks the questions you forgot")
                        with l.item(): st_write(bs.body, "Drafts stories and criteria fast")
                        with l.item(): st_write(bs.body, "Spots ambiguous words")
                with g.cell():
                    st_write(bs.bad, "Watch out", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, "Invents requirements nobody asked for")
                        with l.item(): st_write(bs.body, "Fills gaps with generic answers")
                        with l.item(): st_write(bs.body, "Agrees with you too easily")
            st_write(bs.source, "Research is young: most studies are early-stage — ",
                     cite("cheng-genai-re2025"), tag=t.div)
