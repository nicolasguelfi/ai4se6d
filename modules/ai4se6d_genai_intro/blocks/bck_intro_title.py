"""Slide 1 — Title: AI for Software Engineering."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE


# Viewport-filling container: content centered, fills 85vh
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "title_page_fill",
)


class BlockStyles:
    """Slide: Title — maximize-viewport archetype: image-dominant."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.text.colors.white
        + ns("line-height:1.1;", "intro_title_lh"),
        "intro_title",
    )
    subtitle = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "intro_subtitle",
    )
    info = Style.create(
        s.project.titles.caption + s.center_txt,
        "intro_info",
    )
bs = BlockStyles

# Master prompt components (from plan)
_PREFIX = (
    "Minimalist digital illustration on a pure dark background (#1A1A2E). "
    "Flat vector style with soft gradients. Limited color palette: electric blue (#7AB8F5), "
    "teal (#2EC4B6), amber (#F39C12), white (#FFFFFF). Clean geometric shapes, no text, "
    "no watermarks, no photorealism. Ample negative space. Professional and modern aesthetic, "
    "suitable for tech conference projection."
)
_SUFFIX = "No text, no letters, no words, no labels, no watermarks. 16:9 aspect ratio. Dark background #1A1A2E."

HERO_PROMPT = (
    f"{_PREFIX} A luminous brain made of interconnected circuit nodes and neural pathways, "
    "half organic half digital, radiating soft electric blue light. Central focal point with "
    f"subtle teal and amber sparks emanating outward. Symbolizes the fusion of human intelligence "
    f"and artificial intelligence. {_SUFFIX}"
)


def build():
    # P1: content fills viewport — flex container centered vertically
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.title, "AI for Software Engineering", tag=t.div, toc_lvl="1")

            st_image(
                s.none,
                width="80%",
                editable=IS_EDITABLE,
                name="hero_title",
                prompt=HERO_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(
                bs.subtitle,
                "VibeEngineering: The Future of Software",
                tag=t.div,
            )
            st_write(
                bs.subtitle,
                "Development with Generative AI",
                tag=t.div,
            )
            st_space("v", 0.5)
            st_write(
                bs.info,
                (s.project.colors.muted, "Session 1 — Day 1, April 9, 2026"),
                (s.project.colors.muted, "  ·  DLH Luxembourg"),
            )
