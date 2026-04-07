"""Slide — Exercise: Customize GenSEMOne for Your Project."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Method adaptation exercise slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(
            bs.heading,
            "Exercise: Customize GenSEMOne for Your Project",
            tag=t.div,
            toc_lvl="1",
        )
        st_space("v", 0.5)

        st_write(
            bs.body,
            (bs.stat, "20 minutes"),
            " \u2014 Given YOUR team's stack and project, adapt GenSEMOne:",
        )
        st_space("v", 0.5)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, "Which steps would you ", (bs.keyword, "modify"), "? Why?")
            with l.item():
                st_write(bs.body, "What would ", (bs.keyword, "YOUR"), " .cursor/rules/project.mdc contain?")
            with l.item():
                st_write(bs.body, "Which FRs would you ", (bs.keyword, "prioritize"), " for 1.5 days?")
            with l.item():
                st_write(
                    bs.body,
                    "What is your ",
                    (bs.keyword, "minimum viable subset"),
                    " (4 FRs)?",
                )

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "This is the DESIGN activity \u2014 you're not just following a recipe, "
                "you're adapting a method.",
            )
