"""Slide 38 — You Will Master Cursor: rationale for the training choice."""
# @guideline: maximize-viewport
from streamtex import *
<<<<<<< HEAD
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


# Viewport-filling wide centered container
_page_fill = s.project.containers.page_fill_center_wide


=======
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
class BlockStyles:
    """Cursor choice slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
<<<<<<< HEAD
bs = BlockStyles


def build():
    with st_block(_page_fill):
=======
    source = s.project.titles.caption
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_center_wide):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "You Will Master Cursor", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Best compromise"), " \u2014 full IDE integration + powerful agent mode")
<<<<<<< HEAD
=======
                # REF: cursor-ainative2025
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
                with l.item():
                    st_write(bs.body, (bs.keyword, "8 parallel agents"), " \u2014 your brigade, running concurrently on different tasks")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "Rules & hooks"), " \u2014 encode your engineering standards into every interaction")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Plugin marketplace"), " \u2014 extend with MCP servers, custom tools, integrations")
<<<<<<< HEAD
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Industry standard"), " \u2014 1M+ daily users, transferable skills across teams")
=======
                # REF: cursor-ainative2025
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Industry standard"), " \u2014 1M+ daily users, transferable skills across teams")

            st_write(bs.source, cite("cursor-ainative2025"))
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
