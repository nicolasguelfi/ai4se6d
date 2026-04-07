"""Slide — GenSE Prompting Strategy for v0.3."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Prompting strategy slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    good_title = s.bold + s.project.colors.success + s.Large
    bad_title = s.bold + s.project.colors.highlight + s.Large
    anti = s.project.titles.body + s.project.colors.highlight
bs = BlockStyles

# Callout with success (green) left border
_callout_success = Style.create(
    s.project.containers.callout
    - "callout_border"
    + Style("border-color: #27AE60; border-width: 0 0 0 4px;", "callout_success_border"),
    "callout_success",
)

# Callout with highlight (orange) left border
_callout_warn = Style.create(
    s.project.containers.callout
    - "callout_border"
    + Style("border-color: #F39C12; border-width: 0 0 0 4px;", "callout_warn_border"),
    "callout_warn",
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "GenSE Prompting Strategy for v0.3",
                tag=t.div,
                toc_lvl="1",
            )
            st_space("v", 1)

        # GOOD prompting
        with st_block(_callout_success):
            st_write(bs.good_title, "GOOD \u2014 Structured Prompting", tag=t.div)
            st_space("v", 0.5)
            with st_list(li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Context first:"),
                        " Load FR document (@file docs/requirements/functional-requirements.md)",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "One FR at a time:"),
                        ' "Implement FR-001..."',
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Scope constraint:"),
                        ' "Only modify files related to this FR"',
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Verification:"),
                        ' "Run all tests for FR-001. Show traceability."',
                    )

        st_space("v", 1)

        # BAD prompting
        with st_block(_callout_warn):
            st_write(bs.bad_title, "BAD \u2014 Anti-Pattern", tag=t.div)
            st_space("v", 0.5)
            st_write(
                bs.anti,
                '"Add edit, search, sort, categories and monthly view to CalcApp"',
            )
            st_space("v", 0.3)
            st_write(
                bs.body,
                "\u2192 VibeCoding: no traceability, no verification, no structure.",
            )
