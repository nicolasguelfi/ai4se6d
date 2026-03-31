"""Slide — VibeCoding origin: Karpathy quote, definition, role shift."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


# Viewport-filling containers
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_vc_origin",
)

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vc_origin_cell",
)


class BlockStyles:
    """VibeCoding origin slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    quote = Style.create(
        s.Large + s.italic + s.text.wrap.hyphens,
        "vc_origin_quote",
    )
    attribution = Style.create(
        s.project.titles.caption,
        "vc_origin_attribution",
    )
    badge = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "vc_origin_badge",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A director's chair facing a giant glowing screen showing flowing code. "
    "The chair is teal, the code on screen is electric blue streams. A megaphone rests "
    "on the armrest emitting amber sound waves. Symbolizes the shift from writing code "
    f"to directing AI. {_SUFFIX}"
)


def build():
    # Sub-slide 1: Karpathy quote + Collins badge
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Birth of VibeCoding", tag=t.div, toc_lvl="1")

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
                        name="vc_origin",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(
                        bs.quote,
                        "\u201CYou just see stuff, say stuff, run stuff, "
                        "and copy-paste stuff, and it mostly works.\u201D",
                    )
                    st_space("h", "1rem")
                    st_write(
                        bs.attribution,
                        "\u2014 Andrej Karpathy, February 2025",
                    )
                    st_space("h", "2rem")
                    st_write(
                        bs.badge,
                        "Collins Dictionary — Word of the Year 2025",
                    )

    st_slide_break()

    # Sub-slide 2: Definition
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.subheading, "What is VibeCoding?", tag=t.div)
            st_space("v", 1)
            st_write(
                bs.body,
                "A practice where developers describe tasks to LLMs, "
                "accept generated code without closely reviewing its internal "
                "structure, and iterate based on whether it works.",
            )

    st_slide_break()

    # Sub-slide 3: From Author to Director
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.subheading, "From Author to Director", tag=t.div)
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.keyword, "Traditional SE: "),
                (bs.body, "You write every line. You ARE the author."),
            )
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.keyword_accent, "VibeCoding: "),
                (bs.body, "You describe intent. AI writes. You direct."),
            )
