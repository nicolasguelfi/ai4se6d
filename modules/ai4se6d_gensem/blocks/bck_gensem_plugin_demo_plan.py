"""Slide — Live demo: /ce:plan phase."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Plan demo slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    callout_text = s.project.titles.body + s.project.colors.highlight
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Live Demo: /ce:plan", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, "Continues from the brainstorm output. The plan phase transforms exploration into a ", (bs.keyword, "contract"), ".")

        st_space("v", 1)
        st_write(bs.label, "Plan Produces", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Task decomposition"), " \u2014 8 atomic tasks, each with clear acceptance criteria")
            with l.item():
                st_write(bs.body, (bs.keyword, "File-level specs"), " \u2014 which files to create, modify, or delete with expected diffs")
            with l.item():
                st_write(bs.body, (bs.keyword, "Test strategy"), " \u2014 12 test cases covering happy path, edge cases, and error scenarios")
            with l.item():
                st_write(bs.body, (bs.keyword, "Risk mitigation"), " \u2014 identified blockers with fallback strategies")

        st_space("v", 1)
        st_write(bs.label, "Key Properties", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Plan as contract"), " \u2014 the work phase executes exactly what was planned, nothing more")
            with l.item():
                st_write(bs.body, (bs.keyword, "Scope creep detection"), " \u2014 any deviation triggers an explicit re-planning step")
            with l.item():
                st_write(bs.body, (bs.keyword, "Traceability"), " \u2014 plan references brainstorm output for full audit trail")

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(bs.callout_text, "A good plan is the single highest-leverage artifact in generative SE.")
