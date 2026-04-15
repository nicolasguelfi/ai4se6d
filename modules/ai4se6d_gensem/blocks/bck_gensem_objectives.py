"""Slide — Learning objectives for GSE-One module."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Learning objectives slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    verb = s.bold + s.project.colors.accent
bs = BlockStyles

def build():
    st_marker("Learning Objectives")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Learning Objectives", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="Learning Objectives",
                entries=[
                    ("Bloom's taxonomy", "Each objective uses a specific action verb (Explain, Compare, Apply, Adapt, Execute) mapping to increasing cognitive complexity."),
                    ("Discipline focus", "By the end of this module, you will understand Generative SE as a discipline and be able to practice it through GSE-One."),
                    ("Transferable skills", "The principles you learn transfer to any Generative SE methodology \u2014 current or future."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 2)

            with st_zoom(100):
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                    with l.item():
                        st_write(bs.body, (bs.verb, "Explain"), " how GenAI transforms the SDLC and why a new engineering discipline is emerging")
                    with l.item():
                        st_write(bs.body, (bs.verb, "Compare"), " methodologies for Generative SE and identify their common principles")
                    with l.item():
                        st_write(bs.body, (bs.verb, "Apply"), " Generative SE principles through the GSE-One lifecycle")
                    with l.item():
                        st_write(bs.body, (bs.verb, "Adapt"), " the Generative SE framework to your tools and project context")
                    with l.item():
                        st_write(bs.body, (bs.verb, "Execute"), " a structured Generative SE sprint on CalcApp")
