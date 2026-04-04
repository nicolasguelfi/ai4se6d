"""Slide — Artificial Intelligence: John McCarthy's 1955 definition."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "ai_mccarthy_cell",
)


class BlockStyles:
    """Slide: AI McCarthy — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    quote = Style.create(
        s.Large + s.italic + s.text.wrap.hyphens,
        "ai_mccarthy_quote",
    )
    attribution = Style.create(
        s.project.titles.caption,
        "ai_mccarthy_attribution",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} Two abstract heads facing each other in profile. Left head is organic "
    "with smooth curves in teal. Right head is geometric with circuit patterns in electric "
    "blue. A subtle amber bridge of light connects them at eye level. Symbolizes human vs "
    f"artificial intelligence. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Artificial Intelligence", tag=t.div, toc_lvl="1")

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
                        name="ai_mccarthy",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(
                        bs.quote,
                        (bs.quote, "\u201CEvery aspect of learning or any other feature "
                         "of intelligence can in principle be so precisely described "
                         "that a machine can be made to simulate it.\u201D"),
                    )
                    st_space("h", "1.5rem")
                    # REF: https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904
                    st_write(bs.attribution, cite("mccarthy1955dartmouth"))
