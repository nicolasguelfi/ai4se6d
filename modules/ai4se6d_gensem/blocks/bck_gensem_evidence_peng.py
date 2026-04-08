"""Slide — RCT 1: Peng et al. (2023) — +55.8% on HTTP task."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    body = s.project.titles.body
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "RCT 1: Peng et al. (2023)", tag=t.div, toc_lvl="1")
            st_space("v", 1)
            st_write(bs.stat, "+55.8%")
            st_space("v", 1)
            st_write(
                bs.body,
                "HTTP server task completed faster with GitHub Copilot. "
                "95% CI: 21\u201389%. Less experienced developers benefited more.",
            )

        st_space("v", 2)
        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                (s.project.titles.label, "Limitation: "),
                "Single constrained task. Not representative of complex "
                "real-world projects.",
            )

        st_space("v", 1)
        st_write(bs.source, cite("peng-copilot2023"))
