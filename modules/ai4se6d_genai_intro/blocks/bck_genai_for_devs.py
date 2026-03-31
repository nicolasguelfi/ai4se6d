"""Slide — GenAI for Software Engineers: balanced image + 4 capabilities."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_genai_for_devs",
)

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "genai_for_devs_cell",
)


class BlockStyles:
    """Slide: GenAI for Devs — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "genai_for_devs_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "genai_for_devs_keyword",
    )
bs = BlockStyles


# Master prompt components
_PREFIX = (
    "Minimalist digital illustration on a pure dark background (#1A1A2E). "
    "Flat vector style with soft gradients. Limited color palette: electric blue (#7AB8F5), "
    "teal (#2EC4B6), amber (#F39C12), white (#FFFFFF). Clean geometric shapes, no text, "
    "no watermarks, no photorealism. Ample negative space. Professional and modern aesthetic, "
    "suitable for tech conference projection."
)
_SUFFIX = "No text, no letters, no words, no labels, no watermarks. 2:3 portrait aspect ratio. Dark background #1A1A2E."

_PROMPT = (
    f"{_PREFIX} Four floating panels arranged in a 2x2 grid: top-left shows code brackets "
    "in electric blue, top-right shows a document icon in teal, bottom-left shows a "
    "checkmark/test icon in amber, bottom-right shows an architecture diagram outline in "
    f"white. All connected by subtle dotted lines. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "GenAI for Software Engineers", tag=t.div, toc_lvl="1")

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
                        name="genai_for_devs",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_list(
                        list_type=lt.unordered,
                        li_style=bs.body,
                    ) as l:
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Source code"),
                                (bs.body, " — dozens of languages from natural language"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Documentation"),
                                (bs.body, " — explanations, specs, commit messages"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Tests"),
                                (bs.body, " — test cases, test data, edge cases"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Architecture"),
                                (bs.body, " — design suggestions from descriptions"),
                            )
