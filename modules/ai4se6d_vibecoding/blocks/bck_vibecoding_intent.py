"""Slide — VibeCoding Principle 1: Intent over Implementation."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vc_intent_cell",
)


class BlockStyles:
    """Principle 1 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_intent_number",
    )
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A thought bubble in amber floating above, connected by a beam of light "
    "down to a code block in electric blue below. The thought bubble is large and "
    "prominent, the code block smaller and subordinate. Represents intent driving "
    f"implementation, not the other way around. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Intent over Implementation", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_intent",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with st_zoom(130),g.cell():
                    st_write(bs.number, "1")
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.keyword, "Describe WHAT you want,<br> "),
                        "not HOW to build it.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted, "You specify the goal. The AI determines the implementation."),
                        "<br>The shift: from writing code to expressing intent.",
                    )
