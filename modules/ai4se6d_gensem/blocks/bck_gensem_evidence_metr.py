"""Slide — RCT 3: METR (2025) — The Counterpoint."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    stat = Style.create(
        s.GIANT + s.bold + s.project.colors.critical + s.center_txt,
        "gs_ev_metr_stat",
    )
    body = s.project.titles.body
    source = s.project.titles.caption + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "RCT 3: METR (2025) \u2014 The Counterpoint",
                tag=t.div, toc_lvl="1",
            )
            st_space("v", 1)
            st_write(bs.stat, "\u221219%")
            st_space("v", 1)
            st_write(
                bs.body,
                "16 experienced OSS developers, 246 tasks on large familiar "
                "repositories. Used Cursor Pro + Claude 3.5 Sonnet.",
            )

        st_space("v", 2)
        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "Developers predicted they would be ",
                (s.project.titles.stat, "24% faster"),
                ". They were actually ",
                (s.bold + s.project.colors.critical, "19% slower"), ".",
            )

        st_space("v", 1)
        st_write(bs.source, cite("metr2025"))
