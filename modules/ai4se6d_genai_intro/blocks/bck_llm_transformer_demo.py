"""Slide — Transformer Demo: interactive visualization link."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:0.5rem;",
    "page_fill_transformer_demo",
)

_DEMO_URL = "https://poloclub.github.io/transformer-explainer/"


class BlockStyles:
    """Slide: Transformer Demo — maximize-viewport archetype: image-dominant."""
    heading = s.project.titles.slide_title + s.center_txt
    link_label = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.accent,
        "transformer_demo_link",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Transformer Demo", tag=t.div, toc_lvl="1")

            st_image(
                s.none,
                uri="_SHARED/images/transformer_explained.png",
                width="100%",
                link=_DEMO_URL,
                editable=IS_EDITABLE,
                name="transformer_demo",
            )

            st_write(
                bs.link_label,
                "_",
                link=_DEMO_URL,
                no_link_decor=True,
            )
