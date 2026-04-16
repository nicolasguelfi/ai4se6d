"""Slide — Traceability: The GSE-One Difference."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
    st_marker("Traceability Chain → 78 Tests")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Traceability \u2014 The GSE-One Difference", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Traceability in GSE-One",
                        entries=[
                            ("GSE-One principle", "Every requirement traces from user story through acceptance criteria to test file."),
                            ("Chain", "User Story -> Acceptance Criteria -> Test File -> Implementation -> Verification."),
                            ("Scale", "9 requirements x ~8.7 scenarios = 78 automated tests + 8 manual."),
                            ("Key insight", "Traceability lets you VERIFY AI-generated code meets requirements objectively."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

        with st_zoom(120):
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
