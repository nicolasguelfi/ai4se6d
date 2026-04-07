"""Slide — From Theory to Practice: mapping CE phases to today's activities."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """CE transition slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    phase = s.bold + s.project.colors.accent
    activity = s.bold + s.project.colors.highlight
    question = s.project.titles.body + s.project.colors.primary + s.bold
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "From Theory to Practice", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        st_write(bs.body, "Mapping CE phases to today's hands-on activities:")
        st_space("v", 0.5)

        with st_list(li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.phase, "CE Brainstorm"), " \u2192 ", (bs.activity, "Requirements elicitation workshop"))
            with l.item():
                st_write(bs.body, (bs.phase, "CE Plan"), " \u2192 ", (bs.activity, "Functional requirements + acceptance criteria"))
            with l.item():
                st_write(bs.body, (bs.phase, "CE Work"), " \u2192 ", (bs.activity, "TDD, project rules, structured prompts"))
            with l.item():
                st_write(bs.body, (bs.phase, "CE Review"), " \u2192 ", (bs.activity, "V&V, cross-feedback"))
            with l.item():
                st_write(bs.body, (bs.phase, "CE Compound"), " \u2192 ", (bs.activity, "Debrief, capture what worked"))

        st_space("v", 2)

        with st_block(s.project.containers.callout):
            st_write(
                bs.question,
                "How many of you currently write requirements BEFORE asking AI to generate code?",
            )
