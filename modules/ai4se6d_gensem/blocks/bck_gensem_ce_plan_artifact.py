"""Slide — Plan: The Artifact."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Plan artifact slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label

bs = BlockStyles

_PLAN = """\
# Plan: Budget Alerts (from brainstorm)

## Tasks (8 total, 3 dependencies)
1. Create BudgetAlert model [no deps]
2. Add alert threshold to Budget [depends: 1]
3. Write alert check service [depends: 1]
4. Create alert banner component [no deps]
5. Wire service to UI [depends: 3, 4]
6. Write tests for service [depends: 3]
7. Write tests for component [depends: 4]
8. Integration test [depends: 5, 6, 7]

## Files to modify: 6 | Files to create: 4
## Test strategy: 12 test cases"""


def build():
    st_marker("plan.md Artifact Example")
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Plan: The Artifact", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="Plan Artifact in GSE-One",
            entries=[
                ("Phase", "CE Plan = /gse:plan in GSE-One. Produces a concrete plan artifact."),
                ("Content", "Tasks with dependencies, files to modify/create, test strategy."),
                ("Purpose", "Acts as an executable contract that constrains the AI during /gse:produce."),
                ("Example", "Budget Alerts: 8 tasks, 3 dependencies, 6 files to modify, 4 to create."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 0.5)

        with st_zoom(120):
            st_write(bs.body, (bs.label, "Example output"), " from a plan phase:")
            st_space("v", 0.5)

            st_code(s.none, code=_PLAN, language="markdown")
