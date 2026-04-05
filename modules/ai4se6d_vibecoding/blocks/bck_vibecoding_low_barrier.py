"""Slide — VibeCoding Principle 4: Low Barrier to Entry."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Principle 4 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_low_barrier_number",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A wide-open gate made of simple geometric lines in electric blue, "
    "with diverse abstract human silhouettes of varying sizes walking through. "
    "No walls on either side. Amber glow at the threshold. Represents the "
    f"democratization of software creation. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Low Barrier to Entry", tag=t.div, toc_lvl="1")

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
                        name="vc_low_barrier",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.number, "4")
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.keyword, "Anyone with an idea "),
                        "can build a working prototype.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "Non-programmers can produce functional prototypes, "
                        "blurring the traditional boundary between developers "
                        "and non-developers.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.accent + s.LARGE + s.bold,
                         "Software creation made easier."),
                    )
