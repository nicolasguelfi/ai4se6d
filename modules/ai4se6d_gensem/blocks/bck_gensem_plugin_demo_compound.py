"""Slide — Live demo: /ce:compound phase."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Compound demo slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    callout_text = s.project.titles.body + s.project.colors.highlight
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Live Demo: /ce:compound", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, "The knowledge flywheel \u2014 each cycle feeds the next.")

        st_space("v", 1)
        st_write(bs.label, "What Gets Compounded", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Patterns extracted"), " \u2014 recurring code structures promoted to reusable templates")
            with l.item():
                st_write(bs.body, (bs.keyword, "Rules updated"), " \u2014 new constraints added to CLAUDE.md or .cursor/rules based on review findings")
            with l.item():
                st_write(bs.body, (bs.keyword, "Skills refined"), " \u2014 prompt chains improved with lessons from this cycle")
            with l.item():
                st_write(bs.body, (bs.keyword, "ADR created"), " \u2014 Architecture Decision Record for significant design choices")

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(bs.callout_text, "In 5 cycles, your project rules become comprehensive enough that AI generates correct code 90%+ on first attempt.")
