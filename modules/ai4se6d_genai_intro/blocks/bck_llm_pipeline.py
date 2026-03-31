"""Slide — The LLM Pipeline: image-dominant overview."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_llm_pipeline",
)


class BlockStyles:
    """Slide: LLM Pipeline — maximize-viewport archetype: image-dominant."""
    heading = s.project.titles.slide_title + s.center_txt
    caption = Style.create(
        s.project.titles.caption + s.center_txt + s.Large,
        "llm_pipeline_caption",
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
_SUFFIX = "No text, no letters, no words, no labels, no watermarks. 16:9 aspect ratio. Dark background #1A1A2E."

_PROMPT = (
    f"{_PREFIX} A horizontal pipeline of 5 distinct schematic icons flowing left to right, "
    "connected by glowing arrows. Stage 1: a paragraph of horizontal lines (text input) in white. "
    "Stage 2: the paragraph broken into small separate tiles (tokenization) in teal. "
    "Stage 3: the tiles transformed into dots scattered in a cloud (embeddings) in electric blue. "
    "Stage 4: the dots connected by a dense web of crossing beams (attention layers) in bright electric blue. "
    "Stage 5: a single glowing circle emerging from the web (next-token prediction) in amber. "
    f"Each stage is a simple geometric icon, no realism. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "The LLM Pipeline", tag=t.div, toc_lvl="1")

            st_image(
                s.none,
                width="80%",
                editable=IS_EDITABLE,
                name="llm_pipeline",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(
                bs.caption,
                "Input \u2192 Tokenization \u2192 Embeddings \u2192 Attention \u2192 Prediction",
                tag=t.div,
            )
