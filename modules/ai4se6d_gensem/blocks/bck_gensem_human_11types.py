"""Slide — 11 Types of Human-AI Interaction (Treude & Gerosa)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """11 interaction types styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    source = s.project.citation + s.large + s.center_txt
    takeaway = s.project.titles.body_accent + s.center_txt

bs = BlockStyles


_TYPES = [
    "Autocompletion",
    "Code transformation",
    "Code explanation",
    "Test generation",
    "Documentation generation",
    "Error diagnosis",
    "Code review",
    "Architecture advice",
    "Conversational assistance",
    "Task delegation",
    "Agent orchestration",
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "11 Types of Human-AI Interaction", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(280px, 1fr))",
            gap="12px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_sm,
        ) as g:
            for i, name in enumerate(_TYPES, 1):
                with g.cell():
                    st_write(bs.body, (bs.label, f"{i}. "), name)

        st_space("v", 1)
        st_write(
            bs.takeaway,
            "Establishes vocabulary for designing human-AI interaction patterns.",
        )
        st_space("v", 1)
        st_write(bs.source, cite("treude-interactions2025"))
