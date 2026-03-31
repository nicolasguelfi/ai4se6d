"""Slide 7 — Image-dominant: Transformers in 60 Seconds."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_transformers",
)


class BlockStyles:
    """Slide: Transformers — maximize-viewport archetype: image-dominant."""
    heading = s.project.titles.section_title + s.center_txt
    caption = Style.create(
        s.project.titles.caption + s.center_txt,
        "transformers_caption",
    )
bs = BlockStyles

# Master prompt components

TRANSFORMER_PROMPT = (
    f"{_PREFIX} A simplified neural network architecture flowing left to right: "
    "an input stream of small glowing cubes enters from the left, passes through "
    "three stacked translucent layers with electric blue attention beams connecting "
    "nodes across layers, and exits as a coherent output stream on the right. "
    "Soft teal glow on the attention connections, amber highlights on key nodes. "
    f"Clean horizontal data flow. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Transformers in 60 Seconds",
                tag=t.div,
                toc_lvl="1",
            )

            # Large AI image: ~75% of viewport
            st_image(
                s.none,
                width="80%",
                editable=IS_EDITABLE,
                name="transformer_arch",
                prompt=TRANSFORMER_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(
                bs.caption,
                "The engine behind every LLM",
                tag=t.div,
            )
