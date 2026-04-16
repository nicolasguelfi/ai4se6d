"""Slide — Step 2: Architecture Plan - The Roadmap."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Step 2 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    timing = s.bold + s.project.colors.highlight
bs = BlockStyles

_PLAN_PROMPT = """\
@docs/requirements.md Based on these requirements, propose:
(1) folder structure,
(2) key components,
(3) implementation order,
(4) todo list per FR."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Step 2: Architecture Plan \u2014 The Roadmap", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, (bs.label, "Plan Mode prompt:"))
        st_space("v", 0.5)
        st_code(s.none, code=_PLAN_PROMPT, language="text")

        st_space("v", 1)
        st_write(
            bs.body,
            (bs.label, "Output: "),
            ".gse/plan.yaml. Maintained by the orchestrator throughout the sprint.",
        )

        st_space("v", 1)
        st_write(bs.label, "Architecture Decisions to Make", tag=t.div)
        st_space("v", 0.5)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "State management"), " \u2014 local vs global store")
            with l.item():
                st_write(bs.body, (bs.keyword, "Routing"), " \u2014 file-based vs programmatic")
            with l.item():
                st_write(bs.body, (bs.keyword, "Persistence"), " \u2014 localStorage, IndexedDB, or API")
            with l.item():
                st_write(bs.body, (bs.keyword, "API patterns"), " \u2014 REST, GraphQL, or mock")

        st_space("v", 1)
        st_write(
            bs.body,
            (bs.timing, "Time: 15 min."),
            " Keep simple \u2014 adjust during iteration.",
        )
