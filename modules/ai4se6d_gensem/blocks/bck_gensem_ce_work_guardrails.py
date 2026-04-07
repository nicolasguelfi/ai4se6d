"""Slide — Work: Guardrails in Detail."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Work guardrails slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Work: Guardrails in Detail", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Scope enforcement: "),
                    "Agent attempts to modify unlisted file \u2192 warning + return to plan",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Task tracking: "),
                    "Each plan task checked off as completed, visible progress",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Test-first: "),
                    "Tests written before implementation for each task",
                )

        st_space("v", 2)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "Deviations from plan require explicitly returning to the Plan phase.",
            )
