"""Slide — Learning objectives for GenSEM module."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Learning objectives slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    verb = s.bold + s.project.colors.accent
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Learning Objectives", tag=t.div, toc_lvl="1")
            st_space("v", 2)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.verb, "Explain"), " how GenAI transforms the SDLC and why process discipline matters more with AI")
                with l.item():
                    st_write(bs.body, (bs.verb, "Compare"), " the main methodological frameworks for generative SE")
                with l.item():
                    st_write(bs.body, (bs.verb, "Apply"), " the Compound Engineering 5-phase workflow")
                with l.item():
                    st_write(bs.body, (bs.verb, "Design"), " a lightweight GenSEM using only Cursor native features")
                with l.item():
                    st_write(bs.body, (bs.verb, "Execute"), " structured SE activities with AI on CalcApp v0.3")
