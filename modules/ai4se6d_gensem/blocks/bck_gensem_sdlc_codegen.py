"""Slide — Three Paradigms of Code Generation (transposed table)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Code gen paradigms styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
bs = BlockStyles

_HEADERS = ("Paradigm", "Principle", "Key Characteristic")

_PARADIGMS = [
    (
        "CHOP",
        "Multi-turn conversations",
        "33-37% of interactions. A departure from text-editing.",
    ),
    (
        "VibeCoding",
        "Intent over implementation",
        "Karpathy: \"You just see stuff, say stuff, run stuff.\" Developer = director.",
    ),
    (
        "VibeEngineering",
        "Discipline reintroduced",
        "Kent Beck\u2019s \"augmented coding.\" Requirements, TDD, architecture.",
    ),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Three Paradigms of Code Generation", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        # Header row
        with st_grid(
            cols="20% 30% 50%",
            gap="8px",
            cell_styles=s.project.containers.table_header_cell,
        ) as g:
            for header in _HEADERS:
                with g.cell():
                    st_write(s.project.titles.table_header, header)

        # Data rows
        for name, principle, desc in _PARADIGMS:
            with st_grid(
                cols="20% 30% 50%",
                gap="8px",
                cell_styles=s.project.containers.table_normal_cell,
            ) as g:
                with g.cell():
                    st_write(s.project.titles.table_label, name)
                with g.cell():
                    st_write(s.project.titles.table_cell, principle)
                with g.cell():
                    st_write(s.project.titles.table_cell, desc)
