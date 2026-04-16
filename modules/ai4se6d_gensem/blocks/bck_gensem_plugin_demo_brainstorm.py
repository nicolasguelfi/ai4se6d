"""Slide — Live demo: /ce:brainstorm phase."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Brainstorm demo slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    callout_text = s.project.titles.body + s.project.colors.highlight
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, 'Live Demo: /ce:brainstorm', tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, (bs.label, "Scenario: "), 'Adding a "budget alerts" feature to CalcApp.')

        st_space("v", 1)
        st_write(bs.label, "What Happens", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Clarifies requirement"), " \u2014 AI asks probing questions about thresholds, notification channels, user preferences")
            with l.item():
                st_write(bs.body, (bs.keyword, "Identifies edge cases"), " \u2014 multi-currency budgets, timezone-dependent resets, concurrent updates")
            with l.item():
                st_write(bs.body, (bs.keyword, "Proposes 3 architectural strategies"), " \u2014 polling vs event-driven vs hybrid, with trade-off analysis")
            with l.item():
                st_write(bs.body, (bs.keyword, "Surfaces risks"), " \u2014 performance impact on large datasets, notification spam, false positives")

        st_space("v", 1)
        st_write(bs.body, (bs.label, "Artifact produced: "), "brainstorm document saved to docs/brainstorm/budget-alerts.md")

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(bs.callout_text, "5-minute conversation replaces 30 minutes of ambiguous back-and-forth.")
