"""Slide — Why this matters: the junior developer analogy."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Analogy styles."""
    heading = s.project.titles.heading
    quote = Style.create(s.project.titles.body + s.italic + s.center_txt, "ocwhy_quote")
    body = Style.create(s.project.titles.body + s.center_txt, "ocwhy_body")
    punch = Style.create(s.project.titles.body_accent + s.center_txt, "ocwhy_punch")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_zoom(75):
            st_write(bs.heading, "Why This Matters", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.quote,
                "You hire a talented junior. No README, no coding standards, no architecture notes. "
                "How well will they do?", tag=t.div,
            )
        st_space("v", 1)
        st_write(bs.body, "Good code — in the wrong folder, with the wrong conventions.", tag=t.div)
        st_space("v", 1)
        st_write(bs.punch, "The agent is only as good as the context you give it.", tag=t.div)
