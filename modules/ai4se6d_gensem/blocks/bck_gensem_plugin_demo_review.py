"""Slide — Live demo: /ce:review phase."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Review demo slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    critical = s.bold + Style("color: #E74C3C;", "review_critical")
    major = s.bold + s.project.colors.highlight
    minor = s.bold + s.project.colors.muted
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Live Demo: /ce:review", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, "Multi-perspective review \u2014 analogous to N-version verification in safety-critical systems.")

        st_space("v", 1)
        st_write(bs.label, "Four Review Perspectives", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Correctness"), " \u2014 does the code match the plan? Are all test cases passing?")
            with l.item():
                st_write(bs.body, (bs.keyword, "Security"), " \u2014 input validation, authentication checks, data exposure risks")
            with l.item():
                st_write(bs.body, (bs.keyword, "Architecture"), " \u2014 coupling, cohesion, separation of concerns, SOLID principles")
            with l.item():
                st_write(bs.body, (bs.keyword, "Learning extraction"), " \u2014 patterns worth capitalizing, mistakes to prevent next time")

        st_space("v", 1)
        st_write(bs.label, "Output: Severity-Rated Findings", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, (bs.critical, "CRITICAL"), " \u2014 must fix before merge (security holes, data loss risks)")
            with l.item():
                st_write(bs.body, (bs.major, "MAJOR"), " \u2014 should fix (architectural debt, missing edge cases)")
            with l.item():
                st_write(bs.body, (bs.minor, "MINOR"), " \u2014 nice to fix (naming, documentation, style)")
