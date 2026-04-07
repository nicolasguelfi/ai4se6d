"""Slide — Layer 2: Knowledge (C4-C8)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Knowledge layer styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    callout_text = s.project.titles.body + s.project.colors.highlight

bs = BlockStyles


_CONCEPTS = [
    ("C4 Project Rules", ".cursor/rules, CLAUDE.md \u2014 declarative process constraints"),
    ("C5 Memory", "Persistent context across sessions \u2014 decisions survive restarts"),
    ("C6 Skills", "Reusable process fragments \u2014 encode methodology as executable steps"),
    ("C7 MCP", "External tool integration \u2014 extend the agent\u2019s capability surface"),
    ("C8 Codebase Indexing", "Semantic search \u2014 the agent understands your project structure"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Layer 2: Knowledge (C4-C8)", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            for name, desc in _CONCEPTS:
                with l.item():
                    st_write(bs.body, (bs.label, name), f" \u2014 {desc}")

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_text,
                "These are the mechanisms through which SE processes are expressed.",
            )
