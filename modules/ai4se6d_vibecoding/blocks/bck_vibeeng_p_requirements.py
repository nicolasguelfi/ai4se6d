"""Slide — P1: Requirements Before Prompts."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """P1 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p1_number",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A solid foundation block in amber at the base, with a requirements "
    "checklist outline above it in electric blue. A faint chat prompt bubble waits "
    f"above. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "P1 — Requirements Before Prompts", tag=t.div, toc_lvl="1")

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
                        name="ve_p1_requirements",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.number, "1")
                    st_space("v", 1)
                    with st_zoom(110):
                        st_write(
                            bs.body,
                            (bs.keyword, "Functional and non-functional requirements"),
                            " are explicitly defined ",
                            (bs.keyword, "before"),
                            " engaging the AI agent.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "The client's order — allergies, "
                            "preferences, occasion — before the kitchen starts."),
                        )
