"""Slide — FreeSelfApp workshop opener: a first prototype by pure prompting."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Workshop opener styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "setup_ws_subtitle")
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_ws_caption")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.heading, "FreeSelfApp Workshop", tag=t.div, toc_lvl="1")
        st_write(bs.subtitle, "Your first prototype — by pure prompting", tag=t.div)
        # Reused from the vibecoding module (ex_vibecoding) — no new AI image.
        st_image(uri="images/setup_freeselfapp.webp", width="45%", max_vh=50, align="center")
        st_write(bs.caption, "2 × 45 min · no rules, no plan — on purpose", tag=t.div)
