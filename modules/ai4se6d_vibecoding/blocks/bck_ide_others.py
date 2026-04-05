"""Slide 35 — Windsurf + GitHub Copilot: other notable tools."""
# @guideline: maximize-viewport
from streamtex import *
<<<<<<< HEAD
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = s.project.containers.page_fill_top


=======
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
class BlockStyles:
    """Other IDEs slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
<<<<<<< HEAD
bs = BlockStyles


def build():
    # Slide 1 — Windsurf
    with st_block(_page_fill):
=======
    source = s.project.titles.caption
bs = BlockStyles

def build():
    # Slide 1 — Windsurf
    with st_block(s.project.containers.page_fill_top):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "Windsurf", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "Cascade"), " \u2014 multi-step AI flow engine for guided coding")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Memories"), " \u2014 persistent project context across sessions")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "SOC 2 / FedRAMP"), " \u2014 enterprise-grade security compliance")
<<<<<<< HEAD
                with l.item():
                    st_write(bs.body, (bs.keyword, "800K+ developers"), " \u2014 growing community adoption")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "Acquired by Cognition"), " \u2014 merged with Devin AI team")

    st_slide_break()

    # Slide 2 — GitHub Copilot
    with st_block(_page_fill):
=======
                # REF: windsurf-cascade2025
                with l.item():
                    st_write(bs.body, (bs.keyword, "800K+ developers"), " \u2014 growing community adoption")
                # REF: windsurf-cascade2025
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "Acquired by Cognition"), " \u2014 merged with Devin AI team")

            st_write(bs.source, cite("windsurf-cascade2025"), " \u00b7 ", cite("copilot-plans2025"))

    st_slide_break()

    # Slide 2 — GitHub Copilot
    with st_block(s.project.containers.page_fill_top):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "GitHub Copilot", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
<<<<<<< HEAD
=======
                # REF: copilot-plans2025
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "20M+ developers"), " \u2014 largest AI coding user base")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Agent Mode"), " \u2014 autonomous file editing and terminal access")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "Coding Agent"), " \u2014 async background agent for issues and PRs")
                with l.item():
                    st_write(bs.body, (bs.keyword, "MCP support"), " \u2014 extensible via Model Context Protocol servers")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "IP indemnity"), " \u2014 Microsoft legal protection for enterprise customers")
<<<<<<< HEAD
=======

            st_write(bs.source, cite("windsurf-cascade2025"), " \u00b7 ", cite("copilot-plans2025"))
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
