"""Slide 8 — Balanced: Tokens & Context Windows."""
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
    "page_fill_tokens",
)

# Cell centering: vertical + horizontal
_cell_center = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "tokens_cell_center",
)


class BlockStyles:
    """Slide: Tokens — maximize-viewport archetype: balanced (image + list)."""
    heading = s.project.titles.section_title + s.center_txt
    body = Style.create(
        s.project.titles.body + s.text.wrap.hyphens,
        "tokens_body",
    )
    keyword = Style.create(
        s.project.titles.body_accent,
        "tokens_keyword",
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

TOKENS_PROMPT = (
    f"{_PREFIX} A horizontal sequence of glowing rectangular tiles in varying sizes, "
    "representing word sub-pieces (tokens). Each tile has a distinct color from the palette: "
    "some electric blue, some teal, some amber. Tiles are slightly separated with thin white "
    "borders. A large translucent bracket or window frame surrounds a group of tiles, "
    "symbolizing the context window. Soft glow effects on the edges of the bracket. "
    f"Clean geometric composition. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Tokens & Context Windows",
                tag=t.div,
                toc_lvl="1",
            )

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=_cell_center,
            ) as g:
                # Left: AI image
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="tokens_visual",
                        prompt=TOKENS_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                # Right: 4 key points
                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Tokens"), (bs.body, " — words split into sub-word pieces"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Context window"), (bs.body, " — how much the model 'sees' (128K-1M tokens)"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Attention"), (bs.body, " — tokens relate to each other"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Temperature"), (bs.body, " — creativity vs. predictability dial"))
