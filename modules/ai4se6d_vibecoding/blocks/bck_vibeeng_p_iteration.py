"""Slide — P4: Iterative Refinement (skippable)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """P4 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p4_number",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A spiral staircase viewed from above, each step clearly defined in "
    "electric blue. Gate checkpoints between iterations glow in amber. "
    f"{_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "P4 — Iterative Refinement", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p4_iteration",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.number, "4")
                    st_space("v", 1)
                    with st_zoom(100):
                        st_write(
                            bs.body,
                            (bs.keyword, "Planned iterations"),
                            " with defined scope, ",
                            (bs.keyword, "acceptance criteria"),
                            ", and review gates.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            "Not ",
                            (s.project.colors.muted, '"generate everything at once"'),
                            " — each cycle delivers a ",
                            (bs.keyword, "validated increment"),
                            ".",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "A tasting menu — each course refined "
                            "before the next is plated."),
                        )
