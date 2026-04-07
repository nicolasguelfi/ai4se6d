"""Slide — Traceability: The GenSE Difference."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Traceability slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    stat = s.bold + s.project.colors.highlight + s.Large
    key_message = s.project.titles.body + s.project.colors.primary + s.bold
    closing = s.project.titles.body + s.project.colors.highlight + s.bold
bs = BlockStyles

_CHAIN = [
    "User Story",
    "Acceptance Criteria",
    "Test File",
    "Implementation",
    "Verification",
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Traceability \u2014 The GenSE Difference", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        st_write(
            bs.key_message,
            "Not just \u2018make it work\u2019 but \u2018prove it works for the right reasons.\u2019",
        )

        st_space("v", 0.5)

        st_write(bs.body, (bs.keyword, "Traceability chain:"))
        with st_list(li_style=bs.body, list_type=lt.ordered) as l:
            for step in _CHAIN:
                with l.item():
                    st_write(bs.body, step)

        st_space("v", 0.5)

        st_write(
            bs.body,
            (bs.stat, "9 requirements"),
            " \u00d7 ~8.7 scenarios = ",
            (bs.stat, "78 automated tests"),
            " + 8 manual",
        )

        st_space("v", 0.5)

        st_write(bs.body, (bs.keyword, "Test naming convention:"))
        st_code(s.none, code="tests/acceptance/fr-001-edit-expense.test.tsx", language="text")

        st_space("v", 0.5)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "When AI generates code, you can VERIFY it meets requirements objectively.",
            )
