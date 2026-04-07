"""Slide — SE 3.0: Intent-Centric + Conversation-Oriented."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """SE 3.0 intent slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    label = s.project.titles.label
    source = s.project.titles.source
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "SE 3.0: Intent-Centric + Conversation-Oriented", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="24px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            # Left — Intent-centric
            with g.cell():
                with st_block(
                    s.project.containers.cell_primary_bg
                    + s.project.containers.cell_pad_md,
                ):
                    st_write(bs.label, "Intent-Centric", tag=t.div)
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "Describe ", (bs.keyword, "WHAT"), ", not HOW. "
                        "The fundamental shift from code authoring to ",
                        (bs.keyword, "intent specification"),
                        ". Developers become architects of intent; "
                        "AI translates that intent into implementation.",
                    )

            # Right — Conversation-oriented
            with g.cell():
                with st_block(
                    s.project.containers.cell_accent_bg
                    + s.project.containers.cell_pad_md,
                ):
                    st_write(bs.label, "Conversation-Oriented", tag=t.div)
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "Multi-turn dialogue replaces text editing as the ",
                        (bs.keyword, "primary interaction mode"),
                        ". Evidence: CHOP metric shows ",
                        (bs.stat, "33\u201337%"),
                        " of development time spent in conversational exchanges with AI.",
                    )

        st_space("v", 1)
        st_write(bs.source, cite("hassan-se30-2025"))
