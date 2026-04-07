"""Slide — Live demo: /ce:work phase."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Work demo slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    callout_text = s.project.titles.body + s.project.colors.highlight
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Live Demo: /ce:work", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, "Execution with guardrails \u2014 the AI follows the plan as a strict contract.")

        st_space("v", 1)
        st_write(bs.label, "Execution Steps", tag=t.div)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Worktree creation"), " \u2014 isolated git worktree prevents polluting the main branch")
            with l.item():
                st_write(bs.body, (bs.keyword, "Task-by-task execution"), " \u2014 each of the 8 tasks completed sequentially with verification")
            with l.item():
                st_write(bs.body, (bs.keyword, "Test-first approach"), " \u2014 tests written before implementation, validated after each task")
            with l.item():
                st_write(bs.body, (bs.keyword, "Scope enforcement"), " \u2014 AI refuses to implement anything not in the plan without re-planning")

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(bs.callout_text, "~10 min for a well-planned feature vs ~45 min unplanned.")
