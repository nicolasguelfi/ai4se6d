"""Slide — Layer 3: Execution (C9-C14)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Execution layer styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat

bs = BlockStyles


_CONCEPTS = [
    ("C9 Multi-file Editing", "Apply changes across an entire codebase atomically"),
    ("C10 Terminal Integration", "Execute commands, read output, iterate automatically"),
    ("C11 Background Agents", "Parallel autonomous tasks \u2014 CI-triggered, headless"),
    ("C12 Git Safety", "Structured commit/rollback \u2014 never lose work"),
    ("C13 Hooks", "Event-triggered enforcement \u2014 lint, test, validate on every action"),
    ("C14 Enterprise Governance", "Policies, audit trails, cost controls at scale"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Layer 3: Execution (C9-C14)", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            for name, desc in _CONCEPTS:
                with l.item():
                    st_write(bs.body, (bs.label, name), f" \u2014 {desc}")

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "Hooks highlighted: a ",
                (bs.stat, "hook = process enforcement mechanism"),
                ".",
            )
