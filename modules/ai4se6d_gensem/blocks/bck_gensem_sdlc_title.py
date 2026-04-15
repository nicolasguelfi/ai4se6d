"""Slide 1 — Module title: GSE-One promo video (small, autoplay, loop)."""
# @guideline: maximize-viewport
from pathlib import Path

from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

_page_fill = s.project.containers.page_fill_center

_MODULE_DIR = Path(__file__).resolve().parent.parent
_VIDEO_PATH = str(
    _MODULE_DIR / "static" / "images" / "managed" / "GSE" / "videos"
    / "GSE-One-promo-V02-LONG-64s.mp4"
)


class BlockStyles:
    title = Style.create(
        s.bold + s.Huge + s.center_txt,
        "gse_title_main",
    )
    title_g = Style.create(s.bold + s.Huge + s.gse.g, "gse_title_g")
    title_s = Style.create(s.bold + s.Huge + s.gse.s, "gse_title_s")
    title_e = Style.create(s.bold + s.Huge + s.gse.e, "gse_title_e")
    sub = Style.create(
        Style("font-size: 64pt;", "pt64") + s.center_txt + s.project.colors.muted,
        "gse_title_sub",
    )
bs = BlockStyles


def build():
    st_marker("Generative Software Engineering")
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.title,
                (bs.title_g, "G"), "enerative ",
                (bs.title_s, "S"), "oftware ",
                (bs.title_e, "E"), "ngineering",
                tag=t.div, toc_lvl="1",
            )
            st_space("v", 1)
            with st_grid(cols="1fr 2fr 1fr", gap="0px") as g:
                with g.cell():
                    pass
                with g.cell():
                    st_video(_VIDEO_PATH, autoplay=True, loop=True, muted=True)
                with g.cell():
                    pass
            st_space("v", 1)
            st_write(
                bs.sub,
                "GSE-One — Built by AI. Governed by Humans.",
            )
            st_space("v", "30vh")
