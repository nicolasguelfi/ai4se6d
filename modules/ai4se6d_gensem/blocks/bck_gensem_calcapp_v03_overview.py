"""Slide — v0.3 Objectives: Requirements-Driven Development."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """v0.3 overview slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    col_title = s.bold + s.project.colors.primary + s.Large
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
bs = BlockStyles

_FR = [
    ("FR-001:", " Edit existing expenses"),
    ("FR-002:", " Category management"),
    ("FR-003:", " Expense sorting"),
    ("FR-004:", " Search & filter"),
    ("FR-005:", " Monthly summary"),
]

_NFR = [
    ("NFR-001:", " Form validation < 100ms"),
    ("NFR-002:", " Accessible labels (WCAG 2.1 AA)"),
    ("NFR-003:", " Keyboard navigable"),
    ("NFR-004:", " Responsive layout 320px\u20131920px"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading,
                "v0.3 Objectives \u2014 Requirements-Driven Development",
                tag=t.div,
                toc_lvl="1",
                )
            st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="24px",
            cell_styles=s.project.containers.cell_pad_md,
        ) as g:
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                    st_write(bs.col_title, "Functional Requirements", tag=t.div)
                    st_space("v", 0.5)
                    with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                        for code, desc in _FR:
                            with l.item():
                                st_write(bs.body, (bs.keyword, code), desc)

            with g.cell():
                with st_block(s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md):
                    st_write(bs.col_title, "Non-Functional Requirements", tag=t.div)
                    st_space("v", 0.5)
                    with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                        for code, desc in _NFR:
                            with l.item():
                                st_write(bs.body, (bs.keyword, code), desc)
