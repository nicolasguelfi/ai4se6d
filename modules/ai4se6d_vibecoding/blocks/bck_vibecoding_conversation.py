"""Slide — VibeCoding Principle 3: Conversational Iteration."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Principle 3 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_conversation_number",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A spiral conversation pattern: alternating speech bubbles in electric "
    "blue (human) and teal (AI), spiraling inward toward a solution point in amber at "
    "the center. Each iteration is closer to the center. Represents debugging by "
    f"describing symptoms rather than reading code. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Conversational Iteration", tag=t.div, toc_lvl="1")

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
                        name="vc_conversation",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with st_zoom(115), g.cell():
                    st_write(bs.number, "3")
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.keyword, "Bug? Describe the symptom. "),
                        "The AI fixes it.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted,
                         "Errors are addressed by describing the problem back "
                         "to the LLM rather than by reading and debugging "
                         "the code directly."),
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "No need to understand the implementation.",
                    )
