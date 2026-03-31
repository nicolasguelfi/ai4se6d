"""Slide — Step 3: Self-Attention: balanced image + key points."""
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
    "page_fill_llm_attention",
)

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "llm_attention_cell",
)


class BlockStyles:
    """Slide: Self-Attention — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_attention_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_attention_keyword",
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
    f"{_PREFIX} A row of 7 glowing circles (tokens) in electric blue. From one highlighted "
    "amber circle, curved light beams of varying thickness connect to all other circles. "
    "Thicker beams indicate stronger attention. Represents the self-attention mechanism. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Step 3: Self-Attention", tag=t.div, toc_lvl="1")

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
                        name="llm_attention",
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
                                (bs.keyword, "Key innovation"),
                                (bs.body, " \u2014 The Transformer's breakthrough mechanism"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Parallel"),
                                (bs.body, " \u2014 Every token attends to every other at once"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Context"),
                                (bs.body, " \u2014 'river' disambiguates 'bank' via attention"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Faster"),
                                (bs.body, " \u2014 Parallelism enables efficient GPU training"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Dozens of layers"),
                                (bs.body, " \u2014 Each layer deepens contextual understanding"),
                            )
