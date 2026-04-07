"""Slide — RCT 2: Cui et al. (2024) — The Largest Study."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    stat = Style.create(
        s.GIANT + s.bold + s.project.colors.primary + s.center_txt,
        "gs_ev_cui_stat",
    )
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    source = s.project.titles.caption + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "RCT 2: Cui et al. (2024) \u2014 The Largest Study",
                tag=t.div, toc_lvl="1",
            )
            st_space("v", 1)
            st_write(bs.stat, "4,867")
            st_space("v", 0.5)
            st_write(bs.body, "developers across 3 field experiments.")
            st_space("v", 1)
            st_write(
                bs.body,
                "Microsoft, Accenture, Fortune 100. 2\u20138 months duration. ",
                (bs.keyword, "+26.08%"), " increase in completed tasks.",
            )
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.label, "Juniors: "), "+27\u201339% speedup. ",
                (bs.label, "Seniors: "), "+8\u201313%.",
            )

        st_space("v", 1)
        st_write(bs.source, cite("cui-fieldexperiments2024"))
